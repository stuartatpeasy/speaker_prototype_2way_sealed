#!/usr/bin/env python3
"""Compact, standard-library analysis of loudspeaker measurement data.

The module deliberately keeps full sample arrays inside the process and returns
only JSON-serialisable summaries.  It supports REW text FRD/ZMA files, the CSV
files produced by ``rew_api_extract.py``, and decoded or Base64 REW API payloads.
"""

from __future__ import annotations

import base64
import binascii
import csv
import hashlib
import json
import math
import re
import struct
from bisect import bisect_left
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


SCHEMA = "speaker-measurement-summary/v1"


@dataclass(frozen=True)
class Curve:
    """A complex frequency response held in memory, never emitted wholesale."""

    frequencies_hz: tuple[float, ...]
    magnitudes: tuple[float, ...]
    phases_degrees: tuple[float | None, ...]
    kind: str = "response"
    unit: str | None = None
    source: Mapping[str, Any] = field(default_factory=lambda: {"type": "memory"})
    metadata: Mapping[str, Any] = field(default_factory=dict)
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True)
class Impulse:
    """An impulse response with explicit sample times."""

    times_s: tuple[float, ...]
    amplitudes: tuple[float, ...]
    sample_rate_hz: float
    source: Mapping[str, Any] = field(default_factory=lambda: {"type": "memory"})
    metadata: Mapping[str, Any] = field(default_factory=dict)
    warnings: tuple[str, ...] = ()


def _float(value: Any, label: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} is not numeric: {value!r}") from exc


