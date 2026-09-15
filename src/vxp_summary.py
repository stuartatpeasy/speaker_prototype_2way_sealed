#!/usr/bin/env python3
"""Produce bounded, reviewable summaries and semantic diffs of VituixCAD VXP files."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path, PureWindowsPath
from typing import Any, Mapping, Sequence


SCHEMA_VERSION = 1
MAX_INPUT_BYTES = 8 * 1024 * 1024
MAX_TEXT_CHARS = 1_000
MAX_DRIVERS = 32
MAX_RESPONSES_PER_DRIVER = 181
MAX_COMPONENTS = 256
MAX_PARAMETERS_PER_COMPONENT = 32
DEFAULT_MAX_DIFFERENCES = 100
HARD_MAX_DIFFERENCES = 500

GLOBAL_FIELDS = (
    "ReferenceAngle",
    "XMin",
    "XMax",
    "Interpolate",
    "IntensitySphere",
    "IntensityCylinder",
    "IncludeHor",
    "IncludeVer",
    "HalfSpace",
    "Corner",
    "AngleStep",
    "Toein",
    "ReferDistance",
    "PlaneRotation",
    "DrvOffsetX",
    "DrvOffsetY",
)

DRIVER_FIELDS = {
    "SPL": "nominalSplDb",
    "Z": "nominalImpedanceOhm",
    "ExtendedData": "extendedData",
    "ResponseScale": "responseScale",
    "ResponseDelay": "responseDelay",
    "ResponseInvert": "responseInverted",
    "ResponseMute": "responseMuted",
    "MinimumPhase": "minimumPhase",
    "ResponseSmooth": "responseSmoothing",
    "ImpedanceScale": "impedanceScale",
}

class VxpError(RuntimeError):
    """The VXP cannot be safely parsed or represented."""


def _text(element: ET.Element | None, tag: str, default: str = "") -> str:
    if element is None:
        return default
    child = element.find(tag)
    if child is None or child.text is None:
        return default
    return child.text.strip()


def _bounded(value: str) -> tuple[str, bool]:
    if len(value) <= MAX_TEXT_CHARS:
        return value, False
    return value[:MAX_TEXT_CHARS] + "...", True


def _scalar(value: str) -> Any:
    stripped = value.strip()
    lowered = stripped.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if not stripped:
        return ""
    try:
        number = float(stripped)
    except ValueError:
        return _bounded(stripped)[0]
    if math.isfinite(number) and number.is_integer() and not any(c in stripped.lower() for c in ".e"):
        return int(number)
    return number if math.isfinite(number) else stripped


def find_project_root(vxp_path: Path) -> Path:
    """Find the checkout root used by the project's stored Windows paths."""
    for candidate in (vxp_path.parent, *vxp_path.parents):
        if (candidate / "README.md").is_file() and (candidate / "vituixcad").is_dir():
            return candidate.resolve()
    return vxp_path.parent.resolve()


def _windows_project_relative(raw: str, project_root: Path) -> Path | None:
    windows = PureWindowsPath(raw)
    if not windows.is_absolute():
        return None
    root_name = project_root.name.casefold()
    matches = [index for index, part in enumerate(windows.parts) if part.casefold() == root_name]
    if not matches:
        return None
    suffix = windows.parts[matches[-1] + 1 :]
    return project_root.joinpath(*suffix)


