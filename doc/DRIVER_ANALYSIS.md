# Driver Analysis and Measurement Record

**Project:** sealed passive two-way loudspeaker prototype
**Woofer:** SB Acoustics **SB17NRX2C35-8**
**Tweeter:** SB Acoustics **SB26STWGC-4**
**Record created:** 2026-08-27
**Last updated:** 2026-09-15

> - **Lifecycle:** ACTIVE DRIVER EVIDENCE AUTHORITY
> - **Owns:** evidence classes, approved driver ZMA/FRD sources, measurement conditions and quality, woofer/tweeter results and derivations, retention and procurement decisions, driver-specific modelling consequences, uncertainties, and next evidence gates
> - **Does not own:** REW/interface qualification chronology, fixture design, detailed acoustic-capture procedure, crossover-component construction, or room-placement evidence
> - **Current decision:** retain both installed drivers and Seed A; acoustic, as-built load, bounded level/distortion, and external-component surface-thermal gates pass proportionately
> - **Next gate:** procure/build and measure speaker two under matched conditions, including a correct immediate hot `0-degree` comparison and confirmation of the narrow approximately `1.28 dB` high-level shape change near `2.18 kHz`; retest speaker one only if the second unit reveals an anomaly
> - **Limitations:** one sample of each driver; incomplete baseline conditions; approximate rather than steady sweep-voltage readings; generic rather than absolute-SPL microphone calibration; the attempted post-thermal trace is excluded because the speaker was at `60 degrees`; contact probes do not measure voice-coil temperature; known local woofer early-tail variability near `2.03 kHz`; C2 scale is derived; the parked undamped tweeter-only mechanism and possible ultrasonic behaviour remain unproved; positive-side sparse polar evidence only
> - **As of:** 2026-09-15

This is the durable engineering record for the driver investigation. It supplements [README.md](../README.md). Detailed dated driver-impact history is retained in [DRIVER_ANALYSIS_CHANGELOG.md](history/DRIVER_ANALYSIS_CHANGELOG.md).

## 1. Authority, evidence, and current sources

### 1.1 Evidence labels

- **VERIFIED MEASUREMENT** — directly present in retained measurement evidence and independently read back or checked; a user-transcribed instrument result remains **USER-REPORTED** unless its own durable record supports verification.
- **DERIVED** — calculated from stated measured or published inputs and retained equations.
- **PUBLISHED** — manufacturer specification or manufacturer technical guidance.
- **EXTERNAL RESEARCH** — relevant non-manufacturer technical literature.
- **USER-REPORTED** — a configuration, condition, or observation reported by the user but not independently encoded in an archived measurement.
- **USER-CONFIRMED CONFIGURATION** — a user-confirmed setting or connection state used to interpret evidence.
- **INFERRED** — a physically plausible interpretation requiring assumptions that have not been measured.
- **PROVISIONAL DECISION** — a present engineering direction subject to stated test gates.
- **OPEN ITEM** — measurement, decision, or archival work still outstanding.
- **HISTORICAL EVIDENCE** — retained evidence whose conclusion or procedure has been superseded.

### 1.2 Approved impedance sources

The only current driver-impedance baselines approved for crossover modelling are:

- Woofer: [`rew/SB17NRX2C35-8 installed.zma`](../rew/SB17NRX2C35-8%20installed.zma)
- Tweeter: [`rew/SB26STWGC-4 installed.zma`](../rew/SB26STWGC-4%20installed.zma)

Both drivers were correctly mounted in the sealed prototype enclosure in their normal mechanical configuration, without temporary sealing putty. The woofer baseline was taken immediately after installation and before deliberate run-in. The matched-rate post-conditioning trace remains comparison evidence only because its approximately 0.342 ohm broadband series-resistance offset prevents promotion to the cooled modelling baseline.

### 1.3 Approved acoustic-source manifest

**PROVISIONAL DESIGN RELEASE:** retain C6 as the installed-woofer-axis source, with C5 as its immediate repeatability witness. Retain TW1 and protected-tweeter C2 as the common-position, tweeter-axis pair. The positive-side `0/+20/+40/+60 degree` woofer and protected-tweeter families are approved sparse-polar evidence. This is a prototype-design release, with the stated uncertainty; it is not a production response specification.

