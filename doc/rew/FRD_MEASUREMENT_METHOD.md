# Installed-Driver FRD Measurement Method

Lifecycle: **METHOD**
Owns: interface-neutral geometry, timing, repeatability, windowing, naming, and
provenance requirements for installed-driver acoustic measurements.
Does not own: interface qualification, fixture operation, a particular
driver's safe sweep limits, or authorisation to power equipment.
Last reviewed: 2026-09-06

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
records a protected electrical reference derived from the same amplifier
output that drives the unit under test. The acoustic response is therefore
referenced to amplifier output rather than directly to driver terminals. Keep
the loudspeaker cable unchanged within a driver set and record any later change
of reference plane.

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

Use one controlled first capture. Immediately afterward inspect:

1. both input headrooms and any clipping warning;
2. the stored microphone and soundcard-calibration metadata;
3. measurement and reference input/output identities;
4. timing-reference index, System Delay, IR start, and clock adjustment;
5. the direct impulse and ETC for a single plausible dominant arrival;
6. audible or equipment abnormalities during the sweep; and
7. whether the proposed right window excludes the first material reflection.

Do not repeat, rotate the cabinet, export FRD, or change a setting before that
review when the active runbook imposes a one-capture gate. This prevents a
misrouted or uncalibrated setup from generating a large internally consistent
but invalid dataset.

After the first capture passes, make two further unchanged captures when a new
chain, timing mode, or geometry requires repeatability evidence. Store all
three in one raw REW session without overwriting prior diagnostic evidence.

## 5. Repeatability Evaluation

The project acceptance targets around the intended crossover region are:

- maximum magnitude spread over `1-5 kHz` no greater than approximately
  `0.2 dB`;
- System Delay spread preferably no greater than `5 us`;
- phase traces nearly coincident, with no unexplained jump or drift; and
- no microphone/reference clipping or reference dropout.

Delay and phase are linked. At `2.3 kHz`, a `5 us` timing difference gives:

```text
phase = 360 degrees x 2300 1/s x 5e-6 s = 4.14 degrees
```

The seconds cancel, leaving degrees. This is a useful sanity limit: a few
microseconds matter around crossover, even when they look tiny on an impulse
plot.

Compare all repeats on the same frequency grid, window, smoothing, and timing
convention. Use circular phase differences rather than ordinary subtraction at
the `+/-180 degree` wrap. If a long default window fails because room energy
changes after the direct arrival, preserve that result and repeat the analysis
on the raw impulses using one common direct-sound window. Do not silently alter
the raw session or call the first comparison invalid after the fact.

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

That can be adequate for a repeatability gate around `2.2-2.4 kHz`, but it is
too coarse to establish low-frequency response. The UMC22 qualification used a
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
geometry; reference voltage; impulse ambiguity; then sweep length or window.
Change one variable at a time and preserve the failed result.

Raw-tweeter work requires a separately agreed sweep band, voltage, and
protective high-pass. Polar work requires its own rotation, naming, and
position-verification procedure. Neither is authorised by this general method
or by the current installed-woofer release.
