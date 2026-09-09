#!/usr/bin/env python3
"""Capture REW session state and extract reviewable .mdat data through its API.

REW remains responsible for interpreting its Java-serialised project format.
This script only loads a file, requests documented API representations, and
writes ordinary JSON/CSV files. It uses the Python standard library so the same
file can run under the project's Windows Python or under WSL.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import csv
import hashlib
import json
import math
import os
import re
import struct
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from urllib import error, parse, request


DEFAULT_API = "http://127.0.0.1:4735"
DEFAULT_TIMEOUT = 10.0
MAX_SUMMARY_MEASUREMENTS = 64
MAX_POINT_QUERIES = 64
MAX_SUMMARY_TEXT = 500
MAX_SUMMARY_COLLECTION = 64

SNAPSHOT_ENDPOINTS = {
    "application": (
        ("blocking", "/application/blocking"),
        ("lastWarning", "/application/last-warning"),
        ("warnings", "/application/warnings"),
        ("lastError", "/application/last-error"),
        ("errors", "/application/errors"),
    ),
    "audio": (
        ("status", "/audio/status"),
        ("configuration", "/audio/configuration"),
        ("driver", "/audio/driver"),
        ("sampleRate", "/audio/samplerate"),
        ("inputCalibration", "/audio/input-cal"),
        ("outputCalibration", "/audio/output-cal"),
        ("inputOptions", "/audio/input-options"),
        ("outputOptions", "/audio/output-options"),
    ),
    "measure": (
        ("naming", "/measure/naming"),
        ("notes", "/measure/notes"),
        ("level", "/measure/level"),
        ("protectionOptions", "/measure/protection-options"),
        ("sweepConfiguration", "/measure/sweep/configuration"),
        ("sweepRepetitions", "/measure/sweep/repetitions"),
        ("measurementMode", "/measure/measurement-mode"),
        ("playbackMode", "/measure/playback-mode"),
        ("timingReference", "/measure/timing/reference"),
        ("timingOffset", "/measure/timing/offset"),
        ("numberOfRepetitions", "/measure/number-of-repetitions"),
        ("startDelay", "/measure/start-delay"),
        ("invertSecondOutput", "/measure/invert-second-output"),
        ("fillSilenceWithDither", "/measure/fill-silence-with-dither"),
        ("captureNoiseFloor", "/measure/capture-noise-floor"),
    ),
    "generator": (
        ("status", "/generator/status"),
        ("signal", "/generator/signal"),
        ("signalConfiguration", "/generator/signal/configuration"),
        ("level", "/generator/level"),
        ("frequency", "/generator/frequency"),
        ("fullScaleVrms", "/generator/full-scale-vrms"),
        ("invertSecondOutput", "/generator/invert-second-output"),
        ("protection", "/generator/protection"),
    ),
    "inputLevels": (
        ("lastLevels", "/input-levels/last-levels"),
    ),
}

JAVA_AUDIO_ENDPOINTS = (
    ("format", "/audio/java/format"),
    ("stereoOnly", "/audio/java/stereo-only"),
    ("inputDevice", "/audio/java/input-device"),
    ("input", "/audio/java/input"),
    ("inputChannel", "/audio/java/input-channel"),
    ("referenceInputChannel", "/audio/java/ref-input-channel"),
    ("lastInputChannel", "/audio/java/last-input-channel"),
    ("outputDevice", "/audio/java/output-device"),
    ("output", "/audio/java/output"),
    ("outputChannel", "/audio/java/output-channel"),
    ("referenceOutputChannel", "/audio/java/ref-output-channel"),
    ("outputChannelMapping", "/audio/java/output-channel-mapping"),
)

ASIO_AUDIO_ENDPOINTS = (
    ("format", "/audio/asio/format"),
    ("device", "/audio/asio/device"),
    ("input", "/audio/asio/input"),
    ("referenceInput", "/audio/asio/ref-input"),
    ("lastInput", "/audio/asio/last-input"),
    ("output", "/audio/asio/output"),
    ("referenceOutput", "/audio/asio/ref-output"),
    ("secondaryOutput", "/audio/asio/secondary-output"),
    ("secondaryOutputEnabled", "/audio/asio/secondary-output-enable"),
)

# Known REW V5.40 measurement-summary fields that are useful as provenance.
# A whitelist avoids accidentally copying an absolute path or a future field
# containing machine-specific information into the manifest.
SUMMARY_FIELDS = (
    "title",
    "notes",
    "date",
    "uuid",
    "groupName",
    "groupNotes",
    "groupID",
    "startFreq",
    "endFreq",
    "inverted",
    "sampleRate",
    "rewVersion",
    "timingReference",
    "delay",
    "timingOffset",
    "signalToNoisedB",
    "splOffsetdB",
    "alignSPLOffsetdB",
    "cumulativeIRShiftSeconds",
    "clockAdjustmentPPM",
    "timeOfIRStartSeconds",
    "timeOfIRPeakSeconds",
)


class RewApiError(RuntimeError):
    """An API request failed or returned data that cannot be used safely."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        super().__init__(message)
        self.status = status