| Use | Current source and interpretation limit |
| --- | --- |
| Woofer-axis crossover source | `rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C6_2026-09-06.mdat`, UUID `1547767f-1781-4e51-b824-462b5a2788e1`; durable export [`000deg_1m_UMC22_2026-09-06.frd`](../rew/frd/SB17NRX2C35-8/000deg_1m_UMC22_2026-09-06.frd), SHA-256 `af3142aeff9dcd232ddb61878452c31afe5cae5446e4bd266b2e4e337488c1ca`; use `500 Hz-12 kHz`. |
| Common-position woofer source | `rew/SB17NRX2C35-8_installed_000deg_tweeter-axis_1m_UMC22_2026-09-06.mdat`, TW1 UUID `12568bef-2ec1-4cc7-be3a-91460b0659fa`; durable export [`000deg_tweeter-axis_1m_UMC22_2026-09-06.frd`](../rew/frd/SB17NRX2C35-8/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd), SHA-256 `03923152b08c36e066cb0f9520c7a76489bf6837e3b85cd06c67af0c12a8e4b7`; use `500 Hz-12 kHz`. |
| Common-position protected-tweeter source | `rew/SB26STWGC-4_installed_0deg_tweeter-axis_1m_UMC22_2026-09-06.mdat`, C2 UUID `898195c2-fc7d-4eee-a877-7be9d3782f0d`; durable export [`000deg_tweeter-axis_1m_UMC22_2026-09-06.frd`](../rew/frd/SB26STWGC-4/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd), SHA-256 `a409445a40e645682b188b7a12596c10f727d8a0f78138f052c043d60bb0ea1e`; use `500 Hz-12 kHz` and apply `+11.14 dB` magnitude only in VituixCAD. |
| Sparse positive-horizontal families | Woofer: `1.5-5 kHz`; protected tweeter: `1.5-12 kHz`. Use their separate `polar/` FRDs, native phase, their approved windows, and no added alignment. |

All current source identities, raw-file and FRD hashes, UUIDs, capture conditions, window validation, rejected attempts, export/release checks, polar results, and the derivation of the protected-tweeter scale are retained once in the audit-only [installed-driver acoustic-source qualification](rew/qualification/INSTALLED_DRIVER_ACOUSTIC_SOURCES_2026-09-06_TO_07.md). Read it to audit a source, change its release, investigate a failure, or reproduce an export; do not load it for routine modelling.

Durable acoustic exports use `rew/frd/<driver>/<AAA>deg_<distance>_<interface>_<date>.frd`; do not overwrite a dataset when a new condition needs a distinct identity.
### 1.4 Current driver state

- Only one woofer and one tweeter are presently available.
- The prototype's geometric net volume is approximately 21.7 L before damping-material effective-volume change.
- The cooled pre-conditioning woofer baseline has one clean sealed-box resonance at approximately 67.0 Hz and no separate resonance near 83 Hz.
- The matched 48 kHz post-conditioning trace moves the resonance to approximately 65.71 Hz, a 1.88% decrease, but still awaits a fully cooled confirmation.
- The woofer's installed total system Q is approximately 0.81–0.82 and remains manageable for development.
- The tweeter's installed impedance agrees closely with published parameters and has no suspicious additional resonance.
- Both drivers remain provisionally retained.
- Seed A's measured filtered branches cross broadly near 1.83 kHz with nearly coincident phase; constructive sum, physical reverse null, and the sparse positive-horizontal full-system set pass proportionately.
- The moderate approximately 2.5–3.1 dB beamwidth change through 1.5–2.5 kHz is retained as a possible later refinement target, not a present failure.
- The as-built Seed A load passes: minimum magnitude is `4.366 ohm`, minimum real part is `4.284 ohm`, and minimum idealised class-B EPDR is `2.563 ohm`; detailed system evidence is in the [Seed A load record](rew/qualification/SEED_A_AS_BUILT_IMPEDANCE_AND_EPDR_2026-09-09.md).
- The raw woofer, protected-tweeter, sparse-polar, Seed A acoustic/load, bounded level/distortion, and external-component surface-thermal packages are complete. The wrong-angle post-thermal trace is excluded; the next driver-relevant gate is matched speaker-two measurement, including a valid hot `0-degree` comparison and confirmation of the narrow high-level feature near `2.18 kHz`.

