# Driver Analysis and Measurement Record

**Project:** sealed passive two-way loudspeaker prototype
**Woofer:** SB Acoustics **SB17NRX2C35-8**
**Tweeter:** SB Acoustics **SB26STWGC-4**
**Record created:** 2026-08-27
**Last updated:** 2026-09-06

> - **Lifecycle:** ACTIVE DRIVER EVIDENCE AUTHORITY
> - **Owns:** evidence classes, approved driver ZMA/FRD sources, measurement conditions and quality, woofer/tweeter results and derivations, retention and procurement decisions, driver-specific modelling consequences, uncertainties, and next evidence gates
> - **Does not own:** REW/interface qualification chronology, fixture design, detailed acoustic-capture procedure, crossover-component construction, or room-placement evidence
> - **Current decision:** provisionally retain both installed drivers and continue modelling from the approved ZMA baselines; no FRD is yet approved as a driver-design source
> - **Next gate:** one reviewed 0-degree installed-woofer capture, followed by a reusable installed-baffle FRD series and a cooled reproducible woofer ZMA
> - **Limitations:** one sample of each driver; incomplete baseline conditions; no approved installed acoustic response, directivity, or distortion data
> - **As of:** 2026-09-06

This is the durable engineering record for the driver investigation. It supplements [README.md](../README.md). Detailed dated driver-impact history is retained in [DRIVER_ANALYSIS_CHANGELOG.md](history/DRIVER_ANALYSIS_CHANGELOG.md).

## 1. Authority, evidence, and current sources

### 1.1 Evidence labels

- **VERIFIED MEASUREMENT** — directly present in an archived measurement file or explicitly recorded instrument result.
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

### 1.3 Approved acoustic sources and current capture state

No installed-baffle FRD is yet approved as a driver-design source. The completed UMC22 repeatability sweeps qualify the measurement route; they are not substitutes for reusable driver FRD.

The current user-reported physical/no-signal start state and the one-capture-then-review gate remain reachable in the current [UMC22 installed-woofer FRD runbook](rew/procedures/UMC22_INSTALLED_WOOFER_FRD.md). That record owns the fresh no-excitation audit, exact route and calibration checks, one controlled 0-degree capture, and review of headroom, metadata, impulse/ETC, and the REW-native window before any repeat, rotation, or export. Qualification evidence and its generic microphone/absolute-SPL limitations are in [UMC22 FRD qualification](rew/qualification/UMC22_FRD_QUALIFICATION.md).

### 1.4 Current driver state

- Only one woofer and one tweeter are presently available.
- The prototype's geometric net volume is approximately 21.7 L before damping-material effective-volume change.
- The cooled pre-conditioning woofer baseline has one clean sealed-box resonance at approximately 67.0 Hz and no separate resonance near 83 Hz.
- The matched 48 kHz post-conditioning trace moves the resonance to approximately 65.71 Hz, a 1.88% decrease, but still awaits a fully cooled confirmation.
- The woofer's installed total system Q is approximately 0.81–0.82 and remains manageable for development.
- The tweeter's installed impedance agrees closely with published parameters and has no suspicious additional resonance.
- Both drivers remain provisionally retained.
- The intended approximately 2.2–2.4 kHz LR4-like acoustic region remains provisional pending installed magnitude, common timing/phase, directivity, and distortion evidence.
- The UMC22 route is qualified only for controlled installed-woofer FRD at this stage. Raw-tweeter and polar work require their own protection/procedure gates.

### 1.5 Project file-location convention

- `rew/` — REW measurements and exports, including `.mdat`, `.zma`, tab-delimited impedance exports, and FRD exports.
- `vituixcad/` — VituixCAD projects and VituixCAD-generated outputs.

## 2. Current impedance-measurement data

### 2.1 File metadata

**VERIFIED FROM BOTH FILE HEADERS**

| Field | Value |
|---|---|
| REW version | 5.40 beta 133 |
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

The woofer was measured at 09:30:58 and the tweeter at 10:00:22. The headers do not record driver-terminal voltage, enclosure fill state, ambient temperature, or screw torque. Those conditions should be recorded with future comparison measurements.

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

This does not yet establish acoustic smoothness, maximum output, distortion, compression, or suitability for pair matching.

### 4.6 Conditioning calculation and superseded operating note

**USER-REPORTED TEST CONDITION — 2026-08-31:** the installed woofer was driven with a 45 Hz sine wave at 3.44 V RMS measured at its terminals.

**DERIVED FROM THE CURRENT INSTALLED ZMA:** near 45 Hz the load is approximately 10.42 ohm at +50.6 degrees, corresponding to approximately 0.330 A RMS, 1.14 VA apparent power, and 0.72 W real electrical input. The nominal-resistor shorthand $V^2/8=1.48\ \mathrm{W}$ does not describe this reactive, frequency-dependent load.

