# Seed A External-Crossover Commissioning — 2026-09-08 to 2026-09-09

> - **Lifecycle:** HISTORY / RETAINED MEASUREMENT EVIDENCE
> - **Owns:** detailed chronology and evidence for completed Seed A cold commissioning, filtered-branch captures, the intermittent tweeter-only-load investigation, normal/reversed full-system captures, and the first physical full-system horizontal set
> - **Does not own:** the current crossover decision, component-construction specification, general REW procedure, or the next measurement release
> - **Read when:** auditing a reported value, reconstructing why the test sequence changed, or reviewing the closed intermittent-distortion investigation
> - **Current consequence:** the reversible Seed A prototype passes its completed component, cold, low-level functional, on-axis acoustic, physical-polarity, and sparse-horizontal gates; see [Crossover design](../../CROSSOVER_DESIGN.md)
> - **Last reviewed:** 2026-09-09

This record preserves completed evidence without making the routinely loaded
current authorities into test transcripts. The raw retained authority is
[`rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat`](../../../rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat),
saved at `63,595,690` bytes with SHA-256
`ca95668820aa965e91e45df6929cc82dfacafdf015d130c1f825bd5397619383`.
Signal-free byte-string inspection found each of the seven Seed A measurement
titles in Section 4 exactly once. REW V5.40 beta 133 and the live API supplied
the metadata and response data quoted below.

## 1. Component and cold commissioning

The completed component values remain authoritative in
[Crossover component development](../../CROSSOVER_COMPONENT_DEVELOPMENT.md).
All three capacitor banks, both resistor banks, and all three inductors passed
against Seed A. The practical measured-component VituixCAD project includes the
actual capacitance, ESR, resistance, inductance, and DCR values. The user's
subsequent movement of R(Tpar) in that schematic was explicitly cosmetic and
was accepted without inspecting or rewriting the file.

The completed external network passed user-reported DC topology checks:

- woofer-path resistance was approximately the sum of L(W1) and L(W2) DCR,
  whose expected total is `0.292 + 0.172 = 0.464 ohm`;
- the complete tweeter path was open at DC because of its series capacitors;
- the tweeter shunt inductor showed its DCR to input negative;
- input negative and both negative driver outputs were common; and
- the series/parallel L-pad readings agreed with the intended network.

With both drivers and amplifier output connected in verified polarity but the
amplifier de-energised, the nulled Agilent U1272A measured `5.929 ohm` at the
crossover input. Subtracting measured woofer-filter DCR gives
`5.929 - 0.464 = 5.465 ohm` for the woofer-dominated DC remainder, physically
consistent with the installed woofer evidence. Powered-idle behaviour was
normal. A first `0.10 V RMS`, `200-20000 Hz` functional sweep sounded normal;
no valid REW trace was expected because the measurement input was disconnected.

## 2. Filtered woofer WF1

The intended filtered-woofer level was `1.000 V RMS` at the crossover input for
a `1 kHz`, `-20 dBFS` REW generator tone. The first sweep aborted when both REW
input headrooms reached `0.0 dB`. A read-only audit found that REW had reverted
to a shared UMC22 input instead of the qualified exact-exclusive input. After
the exact-exclusive input was restored, live levels were `-21.23 dBFS` at In
and `-24.58 dBFS` at Ref In. No hardware fault or unexpectedly high acoustic
level was implicated.

The retained retry is:

- title: `SB17_sA_filt_000deg_t-axis_1m_U22_WF1_20260908`;
- level and sweep: `1.000 V RMS`, `20-20000 Hz`, `-20 dBFS`, `256k`, one
  repetition, `48 kHz`;
- minimum microphone headroom `10.3 dB`, reference headroom `24.4 dB`;
- SNR `39.2146 dB`, signal-to-distortion `56.4 dB`;
- timing-reference index `47846.94`, direct peak/System Delay
  `3.1887594 ms`; and
- stored window `Hann 2.0 ms` left / `Tukey 0.25 3.5 ms` right at displayed
  `3.18 ms`, with FDW/MTW off and no alignment.

The capture completed without warning or anomaly. Its comparison with the old
unfiltered woofer source showed a faster real filtered fall through the
crossover region than the practical model predicted; this moved broad measured
branch equality downward but did not alone justify changing Seed A.

## 3. Intermittent tweeter-only-load investigation

