# Measurement Equipment and Workflow

| State | Value |
| --- | --- |
| Lifecycle | **CURRENT POLICY AND ROUTING** |
| Owns | Project-wide measurement principles, file conventions, evidence handling, and task routing |
| Does not own | Interface settings, fixture operation, individual capture steps, qualification results, or crossover fabrication |
| Detailed driver evidence | [Driver analysis](DRIVER_ANALYSIS.md) |
| Procedure dispatcher | [REW documentation map](rew/README.md) |
| Measurement artefacts | [`rew/`](../rew/) |

## 1. Measurement principles

- Separate verified measurements, derivations, inferences, provisional decisions, and open items.
- Compare traces only when mounting, sealing, damping, orientation, ambient conditions, sample rate, calibration, sweep settings, and drive level are controlled or explicitly recorded.
- Treat impedance-derived alignment as electrical evidence, not a substitute for acoustic magnitude, phase, distortion, and directivity.
- Design the passive crossover from installed-baffle, phase-bearing acoustic measurements and current installed ZMA files—not nominal impedances or textbook parts alone.
- Keep exploratory optimisation explicitly provisional until the required measurement gates have passed.
- Use the current specialised procedure for exact interface routing, level, calibration, startup, stop, and capture instructions. Do not reconstruct a live procedure from qualification history.

## 2. Minimum measurement capability

- calibrated measurement microphone;
- two-channel audio interface or equivalent;
- test power amplifier;
- REW;
- VituixCAD;
- calibrated impedance-measurement jig or dedicated equivalent;
- microphone stand;
- repeatable speaker rotation/angle setup;
- tape measure or laser measure; and
- true-RMS multimeter for terminal-voltage and cold-resistance checks.

An audio-frequency spectrum analyser is not required. Swept-sine and impulse-response measurements through a PC audio interface are preferred.

## 3. File and calibration conventions

### 3.1 Project locations

- `rew/`: raw REW measurements and impedance exports. Durable acoustic exports
  use `rew/frd/<driver>/<AAA>deg_<distance>_<interface>_<date>.frd`, with a
  three-digit zero-padded angle so files sort numerically within a driver. Add
  an axis qualifier after the angle when one driver has data from more than one
  vertical observation point.
- `calibration/`: retained measurement-device calibration sources and documented REW-compatible derivatives.
- `vituixcad/`: VituixCAD projects and generated outputs.
- `doc/rew/`: procedures, qualification evidence, active diagnostics, and dated history. Use its [dispatcher](rew/README.md) to select one authority.

### 3.2 Impedance measurements

- Use **48 kHz** for the controlled driver-impedance comparison series unless a new series is deliberately established.
- Recalibrate the impedance rig whenever sample rate, interface path, input gain, leads, sense resistor, or relevant wiring changes.
- Retain headers, decimal points, frequency/magnitude/phase columns, dense unsmoothed data, and descriptive filenames.
- Record actual driver-terminal voltage; dBFS alone does not establish driver excitation when a series sense resistor is present.
- Record cold DCR, ambient temperature, elapsed cooldown, cabinet damping state, driver mounting, screw condition, and wiring changes.
- Treat points below the validated low-frequency range as artefacts rather than using them for $R_e$, Q, or alignment estimates.

For the controlled conditioning comparison, use [Driver run-in and stabilisation](DRIVER_RUNIN.md).

### 3.3 Acoustic measurements

- Preserve one electrical timing reference and fixed microphone/rotation geometry across both drivers.
- Use the [interface-neutral FRD method](rew/FRD_MEASUREMENT_METHOD.md) for geometry, timing, repeatability, impulse/ETC review, production-window selection, naming, and provenance.
- Use exactly one current interface procedure for device routing, calibration assignment, level checks, capture sequence, and stop conditions. Use [UMC22 installed-woofer FRD](rew/procedures/UMC22_INSTALLED_WOOFER_FRD.md) and [UMC22 protected installed-tweeter FRD](rew/procedures/UMC22_INSTALLED_TWEETER_FRD.md) for the retained, validated common-position source pair and any later explicitly bounded measurement package.
- Use [UMC22 installed horizontal off-axis FRD](rew/procedures/UMC22_INSTALLED_HORIZONTAL_OFF_AXIS_FRD.md) for the first sparse `+20/+40/+60 degree` raw-driver directivity package; it owns the pivot convention, batch boundaries, topology-change gates, and polar filenames.
- When a generated loopback-calibration response contains a deliberate series
  protection network, remember that REW normalises its magnitude to `0 dB` at
  `1 kHz`. The correction removes the network's frequency-dependent shape but
  leaves its gain at the normalisation frequency as a constant response offset.
  For retained protected-tweeter C2, apply the documented derived `+11.14 dB`
  magnitude scale in the model; do not alter its measured phase or delay.
