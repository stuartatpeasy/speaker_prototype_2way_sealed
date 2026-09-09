# Compact Measurement Data Tooling

| State | Value |
| --- | --- |
| Lifecycle | **CURRENT SUPPORTING REFERENCE** |
| Owns | Compact commands for FRD, ZMA, extracted REW response/impulse, `.mdat`, and VituixCAD VXP inspection or comparison |
| Does not own | Raw measurement authority, measurement procedures, driver baselines, crossover conclusions, or live REW qualification |
| Read when | A task needs facts from a large supported data file, a comparison between files, or maintenance of these tools |
| Current approved action | Use the narrowest applicable command before reading raw rows or writing a temporary parser |
| Limitations | `.mdat` needs a running REW API and mutates its workspace; VXP analysis audits stored semantics and sources but does not solve the circuit |
| Last reviewed | 2026-09-09 |

## 1. Authority and output policy

The retained FRD, ZMA, `.mdat`, impulse export, or VXP remains the source
authority. Tool output is a derived convenience summary. Each file-based result
identifies its source path, size, and SHA-256 hash; analysis results also record
the requested band, grid policy, points, window, or fit choices and any parser
warnings.

Use these commands to keep full sample arrays inside the process and return only
decision-relevant JSON. Start with a narrow band or small point set. Read raw
rows only when investigating an anomaly, checking the parser, or answering a
question outside the supported analyses. If the same missing analysis is likely
to recur, add it to the committed tool and tests instead of leaving its only
implementation in `/tmp`.

All three tools use only the Python standard library and write their normal
results to standard output. Run them from the project root with `python3` in WSL
or replace `python3` with `.venv\Scripts\python.exe` in Windows PowerShell.

## 2. FRD, ZMA, and extracted response or impulse data

[`src/measurement_summary.py`](../src/measurement_summary.py) is the command-line
front end; [`src/measurement_analysis.py`](../src/measurement_analysis.py) is its
reusable in-memory implementation. The parser accepts REW text FRD/ZMA files,
frequency-response CSV written by the REW API client, and impulse CSV or a saved
REW impulse-response JSON payload.

### 2.1 Inspect one curve or selected points

```text
python3 src/measurement_summary.py inspect FILE --band LOW_HZ HIGH_HZ
python3 src/measurement_summary.py points FILE --frequency HZ --frequency HZ --method interpolate
```

`inspect` reports source and selected sample counts, frequency range and grid,
magnitude/phase availability and extrema, metadata, and validation warnings.
`points` uses either the nearest retained sample or explicit interpolation. For
impedance data it also converts magnitude and phase to real and imaginary ohms.

### 2.2 Impedance and EPDR

```text
python3 src/measurement_summary.py impedance FILE --band LOW_HZ HIGH_HZ
```

This reports extrema of magnitude, phase, real and imaginary impedance, plus the
minimum ideal full-rail class-B EPDR. Optional `--q-band LOW HIGH` requests a
single-peak magnitude-bandwidth estimate; `--q-threshold-ohm VALUE` supplies its
explicit crossing threshold. This is not a fitted loudspeaker equivalent-circuit
or Thiele-Small parameter extraction.

### 2.3 Curve and polar comparisons

```text
python3 src/measurement_summary.py compare A B --band LOW_HZ HIGH_HZ --grid exact
python3 src/measurement_summary.py polar REFERENCE --curve 20deg=FILE --curve 40deg=FILE --band LOW_HZ HIGH_HZ --grid interpolate --frequency HZ
```

`compare` uses the signed convention A minus B and reports compact magnitude and
circular-phase statistics. `--fit-gain` removes a constant magnitude offset;
`--fit-delay` reports the delay correction implied by the unwrapped phase slope.
`exact` refuses mismatched grids. `interpolate` evaluates B on A's in-band grid
without extrapolation. The polar form reports attenuation, any off-axis excess,
and optional selected-frequency differences for named curves.

### 2.4 Impulse comparison

```text
python3 src/measurement_summary.py impulse A B --window START_S END_S --grid exact --max-lag-ms VALUE
```

The required window and grid policy prevent an accidental whole-response or
implicit-resampling comparison. The result reports gain, correlation, RMS and
maximum residual, and an optional sample-quantised delay fit bounded by
`--max-lag-ms`. Gain fitting is on by default; add `--no-fit-gain` to compare
absolute amplitudes. Use `--sample-rate-hz` when the rate must be asserted rather
than derived from the time columns.

## 3. Compact `.mdat` analysis through REW

[`src/rew_api_extract.py`](../src/rew_api_extract.py) delegates binary `.mdat`
interpretation to REW, then calls the same in-memory analysis functions:

```text
python3 src/rew_api_extract.py summarize FILE --band LOW_HZ HIGH_HZ --frequency-unit UNIT --smoothing None --ppo 96 --at HZ
```

The result contains no raw arrays and writes no files. The band and unit are
required; `--measurement` and `--at` are repeatable. For `ohm`, the output adds
real/imaginary extrema and EPDR. It records the source hash, REW versions,
request settings, returned scalar metadata, warnings, and the fact that loading
the file added measurements to the current REW workspace. The workspace is not
saved or cleaned up. Runtime setup, live-access constraints, extraction, and
qualification are owned by the [REW API client](REW_API_CLIENT.md).

The default `96` PPO is a compact, consistent review grid. Because REW may apply
PPO/2 anti-alias smoothing during resampling, use the full extraction route with
PPO omitted when a native-grid extremum or narrow feature could affect the
decision.

## 4. VituixCAD VXP summary and semantic comparison

[`src/vxp_summary.py`](../src/vxp_summary.py) parses the XML VXP without opening
VituixCAD:

```text
python3 src/vxp_summary.py summary FILE
python3 src/vxp_summary.py compare LEFT RIGHT --max-differences 25
```

`summary` reports global project settings, driver FRD/ZMA assignments and their
existence, angular responses, scale/delay/polarity/minimum-phase settings, and
crossover component values and parasitics. Stored Windows paths are mapped into
the current checkout when possible. `compare` returns a bounded normalized
semantic diff and deliberately excludes schematic layout-only movement.

This is a source/reference and configuration audit, not a circuit solver. It
does not calculate acoustic summation, load impedance, transfer functions, or
whether two differently drawn networks are electrically equivalent. Use
VituixCAD and retained measurement evidence for those questions.

## 5. Verification and reconstruction

Run the complete standard-library suite after changing any tool:

```text
python3 -m unittest discover -s tests -v
python3 -m py_compile src/measurement_analysis.py src/measurement_summary.py src/rew_api_extract.py src/vxp_summary.py
```

Representative retained-data checks should confirm that:

- the installed-axis FRD contains `31,404` samples and its retained polar copy
  compares with zero magnitude and phase difference;
- the 2026-09-09 Seed A ZMA reproduces approximately `4.3664 ohm` minimum
  magnitude, `4.28443 ohm` minimum real part, and `2.56334 ohm` minimum EPDR;
  and
- each retained VXP parses, the practical project reports two drivers and eight
  electrical components, and no referenced FRD/ZMA source is missing.

No new ignored output class is required: summaries normally remain on standard
output, and disposable redirected results may use the existing ignored
`outputs/` tree. Reconstruct a summary from the retained source, its recorded
hash, the committed tool, and the recorded command parameters.
