# Crossover Design

> - **Lifecycle:** ACTIVE DESIGN AUTHORITY
> - **Owns:** current acoustic direction, driver polarity/topology, NL4 allocation, evidence dependencies, validation gates, and open design decisions
> - **Does not own:** detailed component construction, installed-driver evidence, measurement procedures, or superseded design development
> - **Read when:** modelling, assessing the present crossover, or planning an authorised controlled refinement
> - **Current decision:** retain same-polarity third-order Seed A as the reversible external prototype; measured acoustic, load, bounded level/distortion, and external-component surface-thermal gates pass
> - **Next gate:** build and test speaker two under matched conditions, including a correct immediate hot `0-degree` comparison and a check that the narrow approximately `1.28 dB` high-level shape change near `2.18 kHz` repeats
> - **Limitations:** one speaker only; approximate rather than steady sweep-voltage readings; generic rather than absolute-SPL microphone calibration; the attempted post-thermal trace is excluded because it was captured at `60 degrees`; positive-side sparse-horizontal evidence only; the parked undamped tweeter-only mechanism and possible ultrasonic behaviour remain unproved
> - **As of:** 2026-09-15

This is the current passive-crossover authority. Read the [design-development
history](history/CROSSOVER_DESIGN_DEVELOPMENT_2026-09-07_TO_08.md) only to
audit the exploratory Seed A/Seed B work or the VituixCAD correction history.
Current driver sources are in [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md), and
component construction is in
[CROSSOVER_COMPONENT_DEVELOPMENT.md](CROSSOVER_COMPONENT_DEVELOPMENT.md).

## 1. Prototype interface and external crossover

The prototype brings the woofer and tweeter out separately through a **Neutrik
speakON NL4**:

- 1+ / 1-: woofer positive / negative;
- 2+ / 2-: tweeter positive / negative.

Keep the crossover external on a board with secure terminals, accessible
inductor taps, and enough room for safe substitutions. Do not switch taps with
the amplifier energised. Leave unused winding sections open-circuit, insulated,
and restrained so they cannot become a shorted turn.

## 2. Current crossover direction

Design from installed phase-bearing driver responses and impedances, not nominal
impedances or textbook equations. The initial approximately `2.2-2.4 kHz`,
LR4-like direction has been superseded by the measured Seed A prototype, which
crosses broadly near `1.83 kHz` and passes its physical summation gates.

Seed A uses normal (same) acoustic polarity and the measured third-order
electrical network in Section 2.2. Its shallow woofer upper transition and
moderate crossover-region beamwidth flare remain possible refinement targets.
The bounded alternative search found extra woofer suppression traded away
response span, phase/null margin, or load, while fourth-order and targeted-notch
variants were negligible or locally overfit. Do not promote Seed B unless
matched speaker-two evidence repeats a broad, design-relevant weakness.

Retain these design rules for later controlled work:

- electrical and acoustic order can differ because natural driver responses
  contribute to the final slopes;
- use partial rather than full baffle-step compensation;
- keep tweeter attenuation and check the complete measured load; and
- add impedance equalisation, breakup suppression, or sixth-order slopes only
  for a measured whole-system benefit.

### 2.1 Verified measured baseline

[`vituixcad/Prototype loudspeaker measured baseline verified 2026-09-07.vxp`](../vituixcad/Prototype%20loudspeaker%20measured%20baseline%20verified%202026-09-07.vxp)
is `10,825` bytes with SHA-256
`a456b8c2773cf0412394c75811aa6fdb41c2047a15f5f193f130904a7fb85645`.
It contains correct TW1/C2 FRDs at `0 degrees`, current installed ZMAs, TW1
scale `0.00 dB`, C2 scale `+11.14 dB`, zero response delays, native
unsmoothed phase, normal polarity, and direct unfiltered branches. It is the
raw software baseline, not a listening network.

### 2.2 Practical measured-component model