def resolve_source_path(raw: str, vxp_path: Path, project_root: Path) -> Path:
    """Resolve VituixCAD's Windows-absolute and project-relative source paths."""
    value = raw.strip().strip('"')
    if not value:
        return project_root

    if re.match(r"^[A-Za-z]:[\\/]", value):
        if os.name == "nt":
            return Path(value).resolve()
        mapped = _windows_project_relative(value, project_root)
        if mapped is not None:
            return mapped.resolve()
        # Preserve an unresolvable foreign Windows path as a deterministic local
        # sentinel rather than accidentally treating it as a relative POSIX path.
        windows = PureWindowsPath(value)
        return project_root.joinpath("__external_windows_path__", windows.drive.rstrip(":"), *windows.parts[1:])

    candidate = Path(value.replace("\\", "/"))
    if candidate.is_absolute():
        return candidate.resolve()

    parts = candidate.parts
    project_scoped = bool(parts) and parts[0].casefold() in {
        "calibration", "rew", "src", "vituixcad"
    }
    candidates = (
        (project_root / candidate, vxp_path.parent / candidate)
        if project_scoped
        else (vxp_path.parent / candidate, project_root / candidate)
    )
    for resolved in candidates:
        if resolved.exists():
            return resolved.resolve()
    return candidates[0].resolve()


def _path_record(raw: str, vxp_path: Path, project_root: Path) -> dict[str, Any]:
    clipped, clipped_flag = _bounded(raw)
    if not raw.strip():
        return {"stored": "", "resolved": None, "exists": False, "projectRelative": None}
    if clipped_flag:
        return {
            "stored": clipped,
            "storedTruncated": True,
            "resolved": None,
            "exists": False,
            "projectRelative": None,
            "resolutionError": "stored path exceeds bounded path length",
        }
    resolved = resolve_source_path(raw, vxp_path, project_root)
    record: dict[str, Any] = {
        "stored": clipped,
        "resolved": str(resolved),
        "exists": resolved.exists(),
    }
    try:
        record["projectRelative"] = resolved.relative_to(project_root).as_posix()
    except ValueError:
        record["projectRelative"] = None
    if clipped_flag:
        record["storedTruncated"] = True
    return record


def _join_stored_path(directory: str, filename: str) -> str:
    if not directory:
        return filename
    if re.match(r"^[A-Za-z]:[\\/]", directory) or "\\" in directory:
        return str(PureWindowsPath(directory) / PureWindowsPath(filename))
    return str(Path(directory) / filename)


def _parse_driver(
    element: ET.Element, index: int, vxp_path: Path, project_root: Path
) -> dict[str, Any]:
    directory = _text(element, "ResponseDirectory")
    driver: dict[str, Any] = {
        "index": index,
        "model": _bounded(_text(element, "Model"))[0],
    }
    for xml_name, output_name in DRIVER_FIELDS.items():
        value = _text(element, xml_name)
        if value != "":
            driver[output_name] = _scalar(value)

    driver["responseDirectory"] = _path_record(directory, vxp_path, project_root)
    impedance = _text(element, "ImpedanceFile")
    driver["impedanceFile"] = _path_record(impedance, vxp_path, project_root)

    responses = element.findall("RESPONSE")
    parsed_responses = []
    for response in responses[:MAX_RESPONSES_PER_DRIVER]:
        filename = _text(response, "FileName")
        combined = _join_stored_path(directory, filename)
        parsed_responses.append({
            "fileName": _bounded(filename)[0],
            "horizontalDegrees": _scalar(_text(response, "Hor")),
            "verticalDegrees": _scalar(_text(response, "Ver")),
            "source": _path_record(combined, vxp_path, project_root),
        })
    driver["responses"] = parsed_responses
    if len(responses) > MAX_RESPONSES_PER_DRIVER:
        driver["responsesTruncated"] = len(responses) - MAX_RESPONSES_PER_DRIVER

    scale = driver.get("responseScale")
    if isinstance(scale, (int, float)) and scale > 0:
        driver["responseScaleDb"] = 20.0 * math.log10(scale)
    return driver


def _parse_parameter(element: ET.Element) -> dict[str, Any]:
    parameter: dict[str, Any] = {
        "name": _bounded(_text(element, "Name"))[0],
        "value": _scalar(_text(element, "Value")),
        "unit": _bounded(_text(element, "Unit"))[0],
    }
    for xml_name, output_name in (
        ("Optimize", "optimize"),
        ("Expression", "expression"),
        ("Min", "minimum"),
        ("Max", "maximum"),
        ("OptiBlock", "optimizationBlocked"),
    ):
        value = _text(element, xml_name)
        if value != "":
            parameter[output_name] = _scalar(value)
    return parameter


