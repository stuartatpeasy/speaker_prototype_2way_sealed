# Driver Analysis Change Log

> - **Lifecycle:** DRIVER-IMPACT HISTORY
> - **Owns:** dated changes to driver baselines, conclusions, retention decisions, and the evidence gates that superseded them
> - **Does not own:** full REW, interface, UI, fixture, or troubleshooting chronology
> - **Current authority:** [DRIVER_ANALYSIS.md](../DRIVER_ANALYSIS.md)
> - **Use when:** auditing why a driver conclusion or approved source changed
> - **Limitations:** detailed measurement-route evidence remains in the linked REW qualification and history records
> - **As of:** 2026-09-10

## 1. 2026-08-30 - installed-driver baseline

- Established the two correctly installed ZMA exports as the sole current impedance baseline.
- Recorded the woofer's single approximately 67 Hz sealed-box resonance and derived $Q_{tc}\approx0.82$.
- Recorded the absence of a separate approximately 83 Hz resonance under normal mounting.
- Recorded the tweeter's approximately 761 Hz resonance and close agreement with published Q values.
- Replaced nominal crossover-region loads with the current installed magnitude and phase values.
- Removed obsolete source references and all numerical conclusions dependent on them.

## 2. 2026-08-31 - woofer conditioning procedure

- Recorded the user-reported 45 Hz, 3.44 V RMS terminal-drive condition.
- Replaced the nominal 8-ohm power estimate with current-ZMA estimates of current, real power, and apparent power.
- Added an equivalent-circuit displacement estimate and a conservative 30 Hz, 4.0 V RMS provisional conditioning point.
- Defined cooled repeat impedance measurements, rather than elapsed time alone, as the conditioning stopping criterion.

## 3. 2026-08-31 - matched 48 kHz conditioning comparison and formal run-in procedure

- Clarified that the original installed woofer trace predates all deliberate conditioning.
- Recorded the matched 48 kHz resonance movement from 66.9712 Hz to 65.7115 Hz.
- Identified the post-run trace's approximately 0.342 ohm broadband real-resistance offset and retained the cooled original as the crossover baseline.
- Recorded the conditional effective free-air estimate of approximately 52.66 Hz.
- Linked the formal bounded conditioning, cooldown, measurement, and stopping procedure in `doc/DRIVER_RUNIN.md`.
- Recorded that no dedicated tweeter run-in is presently justified.


## 4. 2026-09-01 to 2026-09-04 — acoustic route remained blocked

- Reference-path qualification and checkout did not change either driver's electrical baseline or retention decision.
- The UMC202HD reached a clean 1.00 V RMS at the woofer but its desktop source-stream dropout prevented reusable FRD; no attempted response from that route became driver-design evidence.
- The active diagnostic and live-Linux discriminator remain in [UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md](../rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md).

## 5. 2026-09-05 — UMC22 qualification changed the next driver gate

- The risk-accepted UMC22 route passed its bounded electrical, routing, timing, calibration, and three-run repeatability qualification.
- This did not create an approved driver FRD. It removed the interface blocker for controlled installed-woofer capture, subject to the generic microphone-calibration and absent absolute-SPL limitations.
- Raw-tweeter and polar work were not released. The active procedure is [UMC22_INSTALLED_WOOFER_FRD.md](../rew/procedures/UMC22_INSTALLED_WOOFER_FRD.md); decisive measurements are in [UMC22_FRD_QUALIFICATION.md](../rew/qualification/UMC22_FRD_QUALIFICATION.md); failed and superseded attempts remain in [the dated UMC22 history](../rew/history/UMC22_FRD_QUALIFICATION_LOG_2026-09-05.md).

## 6. 2026-09-06 - first reusable installed-woofer FRD start

- Recorded the user's report that the complete UMC22/SU-V570/woofer system,
  controls, wiring, microphone geometry, enclosure/room state, and no-signal
  condition remain identical to the passed qualification, with no anomaly.
- Classified that checkpoint as a user-reported current state rather than a
  new verified electrical or acoustic measurement.
- Held every signal pending a no-excitation audit of the exact REW route and
  active-source microphone calibration. After that review, only one controlled
  `0-degree` capture is to be run before reviewing headroom, stored metadata,
  impulse/ETC, and the REW-native production window.

## 7. 2026-09-06 to 2026-09-07 - raw acoustic sources and Seed A selection

- Promoted C6 as the selected installed-woofer axis source and retained C5 as
  its immediate repeatability witness.
- Completed the protected-tweeter common-position capture and the matched
  positive-horizontal `0/+20/+40/+60 degree` raw-driver families.
- Corrected the VituixCAD response-scale and shunt-connectivity entries, then
  retained same-polarity third-order Seed A after a bounded alternative audit.

## 8. 2026-09-08 to 2026-09-09 - measured build and acoustic validation

- Recorded the measured capacitor banks, inductors and DCRs, resistor banks,
  coherent cold topology, and `5.929 ohm` complete-input resistance.
- Replaced nominal prototype parasitics with the measured values in the
  practical Seed A model; its retained prediction is `2.116 kHz` branch
  equality, `13.2 degrees` relative phase, `18.6 dB` normal-to-reverse
  difference, and `3.805 ohm` minimum impedance.
- Completed filtered woofer/tweeter, normal sum, physical reverse-null, and
  full-system `0/+20/+40/+60 degree` measurements. Real branch equality is
  broadly `1.83 kHz`; summation, reverse null, and sparse horizontal behaviour
  pass proportionately.
- Retained the moderate crossover-region directivity flare for possible later
  refinement and classified the approximately `11 kHz` axial dip as a
  pre-existing angular tweeter/baffle feature that does not justify EQ.
- Closed/parked the intermittent tweeter-only `1 kHz` distortion investigation
  after clean resistor-dummy, damped-branch, and complete-system tests; the
  exact undamped-load mechanism and possible ultrasonic behaviour remain
  unproved.
- Advanced the next gate to qualified as-built system impedance/phase, followed
  by controlled full-system distortion/compression and thermal validation.
  Detailed chronology moved to the [Seed A commissioning
  record](../rew/history/SEED_A_EXTERNAL_CROSSOVER_COMMISSIONING_2026-09-08_TO_09.md).

## 9. 2026-09-10 - bounded level, distortion, and thermal gate

- Retained the nominal `0.5/1/2/4 V RMS` complete-system series with at least
  `27.9 dB` input headroom, no reported warning or audible anomaly, sampled
  distortion within the project gates, and no demonstrated broad compression
  above `0.5 dB`.
- Recorded the narrow approximately `-1.28 dB` 4-versus-2 V shape difference
  near `2.18 kHz` as a matched speaker-two confirmation item, not a broad
  driver or crossover failure.
- Recorded the 15-minute nominal `2 V RMS` CTA-2034 result: R(Tser) and L(W1)
  external-surface rises were only `0.4` and `0.2 degrees C`, with no rise in
  the final five minutes and no reported anomaly.
- Excluded the attempted post-thermal sweep because it was captured at
  `60 degrees`, not `0 degrees`; it is neither an on-axis hot comparison nor
  intentional polar evidence.
- Advanced the driver decision to second-speaker procurement/build and matched
  confirmation. Obtain a valid hot `0-degree` comparison on speaker two and
  retest speaker one only if the new unit reveals an anomaly.
- Detailed evidence is in the [Seed A level/thermal
  qualification](../rew/qualification/SEED_A_FULL_SYSTEM_LEVEL_AND_THERMAL_QUALIFICATION_2026-09-10.md).