**DERIVED PRACTICAL MODEL / SIGNAL-FREE GATES PASSED:**
[`vituixcad/Prototype loudspeaker crossover Seed A practical measured 2026-09-08.vxp`](../vituixcad/Prototype%20loudspeaker%20crossover%20Seed%20A%20practical%20measured%202026-09-08.vxp)
retains the verified sparse-polar source assignments, topology, normal polarity,
and C2 scale multiplier `3.605786`, while using the completed measurements:

| Part | Practical value |
|---|---:|
| L(W1) | `0.724 mH`, `0.292 ohm` DCR, `1.8 mm` wire |
| C(W1) | `17.96 uF`, `0.04 ohm` ESR |
| L(W2) | `0.111 mH`, `0.172 ohm` DCR, `1.8 mm` wire |
| C(T1) | `12.22 uF`, `0.04 ohm` ESR |
| L(T1) | `0.219 mH`, `0.193 ohm` DCR, `1.8 mm` wire |
| C(T2) | `22.59 uF`, `0.04 ohm` ESR |
| R(Tser) | `1.401 ohm`; aggregate bank power field `20 W` |
| R(Tpar) | `39.032 ohm`; aggregate bank power field `15 W` |

The current practical file is `26,354` bytes with SHA-256
`16676944a98b625bb59effa4757f4224e0da763b36293679ace8dc0c67861a04`.
It parses with two drivers, eight measured components, four horizontal responses
per driver, installed ZMA paths, and unchanged tweeter scale; no source is
missing. Complex replay gives `2.116 kHz` branch equality, `13.2 degrees`
relative phase, `18.6 dB` normal-to-reverse difference, and `3.805 ohm`
minimum input impedance near `2.792 kHz` at `-9.4 degrees`. These pass the
bounded `2.05-2.25 kHz`, `20 degree`, `15 dB`, and `3.5 ohm` gates.

### 2.3 Measured acoustic consequence

**MEASURED ACOUSTIC VALIDATION - PROPORTIONATE PASS:** the retained authority is
[`rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat`](../rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat).
Capture detail and diagnostics are in the [Seed A commissioning
history](rew/history/SEED_A_EXTERNAL_CROSSOVER_COMMISSIONING_2026-09-08_TO_09.md).

- WF1 and TF1 place broad measured branch equality near `1.83 kHz`, about
  `13-14%` below the practical model, with essentially coincident phase.
- SUM1 correlates `0.99566` with voltage-corrected WF1+TF1; REV1 correlates
  `0.99463` with WF1-TF1. The physical polarity gate passes: the
  normal-to-reverse difference peaks at `25.31 dB` near `1.636 kHz` and is
  `15.82 dB` near `1.83 kHz`.
- The approximately `5.3 dB` axial dip near `11 kHz` predates Seed A and
  partly fills/moves off axis; it does not justify EQ.
- The `0/+20/+40/+60 degree` full-system set has no broad crossover hole. A
  moderate roughly `2.5-3.1 dB` beamwidth change through `1.5-2.5 kHz`
  remains a possible controlled-refinement target.

The intermittent distorted `1 kHz` tone occurred only with the undamped
tweeter-only load. It is closed/parked after clean resistor-dummy, damped
real-tweeter, and complete-system tests; an amplifier/load interaction remains
an inference, not a diagnosis.

### 2.4 As-built complete-system load

**VERIFIED MEASUREMENT / DERIVED - LOAD GATE PASSED:**
[`rew/SPK_impedance_WT_1_20260909.mdat`](../rew/SPK_impedance_WT_1_20260909.mdat)
and
[`rew/SPK_impedance_both_drivers_run1_2026-09-09.zma`](../rew/SPK_impedance_both_drivers_run1_2026-09-09.zma)
are owned by the [load record](rew/qualification/SEED_A_AS_BUILT_IMPEDANCE_AND_EPDR_2026-09-09.md).

