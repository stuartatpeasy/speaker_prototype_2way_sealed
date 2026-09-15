# Measurement Planning and Evidence

| State | Value |
| --- | --- |
| Lifecycle | **CURRENT SUPPORTING REFERENCE** |
| Owns | Reusable measurement planning, file/calibration conventions, generic development order, and evidence handover |
| Does not own | Interface routing, live capture steps, device qualification, or individual measurement conclusions |
| Read when | Planning a new or deliberately repeated measurement series, interpreting measurement evidence, or updating its owning authority |
| Current approved action | Select the active gate and its exact procedure through the [REW dispatcher](README.md); use this record only for the reusable plan and evidence rules |
| Limitations | It does not release a signal, qualify hardware, or replace the applicable procedure's prerequisites and stop rules |
| Last reviewed | 2026-09-15 |

## 1. Planning principles

- Separate verified measurements, derivations, inferences, provisional decisions, and open items.
- Compare traces only when mounting, sealing, damping, orientation, ambient conditions, sample rate, calibration, sweep settings, and drive level are controlled or explicitly recorded.
- Treat impedance-derived alignment as electrical evidence, not a substitute for acoustic magnitude, phase, distortion, and directivity. Design the passive crossover from installed-baffle, phase-bearing acoustic measurements and current installed ZMA files, not nominal impedances or textbook parts alone.
- Keep exploratory optimisation provisional until its named measurement gates pass.
- Before loading a large supported FRD, ZMA, impulse, `.mdat`, or VituixCAD file, use [Measurement data tooling](../MEASUREMENT_DATA_TOOLING.md) for the smallest relevant band, point set, or semantic comparison. Carry the raw-file hash, parameters, and warnings with the derived result.
- Use exactly one current specialised procedure for device routing, calibration, level, startup, stop, and capture instructions. Qualification and history record evidence; they do not reconstruct a live procedure.
- For the qualified `5 V` USB-powered impedance jig, stop signal generation before changing the DUT. Carry unchanged settings and passed checks forward; repeat qualification only after a relevant change, anomaly, or failed control.

## 2. Capability and file conventions

The minimum useful set is a calibrated measurement microphone, two-channel interface or equivalent, test amplifier, REW, VituixCAD, calibrated impedance jig or equivalent, microphone stand, repeatable rotation/angle setup, tape or laser measure, and true-RMS multimeter for terminal-voltage and cold-resistance checks. Swept-sine and impulse-response work through a PC interface is preferred; an audio-frequency spectrum analyser is not required.

- `rew/` holds raw REW measurements and impedance exports. Durable acoustic exports use `rew/frd/<driver>/<AAA>deg_<distance>_<interface>_<date>.frd`, with zero-padded angles; add an axis qualifier if one driver has multiple vertical observation points.
- `calibration/` holds retained calibration sources and documented REW-compatible derivatives; `vituixcad/` holds projects and generated outputs. The [REW dispatcher](README.md) maps procedures, qualification evidence, active diagnostics, and history under `doc/rew/`.
- Retain impedance headers, decimal points, frequency/magnitude/phase columns, dense unsmoothed data, and descriptive filenames. Record terminal voltage, cold DCR, ambient temperature, cooldown, damping state, mounting, screw condition, and wiring changes. Treat data below the validated low-frequency range as artefacts, not inputs to $R_e$, Q, or alignment estimates.
- Use the applicable procedure for interface and calibration settings. The controlled driver-impedance comparison series uses `48 kHz` unless a new series is deliberately established; recalibrate after a changed sample rate, interface path, input gain, measurement leads, sense resistor, or jig wiring, not an ordinary DUT swap on the unchanged qualified route.

## 3. Acoustic plan and safeguards

- Preserve one electrical timing reference and fixed microphone/rotation geometry across both drivers. Use the [FRD measurement method](FRD_MEASUREMENT_METHOD.md) for geometry, impulse/ETC review, production windows, naming, and provenance.
- Match microphone calibration to the actual device, selector, channel, and orientation, and verify it in stored metadata. A generic response file is generic-calibrated, not serial-number-specific or absolute-SPL calibration; record that limitation.
- A first low-level sweep is the headroom and metadata check. Once it validates a bounded package, run its remaining named captures consecutively under one unchanged-state declaration and common stop rules. Repeat the audit after a relevant physical, electrical, application, or day/session boundary.
- Select a REW-native production window from the actual impulse/ETC and required bandwidth. A short qualification window does not automatically become the production window. Record distance, axis, height, gate/window, sample rate, amplifier setting, terminal voltage, and room state.
- Measure individual drivers before filtered sums; retain normal- and reverse-polarity results. Name files for driver, angle, polarity/filter state, level, and date or sequence.
- A loopback calibration with deliberate series protection is normalised by REW to `0 dB` at `1 kHz`. It removes the network's frequency-dependent shape but leaves its normalisation-frequency gain as a constant offset. For protected-tweeter C2, apply the documented `+11.14 dB` magnitude scale in the model; do not change its measured phase or delay.
- Completed Seed A filtered-branch, sum, reverse-null, and horizontal evidence is in the [commissioning history](history/SEED_A_EXTERNAL_CROSSOVER_COMMISSIONING_2026-09-08_TO_09.md), for audit only. The [Seed A level/thermal qualification](qualification/SEED_A_FULL_SYSTEM_LEVEL_AND_THERMAL_QUALIFICATION_2026-09-10.md) owns that result and its excluded wrong-angle trace. For speaker two, retain the `4.000 V RMS` ceiling, both Type-K contact probes, and a correct immediate hot `0-degree` sweep; retest speaker one only if matched evidence reveals an anomaly.

## 4. Reusable development order

Use this order only from the active gate on the [dashboard](../../README.md): confirm dimensions and sealing; record damping, mounting, ambient conditions, and cold baselines; condition drivers when still needed; establish cooled installed ZMA baselines; satisfy the selected procedure; measure installed drivers with common timing; obtain gated far-field, near-field bass, and useful horizontal data; measure protected distortion; import current phase-bearing FRD/ZMA into VituixCAD; design a realisable passive network; then measure filtered branches, normal sum, reverse null, impedance/EPDR, distortion, and off-axis behaviour. Change one crossover, damping, or placement variable at a time and repeat only decisive checks. Move the crossover inside only after the external assembly passes the [crossover design](../CROSSOVER_DESIGN.md) gates, then repeat final installed-system measurements in intended placement.

## 5. Evidence handover

After a material series, preserve the raw REW/VituixCAD source in its data tree, record controlled conditions and deviations, and recalculate derived quantities from the retained export with an explicit band, comparison policy, or point set. Update [Driver analysis](../DRIVER_ANALYSIS.md) or the relevant topic authority with a dated evidence-labelled entry. Put detailed superseded chronology in its designated history record; update the [dashboard](../../README.md) only for high-level state or a locked decision.