### 1.5 Project file-location convention

- `rew/` — raw REW measurements and impedance exports; durable acoustic
  exports use the driver-specific `rew/frd/<driver>/` subtree and the naming
  convention in Section 1.3.
- `vituixcad/` — VituixCAD projects and VituixCAD-generated outputs.

## 2. Current impedance-measurement data

### 2.1 File metadata

**VERIFIED FROM BOTH FILE HEADERS**

| Field | Value |
|---|---|
| REW version | 5.40 beta 133 |
| Interface | StarTech ICUSBAUDIO2D generic external USB sound card (**USER-CONFIRMED for all impedance measurements to date**) |
| Measurement date | 2026-08-30 |
| Sweep | 1M logarithmic swept sine, one sweep, -12 dBFS |
| Sample rate | 48 kHz |
| Sense resistor | 100.0 ohm |
| Entered lead resistance | 0.000 ohm |
| Input resistance | 20 kohm |
| Calibration factor | 0.9783 |
| Smoothing / spacing | none / 1/96 octave |
| Point count | 1,276 per file |
| Recorded span | 2.211 Hz to 22.013 kHz |

The woofer was measured at 09:30:58 and the tweeter at 10:00:22. The exported
headers preserve only a generic Windows USB-audio source name, so the StarTech
identity comes from the user's measurement-history confirmation rather than
independent file metadata. The headers do not record driver-terminal voltage,
enclosure fill state, ambient temperature, or screw torque. Those conditions
should be recorded with future comparison measurements.

### 2.2 Data quality and usable range

Both files are valid, densely sampled ZMA exports with frequency, impedance magnitude, and phase. Their traces are smooth and physically coherent through the resonances and crossover region.

**VERIFIED MEASUREMENT:** points below approximately **8-10 Hz** are measurement artifacts. They fall below credible voice-coil resistance and must not be used to estimate DCR, Q, or low-frequency load. This does not affect crossover modelling or the sealed-box result around 67 Hz.

### 2.3 Reproducible impedance-peak calculation

The fitted Q values below use a curve-consistent baseline resistance, $R_0$, estimated from the real part of impedance at 10 Hz:

$$
R_0=|Z|\cos\phi.
$$

For a single dominant impedance resonance, define the bandwidth level and crossing frequencies by

$$
Z_{th}=\sqrt{R_0Z_{max}},
$$

with $f_1$ and $f_2$ at the rising and falling crossings of that magnitude. Log-frequency interpolation between adjacent measured points is used. Then

$$
f_0=\sqrt{f_1f_2},
$$

$$
Q_m=\frac{f_0}{f_2-f_1}\sqrt{\frac{Z_{max}}{R_0}},
\qquad
Q_e=\frac{Q_m}{Z_{max}/R_0-1},
\qquad
Q_t=\frac{Q_m}{Z_{max}/R_0}.
$$

For the installed woofer these are box-system quantities $Q_{mc}$, $Q_{ec}$, and $Q_{tc}$. For the tweeter, whose own rear chamber defines its mechanical system, they are reported conventionally as $Q_{ms}$, $Q_{es}$, and $Q_{ts}$. They are approximate equivalent-circuit fits, not independent direct measurements of every loss mechanism.

## 3. Woofer published reference data

### 3.1 Manufacturer specifications

**PUBLISHED - SB Acoustics SB17NRX2C35-8 datasheet**

| Parameter | Published value |
|---|---:|
| Nominal impedance | 8 ohm |
| DC resistance, $R_e$ | 5.7 ohm |
| Voice-coil inductance, $L_e$ | 0.15 mH |
| Effective diaphragm area, $S_d$ | 118 cm2 |
| Free-air resonance, $F_s$ | 36.5 Hz |
| Sensitivity | 87 dB at 2.83 V/1 m |
| $Q_{ms}$ | 4.55 |
| $Q_{es}$ | 0.47 |
| $Q_{ts}$ | 0.42 |
| Moving mass, $M_{ms}$ | 13.9 g |
| Force factor, $Bl$ | 6.25 T m |
| Equivalent compliance volume, $V_{as}$ | 27 L |
| Suspension compliance, $C_{ms}$ | 1.37 mm/N |
| Mechanical resistance, $R_{ms}$ | 0.7 kg/s |
| Linear excursion, $X_{max}$ | +/-5.5 mm |
| Rated power | 50 W |