def _parse_component(element: ET.Element, source_index: int) -> dict[str, Any]:
    component: dict[str, Any] = {
        "sourceIndex": source_index,
        "id": _bounded(_text(element, "PartID"))[0],
        "type": _bounded(_text(element, "Type"))[0],
    }
    for xml_name, output_name in (
        ("Open", "open"),
        ("Shorted", "shorted"),
        ("Inverted", "inverted"),
        ("Muted", "muted"),
    ):
        value = _text(element, xml_name)
        if value != "":
            component[output_name] = _scalar(value)
    parameters = element.findall("PARAM")
    component["parameters"] = [
        _parse_parameter(parameter)
        for parameter in parameters[:MAX_PARAMETERS_PER_COMPONENT]
    ]
    if len(parameters) > MAX_PARAMETERS_PER_COMPONENT:
        component["parametersTruncated"] = len(parameters) - MAX_PARAMETERS_PER_COMPONENT
    return component


def parse_vxp(path: Path, *, fingerprint_sources: bool = False) -> dict[str, Any]:
    source = path.resolve()
    if not source.is_file():
        raise VxpError(f"VXP file does not exist: {source}")
    size = source.stat().st_size
    if size > MAX_INPUT_BYTES:
        raise VxpError(
            f"VXP file is {size} bytes; maximum supported size is {MAX_INPUT_BYTES} bytes"
        )
    raw = source.read_bytes()
    try:
        root = ET.fromstring(raw)  # Handles UTF-8/UTF-16 BOMs and declarations.
    except (ET.ParseError, UnicodeError) as exc:
        raise VxpError(f"Invalid VXP XML in {source.name}: {exc}") from exc
    if root.tag != "SPEAKER":
        raise VxpError(f"Expected SPEAKER root element, found {root.tag!r}")

    project_root = find_project_root(source)
    description, description_truncated = _bounded(_text(root, "Description"))
    globals_record = {
        field: _scalar(_text(root, field))
        for field in GLOBAL_FIELDS
        if _text(root, field) != ""
    }
    crossover = root.find("CROSSOVER")
    crossover_record: dict[str, Any] = {}
    for field in ("DSP", "SampleRate"):
        value = _text(crossover, field)
        if value != "":
            crossover_record[field[0].lower() + field[1:]] = _scalar(value)

    driver_elements = root.findall("DRIVER")
    drivers = [
        _parse_driver(element, index, source, project_root)
        for index, element in enumerate(driver_elements[:MAX_DRIVERS])
    ]

    part_elements = crossover.findall("PART") if crossover is not None else []
    electrical = [
        (index, element)
        for index, element in enumerate(part_elements)
        if _text(element, "Type") not in {"Generator", "Driver", "Wire", "Ground"}
        and (_text(element, "PartID") or element.findall("PARAM"))
    ]
    components = [
        _parse_component(element, source_index)
        for source_index, element in electrical[:MAX_COMPONENTS]
    ]

    path_records = []
    for driver in drivers:
        path_records.extend((driver["responseDirectory"], driver["impedanceFile"]))
        path_records.extend(response["source"] for response in driver["responses"])
    fingerprints: dict[str, dict[str, Any]] = {}
    if fingerprint_sources:
        for record in path_records:
            resolved = record.get("resolved")
            if not resolved or not Path(resolved).is_file():
                continue
            if resolved not in fingerprints:
                digest = hashlib.sha256()
                with Path(resolved).open("rb") as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        digest.update(chunk)
                fingerprints[resolved] = {"sizeBytes": Path(resolved).stat().st_size,
                                          "sha256": digest.hexdigest()}
            record.update(fingerprints[resolved])
    missing = sorted({
        record.get("projectRelative") or record["stored"] or "<empty>"
        for record in path_records
        if not record["exists"]
    })

    result: dict[str, Any] = {
        "schemaVersion": SCHEMA_VERSION,
        "kind": "vituixcadProjectSummary",
        "source": {
            "path": str(source),
            "sizeBytes": size,
            "sha256": hashlib.sha256(raw).hexdigest(),
        },
        "projectRoot": str(project_root),
        "project": {
            "description": description,
            "globals": globals_record,
            "crossover": crossover_record,
        },
        "drivers": drivers,
        "components": components,
        "sourceAudit": {
            "referenceCount": len(path_records),
            "missingCount": len(missing),
            "missing": missing,
            "fingerprintedFileCount": len(fingerprints),
        },
        "counts": {
            "drivers": len(driver_elements),
            "reportedDrivers": len(drivers),
            "crossoverParts": len(part_elements),
            "electricalComponents": len(electrical),
            "reportedElectricalComponents": len(components),
        },
    }
    if description_truncated:
        result["project"]["descriptionTruncated"] = True
        result["project"]["descriptionLength"] = len(_text(root, "Description"))
        result["project"]["descriptionSha256"] = hashlib.sha256(
            _text(root, "Description").encode("utf-8")
        ).hexdigest()
    if len(driver_elements) > MAX_DRIVERS:
        result["counts"]["driversTruncated"] = len(driver_elements) - MAX_DRIVERS
    if len(electrical) > MAX_COMPONENTS:
        result["counts"]["componentsTruncated"] = len(electrical) - MAX_COMPONENTS
    return result