class RewApi:
    def __init__(self, base_url: str = DEFAULT_API, timeout: float = DEFAULT_TIMEOUT) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def request(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, object] | None = None,
        body: object | None = None,
    ) -> Any:
        url = f"{self.base_url}/{path.lstrip('/')}"
        if query:
            values = {key: str(value).lower() if isinstance(value, bool) else str(value)
                      for key, value in query.items() if value is not None}
            url = f"{url}?{parse.urlencode(values)}"

        data = None
        headers = {"Accept": "application/json"}
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"

        api_request = request.Request(url, data=data, headers=headers, method=method)
        try:
            with request.urlopen(api_request, timeout=self.timeout) as response:
                raw = response.read()
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace").strip()
            suffix = f": {detail}" if detail else ""
            raise RewApiError(
                f"REW API returned HTTP {exc.code} for {method} {url}{suffix}",
                status=exc.code,
            ) from exc
        except (error.URLError, TimeoutError, OSError) as exc:
            reason = getattr(exc, "reason", exc)
            raise RewApiError(f"Could not reach REW API at {url}: {reason}") from exc

        if not raw:
            return None
        text = raw.decode("utf-8", errors="strict")
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            # Some command/version responses are plain text in REW builds.
            return text.strip()

    def get(self, path: str, *, query: Mapping[str, object] | None = None) -> Any:
        return self.request("GET", path, query=query)

    def post(self, path: str, *, body: object) -> Any:
        return self.request("POST", path, body=body)

    def measurements(self) -> dict[str, Mapping[str, Any]]:
        payload = self.get("/measurements")
        if not isinstance(payload, dict):
            raise RewApiError("REW /measurements response was not an object keyed by measurement ID")
        result: dict[str, Mapping[str, Any]] = {}
        for measurement_id, summary in payload.items():
            if not isinstance(summary, dict):
                raise RewApiError(f"Measurement {measurement_id!r} did not contain an object summary")
            result[str(measurement_id)] = summary
        return result

    def load(self, rew_file_path: str) -> Any:
        return self.post(
            "/measurements/command",
            body={"command": "Load", "parameters": [rew_file_path]},
        )


def decode_float32_be(value: str | Sequence[object], *, field: str = "data") -> list[float]:
    """Decode a REW Base64 big-endian float32 array (or an already-decoded list)."""
    if isinstance(value, (list, tuple)):
        try:
            return [float(item) for item in value]
        except (TypeError, ValueError) as exc:
            raise RewApiError(f"REW field {field!r} contains a non-numeric value") from exc
    if not isinstance(value, str):
        raise RewApiError(f"REW field {field!r} is neither Base64 text nor a numeric list")
    try:
        raw = base64.b64decode(value, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise RewApiError(f"REW field {field!r} is not valid Base64") from exc
    if len(raw) % 4:
        raise RewApiError(
            f"REW field {field!r} has {len(raw)} decoded bytes; float32 data must be a multiple of 4"
        )
    return [item[0] for item in struct.iter_unpack(">f", raw)]


def _first(payload: Mapping[str, Any], names: Iterable[str]) -> Any:
    for name in names:
        if name in payload and payload[name] is not None:
            return payload[name]
    return None


def frequency_axis(payload: Mapping[str, Any], sample_count: int) -> list[float]:
    explicit = _first(payload, ("frequency", "frequencies"))
    if explicit is not None:
        frequencies = decode_float32_be(explicit, field="frequency")
        if len(frequencies) != sample_count:
            raise RewApiError(
                f"Frequency array has {len(frequencies)} values but response has {sample_count}"
            )
        return frequencies

    start = _first(payload, ("startFreq", "startFrequency"))
    ppo = _first(payload, ("ppo", "pointsPerOctave"))
    step = _first(payload, ("freqStep", "frequencyStep"))
    try:
        start_value = float(start)
        if ppo is not None and float(ppo) > 0:
            ppo_value = float(ppo)
            if start_value <= 0:
                raise RewApiError("Logarithmic frequency data requires a positive start frequency")
            return [start_value * math.pow(2.0, index / ppo_value)
                    for index in range(sample_count)]
        if step is not None and float(step) > 0:
            step_value = float(step)
            return [start_value + index * step_value for index in range(sample_count)]
    except (TypeError, ValueError) as exc:
        raise RewApiError("REW frequency-axis metadata is not numeric") from exc
    raise RewApiError("REW response has neither frequencies nor usable startFreq/ppo/freqStep")


def frequency_rows(payload: Mapping[str, Any]) -> tuple[list[tuple[float, float, float | None]], dict[str, Any]]:
    magnitude_value = _first(payload, ("magnitude", "magnitudes"))
    if magnitude_value is None:
        raise RewApiError("REW frequency response does not contain a magnitude array")
    magnitude = decode_float32_be(magnitude_value, field="magnitude")
    phase_value = _first(payload, ("phase", "phases"))
    phase = decode_float32_be(phase_value, field="phase") if phase_value is not None else None
    if phase is not None and len(phase) != len(magnitude):
        raise RewApiError(
            f"Phase array has {len(phase)} values but magnitude has {len(magnitude)}"
        )
    frequencies = frequency_axis(payload, len(magnitude))
    rows = [
        (frequency, mag, phase[index] if phase is not None else None)
        for index, (frequency, mag) in enumerate(zip(frequencies, magnitude))
    ]
    metadata = {
        key: payload[key]
        for key in (
            "unit",
            "smoothing",
            "startFreq",
            "ppo",
            "pointsPerOctave",
            "freqStep",
            "nanotime",
            "totalSamplesProcessed",
            "message",
        )
        if key in payload and not isinstance(payload[key], (dict, list))
    }
    metadata["sampleCount"] = len(rows)
    return rows, metadata


def impulse_rows(payload: Mapping[str, Any]) -> tuple[list[tuple[float, float]], dict[str, Any]]:
    data_value = payload.get("data")
    if data_value is None:
        raise RewApiError("REW impulse response does not contain a data array")
    samples = decode_float32_be(data_value, field="data")
    try:
        start_time = float(payload.get("startTime", 0.0))
        if payload.get("sampleInterval") is not None:
            sample_interval = float(payload["sampleInterval"])
        else:
            sample_interval = 1.0 / float(payload["sampleRate"])
    except (KeyError, TypeError, ValueError, ZeroDivisionError) as exc:
        raise RewApiError("REW impulse response has no usable sample interval or sample rate") from exc
    if sample_interval <= 0:
        raise RewApiError("REW impulse-response sample interval must be positive")
    rows = [(start_time + index * sample_interval, sample)
            for index, sample in enumerate(samples)]
    metadata = {
        key: payload[key]
        for key in (
            "unit",
            "startTime",
            "sampleInterval",
            "sampleRate",
            "timingReference",
            "timingRefTime",
            "timingOffset",
            "delay",
            "message",
        )
        if key in payload and not isinstance(payload[key], (dict, list))
    }
    metadata["sampleCount"] = len(rows)
    return rows, metadata


def safe_summary(summary: Mapping[str, Any]) -> dict[str, Any]:
    return {key: summary[key] for key in SUMMARY_FIELDS if key in summary}


def safe_slug(value: object, fallback: str = "measurement") -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value)).strip("-._")
    return (slug[:80] or fallback).lower()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def path_for_rew(path: Path) -> str:
    """Translate a mounted Windows path for the Windows REW process."""
    resolved = path.resolve()
    text = resolved.as_posix()
    match = re.match(r"^/mnt/([A-Za-z])/(.*)$", text)
    if match:
        return f"{match.group(1).upper()}:/{match.group(2)}"
    if os.name == "nt":
        return str(resolved).replace("\\", "/")
    raise RewApiError(
        f"Cannot translate {resolved} to a Windows path. Keep the .mdat under /mnt/<drive>/ "
        "or run this command with Windows Python."
    )