### 3.2 Published-parameter enclosure prediction

Using the published $F_s=36.5$ Hz, $Q_{ts}=0.42$, $V_{as}=27$ L, and the approximately 21.7 L geometric net volume gives:

- **DERIVED:** $F_c\approx54.7$ Hz;
- **DERIVED:** $Q_{tc}\approx0.63$;
- **DERIVED:** ideal anechoic small-signal $F_3\approx62.3$ Hz;
- no response peak from the nominal second-order sealed alignment.

These remain a record of the datasheet-based design case, not a description of the completed prototype.

## 4. Woofer installed measurement

### 4.1 Principal measured features

**VERIFIED MEASUREMENT / DERIVED FROM CURRENT ZMA**

| Quantity | Result |
|---|---:|
| Curve-consistent $R_0$ estimate | 5.645 ohm |
| Impedance magnitude maximum | 96.544 ohm at 67.272 Hz |
| Bandwidth threshold, $Z_{th}$ | 23.345 ohm |
| Lower threshold crossing, $f_1$ | 57.811 Hz |
| Upper threshold crossing, $f_2$ | 77.583 Hz |
| Derived sealed-system resonance, $F_c$ | 66.971 Hz |
| $Q_{mc}$ | 14.008 |
| $Q_{ec}$ | 0.870 |
| $Q_{tc}$ | 0.819 |
| Positive phase maximum | +61.79 degrees at 57.81 Hz |
| Negative phase minimum | -63.54 degrees at 77.16 Hz |

The impedance maximum is a magnitude in **ohms**, not an inductance. Its height mainly reflects motional back-EMF and the balance of mechanical and electrical damping. High impedance at resonance is not an amplifier-current hazard.

The close agreement between the curve-derived $R_0\approx5.645$ ohm and the published $R_e=5.7$ ohm is reassuring. A nulled cold-DCR measurement taken with this setup would still be preferable when an exact series-resistance model is required.

### 4.2 The secondary-resonance question

**VERIFIED MEASUREMENT:** the correctly installed woofer trace has one low-frequency resonance only. At **82.94 Hz**, the impedance is **16.46 ohm at -61.06 degrees**, lying smoothly on the falling side of the 67 Hz peak. There is no local maximum or phase reversal there.

This is strong evidence that a distinct feature near 83 Hz is not inherent to the normally installed driver/enclosure system. The ordinary mounting has eliminated the leak-related mode without needing temporary sealing compound.

### 4.3 Idealized low-frequency consequence

For a normalized second-order sealed high-pass response,

$$
|H(x)|^2=\frac{x^4}{(1-x^2)^2+x^2/Q_{tc}^2},
\qquad x=\frac{f}{F_c}.
$$

Using the measured $F_c=66.97$ Hz and derived $Q_{tc}=0.819$:

- **DERIVED:** ideal anechoic small-signal $F_3\approx59.0$ Hz;
- **DERIVED:** a modest maximum of approximately **+0.29 dB near 133 Hz**;
- $F_3$ lies below $F_c$, as expected because $Q_{tc}>0.707$.

The apparently similar or slightly lower $F_3$ than the published-parameter design case does not mean equal deep-bass behaviour. With both responses normalized at high frequency, the idealized installed alignment differs approximately as follows:

| Frequency | Installed minus published-parameter case |
|---:|---:|
| 30 Hz | -2.28 dB |
| 40 Hz | -1.32 dB |
| 50 Hz | -0.33 dB |
| 80 Hz | +1.11 dB |
| 100 Hz | +1.08 dB |
| 150 Hz | +0.64 dB |

Physical interpretation: relative to the nominal design calculation, this state trades some output below roughly 50 Hz for a mild broad lift through the upper bass. The predicted lift is small enough to remain quite plausible for the intended prototype, but room placement and the eventual woofer-series resistance will matter.

These response figures are **DERIVED**, not acoustic measurements. They assume that the installed system is adequately represented by a linear second-order sealed model. Leakage, damping material, baffle step, room gain, crossover resistance, excursion, and thermal effects are not included.