def _decode_float32_be(value: str | Sequence[Any], label: str) -> list[float]:
    if isinstance(value, (list, tuple)):
        return [_float(item, label) for item in value]
    if not isinstance(value, str):
        raise ValueError(f"{label} must be a numeric list or Base64 float32 array")
    try:
        raw = base64.b64decode(value, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise ValueError(f"{label} is not valid Base64") from exc
    if len(raw) % 4:
        raise ValueError(f"{label} decoded length is not a multiple of four bytes")
    return [item[0] for item in struct.iter_unpack(">f", raw)]


def _source_for_path(path: Path) -> dict[str, Any]:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return {
        "type": "file",
        "path": str(path.resolve()),
        "sizeBytes": path.stat().st_size,
        "sha256": digest.hexdigest(),
        "format": path.suffix.lower().lstrip(".") or "text",
    }


def _normalise_source(source: Mapping[str, Any] | str | None) -> dict[str, Any]:
    if source is None:
        return {"type": "memory"}
    if isinstance(source, str):
        return {"type": "memory", "name": source}
    return dict(source)


def _row_values(row: Sequence[Any] | Mapping[str, Any]) -> tuple[Any, Any, Any | None]:
    if isinstance(row, Mapping):
        lowered = {str(key).strip().lower(): value for key, value in row.items()}
        frequency = next((lowered[key] for key in
                          ("frequency_hz", "frequency", "freq_hz", "freq") if key in lowered), None)
        magnitude = next((lowered[key] for key in
                          ("magnitude", "spl_db", "spl", "z_ohms", "impedance") if key in lowered), None)
        phase = next((lowered[key] for key in
                      ("phase_degrees", "phase", "phase_deg") if key in lowered), None)
        if frequency is None or magnitude is None:
            raise ValueError("curve mapping rows require frequency and magnitude fields")
        return frequency, magnitude, phase
    if len(row) < 2:
        raise ValueError("curve rows require at least frequency and magnitude")
    return row[0], row[1], row[2] if len(row) > 2 else None


def _curve_warnings(frequencies: Sequence[float], magnitudes: Sequence[float],
                    phases: Sequence[float | None]) -> list[str]:
    warnings: list[str] = []
    nonfinite = sum(
        not math.isfinite(frequency) or not math.isfinite(magnitude)
        or (phase is not None and not math.isfinite(phase))
        for frequency, magnitude, phase in zip(frequencies, magnitudes, phases)
    )
    if nonfinite:
        warnings.append(f"{nonfinite} row(s) contain non-finite values")
    finite_frequencies = [value for value in frequencies if math.isfinite(value)]
    nonpositive = sum(value <= 0 for value in finite_frequencies)
    if nonpositive:
        warnings.append(f"{nonpositive} frequency value(s) are not positive")
    duplicates = len(finite_frequencies) - len(set(finite_frequencies))
    if duplicates:
        warnings.append(f"{duplicates} duplicate frequency value(s)")
    reversals = sum(b < a for a, b in zip(finite_frequencies, finite_frequencies[1:]))
    if reversals:
        warnings.append(f"frequency grid reverses direction {reversals} time(s)")
    missing_phase = sum(value is None for value in phases)
    if missing_phase:
        warnings.append(f"phase is absent from {missing_phase} row(s)")
    return warnings


def curve_from_rows(
    rows: Iterable[Sequence[Any] | Mapping[str, Any]],
    *,
    kind: str = "response",
    unit: str | None = None,
    source: Mapping[str, Any] | str | None = None,
    metadata: Mapping[str, Any] | None = None,
    warnings: Iterable[str] = (),
) -> Curve:
    """Build a curve from decoded rows, including rows from REW ``frequency_rows``."""
    frequencies: list[float] = []
    magnitudes: list[float] = []
    phases: list[float | None] = []
    for index, row in enumerate(rows, 1):
        frequency, magnitude, phase = _row_values(row)
        frequencies.append(_float(frequency, f"row {index} frequency"))
        magnitudes.append(_float(magnitude, f"row {index} magnitude"))
        phases.append(None if phase is None or phase == "" else _float(phase, f"row {index} phase"))
    if not frequencies:
        raise ValueError("curve contains no data rows")
    found_warnings = list(warnings)
    found_warnings.extend(_curve_warnings(frequencies, magnitudes, phases))
    return Curve(
        tuple(frequencies), tuple(magnitudes), tuple(phases), kind, unit,
        _normalise_source(source), dict(metadata or {}), tuple(dict.fromkeys(found_warnings)),
    )


def curve_from_rew_payload(
    payload: Mapping[str, Any],
    *,
    kind: str = "response",
    source: Mapping[str, Any] | str | None = None,
    metadata: Mapping[str, Any] | None = None,
) -> Curve:
    """Decode one REW API frequency-response payload without writing a CSV."""
    magnitude_value = payload.get("magnitude", payload.get("magnitudes"))
    if magnitude_value is None:
        raise ValueError("REW payload has no magnitude array")
    magnitudes = _decode_float32_be(magnitude_value, "magnitude")
    phase_value = payload.get("phase", payload.get("phases"))
    phases = _decode_float32_be(phase_value, "phase") if phase_value is not None else [None] * len(magnitudes)
    if len(phases) != len(magnitudes):
        raise ValueError("REW phase and magnitude arrays have different lengths")
    explicit = payload.get("frequency", payload.get("frequencies"))
    if explicit is not None:
        frequencies = _decode_float32_be(explicit, "frequency")
    else:
        start = payload.get("startFreq", payload.get("startFrequency"))
        ppo = payload.get("ppo", payload.get("pointsPerOctave"))
        step = payload.get("freqStep", payload.get("frequencyStep"))
        if start is None:
            raise ValueError("REW payload lacks frequency-axis metadata")
        start_f = _float(start, "start frequency")
        if ppo is not None:
            ppo_f = _float(ppo, "points per octave")
            if start_f <= 0 or ppo_f <= 0:
                raise ValueError("logarithmic frequency axis needs positive start and PPO")
            frequencies = [start_f * 2 ** (index / ppo_f) for index in range(len(magnitudes))]
        elif step is not None:
            step_f = _float(step, "frequency step")
            frequencies = [start_f + index * step_f for index in range(len(magnitudes))]
        else:
            raise ValueError("REW payload lacks frequency step or points-per-octave")
    if len(frequencies) != len(magnitudes):
        raise ValueError("REW frequency and magnitude arrays have different lengths")
    combined_metadata = dict(metadata or {})
    for key in ("unit", "smoothing", "ppo", "startFreq", "freqStep"):
        if key in payload:
            combined_metadata[key] = payload[key]
    unit = str(payload["unit"]) if payload.get("unit") is not None else None
    return curve_from_rows(zip(frequencies, magnitudes, phases), kind=kind, unit=unit,
                           source=source, metadata=combined_metadata)


def _metadata_from_comments(comments: Sequence[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for comment in comments:
        if ":" in comment:
            key, value = comment.split(":", 1)
            key = key.strip()[:120]
            if key and len(result) < 64:
                result[key] = value.strip()[:500]
    return result


def _infer_curve_kind(path: Path, header: str, requested: str | None) -> tuple[str, str | None]:
    if requested:
        return requested, "ohm" if requested == "impedance" else None
    text = header.lower()
    if path.suffix.lower() == ".zma" or "z(ohm" in text or "z_ohm" in text:
        return "impedance", "ohm"
    return "response", "dB" if (path.suffix.lower() == ".frd" or "spl" in text) else None


def parse_curve(path: str | Path, *, kind: str | None = None, unit: str | None = None) -> Curve:
    """Parse a REW text FRD/ZMA or an extracted frequency-response CSV."""
    source_path = Path(path)
    comments: list[str] = []
    parsed: list[tuple[float, float, float | None]] = []
    skipped = 0
    header = ""
    with source_path.open("r", encoding="utf-8-sig", errors="replace", newline="") as handle:
        for line_number, raw_line in enumerate(handle, 1):
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith(("*", "#")):
                comments.append(line[1:].strip())
                continue
            fields = [part for part in re.split(r"[,;\t ]+", line) if part]
            if len(fields) < 2:
                skipped += 1
                continue
            try:
                values = (float(fields[0]), float(fields[1]),
                          float(fields[2]) if len(fields) >= 3 and fields[2] != "" else None)
            except ValueError:
                if any(word in line.lower() for word in ("freq", "magnitude", "spl(", "z(ohm")):
                    header = line[:500]
                else:
                    skipped += 1
                continue
            parsed.append(values)
    if not parsed:
        raise ValueError(f"{source_path} contains no recognisable curve data")
    inferred_kind, inferred_unit = _infer_curve_kind(source_path, header, kind)
    warnings = [f"{skipped} malformed data-like line(s) were skipped"] if skipped else []
    metadata: dict[str, Any] = _metadata_from_comments(comments)
    if header:
        metadata["columns"] = header
    return curve_from_rows(parsed, kind=inferred_kind, unit=unit or inferred_unit,
                           source=_source_for_path(source_path), metadata=metadata,
                           warnings=warnings)


def _impulse_row_values(row: Sequence[Any] | Mapping[str, Any]) -> tuple[Any, Any]:
    if isinstance(row, Mapping):
        lowered = {str(key).strip().lower(): value for key, value in row.items()}
        time = next((lowered[key] for key in ("time_s", "time", "seconds") if key in lowered), None)
        amplitude = next((lowered[key] for key in ("amplitude", "data", "value") if key in lowered), None)
        if time is None or amplitude is None:
            raise ValueError("impulse mapping rows require time and amplitude fields")
        return time, amplitude
    if len(row) < 2:
        raise ValueError("impulse rows require time and amplitude")
    return row[0], row[1]


def _derive_sample_rate(times: Sequence[float]) -> float:
    if len(times) < 2:
        raise ValueError("at least two impulse samples are required to establish sample rate")
    intervals = [b - a for a, b in zip(times, times[1:])]
    if any(not math.isfinite(value) or value <= 0 for value in intervals):
        raise ValueError("impulse times must be finite and strictly increasing")
    ordered = sorted(intervals)
    median = ordered[len(ordered) // 2]
    tolerance = max(1e-12, abs(median) * 1e-5)
    if max(abs(value - median) for value in intervals) > tolerance:
        raise ValueError("impulse sample times are not uniformly spaced")
    return 1.0 / median


def impulse_from_rows(
    rows: Iterable[Sequence[Any] | Mapping[str, Any]],
    *,
    source: Mapping[str, Any] | str | None = None,
    metadata: Mapping[str, Any] | None = None,
    sample_rate_hz: float | None = None,
) -> Impulse:
    times: list[float] = []
    amplitudes: list[float] = []
    for index, row in enumerate(rows, 1):
        time_value, amplitude_value = _impulse_row_values(row)
        times.append(_float(time_value, f"row {index} time"))
        amplitudes.append(_float(amplitude_value, f"row {index} amplitude"))
    if not times:
        raise ValueError("impulse contains no data rows")
    derived_rate = _derive_sample_rate(times)
    if sample_rate_hz is not None:
        requested_rate = _float(sample_rate_hz, "sample rate")
        if requested_rate <= 0:
            raise ValueError("sample rate must be positive")
        if not math.isclose(derived_rate, requested_rate, rel_tol=1e-4, abs_tol=1e-6):
            raise ValueError(
                f"time axis implies {derived_rate:.9g} Hz, not requested {requested_rate:.9g} Hz"
            )
    else:
        requested_rate = derived_rate
    warnings: list[str] = []
    nonfinite = sum(not math.isfinite(value) for value in amplitudes)
    if nonfinite:
        warnings.append(f"{nonfinite} impulse amplitude(s) are non-finite")
    return Impulse(tuple(times), tuple(amplitudes), requested_rate,
                   _normalise_source(source), dict(metadata or {}), tuple(warnings))


def impulse_from_rew_payload(
    payload: Mapping[str, Any],
    *,
    source: Mapping[str, Any] | str | None = None,
    metadata: Mapping[str, Any] | None = None,
    sample_rate_hz: float | None = None,
) -> Impulse:
    data = payload.get("data")
    if data is None:
        raise ValueError("REW payload has no impulse data array")
    amplitudes = _decode_float32_be(data, "data")
    start = _float(payload.get("startTime", payload.get("startTimeSeconds", 0.0)), "start time")
    interval_value = payload.get("sampleInterval", payload.get("sampleIntervalSeconds"))
    if interval_value is None:
        if sample_rate_hz is None:
            raise ValueError("REW impulse payload needs sample interval or explicit sample rate")
        interval = 1.0 / _float(sample_rate_hz, "sample rate")
    else:
        interval = _float(interval_value, "sample interval")
    if interval <= 0:
        raise ValueError("sample interval must be positive")
    rows = ((start + index * interval, value) for index, value in enumerate(amplitudes))
    combined = dict(metadata or {})
    for key in ("unit", "startTime", "sampleInterval"):
        if key in payload:
            combined[key] = payload[key]
    return impulse_from_rows(rows, source=source, metadata=combined,
                             sample_rate_hz=sample_rate_hz or 1.0 / interval)


def parse_impulse(path: str | Path, *, sample_rate_hz: float | None = None) -> Impulse:
    """Parse REW impulse CSV or a direct REW impulse-response JSON payload."""
    source_path = Path(path)
    if source_path.suffix.lower() == ".json":
        payload = json.loads(source_path.read_text(encoding="utf-8"))
        if not isinstance(payload, Mapping):
            raise ValueError("impulse JSON root must be an object")
        return impulse_from_rew_payload(payload, source=_source_for_path(source_path),
                                        sample_rate_hz=sample_rate_hz)
    rows: list[tuple[float, float]] = []
    with source_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("impulse CSV needs a header")
        for row in reader:
            time_value, amplitude_value = _impulse_row_values(row)
            rows.append((_float(time_value, "time"), _float(amplitude_value, "amplitude")))
    return impulse_from_rows(rows, source=_source_for_path(source_path), sample_rate_hz=sample_rate_hz)


def _band_tuple(band: Sequence[float] | None) -> tuple[float, float] | None:
    if band is None:
        return None
    if len(band) != 2:
        raise ValueError("band requires exactly low and high frequencies")
    low, high = map(float, band)
    if not math.isfinite(low) or not math.isfinite(high) or low <= 0 or high <= low:
        raise ValueError("band must be finite, positive, and ordered low < high")
    return low, high


def _valid_curve_rows(curve: Curve, band: Sequence[float] | None = None,
                      *, require_phase: bool = False) -> list[tuple[float, float, float | None]]:
    limits = _band_tuple(band)
    result = []
    for frequency, magnitude, phase in zip(
            curve.frequencies_hz, curve.magnitudes, curve.phases_degrees):
        if limits and not (limits[0] <= frequency <= limits[1]):
            continue
        if not math.isfinite(frequency) or not math.isfinite(magnitude):
            continue
        if phase is not None and not math.isfinite(phase):
            continue
        if require_phase and phase is None:
            raise ValueError("analysis requires phase at every selected sample")
        result.append((frequency, magnitude, phase))
    if not result:
        raise ValueError("no finite curve samples fall within the requested band")
    return result


def _grid_description(frequencies: Sequence[float]) -> dict[str, Any]:
    if len(frequencies) < 2:
        return {"type": "single-point"}
    increments = [b - a for a, b in zip(frequencies, frequencies[1:])]
    if all(value > 0 for value in increments):
        mean_step = sum(increments) / len(increments)
        linear_error = max(abs(value - mean_step) for value in increments)
        if linear_error <= max(1e-9, abs(mean_step) * 1e-5):
            return {"type": "linear", "stepHz": mean_step}
        if all(value > 0 for value in frequencies):
            ratios = [b / a for a, b in zip(frequencies, frequencies[1:])]
            mean_ratio = sum(ratios) / len(ratios)
            ratio_error = max(abs(value - mean_ratio) for value in ratios)
            if ratio_error <= max(1e-12, abs(mean_ratio) * 1e-6):
                return {"type": "logarithmic", "pointsPerOctave": math.log(2) / math.log(mean_ratio)}
    return {"type": "irregular"}


def _extreme(rows: Sequence[tuple[float, float, Any]], values: Sequence[float],
             mode: str) -> dict[str, float]:
    index = min(range(len(values)), key=values.__getitem__) if mode == "min" \
        else max(range(len(values)), key=values.__getitem__)
    return {"value": values[index], "frequencyHz": rows[index][0]}


def summarize_curve(curve: Curve, *, band: Sequence[float] | None = None) -> dict[str, Any]:
    """Return compact source, validation, grid, and extrema facts."""
    rows = _valid_curve_rows(curve, band)
    frequencies = [row[0] for row in rows]
    magnitudes = [row[1] for row in rows]
    phases = [row[2] for row in rows if row[2] is not None]
    result: dict[str, Any] = {
        "schema": SCHEMA,
        "operation": "inspect",
        "source": dict(curve.source),
        "parameters": {"bandHz": list(_band_tuple(band)) if band else None},
        "validation": {
            "sourceSampleCount": len(curve.frequencies_hz),
            "selectedFiniteSampleCount": len(rows),
            "warnings": list(curve.warnings),
        },
        "analysis": {
            "kind": curve.kind,
            "unit": curve.unit,
            "frequencyRangeHz": [min(frequencies), max(frequencies)],
            "grid": _grid_description(frequencies),
            "magnitude": {
                "minimum": _extreme(rows, magnitudes, "min"),
                "maximum": _extreme(rows, magnitudes, "max"),
            },
            "phaseAvailable": len(phases) == len(rows),
        },
    }
    if phases:
        phase_rows = [row for row in rows if row[2] is not None]
        result["analysis"]["phaseDegrees"] = {
            "minimum": _extreme(phase_rows, phases, "min"),
            "maximum": _extreme(phase_rows, phases, "max"),
        }
    if curve.metadata:
        result["metadata"] = dict(curve.metadata)
    return result


def _strict_curve(curve: Curve, *, require_phase: bool = False) -> list[tuple[float, float, float | None]]:
    rows = _valid_curve_rows(curve, require_phase=require_phase)
    frequencies = [row[0] for row in rows]
    if len(rows) != len(curve.frequencies_hz):
        raise ValueError("analysis requires all source rows to be finite")
    if any(b <= a for a, b in zip(frequencies, frequencies[1:])):
        raise ValueError("analysis requires a strictly increasing, duplicate-free frequency grid")
    return rows


def _wrapped_degrees(value: float) -> float:
    wrapped = (value + 180.0) % 360.0 - 180.0
    return 180.0 if wrapped == -180.0 and value > 0 else wrapped


def _interpolate_curve(curve: Curve, frequency: float) -> tuple[float, float | None]:
    rows = _strict_curve(curve)
    frequencies = [row[0] for row in rows]
    index = bisect_left(frequencies, frequency)
    if index < len(rows) and math.isclose(frequencies[index], frequency, rel_tol=0.0, abs_tol=1e-9):
        return rows[index][1], rows[index][2]
    if index == 0 or index == len(rows):
        raise ValueError(f"{frequency:g} Hz is outside the source frequency range")
    left, right = rows[index - 1], rows[index]
    fraction = (frequency - left[0]) / (right[0] - left[0])
    magnitude = left[1] + fraction * (right[1] - left[1])
    if left[2] is None or right[2] is None:
        phase = None
    else:
        phase = _wrapped_degrees(left[2] + fraction * _wrapped_degrees(right[2] - left[2]))
    return magnitude, phase


def query_points(curve: Curve, frequencies: Iterable[float], *, method: str = "nearest") -> dict[str, Any]:
    if method not in ("nearest", "interpolate"):
        raise ValueError("point method must be 'nearest' or 'interpolate'")
    rows = _strict_curve(curve)
    source_frequencies = [row[0] for row in rows]
    points = []
    for requested in frequencies:
        frequency = _float(requested, "requested frequency")
        if frequency <= 0:
            raise ValueError("requested frequencies must be positive")
        if method == "nearest":
            index = bisect_left(source_frequencies, frequency)
            candidates = [candidate for candidate in (index - 1, index) if 0 <= candidate < len(rows)]
            selected = min(candidates, key=lambda item: abs(rows[item][0] - frequency))
            actual, magnitude, phase = rows[selected]
            point = {"requestedFrequencyHz": frequency, "sourceFrequencyHz": actual,
                     "magnitude": magnitude, "phaseDegrees": phase}
        else:
            magnitude, phase = _interpolate_curve(curve, frequency)
            point = {"requestedFrequencyHz": frequency, "magnitude": magnitude,
                     "phaseDegrees": phase}
        if curve.kind == "impedance" and phase is not None:
            radians = math.radians(phase)
            point["realOhm"] = magnitude * math.cos(radians)
            point["imaginaryOhm"] = magnitude * math.sin(radians)
        points.append(point)
    return {
        "schema": SCHEMA,
        "operation": "points",
        "source": dict(curve.source),
        "parameters": {"method": method, "frequenciesHz": [point["requestedFrequencyHz"] for point in points]},
        "result": points,
        "warnings": list(curve.warnings),
    }


def _epdr(impedance_ohm: float, phase_degrees: float) -> float:
    angle = abs(math.radians(_wrapped_degrees(phase_degrees)))
    factor = 4.0 * (1.0 - math.sin(5.0 * math.pi / 6.0 + 2.0 * angle / 3.0)) \
        * math.sin(5.0 * math.pi / 6.0 - angle / 3.0)
    if factor <= 0:
        return math.inf
    return impedance_ohm / factor


def _crossing(rows: Sequence[tuple[float, float, Any]], start: int, direction: int,
              threshold: float) -> float | None:
    index = start
    while 0 <= index + direction < len(rows):
        following = index + direction
        y1, y2 = rows[index][1], rows[following][1]
        if (y1 - threshold) * (y2 - threshold) <= 0 and y1 != y2:
            fraction = (threshold - y1) / (y2 - y1)
            return rows[index][0] + fraction * (rows[following][0] - rows[index][0])
        index = following
    return None


def summarize_impedance(
    curve: Curve,
    *,
    band: Sequence[float] | None = None,
    q_band: Sequence[float] | None = None,
    q_threshold_ohm: float | None = None,
) -> dict[str, Any]:
    """Summarise complex impedance, ideal class-B EPDR, and optional peak Q."""
    if curve.kind != "impedance":
        raise ValueError("impedance analysis requires kind='impedance'")
    _strict_curve(curve, require_phase=True)
    rows = _valid_curve_rows(curve, band, require_phase=True)
    magnitudes = [row[1] for row in rows]
    real = [row[1] * math.cos(math.radians(row[2])) for row in rows]  # type: ignore[arg-type]
    imaginary = [row[1] * math.sin(math.radians(row[2])) for row in rows]  # type: ignore[arg-type]
    phase = [row[2] for row in rows]  # type: ignore[misc]
    epdr = [_epdr(row[1], row[2]) for row in rows]  # type: ignore[arg-type]
    result: dict[str, Any] = {
        "schema": SCHEMA,
        "operation": "impedance",
        "source": dict(curve.source),
        "parameters": {
            "bandHz": list(_band_tuple(band)) if band else None,
            "qBandHz": list(_band_tuple(q_band)) if q_band else None,
            "qThresholdOhm": q_threshold_ohm,
        },
        "result": {
            "sampleCount": len(rows),
            "frequencyRangeHz": [rows[0][0], rows[-1][0]],
            "magnitudeOhm": {"minimum": _extreme(rows, magnitudes, "min"),
                             "maximum": _extreme(rows, magnitudes, "max")},
            "realOhm": {"minimum": _extreme(rows, real, "min"),
                        "maximum": _extreme(rows, real, "max")},
            "imaginaryOhm": {"minimum": _extreme(rows, imaginary, "min"),
                             "maximum": _extreme(rows, imaginary, "max")},
            "phaseDegrees": {"minimum": _extreme(rows, phase, "min"),
                             "maximum": _extreme(rows, phase, "max")},
            "idealClassBEpdrOhm": {
                "definition": "equal peak output-device dissipation, ideal full-rail class-B",
                "minimum": _extreme(rows, epdr, "min"),
            },
        },
        "warnings": list(curve.warnings),
    }
    if q_band is not None:
        q_rows = _valid_curve_rows(curve, q_band, require_phase=False)
        peak_index = max(range(len(q_rows)), key=lambda index: q_rows[index][1])
        peak = q_rows[peak_index]
        threshold = (_float(q_threshold_ohm, "Q threshold") if q_threshold_ohm is not None
                     else peak[1] / math.sqrt(2.0))
        if threshold <= 0:
            raise ValueError("Q magnitude threshold must be positive")
        low = _crossing(q_rows, peak_index, -1, threshold)
        high = _crossing(q_rows, peak_index, 1, threshold)
        q_result: dict[str, Any] = {
            "method": "explicit magnitude threshold" if q_threshold_ohm is not None
                      else "absolute magnitude peak minus 3.0103 dB",
            "peak": {"frequencyHz": peak[0], "magnitudeOhm": peak[1]},
            "thresholdOhm": threshold,
            "lowerCrossingHz": low,
            "upperCrossingHz": high,
        }
        if low is not None and high is not None and high > low:
            q_result["bandwidthHz"] = high - low
            q_result["q"] = peak[0] / (high - low)
        else:
            q_result["q"] = None
            result["warnings"].append("Q could not be calculated because both threshold crossings were not present")
        result["result"]["singleResonanceQ"] = q_result
    return result


def _stats(values: Sequence[float], frequencies: Sequence[float]) -> dict[str, Any]:
    if not values:
        raise ValueError("statistics require at least one sample")
    mean = sum(values) / len(values)
    rms = math.sqrt(sum(value * value for value in values) / len(values))
    index = max(range(len(values)), key=lambda item: abs(values[item]))
    centered = [value - mean for value in values]
    centered_rms = math.sqrt(sum(value * value for value in centered) / len(centered))
    centered_index = max(range(len(centered)), key=lambda item: abs(centered[item]))
    return {
        "mean": mean,
        "rms": rms,
        "maximumAbsolute": {"value": values[index], "absolute": abs(values[index]),
                            "frequencyHz": frequencies[index]},
        "meanRemoved": {
            "rms": centered_rms,
            "maximumAbsolute": {"value": centered[centered_index],
                                "absolute": abs(centered[centered_index]),
                                "frequencyHz": frequencies[centered_index]},
        },
    }


def _paired_curves(a: Curve, b: Curve, band: Sequence[float], grid: str) \
        -> tuple[list[float], list[float], list[float | None], list[float], list[float | None]]:
    limits = _band_tuple(band)
    if grid not in ("exact", "interpolate"):
        raise ValueError("grid must be 'exact' or 'interpolate'")
    _strict_curve(a)
    _strict_curve(b)
    a_rows = _valid_curve_rows(a, limits)
    if grid == "exact":
        b_rows = _valid_curve_rows(b, limits)
        if len(a_rows) != len(b_rows) or any(
                not math.isclose(left[0], right[0], rel_tol=0.0, abs_tol=1e-9)
                for left, right in zip(a_rows, b_rows)):
            raise ValueError("exact grid comparison requires identical selected frequency arrays")
        return ([row[0] for row in a_rows], [row[1] for row in a_rows], [row[2] for row in a_rows],
                [row[1] for row in b_rows], [row[2] for row in b_rows])
    _strict_curve(b)
    frequencies: list[float] = []
    a_mag: list[float] = []
    a_phase: list[float | None] = []
    b_mag: list[float] = []
    b_phase: list[float | None] = []
    for frequency, magnitude, phase in a_rows:
        if frequency < b.frequencies_hz[0] or frequency > b.frequencies_hz[-1]:
            continue
        interpolated_magnitude, interpolated_phase = _interpolate_curve(b, frequency)
        frequencies.append(frequency)
        a_mag.append(magnitude)
        a_phase.append(phase)
        b_mag.append(interpolated_magnitude)
        b_phase.append(interpolated_phase)
    if not frequencies:
        raise ValueError("curves have no overlapping samples in the requested band")
    return frequencies, a_mag, a_phase, b_mag, b_phase


def _unwrap(values: Sequence[float]) -> list[float]:
    if not values:
        return []
    result = [values[0]]
    for value in values[1:]:
        result.append(result[-1] + _wrapped_degrees(value - result[-1]))
    return result


def _linear_fit(x: Sequence[float], y: Sequence[float]) -> tuple[float, float]:
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    denominator = sum((value - mean_x) ** 2 for value in x)
    if denominator == 0:
        raise ValueError("delay fit requires more than one distinct frequency")
    slope = sum((x_value - mean_x) * (y_value - mean_y)
                for x_value, y_value in zip(x, y)) / denominator
    return slope, mean_y - slope * mean_x


def compare_curves(
    a: Curve,
    b: Curve,
    *,
    band: Sequence[float],
    grid: str = "exact",
    fit_gain: bool = False,
    fit_delay: bool = False,
) -> dict[str, Any]:
    """Compare curve A minus B over an explicit band and explicit grid policy."""
    frequencies, a_mag, a_phase, b_mag, b_phase = _paired_curves(a, b, band, grid)
    magnitude_difference = [left - right for left, right in zip(a_mag, b_mag)]
    result: dict[str, Any] = {
        "schema": SCHEMA,
        "operation": "compare",
        "sources": {"a": dict(a.source), "b": dict(b.source)},
        "parameters": {"bandHz": list(_band_tuple(band)), "grid": grid,
                       "interpolation": "linear-frequency magnitude, circular phase"
                                        if grid == "interpolate" else None,
                       "fitGain": fit_gain, "fitDelay": fit_delay},
        "result": {
            "sampleCount": len(frequencies),
            "frequencyRangeHz": [frequencies[0], frequencies[-1]],
            "differenceConvention": "a-minus-b",
            "magnitude": _stats(magnitude_difference, frequencies),
        },
        "warnings": list(dict.fromkeys((*a.warnings, *b.warnings))),
    }
    if fit_gain:
        gain = sum(magnitude_difference) / len(magnitude_difference)
        result["result"]["gainFit"] = {
            "aMinusBMean": gain,
            "gainToAddToB": gain,
            "residual": _stats([value - gain for value in magnitude_difference], frequencies),
        }
    phase_available = all(value is not None for value in (*a_phase, *b_phase))
    if phase_available:
        phase_difference = [_wrapped_degrees(left - right)  # type: ignore[operator]
                            for left, right in zip(a_phase, b_phase)]
        phase_result = _stats(phase_difference, frequencies)
        sin_mean = sum(math.sin(math.radians(value)) for value in phase_difference) / len(phase_difference)
        cos_mean = sum(math.cos(math.radians(value)) for value in phase_difference) / len(phase_difference)
        phase_result["circularMeanDegrees"] = math.degrees(math.atan2(sin_mean, cos_mean))
        result["result"]["phaseDegrees"] = phase_result
        if fit_delay:
            slope, intercept = _linear_fit(frequencies, _unwrap(phase_difference))
            delay = -slope / 360.0
            corrected = [_wrapped_degrees(value + 360.0 * frequency * delay)
                         for frequency, value in zip(frequencies, phase_difference)]
            result["result"]["delayFit"] = {
                "secondsToAddInCorrection": delay,
                "microsecondsToAddInCorrection": delay * 1e6,
                "unwrappedSlopeDegreesPerHz": slope,
                "unwrappedInterceptDegrees": intercept,
                "correctedPhaseDegrees": _stats(corrected, frequencies),
            }
    elif fit_delay:
        raise ValueError("delay fit requires phase in both curves")
    else:
        result["warnings"].append("phase comparison omitted because one or both curves lack phase")
    return result


def compare_polar(
    reference: Curve,
    curves: Mapping[str, Curve],
    *,
    band: Sequence[float],
    grid: str = "exact",
    frequencies: Iterable[float] = (),
) -> dict[str, Any]:
    """Compare named off-axis curves to one reference without returning arrays."""
    requested_points = tuple(float(value) for value in frequencies)
    comparisons: dict[str, Any] = {}
    warnings: list[str] = list(reference.warnings)
    for name, curve in curves.items():
        compared = compare_curves(curve, reference, band=band, grid=grid)
        magnitude = compared["result"]["magnitude"]
        entry: dict[str, Any] = {
            "sampleCount": compared["result"]["sampleCount"],
            "frequencyRangeHz": compared["result"]["frequencyRangeHz"],
            "offAxisMinusReferenceMagnitude": magnitude,
            "maximumOffAxisExcess": magnitude["maximumAbsolute"],
        }
        # The signed maximum, rather than maximum absolute, answers excess directly.
        paired = _paired_curves(curve, reference, band, grid)
        deltas = [left - right for left, right in zip(paired[1], paired[3])]
        maximum_index = max(range(len(deltas)), key=deltas.__getitem__)
        minimum_index = min(range(len(deltas)), key=deltas.__getitem__)
        entry["maximumOffAxisExcess"] = {
            "value": deltas[maximum_index], "frequencyHz": paired[0][maximum_index]
        }
        entry["maximumAttenuation"] = {
            "value": deltas[minimum_index], "frequencyHz": paired[0][minimum_index]
        }
        if requested_points:
            points = []
            for frequency in requested_points:
                curve_mag, _ = _interpolate_curve(curve, frequency)
                ref_mag, _ = _interpolate_curve(reference, frequency)
                points.append({"frequencyHz": frequency, "offAxisMinusReference": curve_mag - ref_mag})
            entry["selectedFrequencies"] = points
        comparisons[str(name)] = entry
        warnings.extend(curve.warnings)
    return {
        "schema": SCHEMA,
        "operation": "polar",
        "sources": {"reference": dict(reference.source),
                    "curves": {str(name): dict(curve.source) for name, curve in curves.items()}},
        "parameters": {"bandHz": list(_band_tuple(band)), "grid": grid,
                       "frequenciesHz": list(requested_points)},
        "result": comparisons,
        "warnings": list(dict.fromkeys(warnings)),
    }


def _interpolate_impulse(impulse: Impulse, time_value: float) -> float:
    times = impulse.times_s
    index = bisect_left(times, time_value)
    if index < len(times) and math.isclose(times[index], time_value, abs_tol=1e-12):
        return impulse.amplitudes[index]
    if index == 0 or index == len(times):
        raise ValueError("impulse interpolation would require extrapolation")
    fraction = (time_value - times[index - 1]) / (times[index] - times[index - 1])
    return impulse.amplitudes[index - 1] + fraction * (
        impulse.amplitudes[index] - impulse.amplitudes[index - 1])


def _impulse_pairs(a: Impulse, b: Impulse, window: Sequence[float], grid: str) \
        -> tuple[list[float], list[float], list[float]]:
    if len(window) != 2 or not all(math.isfinite(float(value)) for value in window):
        raise ValueError("impulse window needs two finite times")
    start, end = map(float, window)
    if end <= start:
        raise ValueError("impulse window must be ordered start < end")
    if grid not in ("exact", "interpolate"):
        raise ValueError("grid must be 'exact' or 'interpolate'")
    indices = [index for index, value in enumerate(a.times_s) if start <= value <= end]
    if not indices:
        raise ValueError("no A impulse samples fall within the requested window")
    times = [a.times_s[index] for index in indices]
    a_values = [a.amplitudes[index] for index in indices]
    if grid == "exact":
        b_indices = [index for index, value in enumerate(b.times_s) if start <= value <= end]
        b_times = [b.times_s[index] for index in b_indices]
        if len(times) != len(b_times) or any(
                not math.isclose(left, right, rel_tol=0.0, abs_tol=1e-12)
                for left, right in zip(times, b_times)):
            raise ValueError("exact impulse comparison requires identical time arrays in the window")
        return times, a_values, [b.amplitudes[index] for index in b_indices]
    selected = [(time_value, value) for time_value, value in zip(times, a_values)
                if b.times_s[0] <= time_value <= b.times_s[-1]]
    if not selected:
        raise ValueError("impulses have no overlapping samples in the requested window")
    return ([item[0] for item in selected], [item[1] for item in selected],
            [_interpolate_impulse(b, item[0]) for item in selected])


def _correlation(a: Sequence[float], b: Sequence[float]) -> float | None:
    mean_a = sum(a) / len(a)
    mean_b = sum(b) / len(b)
    centered_a = [value - mean_a for value in a]
    centered_b = [value - mean_b for value in b]
    denominator = math.sqrt(sum(value * value for value in centered_a)
                            * sum(value * value for value in centered_b))
    if denominator == 0:
        return None
    return sum(left * right for left, right in zip(centered_a, centered_b)) / denominator


def _lag_fit(a: Sequence[float], b: Sequence[float], max_lag: int) -> tuple[int, float | None]:
    best_lag = 0
    best_correlation: float | None = None
    for lag in range(-max_lag, max_lag + 1):
        if lag < 0:
            left, right = a[-lag:], b[:len(b) + lag]
        elif lag > 0:
            left, right = a[:len(a) - lag], b[lag:]
        else:
            left, right = a, b
        if len(left) < 2:
            continue
        correlation = _correlation(left, right)
        if correlation is not None and (best_correlation is None or correlation > best_correlation):
            best_lag, best_correlation = lag, correlation
    return best_lag, best_correlation


def compare_impulses(
    a: Impulse,
    b: Impulse,
    *,
    window: Sequence[float],
    sample_rate_hz: float | None = None,
    grid: str = "exact",
    fit_gain: bool = True,
    max_lag_s: float = 0.0,
) -> dict[str, Any]:
    """Compare impulses on an explicit time window with optional discrete delay fit."""
    rate = _float(sample_rate_hz, "sample rate") if sample_rate_hz is not None else a.sample_rate_hz
    if rate <= 0:
        raise ValueError("sample rate must be positive")
    if not math.isclose(a.sample_rate_hz, rate, rel_tol=1e-4) or not math.isclose(
            b.sample_rate_hz, rate, rel_tol=1e-4):
        raise ValueError("both impulses must match the explicit or derived sample rate")
    if max_lag_s < 0:
        raise ValueError("maximum lag must not be negative")
    times, a_values, b_values = _impulse_pairs(a, b, window, grid)
    window_sample_count = len(times)
    max_lag_samples = int(round(max_lag_s * rate))
    lag, _ = _lag_fit(a_values, b_values, max_lag_samples)
    if lag < 0:
        times = times[-lag:]
        a_values = a_values[-lag:]
        b_values = b_values[:len(b_values) + lag]
    elif lag > 0:
        times = times[:len(times) - lag]
        a_values = a_values[:len(a_values) - lag]
        b_values = b_values[lag:]
    if not times:
        raise ValueError("delay fit leaves no overlapping impulse samples")
    gain = 1.0
    if fit_gain:
        denominator = sum(value * value for value in b_values)
        if denominator == 0:
            raise ValueError("gain fit cannot use an all-zero B impulse")
        gain = sum(left * right for left, right in zip(a_values, b_values)) / denominator
    fitted_b = [gain * value for value in b_values]
    residual = [left - right for left, right in zip(a_values, fitted_b)]
    rms = lambda values: math.sqrt(sum(value * value for value in values) / len(values))
    lag_correlation = _correlation(a_values, fitted_b)
    result: dict[str, Any] = {
        "schema": SCHEMA,
        "operation": "impulse-compare",
        "sources": {"a": dict(a.source), "b": dict(b.source)},
        "parameters": {"windowSeconds": list(map(float, window)), "sampleRateHz": rate,
                       "grid": grid, "fitGain": fit_gain, "maximumLagSeconds": max_lag_s},
        "result": {
            "windowSampleCountBeforeDelayFit": window_sample_count,
            "sampleCount": len(times),
            "actualWindowSeconds": [times[0], times[-1]],
            "gainToMultiplyB": gain,
            "correlation": _correlation(a_values, fitted_b),
            "aRms": rms(a_values),
            "fittedBRms": rms(fitted_b),
            "residualRms": rms(residual),
            "maximumAbsoluteResidual": max(abs(value) for value in residual),
            "delayFit": {
                "lagSamplesOfBRelativeToA": lag,
                "lagSecondsOfBRelativeToA": lag / rate,
                "correlationAtLag": lag_correlation,
                "resolutionSeconds": 1.0 / rate,
            },
        },
        "warnings": list(dict.fromkeys((*a.warnings, *b.warnings))),
    }
    return result