Across `20 Hz-20 kHz`, minimum magnitude is `4.366 ohm` near `9.617 kHz`,
minimum real part is `4.284 ohm` near `2.156 kHz`, and minimum idealised
class-B EPDR is `2.563 ohm` near `1.942 kHz`, where actual impedance is
`4.905 ohm` at `-25.113 degrees`. The measured load clears the `3.5 ohm`
prototype gate by `0.866 ohm`; retain Seed A unchanged.

### 2.5 Full-system level, distortion, compression, and thermal result

**VERIFIED MEASUREMENT / USER-REPORTED CONDITIONS / DERIVED - BOUNDED PASS
WITH HOT-ACOUSTIC CHECK DEFERRED:** the [level/thermal qualification](rew/qualification/SEED_A_FULL_SYSTEM_LEVEL_AND_THERMAL_QUALIFICATION_2026-09-10.md)
and
[`rew/SPK_Seed_A_full_system_level_thermal_20260910.mdat`](../rew/SPK_Seed_A_full_system_level_thermal_20260910.mdat)
cover `0.5/1/2/4 V RMS` and a 15-minute nominal `2 V RMS` CTA-2034 exposure.

Both UMC22 inputs retained at least `27.9 dB` headroom; no warning, clipping,
dropout, audible distortion, protection event, or anomaly was reported. Sampled
THD and compression pass. A narrow `4 V` versus `2 V` difference reaches
`-1.28 dB` near `2.18 kHz`; it is a speaker-two confirmation item. R(Tser)
rose from `20.4` to `20.8 degrees C` and L(W1) from `20.4` to
`20.6 degrees C`, with neither rising in the final five minutes. The attempted
post-thermal sweep is excluded because it was at `60 degrees`, not `0 degrees`.

## 3. Evidence and model dependencies

Use only approved installed ZMA and phase-bearing FRD sources in
[DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md). The useful present crossover-region
loads near `2.30 kHz` are approximately `7.98 ohm` at `+10.8 degrees` for
the woofer and `3.48 ohm` at `-5.0 degrees` for the tweeter.

The approved C6 woofer source is
[`rew/frd/SB17NRX2C35-8/000deg_1m_UMC22_2026-09-06.frd`](../rew/frd/SB17NRX2C35-8/000deg_1m_UMC22_2026-09-06.frd).
The common-position TW1 source is
[`rew/frd/SB17NRX2C35-8/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd`](../rew/frd/SB17NRX2C35-8/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd).
With the `10.13 uF`, `0.08 ohm` protection capacitor and installed tweeter
ZMA, C2 requires `+11.14 dB`; leave TW1 at `0.00 dB`, delays at `0 us`,
minimum-phase conversion off, and polarity normal. History explains the
multiplier/decibel serialisation correction.

## 4. Excursion and power philosophy

Do not design for routine operation at rated Xmax. Normal use should be well
below Xmax; Xmech/Xlim are emergency limits. Read tweeter power ratings with
their specified high-pass condition and never apply an unfiltered broadband or
low-frequency signal to the bare tweeter.

## 5. Validation state before freezing the crossover

1. **Passed:** approved installed ZMA and phase-bearing FRD sources.
2. **Passed:** measured external network and practical model.
3. **Passed:** filtered drivers, normal sum, physical reverse-polarity null,
   sparse positive-horizontal set, and as-built load/EPDR.
4. **Bounded pass / deferred comparison:** level, sampled distortion, and
   external-component thermal gates. The wrong-angle post-thermal trace is
   excluded; obtain the valid hot `0-degree` comparison and check `2.18 kHz`
   on speaker two.
5. Keep the network external through matched speaker-two and pair checks. Move
   it inside only if those results support final implementation.

## 6. Open crossover items

- whether matched speaker-two evidence supports retaining Seed A unchanged;
- second-channel component matching and final inductor implementation;
- permanent inductor interlock, outer-layer binding, and PCB restraint;
- amplifier headroom at the required listening level; and
- final crossover mounting position and whether DSP remains development-only.