- Match microphone calibration to the actual device, input selector, channel, and orientation. Confirm its application in the stored measurement metadata; preference persistence alone is not evidence that it was applied.
- Treat a generic frequency-response file as generic-calibrated, not serial-number-specific or absolute-SPL calibration. Record the limitation with resulting measurements.
- Treat the first low-level sweep as a headroom and metadata check. Capture and review one sweep before repeats, rotation, or reusable export when a procedure requires that gate.
- After that first capture validates a bounded package, run its remaining named
  captures consecutively under one standing unchanged-state declaration and
  common stop rules. Do not require a settings recital between every sweep or
  merely because a chat changed; repeat the audit after a relevant physical,
  electrical, application, or day/session boundary.
- Select a REW-native production window from the actual impulse/ETC and required bandwidth. A short qualification window does not automatically become the production window.
- Record microphone distance, axis, height, window/gating choices, sample rate, amplifier setting, terminal voltage, and room state.
- Measure individual drivers before filtered sums, and retain normal- and reverse-polarity results.
- Use filenames identifying driver, angle, polarity/filter state, level, and date or sequence.

### 3.4 REW API client

For programmatic REW session-state capture and `.mdat` extraction, use the [REW API client](REW_API_CLIENT.md). It owns commands, reconstructible outputs, runtime limitations, and links to its separate qualification evidence.

## 4. Development sequence

1. Confirm physical driver dimensions and cabinet sealing.
2. Record cabinet fill/lining, driver mounting, ambient conditions, and cold electrical baselines.
3. Complete controlled driver conditioning under [Driver run-in and stabilisation](DRIVER_RUNIN.md), if still required.
4. Establish cooled installed impedance baselines for woofer and tweeter.
5. Select the current procedure through the [REW documentation map](rew/README.md), and satisfy its fixture, interface, no-signal, calibration, and level prerequisites.
6. Measure each driver acoustically in the actual baffle with common timing.
7. Obtain gated far-field measurements around the crossover region.
8. Obtain near-field woofer measurements for bass and merge only with documented scaling and phase treatment.
9. Acquire useful horizontal off-axis responses using fixed geometry.
10. Measure distortion at progressively realistic levels while respecting woofer excursion and tweeter protection.
11. Import the current phase-bearing FRD and ZMA data into VituixCAD.
12. Design a realizable passive network for acoustic slopes, summed response, directivity, impedance, sensitivity, and component limits.
13. Follow [Crossover component development](CROSSOVER_COMPONENT_DEVELOPMENT.md) for construction, measured-value control, and thermal constraints.
14. Measure individual filtered drivers, normal-polarity sum, reverse-polarity null, impedance/EPDR, distortion, and off-axis behaviour.
15. Adjust one controlled crossover, damping, or placement variable at a time and repeat the decisive measurements.
16. Move the crossover inside only after the complete external assembly remains stable under the validation gates in [Crossover design](CROSSOVER_DESIGN.md).
17. Repeat final installed-system measurements in the intended near-wall room placement.

## 5. Specialised authorities

- [REW procedure and evidence dispatcher](rew/README.md)
- [Interface-neutral FRD measurement method](rew/FRD_MEASUREMENT_METHOD.md)
- [Current UMC22 installed-woofer procedure](rew/procedures/UMC22_INSTALLED_WOOFER_FRD.md)
- [Current UMC22 protected installed-tweeter procedure](rew/procedures/UMC22_INSTALLED_TWEETER_FRD.md)
- [Current UMC22 installed horizontal off-axis procedure](rew/procedures/UMC22_INSTALLED_HORIZONTAL_OFF_AXIS_FRD.md)
- [Suspended UMC202HD FRD route](rew/procedures/UMC202HD_FRD_SUSPENDED.md)
- [Reference-fixture operating procedure](rew/fixtures/REFERENCE_FIXTURE_USE.md)
- [Reference-fixture specification](rew/fixtures/REFERENCE_FIXTURE_SPECIFICATION.md)
- [UMC202HD desktop-dropout diagnosis](rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md)
- [REW API client](REW_API_CLIENT.md)
- [Driver run-in and stabilisation](DRIVER_RUNIN.md)
- [Driver evidence and impedance analysis](DRIVER_ANALYSIS.md)
- [Crossover design](CROSSOVER_DESIGN.md)
- [Room geometry and placement evidence](ROOM_DETAILS.md)

Qualification and history files are reached through the [REW dispatcher](rew/README.md); they are not routine operating context.

## 6. Evidence and documentation loop

After each material measurement series:

1. Preserve the raw REW/VituixCAD source in the correct project directory.
2. Record controlled conditions and deviations.
3. Recalculate derived quantities reproducibly from the retained export.
4. Update [Driver analysis](DRIVER_ANALYSIS.md) or the relevant topic authority with a dated, evidence-labelled addition.
5. Preserve superseded conclusions where they explain the engineering process; move detailed chronology to its designated history record rather than copying it into current procedures.
6. Update the root [README](../README.md) only when high-level project state or a locked design decision changes.