With the woofer disconnected, a severe distorted `1 kHz` tone was initially
audible from the quiet tweeter near `0.200 V RMS` crossover input. The connected
tweeter-output resistance was `3.024 ohm`. Brief `2 kHz` and `3 kHz` tests at
the same input sounded pure, and a later `1 kHz` restart was temporarily clean.
The symptom then recurred after the crossover input exceeded about
`0.800 V RMS`, persisted after reduction to `0.200 V RMS`, and could thereafter
be heard from about `0.070 V RMS` until it later cleared. The very low predicted
tweeter power and the clean higher-frequency tones made a persistent thermal
driver state implausible.

UMC22 DIRECT MONITOR was off, Windows `Listen to this device` was unchecked,
and a post-restart process list contained no obvious monitoring application.
That process snapshot could not reproduce the preceding Windows state. The
investigation therefore moved to bounded load substitution rather than repeated
audible triggering.

With both drivers removed and one nominal 5R6 resistor across the tweeter
output, the measured output resistance was `4.866 ohm`, consistent with a
`5.559 ohm` dummy in parallel with R(Tpar). Electrical RTA checks at `0.20`,
`0.50`, `0.80`, and `1.00 V RMS` gave `0.009-0.015%` THD without a threshold
jump or abnormal sound. With the real tweeter restored and two 13R resistors in
parallel across the empty woofer output, measured resistance was `6.448 ohm`
at that output and `6.778 ohm` at the complete input. The same four levels then
gave a pure tone and `0.008-0.013%` THD without a threshold.

These results strongly associate the original symptom with the real tweeter
plus the otherwise undamped tweeter-only Seed A load, not ordinary tweeter or
passive-component distortion. Amplifier/load instability dependent on the
real tweeter's wider-band impedance remains the leading inference; possible
ultrasonic oscillation was outside the UMC22/48 kHz observation band and was
not proved. The bounded fault investigation is closed/parked because the
normal complete system subsequently completed every low-level acoustic sweep
without recurrence. This does not replace the still-pending controlled
full-system distortion/compression gate at required listening levels.

## 4. Retained filtered-system measurements

Every capture used the qualified exact-exclusive UMC22 `L/L/L/R` route,
loopback calibration/timing, the ECM8000 calibration on microphone input L
only, `20-20000 Hz`, `-20 dBFS`, `256k`, one repetition, `48 kHz`, clipping
abort, and no timing shift or clock correction. WF1 and TF1 used
`1.000 V RMS`; SUM1, REV1, and the three full-system angles used
`0.500 V RMS`. Each retained response stores a `Hann 2.0 ms` left /
`Tukey 0.25 3.5 ms` right window at its own displayed direct-peak time, with
FDW/MTW off.

| Role | Title | UUID | SNR | Direct peak | Reported headroom |
|---|---|---|---:|---:|---:|
| Woofer branch | `SB17_sA_filt_000deg_t-axis_1m_U22_WF1_20260908` | not exposed in the retained notes | `39.2146 dB` | `3.1887594 ms` | `10.3 dB` |
| Tweeter branch | `SB26_sA_filt_000deg_t-axis_1m_U22_TF1_20260909` | `af9adf78-3f71-41ba-96a7-0fb8f2452dd9` | `50.3202 dB` | `3.0481671 ms` | `10.4 dB` |
| Normal sum | `SPK_sA_filt_000deg_t-axis_1m_U22_SUM1_20260909` | `153c7078-e6ae-4315-9840-55f8ddb33f5a` | `46.1793 dB` | `3.0468843 ms` | `16.0 dB` |
| Reversed tweeter | `SPK_sA_filt_000deg_t-axis_1m_U22_REV1_20260909` | `d86f4ede-15de-4da6-aa0c-e16bcba2090d` | `45.6138 dB` | `3.0467861 ms` | green |
| Normal `+20 degrees` | `SPK_sA_filt_020deg_t-axis_1m_U22_SUM1_20260909` | `e662c8d0-0213-4255-bef8-a54956e57939` | `44.9512 dB` | `3.0411838 ms` | `14.2 dB` |
| Normal `+40 degrees` | `SPK_sA_filt_040deg_t-axis_1m_U22_SUM1_20260909` | `6b56568b-9d64-4776-9c52-540e7abe19f1` | `42.5508 dB` | `3.0329140 ms` | `16.5 dB` |
| Normal `+60 degrees` | `SPK_sA_filt_060deg_t-axis_1m_U22_SUM1_20260909` | `8cd73344-5f34-41ee-9fbf-979e092289de` | `40.2495 dB` | `3.0207557 ms` | `16.5 dB` |

The `+60 degree` custom setup notes were omitted; its exact title, controlled
sequence, timing, and API identity preserve adequate provenance. No repeat was
justified.

## 5. On-axis acoustic results