def _semantic_path(record: Mapping[str, Any]) -> str:
    relative = record.get("projectRelative")
    if relative:
        return str(relative)
    return str(record.get("stored", "")).replace("\\", "/")


def _semantic_source(record: Mapping[str, Any], include_hash: bool) -> Any:
    path = _semantic_path(record)
    return {"path": path, "sha256": record.get("sha256")} if include_hash else path


def semantic_view(summary: Mapping[str, Any], *, include_source_hashes: bool = False) -> dict[str, Any]:
    """Discard host identity and schematic layout while retaining engineering semantics."""
    driver_map: dict[str, Any] = {}
    for driver in summary["drivers"]:
        key = str(driver.get("model") or f"driver-{driver['index']}")
        if key in driver_map:
            key = f"{key}#{driver['index']}"
        fields = {
            name: value
            for name, value in driver.items()
            if name not in {
                "index", "responseDirectory", "impedanceFile", "responses",
                "responsesTruncated", "responseScaleDb",
            }
        }
        fields["responseDirectory"] = _semantic_path(driver["responseDirectory"])
        fields["impedanceFile"] = _semantic_source(driver["impedanceFile"], include_source_hashes)
        response_map: dict[str, Any] = {}
        for index, response in enumerate(driver["responses"]):
            angle = f"h={response['horizontalDegrees']},v={response['verticalDegrees']}"
            if angle in response_map:
                angle = f"{angle}#{index}"
            response_map[angle] = _semantic_source(response["source"], include_source_hashes)
        fields["responses"] = response_map
        driver_map[key] = fields

    component_map: dict[str, Any] = {}
    for component in summary["components"]:
        key = str(component.get("id") or f"{component['type']}#{component['sourceIndex']}")
        if key in component_map:
            key = f"{key}#{component['sourceIndex']}"
        fields = {
            name: value
            for name, value in component.items()
            if name not in {"id", "sourceIndex", "parameters", "parametersTruncated"}
        }
        parameters: dict[str, Any] = {}
        for index, parameter in enumerate(component["parameters"]):
            parameter_name = str(parameter.get("name") or f"parameter-{index}")
            if parameter_name in parameters:
                parameter_name = f"{parameter_name}#{index}"
            parameters[parameter_name] = {
                name: value for name, value in parameter.items() if name != "name"
            }
        fields["parameters"] = parameters
        component_map[key] = fields

    return {
        "project": summary["project"],
        "drivers": driver_map,
        "components": component_map,
    }


