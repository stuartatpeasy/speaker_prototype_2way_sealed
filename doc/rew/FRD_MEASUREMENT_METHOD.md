# Installed-Driver FRD Measurement Method

Lifecycle: **METHOD**
Owns: interface-neutral geometry, timing, repeatability, windowing, naming, and
provenance requirements for installed-driver acoustic measurements.
Does not own: interface qualification, fixture operation, a particular
driver's safe sweep limits, or authorisation to power equipment.
Last reviewed: 2026-09-09

## 1. Objective And Evidence Boundary

The objective is a reusable complex frequency response—magnitude and phase—of
one installed driver in the actual prototype. Measurements intended for
crossover work must share a physical reference, timing convention, geometry,
level convention, and documented impulse-response window. A visually smooth
trace is not sufficient if its timing, calibration, or provenance is unknown.

Use the applicable interface runbook for connection, level, and safety gates.
For the currently qualified UMC22 woofer route that authority is
[`procedures/UMC22_INSTALLED_WOOFER_FRD.md`](procedures/UMC22_INSTALLED_WOOFER_FRD.md).
The UMC202HD route remains suspended under
[`procedures/UMC202HD_FRD_SUSPENDED.md`](procedures/UMC202HD_FRD_SUSPENDED.md).

Evidence classes used here are:

- **USER-REPORTED** for the present physical state or geometry;
- **VERIFIED MEASUREMENT** for stored observations with identified conditions;
- **DERIVED** for quantities calculated from those observations;
- **INFERRED** for plausible explanations that are not uniquely established;
- **PROVISIONAL DECISION** for a reversible working choice; and
- **OPEN ITEM** for an unresolved input or gate.

## 2. Reference Planes And Common Timing

For full-dual measurement, one input records the microphone and the other
records a protected electrical reference derived from the electrical reference
plane selected for the unit under test. The ordinary woofer route samples the
driver/amplifier output directly; the protected-tweeter route deliberately
samples the tweeter terminals after its series capacitor. Keep the loudspeaker
cable unchanged within a driver set and record any later change of reference
plane.

With REW's `Make calibration data from loopback response` option, the measured
reference response becomes a correction curve whose magnitude is defined as
`0 dB` at `1 kHz`. Frequency-dependent response of the reference path is
therefore removed, but a deliberate network's gain at `1 kHz` remains as a
constant magnitude offset. Correct that scalar during modelling from the
measured network and complex driver load; do not add a second phase or timing
correction to a valid common-timed FRD. For protected-tweeter C2 the retained
derived model correction is `+11.14 dB`.

The electrical reference supplies common timing. Both drivers must use the same
timing convention: do not independently align woofer and tweeter peaks, because
that erases their real relative acoustic delay. A timing offset may remove a
chosen common propagation delay only after one valid impulse is inspected and
the same offset is then applied to the complete set.

At a nominal distance `d = 1.000 m` and sound speed `c = 343 m/s`, the direct
time of flight is:

```text
t = d / c = 1.000 m / 343 m/s = 0.002915 s = 2.915 ms
```

The units reduce to seconds, as they should. This is a geometry check, not a
replacement for the measured impulse and timing-reference metadata.

## 3. Geometry And Physical Control

Record at minimum:

- microphone capsule to the chosen baffle-plane reference point;
- capsule and relevant driver-centre heights;
- horizontal and vertical microphone alignment;
- microphone incidence corresponding to the selected calibration file;
- cabinet angle and rotation-axis definition;
- distances to floor, ceiling, rear wall, and nearest side wall;
- enclosure fill, connected driver, speaker cable, and room boundary state;
- doors/windows and any material airflow capable of moving a stand, cable, or
  light object; and
- objects or supports close enough to create an early reflection.

For the established prototype setup, the nominal on-axis distance is `1000 mm`.
The microphone is fixed and aimed at the cabinet; the loudspeaker may later be
rotated on its secured, 10-degree-marked jig. During an on-axis repeatability
set, do not move the cabinet, microphone, stands, cables, fixture, or nearby
objects.

Geometry determines the available reflection-free time. At `1040 mm` source
and microphone height in the documented room, calculated floor and ceiling
reflections begin at approximately `3.81 ms` and the wall behind the cabinet at
approximately `3.91 ms`. These estimates identify where to inspect the ETC;
they do not prescribe a final window before the actual impulse is captured.

