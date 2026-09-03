# Driver Analysis and Measurement Record

**Project:** sealed passive two-way loudspeaker prototype  
**Woofer:** SB Acoustics **SB17NRX2C35-8**  
**Tweeter:** SB Acoustics **SB26STWGC-4**  
**Record created:** 2026-08-27  
**Last updated:** 2026-09-03

> **Standing instruction for future conversations:** Read this file before doing any work that concerns the drivers, enclosure alignment, crossover, or related measurements. Update it whenever new conditioning, electrical or acoustic measurements, calculations, simulations, crossover tuning, pair matching, procurement decisions, or superseding conclusions materially change the picture. Date each addition and label facts according to the evidence categories below. When the measurement baseline is explicitly replaced, remove obsolete source references and every numerical conclusion that depends on them. If a finding changes a project decision, update the main README as well.

This is the durable engineering record for the driver investigation. It supplements [README.md](README.md); it does not turn electrical measurements or provisional calculations into final acoustic design decisions.

## 1. How to read and maintain this record

### 1.1 Evidence labels

- **VERIFIED MEASUREMENT** - directly present in one of the current archived measurement files.
- **DERIVED** - calculated from stated measured or published inputs and retained equations.
- **PUBLISHED** - manufacturer specification or manufacturer technical guidance.
- **INFERRED** - a physically plausible interpretation requiring assumptions that have not been measured.
- **PROVISIONAL DECISION** - a present engineering direction subject to stated test gates.
- **OPEN ITEM** - measurement, decision, or archival work still outstanding.

### 1.2 Current measurement baseline

The only current driver-impedance baselines approved for crossover modelling are:

- Woofer: [`rew/SB17NRX2C35-8 installed.zma`](rew/SB17NRX2C35-8%20installed.zma)
- Tweeter: [`rew/SB26STWGC-4 installed.zma`](rew/SB26STWGC-4%20installed.zma)

Both drivers were correctly mounted in the sealed prototype enclosure in their normal mechanical configuration. No temporary sealing putty was used. The woofer file was taken immediately after installation and before any deliberate run-in. A later matched-sample-rate comparison is retained as conditioning evidence in Section 4.7, but its broadband series-resistance offset prevents it from replacing the cooled crossover baseline yet.

### 1.3 Project state at this update

- Only **one woofer and one tweeter** are presently on hand.
- The prototype enclosure has already been built. Its nominal geometric net volume is approximately **21.7 L** before any effective-volume change due to damping material.
- The pre-conditioning woofer baseline has one clean sealed-box impedance resonance at approximately **67.0 Hz** and no separate resonance near 83 Hz.
- After programme-material use and one hour at 30 Hz/4 V RMS, the matched 48 kHz trace places that resonance at approximately **65.71 Hz**. This **1.88%** downward movement is encouraging but still awaits a fully cooled confirmation.
- The woofer's installed total system Q remains approximately **0.81-0.82**, a mildly underdamped but quite manageable sealed alignment; the apparent raw peak-magnitude change is explained by a nearly frequency-independent resistance offset in the post-run trace.
- The tweeter's installed impedance remains close to its published electrical parameters and contains no suspicious additional resonance.
- The intended crossover remains a measurement-developed acoustic fourth-order Linkwitz-Riley alignment in the approximate **2.2-2.4 kHz** region. That frequency and all component values remain provisional until installed-baffle acoustic magnitude, phase, directivity, and distortion data exist.
- Both drivers remain provisionally retained.
- The protected amplifier-reference path has passed the SU-V570 common-ground,
  UMC202HD Input 2 phantom-isolation, complete-fixture resistance/DC/physical,
  ground-path, and interface-output-topology gates. The inspected UMC202HD rear
  outputs are mechanically TRS but electrically tip plus a ring/sleeve common.
  The fixture's short unscreened output tail still requires the specified
  no-signal comparison. Its sole remaining electrical gate is AC commissioning,
  beginning with the Output 2 source-adaptor and inline-breakout resistance
  maps; full-dual amplifier use remains unapproved. Use
  [the active AC procedure](rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md) for the
  exact resume point and
  [the qualification record](rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md)
  for all completed readings and calculations.