Using the measured complex impedance with published $R_e=5.7\ \mathrm{ohm}$, $L_e=0.15\ \mathrm{mH}$, and $Bl=6.25\ \mathrm{T\,m}$ gives an **estimated** diaphragm travel of approximately 2.13 mm peak (4.27 mm peak-to-peak). The later 30 Hz, 4.0 V RMS development point predicts approximately 0.565 A RMS, 1.9 W real input, and 2.6 mm peak travel, about 47% of published $X_{max}$. These are linear equivalent-circuit estimates, not displacement measurements.

The former operating steps are superseded by [DRIVER_RUNIN.md](DRIVER_RUNIN.md), which owns the bounded procedure, cold-DCR cooldown gate, fixed 48 kHz calibration, rested confirmation, safety stops, and measurement-based stopping rule.

### 4.7 2026-08-31 matched 48 kHz post-conditioning comparison

**USER-CLARIFIED MEASUREMENT HISTORY:** [`rew/SB17NRX2C35-8 installed.zma`](../rew/SB17NRX2C35-8%20installed.zma) was measured immediately after installation, before any deliberate run-in. [`rew/SB17NRX2C35-8 runin 30Hz 4Vrms 1h 48kHz.zma`](../rew/SB17NRX2C35-8%20runin%2030Hz%204Vrms%201h%2048kHz.zma) followed some intervening programme-material use and then one hour of 30 Hz conditioning at 4 V RMS. The comparison therefore shows the net change across both activities; it cannot assign the change uniquely to the final sine-wave hour.

**VERIFIED MEASUREMENT / DERIVED:** both traces use a 48 kHz sample rate and otherwise matched REW impedance settings. The bandwidth-derived sealed-system resonance changed from **66.9712 Hz** to **65.7115 Hz**, a change of **-1.2597 Hz (-1.881%)**. Interpreted as a stiffness/compliance change at effectively constant moving mass, this corresponds to approximately **+3.87% total system compliance**.

The raw impedance maximum changed only from approximately **96.54 ohm** to **96.85 ohm**, while the post-run trace contains approximately **+0.342 ohm** of nearly frequency-independent real series resistance from 300 Hz to 10 kHz and essentially unchanged reactance there. If that offset were entirely voice-coil copper resistance, it would correspond to roughly a **15 °C** temperature rise; changed lead or contact resistance could contribute instead. Subtracting the series offset gives a post-run peak of approximately **96.50 ohm**, $Q_{mc}\approx13.8$, $Q_{ec}\approx0.86$, and $Q_{tc}\approx0.81$. There is therefore no persuasive evidence of a durable resonance-peak or damping change in this pair of files.

**INFERRED:** combining the pre-run free-air estimate $F_s\approx54.22\ \mathrm{Hz}$, the fixed-box stiffness contribution derived from the earlier installed measurement, and the new $F_c$ gives an effective post-conditioning free-air resonance of approximately **52.66 Hz**. That is approximately **2.9% below** the pre-run estimate and implies approximately **6.0% greater driver compliance**, but it remains roughly **44% above** the published 36.5 Hz value. This is an indirect estimate, not a current free-air measurement.

**PROVISIONAL DECISION:** treat the downward resonance-frequency movement as encouraging, but retain the original cooled installed ZMA as the crossover baseline. Repeat the post-run measurement only after the cold-DCR and matched-condition gates in [DRIVER_RUNIN.md](DRIVER_RUNIN.md) have been met.

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

The intended 2.2-2.4 kHz crossover is approximately three times the measured resonance frequency. That is a plausible region for a steep **acoustic** fourth-order high-pass, but the ratio alone does not prove protection or correct summation. Installed-baffle acoustic response, phase, distortion, level testing, and the complete filtered transfer function remain required.

No dedicated tweeter run-in is presently justified. Use the baseline and protected-use procedure in [DRIVER_RUNIN.md](DRIVER_RUNIN.md); never apply an unfiltered conditioning signal directly to the bare tweeter.

## 7. Driver-specific modelling consequences

### 7.1 Current VituixCAD impedance inputs

Use only:

- `rew/SB17NRX2C35-8 installed.zma` for the woofer;
- `rew/SB26STWGC-4 installed.zma` for the tweeter.

The useful loads near 2.30 kHz are approximately 7.98 ohm at +10.8 degrees for the woofer and 3.48 ohm at -5.0 degrees for the tweeter. The full complex ZMA, not those spot values or nominal impedances, belongs in VituixCAD.

The post-conditioning woofer file remains comparison evidence until a cooled repeat confirms resonance position and broadband resistance. No acoustic optimisation is defensible until phase-bearing installed-baffle FRD exists with common timing.

### 7.2 Consequences for crossover decisions