### 4.4 Crossover-region impedance

**VERIFIED FROM CURRENT ZMA**

| Frequency | \|Z\| | Phase |
|---:|---:|---:|
| 2199.83 Hz | 7.9687 ohm | +10.425 degrees |
| 2297.23 Hz | 7.9767 ohm | +10.753 degrees |
| 2398.93 Hz | 8.0119 ohm | +11.068 degrees |
| 2505.14 Hz | 8.0403 ohm | +11.499 degrees |

The woofer is close to 8 ohm in magnitude around the intended crossover, but it is not an 8 ohm resistor. At 2297 Hz its rectangular equivalent is approximately $7.84+j1.49$ ohm. The full ZMA should therefore be used in VituixCAD.

There is no strong electrical anomaly in the 2.2-2.5 kHz region. Small higher-frequency impedance structure cannot establish cone-breakup amplitude or acoustic suitability; the installed FRD and distortion measurements remain decisive.

### 4.5 Woofer judgement

**PROVISIONAL DECISION:** retain the SB17NRX2C35-8 in the present enclosure.

The measured $Q_{tc}\approx0.82$ sits inside the project's broadly manageable **0.75-0.95** development range. The alignment is warmer than the published-parameter design case but is not severely resonant. No additional low-frequency mode survives normal installation, and the impedance near the intended crossover is smooth and convenient to model.

The later bounded complete-system package establishes proportionate acoustic,
level/distortion, and broad-compression evidence for speaker one. Pair matching
and production spread remain open.

### 4.6 Conditioning status and current baseline

**CURRENT DECISION:** the cooled pre-conditioning installed ZMA remains the crossover baseline. The matched 48 kHz post-conditioning trace remains comparison evidence because its approximately `+0.342 ohm` broadband real-series offset prevents promotion. The detailed 45 Hz and 30 Hz operating estimates, comparison calculation, and supersession rationale are retained in [Driver-analysis change history](history/DRIVER_ANALYSIS_CHANGELOG.md).

Use [DRIVER_RUNIN.md](DRIVER_RUNIN.md) for any future bounded conditioning, cooldown, cold-DCR, calibration, rested-confirmation, safety, and measurement-based stopping rules. No dedicated tweeter run-in is justified.
## 5. Tweeter published reference data

### 5.1 Manufacturer specifications

**PUBLISHED - SB Acoustics SB26STWGC-4 datasheet**

| Parameter | Published value |
|---|---:|
| Nominal impedance | 4 ohm |
| DC resistance, $R_e$ | 3.2 ohm |
| Voice-coil inductance, $L_e$ | 0.04 mH |
| Effective diaphragm area, $S_d$ | 6.2 cm2 |
| Resonance, $F_s$ | 780 Hz |
| Sensitivity | 93 dB at 2.83 V/1 m |
| $Q_{ms}$ | 2.8 |
| $Q_{es}$ | 2.1 |
| $Q_{ts}$ | 1.2 |
| Force factor, $Bl$ | 1.6 T m |
| Moving mass, $M_{ms}$ | 0.3 g |
| Linear excursion, $X_{max}$ | +/-0.6 mm |
| Rated power statement | 120 W with the manufacturer's stated 2.6 kHz, 12 dB/octave Butterworth high-pass condition |

The 120 W figure is conditional, not an unconditional broadband power rating.

## 6. Tweeter installed measurement

### 6.1 Principal measured features

**VERIFIED MEASUREMENT / DERIVED FROM CURRENT ZMA**

| Quantity | Installed result | Published |
|---|---:|---:|
| Curve-consistent $R_0$ estimate | 3.274 ohm | $R_e=3.2$ ohm |
| Impedance magnitude maximum | 7.557 ohm at 755.62 Hz | not stated |
| Bandwidth-derived $F_s$ | 760.91 Hz | 780 Hz |
| $Q_{ms}$ | 2.622 | 2.8 |
| $Q_{es}$ | 2.005 | 2.1 |
| $Q_{ts}$ | 1.136 | 1.2 |
| Positive phase maximum | +24.04 degrees at 574.31 Hz | not stated |
| Negative phase minimum | -22.32 degrees at 979.91 Hz | not stated |