### 1.4 Project file-location convention

- `rew/` - REW measurements and exports, including `.mdat`, `.zma`, tab-delimited impedance exports, FRD exports, and measurement notes.
- `vituixcad/` - VituixCAD projects and VituixCAD-generated outputs.

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

### 4.6 2026-08-31 conditioning calculation and provisional procedure

**USER-REPORTED TEST CONDITION:** the installed woofer is currently being driven with a **45 Hz sine wave at 3.44 V RMS measured at its terminals**.

**DERIVED FROM THE CURRENT INSTALLED ZMA:** near 45 Hz the measured load is approximately **10.42 ohm at +50.6 degrees**. The present condition is therefore approximately **0.330 A RMS**, **1.14 VA apparent power**, and **0.72 W real electrical input**. The nominal-resistor shorthand $V^2/8=1.48\ \mathrm{W}$ does not describe this reactive, frequency-dependent load.

Using the measured complex impedance together with the published $R_e=5.7\ \mathrm{ohm}$, $L_e=0.15\ \mathrm{mH}$, and $Bl=6.25\ \mathrm{T\,m}$ gives an **estimated** diaphragm travel of approximately **2.13 mm peak (4.27 mm peak-to-peak)** at the present setting. This is a linear equivalent-circuit estimate, not a displacement measurement; it becomes less certain as suspension and motor nonlinearities increase.

**PROVISIONAL CONDITIONING PROCEDURE:** use approximately **30 Hz at 4.0 V RMS** at the woofer terminals, with the tweeter disconnected. The current ZMA predicts approximately **0.565 A RMS**, **1.9 W real input**, and **2.6 mm peak diaphragm travel**, about 47% of the published +/-5.5 mm linear excursion. If motion is clean and symmetric, a cautious upper development setting is **4.5 V RMS**, predicting approximately **2.9 mm peak** and **2.4 W real input**. There is no project justification for deliberately approaching $X_{max}$ during conditioning.

Below the measured approximately 67 Hz sealed-system resonance, terminal voltage required for a given displacement is nearly flat from approximately 20-50 Hz. At equal displacement, 30 Hz has approximately 7 dB less idealized far-field pressure than 45 Hz, while producing two-thirds as many displacement cycles per hour. The exact conditioning frequency is therefore a nuisance-versus-time choice rather than a unique driver optimum; approximately 25-35 Hz is the preferred quiet range, avoiding any frequency that excites an observed room or structure rattle.

Run in bounded intervals, inspect for rubbing, knocking, asymmetry, amplifier clipping, or abnormal heating, and stop immediately if any appears. After full return to the same ambient/voice-coil temperature, repeat the installed impedance measurement under matched mounting, fill, and drive conditions. Continue only while the cooled $F_c$, $Q_{tc}$, or trace shape is still changing materially; a practical stopping rule is less than approximately **1% change in $F_c$** across two successive cooled checks. Archive each conditioning duration, voltage, frequency, orientation, ambient temperature, and resulting ZMA.

The operational steps in this provisional note are superseded by the controlled procedure in [DRIVER_RUNIN.md](DRIVER_RUNIN.md), which adds a cold-DCR cooldown gate, fixed 48 kHz calibration, a 12-24 hour rested confirmation before baseline promotion, and a bounded review point.

### 4.7 2026-08-31 matched 48 kHz post-conditioning comparison

**USER-CLARIFIED MEASUREMENT HISTORY:** [`rew/SB17NRX2C35-8 installed.zma`](rew/SB17NRX2C35-8%20installed.zma) was measured immediately after installation, before any deliberate run-in. [`rew/SB17NRX2C35-8 runin 30Hz 4Vrms 1h 48kHz.zma`](rew/SB17NRX2C35-8%20runin%2030Hz%204Vrms%201h%2048kHz.zma) followed some intervening programme-material use and then one hour of 30 Hz conditioning at 4 V RMS. The comparison therefore shows the net change across both activities; it cannot assign the change uniquely to the final sine-wave hour.

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

## 7. Crossover-development consequences

### 7.1 Current VituixCAD impedance sources

The VituixCAD project should use only:

- `rew/SB17NRX2C35-8 installed.zma` for the woofer;
- `rew/SB26STWGC-4 installed.zma` for the tweeter.

The post-conditioning woofer file remains comparison evidence only until a fully cooled repeat confirms both its resonance position and its broadband resistance baseline.

The useful crossover-region loads are therefore approximately:

- Woofer: $7.98$ ohm at $+10.8$ degrees near 2.30 kHz;
- Tweeter: $3.48$ ohm at $-5.0$ degrees near 2.30 kHz.

This makes the impedance side of the model substantially more defensible. It does **not** make crossover optimization defensible in the absence of installed-baffle FRD data with common timing.

### 7.2 Why textbook LR4 parts remain only seeds

A textbook electrical LR4 table assumes a frequency-independent resistor and asks the electrical network alone to create the entire fourth-order shape. The actual design target is an acoustic LR4-like sum, while:

- both impedance magnitude and phase vary with frequency;
- the drivers already have acoustic roll-offs and resonances;
- baffle diffraction and driver spacing affect magnitude and phase;
- the crossover components add DCR and tolerance;
- the final amplifier load is the complete network, not either bare driver.

The installed ZMAs should now replace nominal resistance in every exploratory circuit model. Component optimization should remain provisional until the FRD measurements exist.

### 7.3 Required tuning loop

1. Measure both drivers' installed acoustic magnitude and phase with a shared electrical timing reference and fixed microphone/rotation geometry.
2. Import the installed ZMA and phase-bearing FRD data into VituixCAD.
3. Optimize a realizable network for acoustic slopes, summed response, directivity, impedance, sensitivity, and component limits.
4. Build the external development crossover with measured capacitor values and measured inductor inductance/DCR.
5. Measure individual filtered responses, the normal-polarity sum, the reverse-polarity null, off-axis response, distortion, and final system impedance/EPDR.
6. Update the model with as-built component values and iterate one controlled change at a time.

## 8. Procurement and pair-matching decision

**PROVISIONAL DECISION:** continue with the present driver pair and enclosure. Delay purchase of the second-channel drivers until the prototype has passed the acoustic-response, distortion, crossover-feasibility, and final-load gates.

If the prototype passes:

- buy another SB17NRX2C35-8 and SB26STWGC-4;
- condition and measure them under the same documented conditions;
- compare installed resonance/Q, crossover-region impedance, acoustic response, and distortion;
- establish acceptable pair tolerances before freezing the stereo build.

Matching complete installed behaviour matters more than reproducing every datasheet value exactly.

## 9. Open items and priorities

### 9.1 Highest-priority work

1. Complete the remaining
   [reference-fixture AC commissioning](rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md),
   beginning with the source-adaptor and inline-breakout maps, before connecting
   the fixture to a powered amplifier.
2. Complete the bounded woofer conditioning/cooldown loop in [DRIVER_RUNIN.md](DRIVER_RUNIN.md), then promote a reproducible cooled 48 kHz ZMA to the modelling baseline.
3. Record the present enclosure fill/lining state, ambient temperature, terminal voltage, and mounting condition so this baseline can be reproduced.
4. Acquire installed-baffle acoustic magnitude and phase for both drivers using common loopback timing.
5. Acquire horizontal off-axis responses using fixed microphone and rotation geometry.
6. Measure distortion at progressively realistic levels while respecting tweeter protection and woofer excursion.
7. Build and validate the crossover from the installed ZMA/FRD data.
8. Repeat woofer impedance after adding the actual crossover series resistance and after any damping-material change; compare $F_c$, $Q_{tc}$, and peak shape.
9. Measure final system impedance, phase, and EPDR.

### 9.2 Remaining uncertainties

- Installed acoustic magnitude, phase, and directivity of both drivers.
- Woofer and tweeter distortion/compression at the required listening levels.
- The effect of the documented final damping configuration on the sealed alignment.
- The effect of the as-built woofer-series inductor DCR on $Q_{tc}$.
- Final crossover topology, component values, acoustic polarity, and reverse-null quality.
- Reference-fixture AC transfer/noise commissioning remains unverified; every
  earlier electrical and physical gate passes. The amplifier-terminal reference
  plane excludes the separate loudspeaker-cable drop, so keep that cable fixed
  and record any later move to driver-terminal normalization. Exact completed
  readings and remaining actions are delegated to the two fixture records
  linked in Section 10.3.