Diagnostic `1/12`- and `1/6`-octave branch views place broad WF1/TF1 equality
at `1.814` and `1.844 kHz`, respectively, with relative phase `+2.7` and
`-0.7 degrees`. The practical model had predicted approximately `2.116 kHz`,
so the real crossing is about `13-14%` lower. The earlier derived
`32.5/44.1 dB` reverse figures came from subtracting separately smoothed branch
curves and are not physical-null predictions.

After exact `+6.0206 dB` correction for SUM1's lower test voltage, a common-
absolute-window raw comparison gives `0.99566` correlation with WF1+TF1,
`+0.367 dB` best-fit gain, and residual RMS `20.62 dB` below the measured sum.
Normal acoustic summation therefore passes.

After exact voltage correction, `2 x REV1` correlates `0.99463` with WF1-TF1,
requires only `+0.201 dB` best-fit gain, and leaves residual RMS `19.70 dB`
below the measured difference waveform. At `1/12` octave, measured normal-to-
reverse difference peaks at `25.31 dB` near `1.636 kHz`, remains at least
`15 dB` from approximately `1.544-1.850 kHz`, and is `15.82 dB` near
`1.83 kHz`. At `1/6` octave it peaks at `20.82 dB` near `1.672 kHz` and is
`15.18 dB` at `1.83 kHz`. The physical polarity gate passes, and the tweeter
was returned to normal polarity.

## 6. High-frequency axial feature

At `1/12` octave, SUM1 has a minimum near `10.93 kHz`, approximately `5.26 dB`
below a log-frequency line between adjacent shoulders. Its approximate `3 dB`
width is `10.31-11.83 kHz`; TF1 shows the same `5.33 dB` feature near
`11.00 kHz`, and the earlier protected-tweeter C2 source already contained a
`5.66 dB` minimum near `11.17 kHz`. The generic ECM8000 correction changes only
about `0.5-0.6 dB` across the region.

The dip becomes shallower and moves with angle. Together with its presence
before Seed A, this identifies an angle-dependent tweeter/waveguide/baffle or
very-early local diffraction feature rather than woofer summation, Seed A, or
a conventional later room reflection. It is significant on axis but narrow
and partly filled off axis; no equalisation or crossover change is justified
from this feature alone.

## 7. Physical horizontal result

At `1/6` octave, measured full-system changes from on axis are:

| Frequency | `+20 degrees` | `+40 degrees` | `+60 degrees` |
|---:|---:|---:|---:|
| `1.5 kHz` | `+0.81 dB` | `-1.17 dB` | `-2.84 dB` |
| `1.8 kHz` | `+0.40 dB` | `+0.53 dB` | `-0.83 dB` |
| `2.0 kHz` | `-0.04 dB` | `+1.27 dB` | `-0.30 dB` |
| `2.2 kHz` | `+0.19 dB` | `+0.88 dB` | `-1.17 dB` |
| `2.4 kHz` | `+0.67 dB` | `+1.21 dB` | `-0.03 dB` |
| `3.0 kHz` | `-0.30 dB` | `-0.17 dB` | `-1.11 dB` |
| `4.0 kHz` | `+0.02 dB` | `-1.62 dB` | `-3.27 dB` |
| `5.0 kHz` | `+0.16 dB` | `-2.34 dB` | `-4.52 dB` |
| `8.0 kHz` | `-1.46 dB` | `-6.47 dB` | `-10.19 dB` |

There is no broad off-axis crossover cancellation. Across `1.5-2.5 kHz`, the
angle-to-axis ranges are about `1.35 dB` at `+20 degrees`, `2.53 dB` at
`+40 degrees`, and `3.14 dB` at `+60 degrees`. The largest absolute excess
over on axis is only about `+1.36 dB`; the design-relevant observation is a
moderate beamwidth flare as the narrower woofer gives way to the wider tweeter,
not a large SPL peak. Above `3 kHz`, narrowing progresses coherently with angle.
The `11 kHz` axial dip partly fills off axis. Fine upper-band detail at
`+60 degrees` is more sensitive to the fixed room/jig energy that becomes
stronger relative to diminished direct sound.

## 8. Retained conclusion and next gate

Seed A passes proportionately as a reversible physical prototype. Its measured
crossing is lower than the practical prediction, and the moderate horizontal
directivity flare remains a possible controlled-refinement target, but neither
finding justifies changing components before the independent load gate. No
unchanged on-axis, reverse-polarity, or positive-horizontal acoustic sweep is
currently justified.

The next task is signal-free planning for a qualified as-built full-system
impedance-and-phase measurement. The separate controlled full-system
distortion/compression and thermal gates remain open. The earlier undamped
tweeter-only fault investigation remains parked unless it recurs in the normal
complete system or new evidence exposes a design-relevant mechanism.