The fitted resonance is approximately **2.4% below** the published value; the fitted Q values are within approximately **5-6%**. This is close agreement for a real installed sample and shows no electrical reason to doubt the tweeter.

The magnitude maximum occurs a few hertz below the bandwidth-derived resonance because the rising voice-coil impedance and the discrete frequency samples make the magnitude-peak and ideal phase-centre definitions slightly different. Reporting the result as approximately **761 Hz** is appropriately precise.

### 6.2 Crossover-region impedance

**VERIFIED FROM CURRENT ZMA**

| Frequency | \|Z\| | Phase |
|---:|---:|---:|
| 2199.83 Hz | 3.4884 ohm | -5.699 degrees |
| 2297.23 Hz | 3.4768 ohm | -5.032 degrees |
| 2398.93 Hz | 3.4786 ohm | -4.445 degrees |
| 2505.14 Hz | 3.4787 ohm | -3.725 degrees |

Around the intended crossover the tweeter is approximately **3.48 ohm**, nearly resistive but mildly capacitive. At 2297 Hz its rectangular equivalent is approximately $3.46-j0.30$ ohm. It must not be modelled as a frequency-independent 4 ohm resistor.

There are no suspicious secondary impedance peaks. The normal installed mounting has not introduced an evident rear-cavity or front-cavity electrical resonance.

### 6.3 Tweeter judgement

**PROVISIONAL DECISION:** retain the SB26STWGC-4.

The then-intended `2.2-2.4 kHz` region was approximately three times the
measured resonance frequency. That ratio was only a preliminary plausibility
check; the later installed, filtered, summed, and bounded level evidence now
owns the Seed A decision.

No dedicated tweeter run-in is presently justified. Use the baseline and protected-use procedure in [DRIVER_RUNIN.md](DRIVER_RUNIN.md); never apply an unfiltered conditioning signal directly to the bare tweeter.

### 6.4 Measurement protection and current geometry

**CURRENT CONFIGURATION / DERIVED MODEL CORRECTION:** the common-position source pair uses the fixed microphone on the tweeter axis, `1.000 m` from the baffle-plane pivot; preserve its measured relative timing and do not add a geometric delay. The raw tweeter was captured through the measured `10.13 uF`, `0.08 ohm` ESR series protection capacitor. Its post-capacitor reference leaves a constant `+11.14 dB` magnitude correction for VituixCAD; apply no phase, delay, polarity, smoothing, or minimum-phase correction. This correction is not an absolute-SPL calibration.

Use `Hann 2.0 ms` left / `Tukey 0.25 3.5 ms` right at each own direct peak, with FDW and MTW off, for the phase-bearing on-axis sources. The woofer polar family uses that window; the protected-tweeter polar family uses a `1.5 ms` right window. Preserve native phase and interpret the woofer polar family only over `1.5-5 kHz` and the protected-tweeter family only over `1.5-12 kHz`.

The qualified UMC22 electrical route, protection component, direct sound geometry, source windows, raw capture provenance, and all release checks are in the [installed-driver acoustic-source qualification](rew/qualification/INSTALLED_DRIVER_ACOUSTIC_SOURCES_2026-09-06_TO_07.md). The repeat procedures own the safe operational sequence.
## 7. Driver-specific modelling consequences

### 7.1 Current VituixCAD inputs

Use only `rew/SB17NRX2C35-8 installed.zma` and `rew/SB26STWGC-4 installed.zma`. In `vituixcad/Prototype loudspeaker crossover Seed A practical measured 2026-09-08.vxp`, use the verified common-position TW1/C2 FRDs and sparse `0/+20/+40/+60 degree` families, with native phase, normal polarity, zero coordinates, no response delay/smoothing/minimum-phase conversion, woofer `0.00 dB`, and tweeter `+11.14 dB` (`3.605786` linear multiplier). This is source configuration, not a new crossover decision.

The practical model contains the measured capacitor, resistor, inductor, ESR, and DCR values. The older nominal-component sparse-polar project and its screenshots are historical corroboration only; do not use them as present component evidence. Generated unmeasured-angle curves and the positive-side sparse set remain outside the model evidence boundary.

### 7.2 Full-system level, distortion, and thermal consequence