## 4. Capture Plan

Before excitation, record the exact application version, driver mode, device
endpoints, sample rate, channel routing, timing mode, calibration treatment,
timing offset, sweep range, level, sweep length, repetitions, clipping-abort
state, and measurement name. Confirm no unrelated application can send audio
to the interface.

Use one controlled first capture when the route, driver, protection, timing
mode, or geometry is new or materially changed. Immediately afterward inspect:

1. both input headrooms and any clipping warning;
2. the stored microphone and soundcard-calibration metadata;
3. measurement and reference input/output identities;
4. timing-reference index, System Delay, IR start, and clock adjustment;
5. the direct impulse and ETC for a single plausible dominant arrival;
6. audible or equipment abnormalities during the sweep; and
7. whether the proposed right window excludes the first material reflection.

Do not continue the batch before that review when the active runbook imposes a
one-capture gate. Once the first capture passes, the runbook may release a
bounded batch of named captures to run consecutively under one unchanged-state
declaration and common stop rules. Do not require a fresh settings recital
between captures. Repeat the physical/no-signal audit only after a reported
change, power-cycle or reconnection relevant to the route, REW endpoint/state
change, anomaly, or a new measurement day—not merely because a chat changed.

Where available, use the current [REW API client](../REW_API_CLIENT.md) for a
read-only pre-capture session snapshot and a selected-measurement extraction
from the saved `.mdat`. This provides a reproducible check of API-exposed
settings, measurement summary, native response, stored windows, and impulse
samples without making a convenience export authoritative. Preserve manual
evidence for physical state, geometry, displayed headroom, timing-reference
sample index, historical per-measurement routing, and any result the client
does not expose.

API extraction loads the source `.mdat` into the current REW workspace and
leaves the loaded copies there. Perform it after the live series is complete
or in a disposable session, and keep API-loaded duplicates out of the retained
production `.mdat`.

After the first capture passes, one immediate unchanged repeat is normally
enough for prototype-design repeatability evidence. Add a third in the same
bounded batch when it has low incremental cost, when the first pair disagrees,
or when a new chain genuinely needs stronger qualification. Store the batch in
raw REW data without overwriting prior diagnostic evidence.

## 5. Repeatability Evaluation

Use two different gates for two different questions. Do not demand laboratory-
like agreement over every FFT bin when deciding whether a capture is useful for
an iterative prototype crossover.

For **interface/direct-path qualification**, a short common direct-sound window
should retain the existing tight target: approximately `0.2 dB` maximum spread
over `1-5 kHz`, System Delay spread preferably no greater than `5 us`, nearly
coincident phase, and no microphone/reference clipping or dropout. This asks
whether the chain repeats before room and later decay dominate.

For **initial crossover-design release** with the documented production window,
the project acceptance targets are:

- no clipping, dropout, warning that invalidates the capture, or route/timing/
  calibration inconsistency;
- System Delay spread preferably no greater than `5 us`;
- unsmoothed `1-5 kHz` pairwise magnitude RMS no greater than approximately
  `0.25 dB`;
- unsmoothed maximum magnitude difference over the current intended crossover
  band no greater than approximately `0.25 dB`;
- maximum circular phase difference over the current intended crossover band
  no greater than approximately `5 degrees`; and
- no broad coherent discrepancy large enough to change the provisional filter
  topology or acoustic-slope decision.

Declare the design-relevant band for each package before comparing repeats.
The completed Seed A acoustic evidence now uses the wider approximately
`1.5-2.5 kHz` transition region around its measured `1.83 kHz` branch equality;
`2.2-2.4 kHz` is retained only as the earlier design hypothesis. A maximum over
every native bin across the wider `1-5 kHz` range remains a useful diagnostic,
but it is not by itself a veto.
Record isolated or out-of-band maxima as a modelling uncertainty and preserve
the less favourable capture. These are project design criteria, not claims of
laboratory metrology or production-unit tolerance.

Delay and phase are linked. At `2.3 kHz`, a `5 us` timing difference gives:

```text
phase = 360 degrees x 2300 1/s x 5e-6 s = 4.14 degrees
```

