# Driver Analysis Change Log

> - **Lifecycle:** DRIVER-IMPACT HISTORY
> - **Owns:** dated changes to driver baselines, conclusions, retention decisions, and the evidence gates that superseded them
> - **Does not own:** full REW, interface, UI, fixture, or troubleshooting chronology
> - **Current authority:** [DRIVER_ANALYSIS.md](../DRIVER_ANALYSIS.md)
> - **Use when:** auditing why a driver conclusion or approved source changed
> - **Limitations:** detailed measurement-route evidence remains in the linked REW qualification and history records
> - **As of:** 2026-09-06

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