**VERIFIED MEASUREMENT / USER-REPORTED CONDITIONS / DERIVED — BOUNDED PASS
WITH ONE DEFERRED COMPARISON (2026-09-10):** the retained
[`rew/SPK_Seed_A_full_system_level_thermal_20260910.mdat`](../rew/SPK_Seed_A_full_system_level_thermal_20260910.mdat)
contains the intended nominal `0.5/1/2/4 V RMS` traces. The exact shorter
measurement names, trace identities, source hash, comparison method, and
distortion samples are in the [owning
qualification](rew/qualification/SEED_A_FULL_SYSTEM_LEVEL_AND_THERMAL_QUALIFICATION_2026-09-10.md).

Both interface channels retained at least `27.9 dB` headroom and all intended
sweeps completed without a reported warning or audible anomaly. Sampled
distortion passes the project limits. Nominal-voltage normalisation shows no
broad compression above `0.5 dB`; a narrow `4 V` versus `2 V` difference of
about `-1.28 dB` near `2.18 kHz` is retained for speaker-two confirmation.
R(Tser) and L(W1) surface rises during the 15-minute nominal `2 V RMS`
CTA-2034 exposure were only `0.4` and `0.2 degrees C`, respectively, and
both were stable over the final five minutes.

The post-thermal trace is excluded from all acoustic conclusions because the
speaker was inadvertently at `60 degrees`. The user has explicitly waived an
immediate repeat on proportionality grounds. A correct hot `0-degree`
comparison is required on speaker two; repeat speaker one only if that test
reveals an anomaly.

### 7.3 Consequences for crossover decisions

- Treat the measured approximately `1.83 kHz` Seed A branch equality and its
  moderate directivity flare as the current prototype result; do not relabel it
  as the earlier `2.2-2.4 kHz` LR4-like design hypothesis.
- Include each driver's natural acoustic response, complex impedance, physical offset, baffle effects, component DCR, and tolerances.
- Do not infer cone-breakup control, tweeter protection, directivity, or summation from impedance alone.
- Use [CROSSOVER_DESIGN.md](CROSSOVER_DESIGN.md) for the active topology, polarity, validation loop, and system-load gates.
- Use [CROSSOVER_COMPONENT_DEVELOPMENT.md](CROSSOVER_COMPONENT_DEVELOPMENT.md) only when component procurement, winding, PCB, or construction detail is relevant.

## 8. Procurement and pair-matching decision

**PROVISIONAL DECISION:** continue with the present drivers, Seed A, and
enclosure. The acoustic-response, as-built load, bounded level/distortion, and
external-component surface-thermal gates now pass proportionately. Proceed
with the second-channel SB17NRX2C35-8 and SB26STWGC-4 and use that build as the
next matched confirmation.

For the second speaker:

- condition and measure the drivers under the same documented conditions;
- compare installed resonance/Q, crossover-region impedance, acoustic response, and distortion;
- establish acceptable pair tolerances before freezing the stereo build.

Matching complete installed behaviour matters more than reproducing every datasheet value exactly.

## 9. Open items and priorities

### 9.1 Next driver evidence gates

1. Preserve the raw woofer, protected-tweeter, sparse raw-polar, and completed
   Seed A full-system authorities. The detailed Seed A commissioning evidence
   belongs in its [dated history
   record](rew/history/SEED_A_EXTERNAL_CROSSOVER_COMMISSIONING_2026-09-08_TO_09.md),
   not in this priority list.
2. Preserve the three VituixCAD authorities: the verified measured baseline,
   the nominal sparse-polar Seed A reference, and its practical
   measured-component successor. Its electrical/source semantics parse cleanly;
   retain the user's R(Tpar) symbol move as cosmetic and do not undo it.
3. Preserve the completed [full-system level and thermal
   qualification](rew/qualification/SEED_A_FULL_SYSTEM_LEVEL_AND_THERMAL_QUALIFICATION_2026-09-10.md).
   Exclude its `60-degree` post-thermal trace from every hot-acoustic
   comparison; do not repeat speaker one unless speaker-two evidence reveals an
   anomaly.
4. Procure/build speaker two and repeat the decisive installed, crossover,
   load, level/distortion, and bounded thermal checks under matched conditions.
   Include a correct hot `0-degree` comparison and examine the narrow
   high-level feature near `2.18 kHz`.