def display_source_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        return resolved.name


def measurement_sort_key(value: str) -> tuple[int, int | str]:
    try:
        return (0, int(value))
    except ValueError:
        return (1, value)


def wait_for_loaded_measurements(
    api: RewApi,
    before: Mapping[str, object],
    *,
    timeout: float,
    poll_interval: float = 0.2,
    settle_time: float = 1.0,
) -> dict[str, Mapping[str, Any]]:
    deadline = time.monotonic() + timeout
    previous_added: set[str] = set()
    last_change = time.monotonic()
    latest: dict[str, Mapping[str, Any]] = {}
    while time.monotonic() < deadline:
        latest = api.measurements()
        added = set(latest) - set(before)
        if added:
            now = time.monotonic()
            if added != previous_added:
                previous_added = added
                last_change = now
            elif now - last_change >= settle_time:
                return latest
        time.sleep(poll_interval)
    if set(latest) - set(before):
        return latest
    raise RewApiError(
        f"REW reported no newly loaded measurements within {timeout:g} seconds"
    )


def select_measurements(
    before: Mapping[str, object],
    after: Mapping[str, Mapping[str, Any]],
    requested: Sequence[str] | None,
) -> list[str]:
    if not requested:
        selected = sorted(set(after) - set(before), key=measurement_sort_key)
        if not selected:
            raise RewApiError("The .mdat load did not add a selectable measurement")
        return selected

    new_ids = set(after) - set(before)
    selected: list[str] = []
    for requested_id in requested:
        matches = [
            measurement_id
            for measurement_id, summary in after.items()
            if measurement_id in new_ids
            and (requested_id == measurement_id or requested_id == str(summary.get("uuid", "")))
        ]
        if len(matches) != 1:
            raise RewApiError(
                f"Measurement selector {requested_id!r} matched {len(matches)} measurements; "
                "use an ID shown by the status command or an exact UUID"
            )
        if matches[0] not in selected:
            selected.append(matches[0])
    return selected


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
                    encoding="utf-8")