- Treat approximately 2.2–2.4 kHz LR4-like acoustic slopes as a hypothesis, not a locked electrical network.
- Include each driver's natural acoustic response, complex impedance, physical offset, baffle effects, component DCR, and tolerances.
- Do not infer cone-breakup control, tweeter protection, directivity, or summation from impedance alone.
- Use [CROSSOVER_DESIGN.md](CROSSOVER_DESIGN.md) for the active topology, polarity, validation loop, and system-load gates.
- Use [CROSSOVER_COMPONENT_DEVELOPMENT.md](CROSSOVER_COMPONENT_DEVELOPMENT.md) only when component procurement, winding, PCB, or construction detail is relevant.

## 8. Procurement and pair-matching decision

**PROVISIONAL DECISION:** continue with the present driver pair and enclosure. Delay purchase of the second-channel drivers until the prototype has passed the acoustic-response, distortion, crossover-feasibility, and final-load gates.

If the prototype passes:

- buy another SB17NRX2C35-8 and SB26STWGC-4;
- condition and measure them under the same documented conditions;
- compare installed resonance/Q, crossover-region impedance, acoustic response, and distortion;
- establish acceptable pair tolerances before freezing the stereo build.

Matching complete installed behaviour matters more than reproducing every datasheet value exactly.

## 9. Open items and priorities

### 9.1 Next driver evidence gates

1. Under the [current UMC22 runbook](rew/procedures/UMC22_INSTALLED_WOOFER_FRD.md), reconfirm the user-reported start state without excitation and acquire only the authorised first 0-degree installed-woofer capture.
2. Review headroom, stored calibration/routing/timing metadata, impulse/ETC, and a documented REW-native window before repeats, rotation, or export.
3. Complete the bounded conditioning/cooldown loop in [DRIVER_RUNIN.md](DRIVER_RUNIN.md), then promote a reproducible cooled 48 kHz woofer ZMA only if its resistance and conditions pass.
4. Record enclosure fill/lining, ambient temperature, driver-terminal voltage, mounting, and calibration conditions with replacement evidence.
5. Acquire installed-baffle magnitude/common-timing phase for both drivers, then horizontal off-axis and controlled distortion/compression data.
6. Validate the filtered drivers, acoustic sum, reverse-polarity null, and final impedance/EPDR after crossover construction.

### 9.2 Remaining driver uncertainties

- Installed acoustic magnitude, phase, and directivity of both drivers.
- Woofer and tweeter distortion/compression at required listening levels.
- Final damping's effect on the sealed alignment and the woofer-series inductor DCR's effect on $Q_{tc}$.
- Reproducibility of the cooled woofer impedance after conditioning.
- Generic rather than unit-specific ECM8000 magnitude calibration and lack of absolute-SPL calibration.
- Raw-tweeter protection and polar-measurement release.
- Production spread and stereo-pair matching.
- Individual free-air T/S parameters, if later needed to explain rather than directly model the installed alignment.

## 10. Sources and related authorities

### 10.1 Current project measurements

- [`rew/SB17NRX2C35-8 installed.zma`](../rew/SB17NRX2C35-8%20installed.zma)
- [`rew/SB17NRX2C35-8 runin 30Hz 4Vrms 1h 48kHz.zma`](../rew/SB17NRX2C35-8%20runin%2030Hz%204Vrms%201h%2048kHz.zma) — comparison evidence; not the crossover baseline
- [`rew/SB26STWGC-4 installed.zma`](../rew/SB26STWGC-4%20installed.zma)

### 10.2 Primary sources

- [SB17NRX2C35-8 datasheet](https://sbacoustics.com/wp-content/uploads/2020/02/6in-SB17NRX2C35-8.pdf)
- [SB26STWGC-4 product page](https://sbacoustics.com/product/sb26stwgc-4-fabric/)
- [SB26STWGC-4 datasheet](https://sbacoustics.com/wp-content/uploads/2020/05/SB26STWGC-4.pdf)
- [Klippel, *Mechanical Fatigue and Load-Induced Aging of Loudspeaker Suspension*](https://www.klippel.de/fileadmin/klippel/Bilder/Know-How/Literature/Papers/Aging%20of%20loudspeaker%20suspension_Klippel.pdf)
- [REW impedance-measurement documentation](https://www.roomeqwizard.com/help/help_en-GB/html/impedancemeasurement.html)

### 10.3 Procedures and qualification evidence

- [Woofer conditioning and impedance procedure](DRIVER_RUNIN.md)
- [Installed acoustic-response method](rew/FRD_MEASUREMENT_METHOD.md)
- [Current UMC22 installed-woofer runbook](rew/procedures/UMC22_INSTALLED_WOOFER_FRD.md)
- [UMC22 qualification evidence](rew/qualification/UMC22_FRD_QUALIFICATION.md)
- [UMC202HD desktop-dropout diagnosis](rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md)
- [Driver-impact change history](history/DRIVER_ANALYSIS_CHANGELOG.md)

## 11. Change history

The active file intentionally excludes interface/UI/fixture chronology. Read [DRIVER_ANALYSIS_CHANGELOG.md](history/DRIVER_ANALYSIS_CHANGELOG.md) for driver-impact changes and supersession rationale; use the linked REW qualification/history records only when auditing the measurement route.