The seconds cancel, leaving degrees. This is a useful sanity limit: a few
microseconds matter around crossover, even when they look tiny on an impulse
plot.

Compare all repeats on the same frequency grid, window, smoothing, and timing
convention. Use circular phase differences rather than ordinary subtraction at
the `+/-180 degree` wrap. Report both RMS and maximum magnitude differences;
the maximum over thousands of closely spaced native bins is an extreme-value
diagnostic, while RMS better represents the overall modelling perturbation. If
a long window disagrees because later energy changes, preserve that result and
repeat the analysis on the raw impulses using one common direct-sound window.
Do not silently alter the raw session or call the first comparison invalid.

When a set fails, first fit and report a scalar dB offset. Subtracting the mean
magnitude difference tests gain without changing response shape. For phase,
remove a documented constant-delay difference with

```text
corrected phase difference = circular(delta phase + 360 degrees x f x delta t)
```

where `delta phase = phase_A - phase_B` and `delta t = t_A - t_B`.
Delay correction cannot change magnitude. A shorter common right window may be
used as a diagnostic to locate when the divergence accumulates, but a window
that hides the difference or sacrifices the required low-frequency resolution
does not upgrade the production bandwidth. Likewise, `1/48`- to `1/12`-octave
smoothing may describe whether a residual is broad enough to affect crossover
design, but the release figures above remain native and unsmoothed.

## 6. Window Selection

Inspect the impulse and ETC. Place the right window before the first material
reflection, allowing a suitable taper; use the same time support relative to
the direct arrival for all comparable traces. Begin with a `2.0 ms` left window
unless the noise floor or pre-arrival behaviour justifies another value.

A short window trades low-frequency resolution for reflection exclusion. A
total span of `3.0 ms` has nominal resolution:

```text
Delta f approximately 1 / 0.003 s = 333 Hz
```

That can be adequate for a repeatability gate through an approximately
`1.5-2.5 kHz` crossover region, but it is too coarse to establish low-frequency
response. The UMC22 qualification used a
derived `2.0 ms` left / `1.0 ms` right direct window; that result proves chain
repeatability only. It is not automatically the REW-native production window.

For every reusable series, record the selected REW-native window, taper,
smoothing, frequency range over which the result is valid, and the reflection
that limited the right window. Near-field or low-frequency data and any splice
to the far-field response require their own documented method and provenance.

## 7. Naming, Storage, And Export

Names should identify driver, installation, angle, distance, interface, date,
and capture number. A suitable pattern is:

```text
<driver> installed <angle> <distance> <interface> <date> capture <n>
```

For durable FRD exports, the current compact convention is:

```text
rew/frd/<driver>/<AAA>deg_<distance>_<interface>_<YYYY-MM-DD>.frd
```

`<AAA>` is a three-digit zero-padded non-negative angle (`000`, `010`, and so
on), which keeps a single driver's angular files in numerical order. If future
work adds multiple reference axes, levels, windows, polarities, or sessions at
one angle, add a concise qualifier after the angle (for example,
`000deg_tweeter-axis_...`) before allowing two distinct datasets to share one
path.

Retain the raw `.mdat` as the authority. Record its project-relative path,
byte size, SHA-256, REW version, and capture names. Exports must identify their
source measurement, window, smoothing, reference plane, timing treatment, and
generator/client command where applicable. Reconstructible API exports may be
ignored only when the raw source and complete extraction route remain retained.

Do not promote a diagnostic sweep to reusable FRD merely because it looks
plausible. Missing calibration metadata, insufficient headroom, invalid timing,
or a superseded route must remain visible in its evidence label.

## 8. Failure Triage And Scope Limits

For a repeatability failure, check in this order: exact device endpoints and
sample rate; complete channel matrix; timing/calibration mode; active
microphone calibration; headroom; unchanged physical controls; unchanged
geometry; reference voltage; timing-reference index; impulse ambiguity; then
sweep length or window. Quantify gain, constant-delay, window, and smoothing
sensitivity before assigning a physical cause. Change one variable at a time
and preserve the failed result.

Raw-tweeter work requires a separately agreed sweep band, voltage, and
protective high-pass. Polar work requires its own rotation, naming, and
position-verification procedure. Neither is authorised by this general method
or by the current installed-woofer release.