def semantic_diff(
    left: Mapping[str, Any], right: Mapping[str, Any], *, max_differences: int,
    include_source_hashes: bool = False,
) -> dict[str, Any]:
    differences: list[dict[str, Any]] = []
    difference_count = 0

    def walk(a: Any, b: Any, path: str) -> None:
        nonlocal difference_count
        if isinstance(a, dict) and isinstance(b, dict):
            for key in sorted(set(a) | set(b)):
                child_path = f"{path}.{key}" if path else str(key)
                if key not in a:
                    add(child_path, None, b[key], "added")
                elif key not in b:
                    add(child_path, a[key], None, "removed")
                else:
                    walk(a[key], b[key], child_path)
            return
        if a != b:
            add(path, a, b, "changed")

    def add(path: str, a: Any, b: Any, change: str) -> None:
        nonlocal difference_count
        difference_count += 1
        if len(differences) < max_differences:
            differences.append({"path": path, "change": change, "left": a, "right": b})

    walk(semantic_view(left, include_source_hashes=include_source_hashes),
         semantic_view(right, include_source_hashes=include_source_hashes), "")
    return {
        "equal": difference_count == 0,
        "differenceCount": difference_count,
        "reportedDifferenceCount": len(differences),
        "differencesTruncated": difference_count > len(differences),
        "differences": differences,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Summarise or compare VituixCAD VXP projects")
    parser.add_argument("--pretty", action="store_true", help="indent JSON output")
    subparsers = parser.add_subparsers(dest="command", required=True)

    summary = subparsers.add_parser("summary", help="write a bounded project summary")
    summary.add_argument("file", type=Path)
    summary.add_argument("--fingerprint-sources", action="store_true",
                         help="hash referenced FRD/ZMA files (may read large sources)")

    fingerprints = subparsers.add_parser("fingerprints", help="write only referenced FRD/ZMA fingerprints")
    fingerprints.add_argument("file", type=Path)

    compare = subparsers.add_parser("compare", help="write a normalized semantic diff")
    compare.add_argument("left", type=Path)
    compare.add_argument("right", type=Path)
    compare.add_argument("--fingerprint-sources", action="store_true",
                         help="include source byte hashes in the semantic comparison")
    compare.add_argument(
        "--max-differences", type=int, default=DEFAULT_MAX_DIFFERENCES,
        help=f"maximum differences to report (1-{HARD_MAX_DIFFERENCES})",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if getattr(args, "max_differences", 1) not in range(1, HARD_MAX_DIFFERENCES + 1):
        parser.error(f"--max-differences must be between 1 and {HARD_MAX_DIFFERENCES}")
    try:
        if args.command == "summary":
            payload = parse_vxp(args.file, fingerprint_sources=args.fingerprint_sources)
        elif args.command == "fingerprints":
            summary = parse_vxp(args.file, fingerprint_sources=True)
            found = {}
            for driver in summary["drivers"]:
                for record in [driver["impedanceFile"],
                               *(response["source"] for response in driver["responses"])]:
                    if record.get("sha256"):
                        found[record.get("projectRelative") or record["stored"]] = {
                            "sizeBytes": record["sizeBytes"], "sha256": record["sha256"]}
            payload = {"kind": "vituixcadSourceFingerprints",
                       "source": summary["source"], "fileCount": len(found),
                       "files": {key: found[key] for key in sorted(found)},
                       "missing": summary["sourceAudit"]["missing"]}
        else:
            left = parse_vxp(args.left, fingerprint_sources=args.fingerprint_sources)
            right = parse_vxp(args.right, fingerprint_sources=args.fingerprint_sources)
            payload = {
                "schemaVersion": SCHEMA_VERSION,
                "kind": "vituixcadProjectSemanticDiff",
                "left": left["source"],
                "right": right["source"],
                **semantic_diff(left, right, max_differences=args.max_differences,
                                include_source_hashes=args.fingerprint_sources),
            }
    except (OSError, VxpError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False, separators=(",", ":")), file=sys.stderr)
        return 2

    if args.pretty:
        print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
