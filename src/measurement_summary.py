#!/usr/bin/env python3
"""Command-line interface for bounded summaries of FRD, ZMA, and impulse data."""

from __future__ import annotations

import argparse
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
    return parser


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
        if args.command == "inspect":
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
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"measurement_summary: {exc}", file=sys.stderr)
        return 2
    json.dump(output, sys.stdout, indent=2, sort_keys=True, allow_nan=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
