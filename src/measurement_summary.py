#!/usr/bin/env python3
"""Command-line interface for bounded summaries of FRD, ZMA, and impulse data."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Sequence

try:
    from .measurement_analysis import (
        compare_curves,
        compare_impulses,
        compare_polar,
        parse_curve,
        parse_impulse,
        query_points,
        summarize_curve,
        summarize_impedance,
    )
except ImportError:  # Direct ``python src/measurement_summary.py`` invocation.
    from measurement_analysis import (  # type: ignore[no-redef]
        compare_curves,
        compare_impulses,
        compare_polar,
        parse_curve,
        parse_impulse,
        query_points,
        summarize_curve,
        summarize_impedance,
    )


def _band(values: Sequence[float] | None) -> tuple[float, float] | None:
    return tuple(values) if values is not None else None  # type: ignore[return-value]


def _common_curve(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("path", type=Path)
    parser.add_argument("--kind", choices=("response", "impedance"),
                        help="Override format inference")
    parser.add_argument("--unit", help="Override the reported magnitude unit")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Return compact JSON facts from large loudspeaker measurement files."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect_parser = subparsers.add_parser("inspect", help="Validate and summarise one curve")
    _common_curve(inspect_parser)
    inspect_parser.add_argument("--band", nargs=2, type=float, metavar=("LOW_HZ", "HIGH_HZ"))

    points_parser = subparsers.add_parser("points", help="Query selected frequencies")
    _common_curve(points_parser)
    points_parser.add_argument("--frequency", "-f", action="append", type=float, required=True)
    points_parser.add_argument("--method", choices=("nearest", "interpolate"), default="nearest")

    impedance_parser = subparsers.add_parser("impedance", help="Complex-load and EPDR summary")
    _common_curve(impedance_parser)
    impedance_parser.set_defaults(kind="impedance")
    impedance_parser.add_argument("--band", nargs=2, type=float, required=True,
                                  metavar=("LOW_HZ", "HIGH_HZ"))
    impedance_parser.add_argument("--q-band", nargs=2, type=float,
                                  metavar=("LOW_HZ", "HIGH_HZ"))
    impedance_parser.add_argument("--q-threshold-ohm", type=float)

    compare_parser = subparsers.add_parser("compare", help="Compare curve A minus curve B")
    compare_parser.add_argument("a", type=Path)
    compare_parser.add_argument("b", type=Path)
    compare_parser.add_argument("--kind", choices=("response", "impedance"))
    compare_parser.add_argument("--unit")
    compare_parser.add_argument("--band", nargs=2, type=float, required=True,
                                metavar=("LOW_HZ", "HIGH_HZ"))
    compare_parser.add_argument("--grid", choices=("exact", "interpolate"), required=True)
    compare_parser.add_argument("--fit-gain", action="store_true")
    compare_parser.add_argument("--fit-delay", action="store_true")

    polar_parser = subparsers.add_parser("polar", help="Compare named angles to a reference")
    polar_parser.add_argument("reference", type=Path)
    polar_parser.add_argument("--curve", action="append", required=True, metavar="NAME=PATH")
    polar_parser.add_argument("--band", nargs=2, type=float, required=True,
                              metavar=("LOW_HZ", "HIGH_HZ"))
    polar_parser.add_argument("--grid", choices=("exact", "interpolate"), required=True)
    polar_parser.add_argument("--frequency", "-f", action="append", type=float, default=[])

    impulse_parser = subparsers.add_parser("impulse", help="Compare two REW impulse CSV/JSON files")
    impulse_parser.add_argument("a", type=Path)
    impulse_parser.add_argument("b", type=Path)
    impulse_parser.add_argument("--window", nargs=2, type=float, required=True,
                                metavar=("START_S", "END_S"))
    impulse_parser.add_argument("--sample-rate-hz", type=float)
    impulse_parser.add_argument("--grid", choices=("exact", "interpolate"), required=True)
    impulse_parser.add_argument("--no-fit-gain", action="store_true")
    impulse_parser.add_argument("--max-lag-ms", type=float, default=0.0)

    batch_parser = subparsers.add_parser("batch", help="Run bounded JSON tasks with parsed-file reuse")
    batch_parser.add_argument("recipe", type=Path)
    return parser


def run_batch(recipe_path: Path) -> dict:
    raw = recipe_path.read_bytes()
    if len(raw) > 128 * 1024:
        raise ValueError("batch recipe exceeds 128 KiB")
    recipe = json.loads(raw)
    tasks = recipe.get("tasks") if isinstance(recipe, dict) else None
    if not isinstance(tasks, list) or not 1 <= len(tasks) <= 32:
        raise ValueError("batch recipe must contain 1-32 tasks")
    base = recipe_path.parent
    curve_cache = {}
    impulse_cache = {}

    def curve(name, kind=None, unit=None):
        if not isinstance(name, str) or not name:
            raise ValueError("task source path must be a non-empty string")
        path = (base / name).resolve()
        key = (path, kind, unit)
        if key not in curve_cache:
            for (cached_path, _, cached_unit), cached in curve_cache.items():
                if cached_path == path and cached_unit == unit and (kind is not None and cached.kind == kind):
                    return cached
            curve_cache[key] = parse_curve(path, kind=kind, unit=unit)
        return curve_cache[key]

    def impulse(name, sample_rate=None):
        if not isinstance(name, str) or not name:
            raise ValueError("task impulse path must be a non-empty string")
        path = (base / name).resolve()
        key = (path, sample_rate)
        if key not in impulse_cache:
            impulse_cache[key] = parse_impulse(path, sample_rate_hz=sample_rate)
        return impulse_cache[key]

    def pair(task, field, required=False):
        value = task.get(field)
        if value is None and not required:
            return None
        if not isinstance(value, list) or len(value) != 2 or any(
                not isinstance(item, (int, float)) or isinstance(item, bool) for item in value):
            raise ValueError(f"{field} must contain two numbers")
        return value

    records = []
    names = set()
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            raise ValueError(f"task {index + 1} must be an object")
        name = task.get("name", f"task{index + 1}")
        if not isinstance(name, str) or not name or name in names:
            raise ValueError("task names must be unique non-empty strings")
        names.add(name)
        operation = task.get("operation")
        kind, unit = task.get("kind"), task.get("unit")
        if kind not in (None, "response", "impedance") or unit is not None and not isinstance(unit, str):
            raise ValueError(f"task {name}: invalid kind or unit")
        if operation == "inspect":
            result = summarize_curve(curve(task.get("path"), kind, unit), band=pair(task, "band"))
        elif operation == "points":
            frequencies = task.get("frequencies")
            if not isinstance(frequencies, list) or not 1 <= len(frequencies) <= 32:
                raise ValueError(f"task {name}: frequencies must contain 1-32 points")
            result = query_points(curve(task.get("path"), kind, unit), frequencies,
                                  method=task.get("method", "nearest"))
        elif operation == "impedance":
            result = summarize_impedance(curve(task.get("path"), "impedance", unit),
                                         band=pair(task, "band", True),
                                         q_band=pair(task, "qBand"),
                                         q_threshold_ohm=task.get("qThresholdOhm"))
        elif operation == "compare":
            result = compare_curves(curve(task.get("a"), kind, unit), curve(task.get("b"), kind, unit),
                                    band=pair(task, "band", True), grid=task.get("grid"),
                                    fit_gain=bool(task.get("fitGain", False)),
                                    fit_delay=bool(task.get("fitDelay", False)))
        elif operation == "polar":
            named = task.get("curves")
            if not isinstance(named, dict) or not 1 <= len(named) <= 16:
                raise ValueError(f"task {name}: curves must contain 1-16 named paths")
            frequencies = task.get("frequencies", [])
            if not isinstance(frequencies, list) or len(frequencies) > 32:
                raise ValueError(f"task {name}: at most 32 selected frequencies")
            result = compare_polar(curve(task.get("reference")),
                                   {angle: curve(path) for angle, path in named.items()},
                                   band=pair(task, "band", True), grid=task.get("grid"),
                                   frequencies=frequencies)
        elif operation == "impulse":
            sample_rate = task.get("sampleRateHz")
            result = compare_impulses(impulse(task.get("a"), sample_rate),
                                      impulse(task.get("b"), sample_rate),
                                      window=pair(task, "window", True), sample_rate_hz=sample_rate,
                                      grid=task.get("grid"),
                                      fit_gain=bool(task.get("fitGain", True)),
                                      max_lag_s=task.get("maxLagMs", 0) / 1000)
        else:
            raise ValueError(f"task {name}: unknown operation {operation!r}")
        records.append({"name": name, "operation": operation, "analysis": result})
    return {"kind": "measurementBatch", "recipe": {"path": str(recipe_path.resolve()),
            "sizeBytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()},
            "taskCount": len(records), "parsedCurveCount": len(curve_cache),
            "parsedImpulseCount": len(impulse_cache), "tasks": records}


def _polar_argument(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise ValueError("each --curve must use NAME=PATH")
    name, path = value.split("=", 1)
    if not name.strip() or not path.strip():
        raise ValueError("each --curve must contain a non-empty name and path")
    return name.strip(), Path(path)


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "batch":
            output = run_batch(args.recipe)
        elif args.command == "inspect":
            output = summarize_curve(parse_curve(args.path, kind=args.kind, unit=args.unit),
                                     band=_band(args.band))
        elif args.command == "points":
            output = query_points(parse_curve(args.path, kind=args.kind, unit=args.unit),
                                  args.frequency, method=args.method)
        elif args.command == "impedance":
            output = summarize_impedance(
                parse_curve(args.path, kind="impedance", unit=args.unit),
                band=_band(args.band), q_band=_band(args.q_band),
                q_threshold_ohm=args.q_threshold_ohm,
            )
        elif args.command == "compare":
            output = compare_curves(
                parse_curve(args.a, kind=args.kind, unit=args.unit),
                parse_curve(args.b, kind=args.kind, unit=args.unit),
                band=_band(args.band), grid=args.grid,
                fit_gain=args.fit_gain, fit_delay=args.fit_delay,
            )
        elif args.command == "polar":
            curves = {}
            for specification in args.curve:
                name, path = _polar_argument(specification)
                if name in curves:
                    raise ValueError(f"duplicate polar curve name: {name}")
                curves[name] = parse_curve(path)
            output = compare_polar(parse_curve(args.reference), curves,
                                   band=_band(args.band), grid=args.grid,
                                   frequencies=args.frequency)
        else:
            output = compare_impulses(
                parse_impulse(args.a, sample_rate_hz=args.sample_rate_hz),
                parse_impulse(args.b, sample_rate_hz=args.sample_rate_hz),
                window=args.window, sample_rate_hz=args.sample_rate_hz,
                grid=args.grid, fit_gain=not args.no_fit_gain,
                max_lag_s=args.max_lag_ms / 1000.0,
            )
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        print(f"measurement_summary: {exc}", file=sys.stderr)
        return 2
    json.dump(output, sys.stdout, indent=2, sort_keys=True, allow_nan=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