def write_csv(path: Path, header: Sequence[str], rows: Iterable[Sequence[object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(header)
        for row in rows:
            writer.writerow("" if value is None else f"{value:.9g}" if isinstance(value, float) else value
                            for value in row)


def prepare_output_dir(path: Path, *, overwrite: bool) -> None:
    if path.exists() and not path.is_dir():
        raise RewApiError(f"Output path is not a directory: {path}")
    if path.exists() and any(path.iterdir()) and not overwrite:
        raise RewApiError(
            f"Output directory is not empty: {path}. Use --overwrite to replace named outputs."
        )
    path.mkdir(parents=True, exist_ok=True)


def optional_get(api: RewApi, path: str, *, query: Mapping[str, object] | None = None) -> tuple[Any, str | None]:
    try:
        return api.get(path, query=query), None
    except RewApiError as exc:
        return None, str(exc)


def _normalise_api_label(value: object) -> str:
    return re.sub(r"[\s_-]+", "", str(value).strip().lower())


def validate_frequency_response_settings(
    requested: Mapping[str, object], returned: Mapping[str, object]
) -> list[str]:
    """Check that REW honoured settings that affect interpretation of a trace."""
    requested_unit = requested.get("unit")
    returned_unit = returned.get("unit")
    if requested_unit is not None and (
        returned_unit is None
        or _normalise_api_label(requested_unit) != _normalise_api_label(returned_unit)
    ):
        raise RewApiError(
            f"REW returned frequency-response unit {returned_unit!r}, "
            f"not requested unit {requested_unit!r}"
        )

    requested_ppo = requested.get("ppo")
    returned_ppo = returned.get("ppo", returned.get("pointsPerOctave"))
    if requested_ppo is not None:
        try:
            matches = returned_ppo is not None and float(returned_ppo) == float(requested_ppo)
        except (TypeError, ValueError):
            matches = False
        if not matches:
            raise RewApiError(
                f"REW returned points-per-octave {returned_ppo!r}, "
                f"not requested value {requested_ppo!r}"
            )

    warnings: list[str] = []
    requested_smoothing = requested.get("smoothing")
    returned_smoothing = returned.get("smoothing")
    if requested_smoothing is not None and (
        returned_smoothing is None
        or _normalise_api_label(requested_smoothing) != _normalise_api_label(returned_smoothing)
    ):
        warnings.append(
            f"REW reported smoothing {returned_smoothing!r} after {requested_smoothing!r} was "
            "requested. PPO resampling can impose anti-alias smoothing; inspect the metadata."
        )
    return warnings


_WINDOWS_PATH = re.compile(r"(?i)(?<![A-Za-z0-9])(?:[A-Z]:[\\/])[^\r\n\"<>|]+")
_UNC_PATH = re.compile(r"\\\\[^\\/\s]+[\\/][^\r\n\"<>|]+")
_POSIX_PATH = re.compile(r"(?<![A-Za-z0-9.])/(?:home|mnt|Users|var|tmp)/[^\r\n\"<>|]+")


def _path_basename(value: str) -> str:
    return value.replace("\\", "/").rstrip("/").rsplit("/", 1)[-1]


def redact_snapshot_value(value: Any, *, key: str = "") -> Any:
    """Remove host paths while retaining calibration filenames and engineering state."""
    if isinstance(value, dict):
        return {
            str(child_key): redact_snapshot_value(child_value, key=str(child_key))
            for child_key, child_value in value.items()
        }
    if isinstance(value, list):
        return [redact_snapshot_value(item, key=key) for item in value]
    if not isinstance(value, str):
        return value
    if ("path" in key.lower() or "file" in key.lower()) and (
        re.match(r"(?i)^[A-Z]:[\\/]", value)
        or value.startswith("/")
        or value.startswith("\\\\")
    ):
        return _path_basename(value)
    redacted = _UNC_PATH.sub("<absolute-path>", value)
    redacted = _WINDOWS_PATH.sub("<absolute-path>", redacted)
    return _POSIX_PATH.sub("<absolute-path>", redacted)


def _snapshot_get(api: RewApi, path: str) -> tuple[Any, dict[str, Any]]:
    try:
        raw = api.get(path)
        return raw, {"ok": True, "path": path, "value": redact_snapshot_value(raw)}
    except RewApiError as exc:
        result: dict[str, Any] = {
            "ok": False,
            "path": path,
            "error": redact_snapshot_value(str(exc)),
        }
        if exc.status is not None:
            result["status"] = exc.status
        return None, result


def _driver_kind(value: Any) -> str:
    text = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value
    label = text.lower()
    if "asio" in label:
        return "asio"
    if "java" in label:
        return "java"
    return "unknown"


def _api_value_text(value: Any) -> str:
    if isinstance(value, dict) and "value" in value:
        value = value["value"]
    return str(value).strip().lower()


def build_snapshot(api: RewApi) -> dict[str, Any]:
    """Capture current REW state using GET requests only."""
    measurements = api.measurements()  # Connectivity probe; failure makes the command fail.
    state: dict[str, dict[str, Any]] = {}
    failures: list[str] = []
    raw_driver: Any = None
    raw_timing_reference: Any = None
    for group_name, endpoints in SNAPSHOT_ENDPOINTS.items():
        group: dict[str, Any] = {}
        for name, path in endpoints:
            raw, result = _snapshot_get(api, path)
            group[name] = result
            if path == "/audio/driver":
                raw_driver = raw
            if path == "/measure/timing/reference":
                raw_timing_reference = raw
            if not result["ok"]:
                failures.append(path)
        state[group_name] = group

    driver_kind = _driver_kind(raw_driver)
    driver_endpoints = (
        JAVA_AUDIO_ENDPOINTS if driver_kind == "java"
        else ASIO_AUDIO_ENDPOINTS if driver_kind == "asio"
        else ()
    )
    driver_state: dict[str, Any] = {}
    for name, path in driver_endpoints:
        _raw, result = _snapshot_get(api, path)
        driver_state[name] = result
        if not result["ok"]:
            failures.append(path)
    state["audio"]["driverKind"] = driver_kind
    state["audio"]["driverSpecific"] = driver_state

    timing_path = {
        "none": "/measure/timing/reference/none/tzero",
        "acoustic": "/measure/timing/reference/acoustic/trim",
        "wired": "/measure/timing/reference/wired/trim",
        # "looback" is the spelling used by the beta-133 API route.
        "loopback cal": "/measure/timing/reference/looback-cal/merge",
    }.get(_api_value_text(raw_timing_reference))
    if timing_path is not None:
        _raw, result = _snapshot_get(api, timing_path)
        state["measure"]["timingReferenceSpecific"] = result
        if not result["ok"]:
            failures.append(timing_path)

    choices: dict[str, Any] = {}
    for name, path in (
        ("frequencyResponseUnits", "/measurements/frequency-response/units"),
        ("smoothing", "/measurements/frequency-response/smoothing-choices"),
    ):
        _raw, result = _snapshot_get(api, path)
        choices[name] = result
        if not result["ok"]:
            failures.append(path)

    return {
        "schemaVersion": 1,
        "kind": "rewSessionSnapshot",
        "createdUtc": datetime.now(timezone.utc).isoformat(),
        "api": api.base_url,
        "complete": not failures,
        "failedEndpoints": failures,
        "caveats": [
            "This is current state, not proof of settings used for an earlier measurement.",
            "Last input levels may be absent or stale; this command does not start monitoring.",
            "REW warning and error histories are cumulative and may predate this session.",
            "Absolute paths are redacted; calibration filenames are retained where available.",
        ],
        "measurements": {
            measurement_id: redact_snapshot_value(safe_summary(summary))
            for measurement_id, summary in sorted(
                measurements.items(), key=lambda item: measurement_sort_key(item[0])
            )
        },
        "choices": choices,
        "state": state,
    }


def run_snapshot(args: argparse.Namespace) -> int:
    output = args.output.resolve() if args.output is not None else None
    if output is not None and output.exists() and not args.overwrite:
        raise RewApiError(f"Snapshot output already exists: {output}. Use --overwrite to replace it.")
    api = RewApi(args.api, args.timeout)
    snapshot = build_snapshot(api)
    if output is None:
        print(json.dumps(snapshot, indent=2, sort_keys=True, ensure_ascii=False))
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        write_json(output, snapshot)
        print(json.dumps({
            "output": str(output),
            "complete": snapshot["complete"],
            "failedEndpointCount": len(snapshot["failedEndpoints"]),
        }, indent=2))
    if snapshot["failedEndpoints"]:
        print(
            f"warning: snapshot written with {len(snapshot['failedEndpoints'])} unavailable endpoint(s)",
            file=sys.stderr,
        )
    return 0


def run_status(args: argparse.Namespace) -> int:
    api = RewApi(args.api, args.timeout)
    measurements = api.measurements()
    measurement_versions = sorted({
        str(summary["rewVersion"])
        for summary in measurements.values()
        if summary.get("rewVersion") is not None
    })
    payload: dict[str, Any] = {
        "api": api.base_url,
        "reachable": True,
        "measurementCount": len(measurements),
        "measurementRewVersions": measurement_versions,
        "measurements": {
            measurement_id: safe_summary(summary)
            for measurement_id, summary in sorted(
                measurements.items(), key=lambda item: measurement_sort_key(item[0])
            )
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False))
    return 0


def run_extract(args: argparse.Namespace) -> int:
    source = args.file.resolve()
    if not source.is_file():
        raise RewApiError(f"Input file does not exist: {source}")
    if source.suffix.lower() != ".mdat":
        raise RewApiError(f"Expected a .mdat input file, got: {source.name}")

    digest = sha256_file(source)
    output_dir = (args.output_dir or Path("outputs") / "rew-api" /
                  f"{safe_slug(source.stem)}-{digest[:8]}").resolve()
    prepare_output_dir(output_dir, overwrite=args.overwrite)

    api = RewApi(args.api, args.timeout)
    before = api.measurements()
    api.load(path_for_rew(source))
    after = wait_for_loaded_measurements(
        api,
        before,
        timeout=args.poll_timeout,
        settle_time=args.settle_time,
    )
    selected_ids = select_measurements(before, after, args.measurement)
    measurement_versions = sorted({
        str(after[measurement_id]["rewVersion"])
        for measurement_id in selected_ids
        if after[measurement_id].get("rewVersion") is not None
    })

    manifest: dict[str, Any] = {
        "schemaVersion": 1,
        "createdUtc": datetime.now(timezone.utc).isoformat(),
        "source": {
            "path": display_source_path(source),
            "sizeBytes": source.stat().st_size,
            "sha256": digest,
        },
        "api": {
            "baseUrl": api.base_url,
            "measurementRewVersions": measurement_versions,
        },
        "authority": (
            "Derived convenience export. The source .mdat remains the raw measurement authority; "
            "REW interpreted the file."
        ),
        "measurements": [],
    }
    frequency_request = {
        key: value
        for key, value in (
            ("unit", args.frequency_unit),
            ("smoothing", args.smoothing),
            ("ppo", args.ppo),
        )
        if value is not None
    }

    for ordinal, measurement_id in enumerate(selected_ids, start=1):
        summary = after[measurement_id]
        title = summary.get("title") or f"measurement-{measurement_id}"
        measurement_dir = output_dir / f"{ordinal:03d}-{safe_slug(title)}"
        measurement_dir.mkdir(parents=True, exist_ok=True)
        record: dict[str, Any] = {
            "id": measurement_id,
            "directory": measurement_dir.name,
            "summary": safe_summary(summary),
            "files": {},
            "warnings": [],
            "requests": {"frequencyResponse": frequency_request},
        }

        response = api.get(
            f"/measurements/{parse.quote(measurement_id, safe='')}/frequency-response",
            query=frequency_request or None,
        )
        if not isinstance(response, dict):
            raise RewApiError(f"Frequency response for measurement {measurement_id} was not an object")
        rows, response_metadata = frequency_rows(response)
        record["warnings"].extend(
            validate_frequency_response_settings(frequency_request, response_metadata)
        )
        frequency_name = "frequency-response.csv"
        write_csv(
            measurement_dir / frequency_name,
            ("frequency_hz", "magnitude", "phase_degrees"),
            rows,
        )
        write_json(measurement_dir / "frequency-response-metadata.json", response_metadata)
        record["files"]["frequencyResponse"] = frequency_name
        record["files"]["frequencyResponseMetadata"] = "frequency-response-metadata.json"

        windows, windows_error = optional_get(
            api, f"/measurements/{parse.quote(measurement_id, safe='')}/ir-windows"
        )
        if windows_error is None and isinstance(windows, dict):
            write_json(measurement_dir / "ir-windows.json", windows)
            record["files"]["irWindows"] = "ir-windows.json"
        elif windows_error:
            record["warnings"].append(windows_error)

        if args.include_ir:
            impulse, impulse_error = optional_get(
                api,
                f"/measurements/{parse.quote(measurement_id, safe='')}/impulse-response",
                query={"windowed": args.windowed_ir, "normalised": False},
            )
            if impulse_error is not None:
                record["warnings"].append(impulse_error)
            elif isinstance(impulse, dict):
                ir_data, ir_metadata = impulse_rows(impulse)
                write_csv(measurement_dir / "impulse-response.csv", ("time_s", "amplitude"), ir_data)
                write_json(measurement_dir / "impulse-response-metadata.json", ir_metadata)
                record["files"]["impulseResponse"] = "impulse-response.csv"
                record["files"]["impulseResponseMetadata"] = "impulse-response-metadata.json"
            else:
                record["warnings"].append(
                    f"Impulse response for measurement {measurement_id} was not an object"
                )

        manifest["measurements"].append(record)

    write_json(output_dir / "manifest.json", manifest)
    print(json.dumps({
        "outputDirectory": str(output_dir),
        "measurementCount": len(selected_ids),
        "measurementIds": selected_ids,
        "manifest": str(output_dir / "manifest.json"),
    }, indent=2))
    return 0


def _measurement_analysis() -> Any:
    """Import the shared analyser without making status/snapshot depend on it."""
    try:
        from src import measurement_analysis
    except (ImportError, ModuleNotFoundError):
        # Also support direct execution from inside src/ on Windows.
        try:
            import measurement_analysis  # type: ignore[no-redef]
        except (ImportError, ModuleNotFoundError) as exc:
            raise RewApiError(
                "Compact analysis requires src/measurement_analysis.py in this checkout"
            ) from exc
    return measurement_analysis


def _bounded_json_value(value: Any, *, depth: int = 0) -> Any:
    """Bound API-controlled values so summary output cannot contain raw arrays."""
    if depth >= 4:
        return "<maximum-depth-reached>"
    if isinstance(value, str):
        if len(value) <= MAX_SUMMARY_TEXT:
            return value
        return value[:MAX_SUMMARY_TEXT] + "<truncated>"
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for index, (key, child) in enumerate(value.items()):
            if index >= MAX_SUMMARY_COLLECTION:
                break
            result[str(key)] = _bounded_json_value(child, depth=depth + 1)
        if len(value) > MAX_SUMMARY_COLLECTION:
            result["_truncatedItemCount"] = len(value) - MAX_SUMMARY_COLLECTION
        return result
    if isinstance(value, (list, tuple)):
        result = [
            _bounded_json_value(child, depth=depth + 1)
            for child in value[:MAX_SUMMARY_COLLECTION]
        ]
        if len(value) > MAX_SUMMARY_COLLECTION:
            result.append({"_truncatedItemCount": len(value) - MAX_SUMMARY_COLLECTION})
        return result
    if isinstance(value, (int, float, bool)) or value is None:
        return value
    return _bounded_json_value(str(value), depth=depth)


def _bounded_response_metadata(metadata: Mapping[str, Any]) -> dict[str, Any]:
    """Keep only scalar response facts needed to reproduce interpretation."""
    return {
        str(key): _bounded_json_value(redact_snapshot_value(value, key=str(key)))
        for key, value in metadata.items()
        if isinstance(value, (str, int, float, bool)) or value is None
    }


def _is_impedance_unit(unit: object) -> bool:
    return _normalise_api_label(unit) in {"ohm", "ohms", "omega", "ω", "impedance"}


def _compact_curve_analysis(
    rows: Sequence[tuple[float, float, float | None]],
    *,
    unit: str,
    band: tuple[float, float],
    points: Sequence[float],
) -> dict[str, Any]:
    analyser = _measurement_analysis()
    try:
        curve = analyser.curve_from_rows(
            rows, kind="impedance" if _is_impedance_unit(unit) else "response", unit=unit
        )
        curve_summary = analyser.summarize_curve(curve, band=band)
        analysis: dict[str, Any] = {
            "validation": curve_summary["validation"],
        }
        if points:
            analysis["points"] = analyser.query_points(
                curve, points, method="nearest"
            )["result"]
        if _is_impedance_unit(unit):
            analysis["grid"] = curve_summary["analysis"]["grid"]
            analysis["impedance"] = analyser.summarize_impedance(curve, band=band)["result"]
        else:
            analysis["curve"] = curve_summary["analysis"]
        return analysis
    except (TypeError, ValueError) as exc:
        raise RewApiError(f"Could not analyse REW frequency response: {exc}") from exc


def run_summarize(args: argparse.Namespace) -> int:
    """Load an .mdat through REW and print compact in-memory analysis only."""
    source = args.file.resolve()
    if not source.is_file():
        raise RewApiError(f"Input file does not exist: {source}")
    if source.suffix.lower() != ".mdat":
        raise RewApiError(f"Expected a .mdat input file, got: {source.name}")

    digest = sha256_file(source)
    api = RewApi(args.api, args.timeout)
    before = api.measurements()
    load_response = api.load(path_for_rew(source))
    after = wait_for_loaded_measurements(
        api,
        before,
        timeout=args.poll_timeout,
        settle_time=args.settle_time,
    )
    selected_ids = select_measurements(before, after, args.measurement)
    if len(selected_ids) > MAX_SUMMARY_MEASUREMENTS:
        raise RewApiError(
            f"The .mdat added {len(selected_ids)} measurements; select at most "
            f"{MAX_SUMMARY_MEASUREMENTS} with repeated --measurement options"
        )

    frequency_request = {
        "unit": args.frequency_unit,
        "smoothing": args.smoothing,
        "ppo": args.ppo,
    }
    band = (float(args.band[0]), float(args.band[1]))
    point_frequencies = [float(value) for value in (args.at or [])]
    result: dict[str, Any] = {
        "schemaVersion": 1,
        "kind": "rewMdatSummary",
        "createdUtc": datetime.now(timezone.utc).isoformat(),
        "source": {
            "path": display_source_path(source),
            "sizeBytes": source.stat().st_size,
            "sha256": digest,
        },
        "api": {
            "baseUrl": api.base_url,
            "loadResponse": redact_snapshot_value(_bounded_json_value(load_response)),
            "measurementRewVersions": _bounded_json_value(sorted({
                str(after[measurement_id]["rewVersion"])
                for measurement_id in selected_ids
                if after[measurement_id].get("rewVersion") is not None
            })),
        },
        "authority": (
            "Derived compact analysis. The source .mdat remains the raw measurement "
            "authority; REW interpreted the file."
        ),
        "workspaceMutationWarning": (
            "Loading the .mdat adds its measurements to the current REW workspace. "
            "This command does not remove or save them."
        ),
        "analysisRequest": {
            "bandHz": list(band),
            "pointFrequenciesHz": point_frequencies,
            "frequencyResponse": frequency_request,
            "pointMethod": "nearest",
        },
        "measurements": [],
    }

    for measurement_id in selected_ids:
        summary = after[measurement_id]
        response = api.get(
            f"/measurements/{parse.quote(measurement_id, safe='')}/frequency-response",
            query=frequency_request,
        )
        if not isinstance(response, dict):
            raise RewApiError(f"Frequency response for measurement {measurement_id} was not an object")
        rows, response_metadata = frequency_rows(response)
        warnings = validate_frequency_response_settings(frequency_request, response_metadata)
        analysis = _compact_curve_analysis(
            rows,
            unit=str(response_metadata.get("unit", args.frequency_unit)),
            band=band,
            points=point_frequencies,
        )
        result["measurements"].append({
            "id": measurement_id,
            "summary": _bounded_json_value(redact_snapshot_value(safe_summary(summary))),
            "requests": {"frequencyResponse": frequency_request},
            "responseMetadata": _bounded_response_metadata(response_metadata),
            "analysis": analysis,
            "warnings": warnings,
        })

    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))
    return 0


def add_api_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--api", default=DEFAULT_API, help=f"REW API base URL (default: {DEFAULT_API})")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT,
                        help=f"HTTP timeout in seconds (default: {DEFAULT_TIMEOUT:g})")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Use REW's local API to inspect or extract data from .mdat files."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    status = subparsers.add_parser("status", help="Check API connectivity and list loaded measurements")
    add_api_options(status)
    status.set_defaults(function=run_status)

    snapshot = subparsers.add_parser(
        "snapshot", help="Capture current REW configuration, levels, warnings, and errors"
    )
    snapshot.add_argument("--output", type=Path,
                          help="Write JSON here instead of printing it to stdout")
    snapshot.add_argument("--overwrite", action="store_true",
                          help="Replace an existing --output file")
    add_api_options(snapshot)
    snapshot.set_defaults(function=run_snapshot)

    extract_parser = subparsers.add_parser(
        "extract", help="Load an .mdat in REW and write reviewable JSON/CSV exports"
    )
    extract_parser.add_argument("file", type=Path, help="Source .mdat file")
    extract_parser.add_argument("--output-dir", type=Path,
                                help="Output directory (default: outputs/rew-api/<file>-<hash>)")
    extract_parser.add_argument("--measurement", action="append",
                                help="Extract only this post-load measurement ID or UUID; repeatable")
    extract_parser.add_argument("--include-ir", action="store_true",
                                help="Also write the potentially large impulse-response CSV")
    extract_parser.add_argument("--windowed-ir", action="store_true",
                                help="Apply the stored IR windows to --include-ir output")
    extract_parser.add_argument("--frequency-unit",
                                help="Explicit REW response unit, for example SPL or ohm")
    extract_parser.add_argument("--smoothing",
                                help="Explicit REW smoothing, for example None or 1/12")
    extract_parser.add_argument("--ppo", type=int,
                                help="Resample at this positive points-per-octave value")
    extract_parser.add_argument("--overwrite", action="store_true",
                                help="Replace named files in a non-empty output directory")
    extract_parser.add_argument("--poll-timeout", type=float, default=30.0,
                                help="Seconds to wait for REW to finish loading (default: 30)")
    extract_parser.add_argument("--settle-time", type=float, default=1.0,
                                help="Quiet time after the last loaded trace (default: 1 second)")
    add_api_options(extract_parser)
    extract_parser.set_defaults(function=run_extract)

    summarize = subparsers.add_parser(
        "summarize",
        help="Load an .mdat and print bounded engineering facts without writing response files",
    )
    summarize.add_argument("file", type=Path, help="Source .mdat file")
    summarize.add_argument("--measurement", action="append",
                           help="Summarize only this post-load measurement ID or UUID; repeatable")
    summarize.add_argument(
        "--band", type=float, nargs=2, metavar=("LOW_HZ", "HIGH_HZ"), required=True,
        help="Required inclusive analysis band in hertz",
    )
    summarize.add_argument(
        "--at", type=float, action="append", metavar="FREQUENCY_HZ",
        help=f"Report the nearest sample at this frequency; repeatable (maximum {MAX_POINT_QUERIES})",
    )
    summarize.add_argument(
        "--frequency-unit", required=True,
        help="Explicit REW response unit, for example SPL or ohm",
    )
    summarize.add_argument(
        "--smoothing", default="None",
        help="Explicit REW smoothing (default: None)",
    )
    summarize.add_argument(
        "--ppo", type=int, default=96,
        help="Explicit positive points-per-octave resampling (default: 96)",
    )
    summarize.add_argument("--poll-timeout", type=float, default=30.0,
                           help="Seconds to wait for REW to finish loading (default: 30)")
    summarize.add_argument("--settle-time", type=float, default=1.0,
                           help="Quiet time after the last loaded trace (default: 1 second)")
    add_api_options(summarize)
    summarize.set_defaults(function=run_summarize)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.timeout <= 0 or getattr(args, "poll_timeout", 1) <= 0:
        parser.error("timeouts must be positive")
    if getattr(args, "settle_time", 0) < 0:
        parser.error("settle time cannot be negative")
    ppo = getattr(args, "ppo", None)
    if ppo is not None and ppo <= 0:
        parser.error("PPO must be a positive integer")
    band = getattr(args, "band", None)
    if band is not None and (
        not all(math.isfinite(value) for value in band)
        or band[0] <= 0
        or band[1] <= band[0]
    ):
        parser.error("analysis band must satisfy 0 < LOW_HZ < HIGH_HZ")
    points = getattr(args, "at", None) or []
    if len(points) > MAX_POINT_QUERIES:
        parser.error(f"at most {MAX_POINT_QUERIES} point-frequency queries are allowed")
    if any(not math.isfinite(point) or point <= 0 for point in points):
        parser.error("point frequencies must be positive")
    if args.command == "summarize" and (
        not args.frequency_unit.strip() or not args.smoothing.strip()
    ):
        parser.error("frequency unit and smoothing must be non-empty")
    try:
        return int(args.function(args))
    except RewApiError as exc:
        print(f"error: {exc}", file=sys.stderr)
        if "Could not reach REW API" in str(exc):
            print(
                "hint: start REW V5.40 with its API enabled, normally on 127.0.0.1:4735. "
                "When REW is running on Windows, run this script with Windows Python.",
                file=sys.stderr,
            )
        return 2
    except KeyboardInterrupt:
        print("error: interrupted", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