5. Keep the cooled repeat woofer ZMA in
   [DRIVER_RUNIN.md](DRIVER_RUNIN.md) as a lower-priority alignment question;
   promote it only if its resistance and conditions are reproducible.
6. Record enclosure fill/lining, ambient temperature, driver-terminal voltage,
   mounting, and calibration conditions with any replacement evidence.
7. Do not promote Seed B unless matched speaker-two evidence exposes a broad,
   design-relevant weakness.

### 9.2 Remaining driver uncertainties

- Pair-to-pair distortion/compression consistency and whether the narrow
  approximately `2.18 kHz` high-level feature repeats.
- A valid immediate hot `0-degree` acoustic comparison; the first attempt is
  excluded for wrong orientation.
- Final damping's effect on the sealed alignment and the woofer-series inductor DCR's effect on $Q_{tc}$.
- Reproducibility of the cooled woofer impedance after conditioning.
- Generic rather than unit-specific ECM8000 magnitude calibration and lack of absolute-SPL calibration.
- Production spread and stereo-pair matching.
- Individual free-air T/S parameters, if later needed to explain rather than directly model the installed alignment.

## 10. Sources and related authorities

### 10.1 Selected current project measurements

This short list is not the acoustic-source inventory; Section 1.3 and the
[REW dispatcher](rew/README.md) own the complete retained source map.

- [`rew/SB17NRX2C35-8 installed.zma`](../rew/SB17NRX2C35-8%20installed.zma)
- [`rew/SB17NRX2C35-8 runin 30Hz 4Vrms 1h 48kHz.zma`](../rew/SB17NRX2C35-8%20runin%2030Hz%204Vrms%201h%2048kHz.zma) — comparison evidence; not the crossover baseline
- [`rew/SB26STWGC-4 installed.zma`](../rew/SB26STWGC-4%20installed.zma)
- [`rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat`](../rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat) — Seed A acoustic package
- [`rew/SPK_impedance_WT_1_20260909.mdat`](../rew/SPK_impedance_WT_1_20260909.mdat) — Seed A as-built load package
- [`rew/SPK_Seed_A_full_system_level_thermal_20260910.mdat`](../rew/SPK_Seed_A_full_system_level_thermal_20260910.mdat) — bounded full-system level/distortion and thermal package

### 10.2 Primary sources

- [SB17NRX2C35-8 datasheet](https://sbacoustics.com/wp-content/uploads/2020/02/6in-SB17NRX2C35-8.pdf)
- [SB26STWGC-4 product page](https://sbacoustics.com/product/sb26stwgc-4-fabric/)
- [SB26STWGC-4 datasheet](https://sbacoustics.com/wp-content/uploads/2020/05/SB26STWGC-4.pdf)
- [Klippel, *Mechanical Fatigue and Load-Induced Aging of Loudspeaker Suspension*](https://www.klippel.de/fileadmin/klippel/Bilder/Know-How/Literature/Papers/Aging%20of%20loudspeaker%20suspension_Klippel.pdf)
- [REW impedance-measurement documentation](https://www.roomeqwizard.com/help/help_en-GB/html/impedancemeasurement.html)

### 10.3 Procedures and qualification evidence

- [Woofer conditioning and impedance procedure](DRIVER_RUNIN.md)
- [Installed acoustic-response method](rew/FRD_MEASUREMENT_METHOD.md)
- [Completed UMC22 installed-woofer runbook](rew/procedures/UMC22_INSTALLED_WOOFER_FRD.md)
- [UMC22 qualification evidence](rew/qualification/UMC22_FRD_QUALIFICATION.md)
- [Seed A full-system level and thermal qualification](rew/qualification/SEED_A_FULL_SYSTEM_LEVEL_AND_THERMAL_QUALIFICATION_2026-09-10.md)
- [UMC202HD desktop-dropout diagnosis](rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md)
- [Driver-impact change history](history/DRIVER_ANALYSIS_CHANGELOG.md)

## 11. Change history

The active file intentionally excludes interface/UI/fixture chronology. Read [DRIVER_ANALYSIS_CHANGELOG.md](history/DRIVER_ANALYSIS_CHANGELOG.md) for driver-impact changes and supersession rationale; use the linked REW qualification/history records only when auditing the measurement route.
