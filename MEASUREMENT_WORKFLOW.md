# Measurement Equipment and Workflow

This file is the project-wide measurement map. Detailed driver evidence is in [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md), conditioning is in [DRIVER_RUNIN.md](DRIVER_RUNIN.md), and specialised REW procedures are under [`rew/`](rew/).

## 1. Measurement principles

- Separate verified measurements, derivations, inferences, provisional decisions, and open items.
- Compare traces only when mounting, sealing, damping, orientation, ambient conditions, sample rate, calibration, sweep settings, and drive level are controlled or explicitly recorded.
- Treat impedance-derived alignment as electrical evidence, not a substitute for acoustic magnitude, phase, distortion, and directivity.
- Design the passive crossover from installed-baffle, phase-bearing acoustic measurements and current installed ZMA files—not nominal impedances or textbook parts alone.
- Keep exploratory optimisation explicitly provisional until the required measurement gates have passed.

## 2. Minimum measurement capability

- calibrated measurement microphone;
- two-channel audio interface or equivalent;
- test power amplifier;
- REW;
- VituixCAD;
- calibrated impedance-measurement jig or dedicated equivalent;
- microphone stand;
- repeatable speaker rotation/angle setup;
- tape measure or laser measure;
- true-RMS multimeter for terminal-voltage and cold-resistance checks.

An audio-frequency spectrum analyser is not required. Swept-sine and impulse-response measurements through a PC audio interface are preferred.

## 3. File and calibration conventions

### 3.1 Project locations

- `rew/`: REW measurements and exports, including `.mdat`, `.zma`, tab-delimited impedance exports, FRD exports, and procedure notes.
- `vituixcad/`: VituixCAD projects and generated outputs.

### 3.2 Impedance measurements

- Use **48 kHz** for the controlled driver-impedance comparison series unless a new series is deliberately established.
- Recalibrate the impedance rig whenever sample rate, interface path, input gain, leads, sense resistor, or relevant wiring changes.
- Retain headers, decimal points, frequency/magnitude/phase columns, dense unsmoothed data, and descriptive filenames.
- Record actual driver-terminal voltage; dBFS alone does not establish driver excitation when a series sense resistor is present.
- Record cold DCR, ambient temperature, elapsed cooldown, cabinet damping state, driver mounting, screw condition, and any wiring changes.
- Treat points below the validated low-frequency range as artefacts rather than using them for \(R_e\), Q, or alignment estimates.

### 3.3 Acoustic measurements

- Preserve one electrical timing reference and fixed microphone/rotation geometry across both drivers.
- Record microphone distance, axis, height, window/gating choices, sample rate, amplifier setting, terminal voltage, and room state.
- Measure individual drivers before filtered sums, and retain the normal- and reverse-polarity results.
- Use consistent filenames that identify driver, angle, polarity/filter state, level, and date or sequence.

## 4. Development sequence

1. Confirm physical driver dimensions and cabinet sealing.
2. Record cabinet fill/lining, driver mounting, ambient conditions, and cold electrical baselines.
3. Complete controlled driver conditioning under [DRIVER_RUNIN.md](DRIVER_RUNIN.md), if still required.
4. Establish cooled installed impedance baselines for woofer and tweeter.
5. Measure each driver acoustically in the actual baffle with common timing.
6. Obtain gated far-field measurements around the crossover region.
7. Obtain near-field woofer measurements for bass and merge only with documented scaling and phase treatment.
8. Acquire useful horizontal off-axis responses using fixed geometry.
9. Measure distortion at progressively realistic levels while respecting woofer excursion and tweeter protection.
10. Import the current phase-bearing FRD and ZMA data into VituixCAD.
11. Design a realizable passive network for acoustic slopes, summed response, directivity, impedance, sensitivity, and component limits.
12. Wind, measure, tap, and label oversized development inductors; build the crossover externally using measured capacitor combinations and accessible inductor-tap terminals.
13. Measure individual filtered drivers, normal-polarity sum, reverse-polarity null, impedance/EPDR, distortion, and off-axis behaviour.
14. Adjust one controlled crossover, damping, or placement variable at a time and repeat the decisive measurements.
15. After the acoustic network is stable, wind or trim matched final inductors, verify every component value and DCR, and move the crossover inside only after the complete assembly remains stable under measurement and thermal testing.
16. Repeat final installed-system measurements in the intended near-wall room placement.

## 5. Specialised procedures

- [Driver run-in and stabilisation](DRIVER_RUNIN.md)
- [Driver evidence and impedance analysis](DRIVER_ANALYSIS.md)
- [Installed acoustic-response setup test](rew/FRD_MEASUREMENT_SETUP_TEST.md)
- [SU-V570 output-topology and amplifier-suitability verification](rew/SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md)
- [Complete SU-V570-to-UMC202HD reference fixture](rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md)
- [Room geometry and placement evidence](ROOM_DETAILS.md)

## 6. Evidence and documentation loop

After each material measurement series:

1. Preserve the raw REW/VituixCAD source in the correct project directory.
2. Record the controlled conditions and any deviations.
3. Recalculate derived quantities reproducibly from the retained export.
4. Update [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md) or the relevant topic file with a dated, evidence-labelled addition.
5. Preserve superseded conclusions unless an explicitly replaced baseline requires obsolete dependent values to be removed.
6. Update [README.md](README.md) only when the high-level project state or a locked design decision changes.