- Production spread and stereo-pair matching.
- Individual free-air T/S parameters, if later required to explain the installed alignment rather than simply design from it.

## 10. Sources

### 10.1 Current project measurements

- [`rew/SB17NRX2C35-8 installed.zma`](rew/SB17NRX2C35-8%20installed.zma)
- [`rew/SB17NRX2C35-8 runin 30Hz 4Vrms 1h 48kHz.zma`](rew/SB17NRX2C35-8%20runin%2030Hz%204Vrms%201h%2048kHz.zma) - comparison evidence; not yet the crossover baseline
- [`rew/SB26STWGC-4 installed.zma`](rew/SB26STWGC-4%20installed.zma)

### 10.2 Primary/manufacturer sources

- [SB17NRX2C35-8 datasheet](https://sbacoustics.com/wp-content/uploads/2020/02/6in-SB17NRX2C35-8.pdf)
- [SB26STWGC-4 product page](https://sbacoustics.com/product/sb26stwgc-4-fabric/)
- [SB26STWGC-4 datasheet](https://sbacoustics.com/wp-content/uploads/2020/05/SB26STWGC-4.pdf)
- [Keysight U1280 Series data sheet](https://www.keysight.com/content/dam/keysight/en/doc/ungate/data-sheets/5992-0847.pdf)
- [Behringer UMC202HD quick-start guide](https://mediadl.musictribe.com/media/sys_master/h1f/h9b/8849476255774.pdf)
- [Technics SU-V570 service manual](https://audiocircuit.dk/downloads/technics/Technics-SUV570-int-sm.pdf)
- [Vishay BZX55 small-signal zener data sheet](https://www.vishay.com/docs/85604/bzx55.pdf)
- [Thurlby Thandar PL-series data, including PL310QMD series operation](https://www.farnell.com/datasheets/99860.pdf)
- [Klippel, *Mechanical Fatigue and Load-Induced Aging of Loudspeaker Suspension*](https://www.klippel.de/fileadmin/klippel/Bilder/Know-How/Literature/Papers/Aging%20of%20loudspeaker%20suspension_Klippel.pdf)
- [REW impedance-measurement documentation](https://www.roomeqwizard.com/help/help_en-GB/html/impedancemeasurement.html)

### 10.3 Acoustic-measurement procedures and evidence

- [`DRIVER_RUNIN.md`](DRIVER_RUNIN.md)
- [`rew/FRD_MEASUREMENT_SETUP_TEST.md`](rew/FRD_MEASUREMENT_SETUP_TEST.md)
- [`rew/SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md`](rew/SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md)
- [`rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md`](rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md)
- [`rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md`](rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md)
- [`rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md`](rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md)
- [`rew/SU-V570_power_amp_output_schematic.png`](rew/SU-V570_power_amp_output_schematic.png)

## 11. Change log

### 11.1 2026-08-30 - installed-driver baseline

- Established the two correctly installed ZMA exports as the sole current impedance baseline.
- Recorded the woofer's single approximately 67 Hz sealed-box resonance and derived $Q_{tc}\approx0.82$.
- Recorded the absence of a separate approximately 83 Hz resonance under normal mounting.
- Recorded the tweeter's approximately 761 Hz resonance and close agreement with published Q values.
- Replaced nominal crossover-region loads with the current installed magnitude and phase values.
- Removed obsolete source references and all numerical conclusions dependent on them.

### 11.2 2026-08-30 - UMC202HD acoustic-measurement plan

- Replaced the provisional UMC22 timing-only setup with a UMC202HD full-dual-channel plan.
- The initial plan was an approximately 20 dB protected sample at the driver
  terminals. The built fixture later established the SU-V570 rear speaker
  terminals as its documented reference plane.
- The planned REW mode is `Use loopback as cal and timing reference` with `Merge loopback response into IR`, at 88.2 kHz with common timing and geometry for both drivers.
- At that stage, the protected divider and Technics output topology still
  required commissioning before any amplifier-output connection; a direct
  interface-output loopback remained the safe fallback.

### 11.3 2026-08-31 - woofer conditioning procedure

- Recorded the user-reported 45 Hz, 3.44 V RMS terminal-drive condition.
- Replaced the nominal 8-ohm power estimate with current-ZMA estimates of current, real power, and apparent power.
- Added an equivalent-circuit displacement estimate and a conservative 30 Hz, 4.0 V RMS provisional conditioning point.
- Defined cooled repeat impedance measurements, rather than elapsed time alone, as the conditioning stopping criterion.

### 11.4 2026-08-31 - SU-V570 output-topology verification record

- Preserved the supplied SU-V570 power-amplifier/output schematic in `rew/` with its SHA-256 hash.
- Recorded the schematic evidence for a conventional common-signal-ground output: common negative-terminal ground symbols, one driven output per channel through `L503`/`L504`, relay-switched positive outputs, and a split-supply `0 V` return.
- Identified `C712` (`0.01 uF`) as a likely RF bond between signal and chassis ground, not the speaker-current return; its calculated reactance is approximately `15.9 kohm` at 1 kHz.
- Defined unpowered continuity checks between all negative posts and an RCA
  outer shell as the required decision gate; at that update the topology still
  awaited those readings.
- Retained the protected two-leg high-value UMC202HD divider even if common ground is confirmed, avoiding a second hard ground path through the reference connection.

### 11.5 2026-08-31 - matched 48 kHz conditioning comparison and formal run-in procedure

- Clarified that the original installed woofer trace predates all deliberate conditioning.
- Recorded the matched 48 kHz resonance movement from 66.9712 Hz to 65.7115 Hz.
- Identified the post-run trace's approximately 0.342 ohm broadband real-resistance offset and retained the cooled original as the crossover baseline.
- Recorded the conditional effective free-air estimate of approximately 52.66 Hz.
- Linked the formal bounded conditioning, cooldown, measurement, and stopping procedure in `DRIVER_RUNIN.md`.
- Recorded that no dedicated tweeter run-in is presently justified.

### 11.6 2026-09-01 to 2026-09-03 - reference-path qualification

- Passed the SU-V570 common-ground gate from nulled low-resistance readings:
  negative terminals `0.002-0.045 ohm`, speaker negative to RCA shell
  `0.120-0.150 ohm` (mean `0.130 ohm`), and speaker negative to chassis
  `0.100 ohm`. The optional powered confirmation was waived.
- Passed Input 2 central-TRS phantom isolation under equal `100 kohm` loads;
  every pair displayed `0.000 V` through individual `+48 V` switching.
- Rejected the original one-leg attenuator, then qualified the rebuilt symmetric
  two-leg fixture. Its pre- and post-stress matrices, four-polarity `64.5 V`
  PL310QMD curves, accepted `45.5 V` soft-knee deviation, component evidence,
  heat-shrink construction, and short unscreened tail are preserved in the
  dedicated qualification record.
- Completed the unpowered ground audit through the UMC202HD, USB cable, Class-I
  PC, mapped TS-to-RCA playback cable, SU-V570 RCA shell, and speaker-negative
  node. The path is a signal reference to protective earth, not a protective-
  conductor test; the fixture retains `10.130/10.146 kohm` from its two inputs
  to sleeve.
- Verified both UMC202HD rear outputs as mechanically TRS but electrically TS.
  Powered driven-channel results, an unpowered `0.021 ohm` ring/sleeve reading,
  and direct inspection of both R/S pads on one copper fill agree. The mapped
  TS playback cable is compatible; Output 2 supplies the fixture test from tip
  and common.
- Passed the direct-baseline TRS cable (`0.345/0.337/0.320 ohm` T/R/S;
  cross-paths open) and accepted a short, restrained, unenclosed inline
  terminal-block breakout subject to mapping and matched no-signal testing.
- Consolidated the former event-by-event entries into
  [`rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md`](rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md),
  avoiding duplicate authority while preserving the evidence. The exact next
  action is to map the Output 2 source adaptor and inline breakout under
  [`rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md`](rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md).
  Full-dual amplifier use remains unapproved until that AC gate passes.
