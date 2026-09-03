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
- The 2026-09-01 unpowered SU-V570 resistance checks pass and externally
  support a conventional common-signal-ground output. The UMC202HD Input 2
  central-TRS phantom-isolation gate also passes: under the defined equal
  `100 kohm` loads, all three contact pairs remained at a displayed `0.000 V`
  while `+48 V` was switched on and off separately for each measurement. The
  complete cable-to-TRS assembly is now governed by
  [`rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md`](rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md).
  Its amplifier-end cable is user-reported as `2 m` of red/black `1.5 mm^2`
  cable. The post-rebuild, pre-stress complete-unit resistance matrix passes, with all six
  redundant path sums agreeing within `0-2 ohm` and an unloaded differential
  gain prediction of `-20.094 dB`. The installed zeners are marked `BZX 5V1`,
  each measures close to `5 V` at `2 mA` on the user's analyser, and both pairs
  are connected anode-to-anode. The incomplete part identity is accepted for
  bounded qualification. All four powered DC curves pass clamp action, polarity
  symmetry, current, CV, and thermal checks. Maximum node magnitudes span only
  `5.463-5.520 V`, with each `0.860-0.918 V` below its unclamped prediction; the
  ring pair both measure `5.515 V`. Near `45.5 V`, departures are `0.99-1.24%`,
  so three curves miss the stated approximate `1%` target slightly. This is
  retained as an accepted, characterized soft-knee deviation: every curve stays
  within `0.45%` through `40 V`, then bends smoothly and symmetrically. Both
  current limits were `10 mA`; the supply remained in CV mode, indicated `6 mA`
  maximum, and caused only expected mild fixture warming. The cooled post-stress
  matrix passes with every direct path within `0-4 ohm` of baseline and all
  redundant sums closing within `0-2 ohm`, completing the integrated DC gate.
  Powered driven-channel tests now verify both UMC202HD rear outputs as ring-
  grounded: Output 1 measured `78.69/0.002/78.73 mV` and Output 2 measured
  `78.9/0.000/78.84 mV` tip-sleeve/ring-sleeve/tip-ring. The mapped mono TS-
  to-RCA playback cable therefore adds no new short of an active cold leg, and
  its compatibility hold is lifted. The post-stress matrix's `10.130 kohm` and
  `10.146 kohm` input-to-sleeve paths also satisfy the fixture-alone ground
  check. Remaining physical details, the connected playback-path portion of the
  unpowered ground audit, and AC transfer commissioning remain open. Full-dual
  use is therefore not approved.

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

The fitted Q values below use a curve-consistent baseline resistance, \(R_0\), estimated from the real part of impedance at 10 Hz:

\[
R_0=|Z|\cos\phi.
\]

For a single dominant impedance resonance, define the bandwidth level and crossing frequencies by

\[
Z_{th}=\sqrt{R_0Z_{max}},
\]

with \(f_1\) and \(f_2\) at the rising and falling crossings of that magnitude. Log-frequency interpolation between adjacent measured points is used. Then

\[
f_0=\sqrt{f_1f_2},
\]

\[
Q_m=\frac{f_0}{f_2-f_1}\sqrt{\frac{Z_{max}}{R_0}},
\qquad
Q_e=\frac{Q_m}{Z_{max}/R_0-1},
\qquad
Q_t=\frac{Q_m}{Z_{max}/R_0}.
\]

For the installed woofer these are box-system quantities \(Q_{mc}\), \(Q_{ec}\), and \(Q_{tc}\). For the tweeter, whose own rear chamber defines its mechanical system, they are reported conventionally as \(Q_{ms}\), \(Q_{es}\), and \(Q_{ts}\). They are approximate equivalent-circuit fits, not independent direct measurements of every loss mechanism.

## 3. Woofer published reference data

### 3.1 Manufacturer specifications

**PUBLISHED - SB Acoustics SB17NRX2C35-8 datasheet**

| Parameter | Published value |
|---|---:|
| Nominal impedance | 8 ohm |
| DC resistance, \(R_e\) | 5.7 ohm |
| Voice-coil inductance, \(L_e\) | 0.15 mH |
| Effective diaphragm area, \(S_d\) | 118 cm2 |
| Free-air resonance, \(F_s\) | 36.5 Hz |
| Sensitivity | 87 dB at 2.83 V/1 m |
| \(Q_{ms}\) | 4.55 |
| \(Q_{es}\) | 0.47 |
| \(Q_{ts}\) | 0.42 |
| Moving mass, \(M_{ms}\) | 13.9 g |
| Force factor, \(Bl\) | 6.25 T m |
| Equivalent compliance volume, \(V_{as}\) | 27 L |
| Suspension compliance, \(C_{ms}\) | 1.37 mm/N |
| Mechanical resistance, \(R_{ms}\) | 0.7 kg/s |
| Linear excursion, \(X_{max}\) | +/-5.5 mm |
| Rated power | 50 W |

### 3.2 Published-parameter enclosure prediction

Using the published \(F_s=36.5\) Hz, \(Q_{ts}=0.42\), \(V_{as}=27\) L, and the approximately 21.7 L geometric net volume gives:

- **DERIVED:** \(F_c\approx54.7\) Hz;
- **DERIVED:** \(Q_{tc}\approx0.63\);
- **DERIVED:** ideal anechoic small-signal \(F_3\approx62.3\) Hz;
- no response peak from the nominal second-order sealed alignment.

These remain a record of the datasheet-based design case, not a description of the completed prototype.

## 4. Woofer installed measurement

### 4.1 Principal measured features

**VERIFIED MEASUREMENT / DERIVED FROM CURRENT ZMA**

| Quantity | Result |
|---|---:|
| Curve-consistent \(R_0\) estimate | 5.645 ohm |
| Impedance magnitude maximum | 96.544 ohm at 67.272 Hz |
| Bandwidth threshold, \(Z_{th}\) | 23.345 ohm |
| Lower threshold crossing, \(f_1\) | 57.811 Hz |
| Upper threshold crossing, \(f_2\) | 77.583 Hz |
| Derived sealed-system resonance, \(F_c\) | 66.971 Hz |
| \(Q_{mc}\) | 14.008 |
| \(Q_{ec}\) | 0.870 |
| \(Q_{tc}\) | 0.819 |
| Positive phase maximum | +61.79 degrees at 57.81 Hz |
| Negative phase minimum | -63.54 degrees at 77.16 Hz |

The impedance maximum is a magnitude in **ohms**, not an inductance. Its height mainly reflects motional back-EMF and the balance of mechanical and electrical damping. High impedance at resonance is not an amplifier-current hazard.

The close agreement between the curve-derived \(R_0\approx5.645\) ohm and the published \(R_e=5.7\) ohm is reassuring. A nulled cold-DCR measurement taken with this setup would still be preferable when an exact series-resistance model is required.

### 4.2 The secondary-resonance question

**VERIFIED MEASUREMENT:** the correctly installed woofer trace has one low-frequency resonance only. At **82.94 Hz**, the impedance is **16.46 ohm at -61.06 degrees**, lying smoothly on the falling side of the 67 Hz peak. There is no local maximum or phase reversal there.

This is strong evidence that a distinct feature near 83 Hz is not inherent to the normally installed driver/enclosure system. The ordinary mounting has eliminated the leak-related mode without needing temporary sealing compound.

### 4.3 Idealized low-frequency consequence

For a normalized second-order sealed high-pass response,

\[
|H(x)|^2=\frac{x^4}{(1-x^2)^2+x^2/Q_{tc}^2},
\qquad x=\frac{f}{F_c}.
\]

Using the measured \(F_c=66.97\) Hz and derived \(Q_{tc}=0.819\):

- **DERIVED:** ideal anechoic small-signal \(F_3\approx59.0\) Hz;
- **DERIVED:** a modest maximum of approximately **+0.29 dB near 133 Hz**;
- \(F_3\) lies below \(F_c\), as expected because \(Q_{tc}>0.707\).

The apparently similar or slightly lower \(F_3\) than the published-parameter design case does not mean equal deep-bass behaviour. With both responses normalized at high frequency, the idealized installed alignment differs approximately as follows:

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

The woofer is close to 8 ohm in magnitude around the intended crossover, but it is not an 8 ohm resistor. At 2297 Hz its rectangular equivalent is approximately \(7.84+j1.49\) ohm. The full ZMA should therefore be used in VituixCAD.

There is no strong electrical anomaly in the 2.2-2.5 kHz region. Small higher-frequency impedance structure cannot establish cone-breakup amplitude or acoustic suitability; the installed FRD and distortion measurements remain decisive.

### 4.5 Woofer judgement

**PROVISIONAL DECISION:** retain the SB17NRX2C35-8 in the present enclosure.

The measured \(Q_{tc}\approx0.82\) sits inside the project's broadly manageable **0.75-0.95** development range. The alignment is warmer than the published-parameter design case but is not severely resonant. No additional low-frequency mode survives normal installation, and the impedance near the intended crossover is smooth and convenient to model.

This does not yet establish acoustic smoothness, maximum output, distortion, compression, or suitability for pair matching.

### 4.6 2026-08-31 conditioning calculation and provisional procedure

**USER-REPORTED TEST CONDITION:** the installed woofer is currently being driven with a **45 Hz sine wave at 3.44 V RMS measured at its terminals**.

**DERIVED FROM THE CURRENT INSTALLED ZMA:** near 45 Hz the measured load is approximately **10.42 ohm at +50.6 degrees**. The present condition is therefore approximately **0.330 A RMS**, **1.14 VA apparent power**, and **0.72 W real electrical input**. The nominal-resistor shorthand \(V^2/8=1.48\ \mathrm{W}\) does not describe this reactive, frequency-dependent load.

Using the measured complex impedance together with the published \(R_e=5.7\ \mathrm{ohm}\), \(L_e=0.15\ \mathrm{mH}\), and \(Bl=6.25\ \mathrm{T\,m}\) gives an **estimated** diaphragm travel of approximately **2.13 mm peak (4.27 mm peak-to-peak)** at the present setting. This is a linear equivalent-circuit estimate, not a displacement measurement; it becomes less certain as suspension and motor nonlinearities increase.

**PROVISIONAL CONDITIONING PROCEDURE:** use approximately **30 Hz at 4.0 V RMS** at the woofer terminals, with the tweeter disconnected. The current ZMA predicts approximately **0.565 A RMS**, **1.9 W real input**, and **2.6 mm peak diaphragm travel**, about 47% of the published +/-5.5 mm linear excursion. If motion is clean and symmetric, a cautious upper development setting is **4.5 V RMS**, predicting approximately **2.9 mm peak** and **2.4 W real input**. There is no project justification for deliberately approaching \(X_{max}\) during conditioning.

Below the measured approximately 67 Hz sealed-system resonance, terminal voltage required for a given displacement is nearly flat from approximately 20-50 Hz. At equal displacement, 30 Hz has approximately 7 dB less idealized far-field pressure than 45 Hz, while producing two-thirds as many displacement cycles per hour. The exact conditioning frequency is therefore a nuisance-versus-time choice rather than a unique driver optimum; approximately 25-35 Hz is the preferred quiet range, avoiding any frequency that excites an observed room or structure rattle.

Run in bounded intervals, inspect for rubbing, knocking, asymmetry, amplifier clipping, or abnormal heating, and stop immediately if any appears. After full return to the same ambient/voice-coil temperature, repeat the installed impedance measurement under matched mounting, fill, and drive conditions. Continue only while the cooled \(F_c\), \(Q_{tc}\), or trace shape is still changing materially; a practical stopping rule is less than approximately **1% change in \(F_c\)** across two successive cooled checks. Archive each conditioning duration, voltage, frequency, orientation, ambient temperature, and resulting ZMA.

The operational steps in this provisional note are superseded by the controlled procedure in [DRIVER_RUNIN.md](DRIVER_RUNIN.md), which adds a cold-DCR cooldown gate, fixed 48 kHz calibration, a 12-24 hour rested confirmation before baseline promotion, and a bounded review point.

### 4.7 2026-08-31 matched 48 kHz post-conditioning comparison

**USER-CLARIFIED MEASUREMENT HISTORY:** [`rew/SB17NRX2C35-8 installed.zma`](rew/SB17NRX2C35-8%20installed.zma) was measured immediately after installation, before any deliberate run-in. [`rew/SB17NRX2C35-8 runin 30Hz 4Vrms 1h 48kHz.zma`](rew/SB17NRX2C35-8%20runin%2030Hz%204Vrms%201h%2048kHz.zma) followed some intervening programme-material use and then one hour of 30 Hz conditioning at 4 V RMS. The comparison therefore shows the net change across both activities; it cannot assign the change uniquely to the final sine-wave hour.

**VERIFIED MEASUREMENT / DERIVED:** both traces use a 48 kHz sample rate and otherwise matched REW impedance settings. The bandwidth-derived sealed-system resonance changed from **66.9712 Hz** to **65.7115 Hz**, a change of **-1.2597 Hz (-1.881%)**. Interpreted as a stiffness/compliance change at effectively constant moving mass, this corresponds to approximately **+3.87% total system compliance**.

The raw impedance maximum changed only from approximately **96.54 ohm** to **96.85 ohm**, while the post-run trace contains approximately **+0.342 ohm** of nearly frequency-independent real series resistance from 300 Hz to 10 kHz and essentially unchanged reactance there. If that offset were entirely voice-coil copper resistance, it would correspond to roughly a **15 °C** temperature rise; changed lead or contact resistance could contribute instead. Subtracting the series offset gives a post-run peak of approximately **96.50 ohm**, \(Q_{mc}\approx13.8\), \(Q_{ec}\approx0.86\), and \(Q_{tc}\approx0.81\). There is therefore no persuasive evidence of a durable resonance-peak or damping change in this pair of files.

**INFERRED:** combining the pre-run free-air estimate \(F_s\approx54.22\ \mathrm{Hz}\), the fixed-box stiffness contribution derived from the earlier installed measurement, and the new \(F_c\) gives an effective post-conditioning free-air resonance of approximately **52.66 Hz**. That is approximately **2.9% below** the pre-run estimate and implies approximately **6.0% greater driver compliance**, but it remains roughly **44% above** the published 36.5 Hz value. This is an indirect estimate, not a current free-air measurement.

**PROVISIONAL DECISION:** treat the downward resonance-frequency movement as encouraging, but retain the original cooled installed ZMA as the crossover baseline. Repeat the post-run measurement only after the cold-DCR and matched-condition gates in [DRIVER_RUNIN.md](DRIVER_RUNIN.md) have been met.

## 5. Tweeter published reference data

### 5.1 Manufacturer specifications

**PUBLISHED - SB Acoustics SB26STWGC-4 datasheet**

| Parameter | Published value |
|---|---:|
| Nominal impedance | 4 ohm |
| DC resistance, \(R_e\) | 3.2 ohm |
| Voice-coil inductance, \(L_e\) | 0.04 mH |
| Effective diaphragm area, \(S_d\) | 6.2 cm2 |
| Resonance, \(F_s\) | 780 Hz |
| Sensitivity | 93 dB at 2.83 V/1 m |
| \(Q_{ms}\) | 2.8 |
| \(Q_{es}\) | 2.1 |
| \(Q_{ts}\) | 1.2 |
| Force factor, \(Bl\) | 1.6 T m |
| Moving mass, \(M_{ms}\) | 0.3 g |
| Linear excursion, \(X_{max}\) | +/-0.6 mm |
| Rated power statement | 120 W with the manufacturer's stated 2.6 kHz, 12 dB/octave Butterworth high-pass condition |

The 120 W figure is conditional, not an unconditional broadband power rating.

## 6. Tweeter installed measurement

### 6.1 Principal measured features

**VERIFIED MEASUREMENT / DERIVED FROM CURRENT ZMA**

| Quantity | Installed result | Published |
|---|---:|---:|
| Curve-consistent \(R_0\) estimate | 3.274 ohm | \(R_e=3.2\) ohm |
| Impedance magnitude maximum | 7.557 ohm at 755.62 Hz | not stated |
| Bandwidth-derived \(F_s\) | 760.91 Hz | 780 Hz |
| \(Q_{ms}\) | 2.622 | 2.8 |
| \(Q_{es}\) | 2.005 | 2.1 |
| \(Q_{ts}\) | 1.136 | 1.2 |
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

Around the intended crossover the tweeter is approximately **3.48 ohm**, nearly resistive but mildly capacitive. At 2297 Hz its rectangular equivalent is approximately \(3.46-j0.30\) ohm. It must not be modelled as a frequency-independent 4 ohm resistor.

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

- Woofer: \(7.98\) ohm at \(+10.8\) degrees near 2.30 kHz;
- Tweeter: \(3.48\) ohm at \(-5.0\) degrees near 2.30 kHz.

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

1. Complete the bounded woofer conditioning/cooldown loop in [DRIVER_RUNIN.md](DRIVER_RUNIN.md), then promote a reproducible cooled 48 kHz ZMA to the modelling baseline.
2. Record the present enclosure fill/lining state, ambient temperature, terminal voltage, and mounting condition so this baseline can be reproduced.
3. Having passed the SU-V570 topology, UMC202HD Input 2 TRS phantom-isolation,
   and post-rebuild complete-fixture resistance checks, complete the fixture's
   physical record, the in-progress unpowered ground-path audit, and AC transfer
   gate before connecting it to a powered amplifier. The interface-alone stage,
   USB-cable map, and isolated-PC/PE stage have passed. The present mono TS-to-
   RCA playback cable grounds the UMC202HD output ring, but both powered,
   driven outputs are now verified ring-grounded. The TS plug therefore adds no
   new short of an active conductor and its compatibility hold is lifted.
   The existing disconnected post-stress matrix also closes the fixture-alone
   resistance check. Complete the connected playback-path check.
4. Acquire installed-baffle acoustic magnitude and phase for both drivers using common loopback timing.
5. Acquire horizontal off-axis responses using fixed microphone and rotation geometry.
6. Measure distortion at progressively realistic levels while respecting tweeter protection and woofer excursion.
7. Build and validate the crossover from the installed ZMA/FRD data.
8. Repeat woofer impedance after adding the actual crossover series resistance and after any damping-material change; compare \(F_c\), \(Q_{tc}\), and peak shape.
9. Measure final system impedance, phase, and EPDR.

### 9.2 Remaining uncertainties

- Installed acoustic magnitude, phase, and directivity of both drivers.
- Woofer and tweeter distortion/compression at the required listening levels.
- The effect of the documented final damping configuration on the sealed alignment.
- The effect of the as-built woofer-series inductor DCR on \(Q_{tc}\).
- Final crossover topology, component values, acoustic polarity, and reverse-null quality.
- The SU-V570 common speaker-return topology is externally supported by the
  unpowered resistance readings, and the UMC202HD Input 2 central-TRS phantom-
  isolation gate has passed under the defined symmetric load. The two-leg
  pre-stress fixture resistance matrix also passes. All four powered curves pass
  clamp, symmetry, current, CV, and thermal checks with a documented minor
  `45.5 V` soft-knee deviation from the approximate `1%` target. The post-stress
  matrix also passes, with only `0-4 ohm` path changes and `0-2 ohm` sum-closure
  errors. The ground audit has verified a `0.035 ohm` bond from Input 2 sleeve
  to USB shell. A `0.013 ohm` chassis-to-chassis positive control validates the
  two open enclosure readings, establishing DC isolation of the enclosure from
  the sleeve/USB-shell node under the interface-alone conditions. The intended
  USB cable has `0.130 ohm` shell-to-shell continuity. The isolated-PC stage
  records `0.170 ohm` from PC USB shell to chassis, `0.245 ohm` from chassis to
  the free mains plug's PE pin, `0.412 ohm` from Input 2 sleeve to PC chassis,
  and `0.379 ohm` directly from sleeve to PE. These values confirm the proposed
  earth-reference topology but are not a protective-conductor safety test.
  The proposed playback cable maps cleanly as TS-to-RCA. Although its sleeve
  contacts the UMC202HD output ring, powered driven-channel tests verify both
  outputs as ring-grounded. Output 1 measured `78.69/0.002/78.73 mV` and Output
  2 measured `78.9/0.000/78.84 mV` tip-sleeve/ring-sleeve/tip-ring. The TS plug
  therefore adds no new short of an active cold leg and the compatibility hold
  is lifted. Output 2 must supply the fixture-transfer test from tip and sleeve,
  not as two active balanced legs. The disconnected post-stress matrix already
  verifies the two fixture-alone input-to-sleeve paths. Remaining mechanical
  details, the connected playback-path check, and AC transfer remain unverified.
  The exact clamp manufacturer/family remains unknown but is accepted through
  the bounded installed-function qualification and is not a release blocker.
  The current amplifier-terminal
  reference plane excludes
  the separate loudspeaker-cable drop; keep that cable fixed and reassess the
  reference plane if driver-terminal normalization becomes necessary.
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
- [`rew/SU-V570_power_amp_output_schematic.png`](rew/SU-V570_power_amp_output_schematic.png)

## 11. Change log

### 11.1 2026-08-30 - installed-driver baseline

- Established the two correctly installed ZMA exports as the sole current impedance baseline.
- Recorded the woofer's single approximately 67 Hz sealed-box resonance and derived \(Q_{tc}\approx0.82\).
- Recorded the absence of a separate approximately 83 Hz resonance under normal mounting.
- Recorded the tweeter's approximately 761 Hz resonance and close agreement with published Q values.
- Replaced nominal crossover-region loads with the current installed magnitude and phase values.
- Removed obsolete source references and all numerical conclusions dependent on them.

### 11.2 2026-08-30 - UMC202HD acoustic-measurement plan

- Replaced the provisional UMC22 timing-only setup with a UMC202HD full-dual-channel plan.
- The preferred reference is an approximately 20 dB protected sample taken at the driver terminals and recorded through Input 2 in line mode.
- The planned REW mode is `Use loopback as cal and timing reference` with `Merge loopback response into IR`, at 88.2 kHz with common timing and geometry for both drivers.
- The driver-terminal divider and Technics output topology must be commissioned before any amplifier output is connected to the interface; a direct interface-output loopback remains the safe fallback.

### 11.3 2026-08-31 - woofer conditioning procedure

- Recorded the user-reported 45 Hz, 3.44 V RMS terminal-drive condition.
- Replaced the nominal 8-ohm power estimate with current-ZMA estimates of current, real power, and apparent power.
- Added an equivalent-circuit displacement estimate and a conservative 30 Hz, 4.0 V RMS provisional conditioning point.
- Defined cooled repeat impedance measurements, rather than elapsed time alone, as the conditioning stopping criterion.

### 11.4 2026-08-31 - SU-V570 output-topology verification record

- Preserved the supplied SU-V570 power-amplifier/output schematic in `rew/` with its SHA-256 hash.
- Recorded the schematic evidence for a conventional common-signal-ground output: common negative-terminal ground symbols, one driven output per channel through `L503`/`L504`, relay-switched positive outputs, and a split-supply `0 V` return.
- Identified `C712` (`0.01 uF`) as a likely RF bond between signal and chassis ground, not the speaker-current return; its calculated reactance is approximately `15.9 kohm` at 1 kHz.
- Defined unpowered continuity checks between all negative posts and an RCA outer shell as the required decision gate. The topology remains unverified until those readings are recorded.
- Retained the protected two-leg high-value UMC202HD divider even if common ground is confirmed, avoiding a second hard ground path through the reference connection.

### 11.5 2026-08-31 - matched 48 kHz conditioning comparison and formal run-in procedure

- Clarified that the original installed woofer trace predates all deliberate conditioning.
- Recorded the matched 48 kHz resonance movement from 66.9712 Hz to 65.7115 Hz.
- Identified the post-run trace's approximately 0.342 ohm broadband real-resistance offset and retained the cooled original as the crossover baseline.
- Recorded the conditional effective free-air estimate of approximately 52.66 Hz.
- Linked the formal bounded conditioning, cooldown, measurement, and stopping procedure in `DRIVER_RUNIN.md`.
- Recorded that no dedicated tweeter run-in is presently justified.

### 11.6 2026-09-01 - UMC202HD phantom-power and reference-input clarification

- Clarified that each UMC202HD front input is a combination connector with
  separate outer XLR and central 1/4-inch TRS contacts.
- Retained XLR for the ECM8000 on Input 1 and required the central TRS line jack
  for the protected electrical reference on Input 2, leaving Input 2's XLR
  contacts unused while global phantom power is enabled.
- Added an unpowered-driver phantom-isolation test with a provisional 0.1 V DC
  stop threshold before the divider may be connected to an amplifier output.
- Rejected an ad-hoc blocking capacitor because the specified TRS path should
  avoid phantom power without adding unmatched low-frequency magnitude or
  phase error.

### 11.7 2026-09-01 - SU-V570 unpowered topology gate passed

- Recorded a `0.050 ohm` lead resistance, nulled before the topology readings.
- Recorded `0.002 ohm` between the left A/B negative posts and `0.045 ohm`
  from left A negative to each right-channel negative post.
- Recorded `0.120-0.150 ohm`, mean `0.130 ohm`, from speaker negative to
  AUX/CD RCA signal ground and `0.100 ohm` to bare-metal chassis.
- Classified the readings as verified external support for a conventional
  common-signal-ground output and passed the Section 6 topology gate.
- Retained full-dual approval as `NO` pending the UMC202HD Input 2 TRS
  phantom-isolation test and protected-divider commissioning.

### 11.8 2026-09-01 - optional powered check waived and adaptor rejected

- Recorded the user's decision to bypass the optional low-voltage powered
  SU-V570 confirmation; the passed unpowered topology gate remains sufficient.
- Recorded the reported adaptor signature: approximately `1 kohm` tip to
  sleeve, ring open to every terminal, and approximately `10 kohm` between its
  far-end `+` and `-` leads.
- Identified the exact topology as a single `9.1 kohm` series / `1.0 kohm`
  shunt tip/sleeve divider with the speaker-negative lead hard-connected to
  sleeve, rather than the required balanced two-leg divider.
- Prohibited use of that adaptor for the phantom-isolation test or amplifier
  reference. Required a plain three-contact breakout for phantom testing and
  rework with a second `9.1 kohm` ring leg, second `1.0 kohm` ring-to-sleeve
  shunt, no hard speaker-terminal-to-sleeve connection, and both voltage clamps.

### 11.9 2026-09-01 - initial UMC202HD phantom-isolation report, superseded

- Recorded approximately `2 V` from tip to sleeve and ring to sleeve, decaying
  towards zero, and approximately `0.1 V` tip to ring, also decaying.
- Recorded the same qualitative behaviour with `+48 V` off and on, with no
  reported sustained phantom-dependent change.
- Interpreted the nearly equal tip and ring readings as predominantly common-
  mode stored charge rather than evidence of a stiff phantom feed; retained the
  exact internal source as unresolved.
- Kept the phantom-isolation gate pending because initial values exceeded the
  provisional `0.1 V` settled threshold and no settling times or final voltages
  were recorded.
- Required a fixed-probe timed repeat for each contact pair before any loaded
  divider commissioning or full-dual connection.

This account was superseded by the corrected observation in Section 11.10
before the phantom-isolation gate was evaluated. It remains here only to
preserve the measurement history and must not be used as current evidence.

### 11.10 2026-09-01 - corrected unloaded transient and revised phantom gate

- Replaced the earlier simple-decay account with the corrected fixed-probe
  tip-to-sleeve observation made with `+48 V` off: a brief approximately
  `3.3 V` peak at USB power-up, rapid fall near zero, slow rise towards
  approximately `1.5 V`, and subsequent decay over several minutes.
- Classified the non-monotonic waveform as evidence of multiple time constants,
  changing bias, charge redistribution, meter interaction, or a combination;
  retained the exact internal cause as unresolved.
- Stopped using unloaded-node settling as the isolation gate. The formal test
  now uses equal `100 kohm` tip-to-sleeve and ring-to-sleeve loads so the input
  nodes have a defined DC condition while a real P48 feed remains unmistakable.
- Kept full-dual use unapproved pending that symmetric-load test and subsequent
  commissioning of the conforming two-leg protected divider.

### 11.11 2026-09-01 - symmetric-load phantom test, off-state stage passed

- Recorded the Keysight U1282A in normal DCV mode on its `+/-60 V` range and
  the specified equal `100 kohm` tip-to-sleeve and ring-to-sleeve test loads.
- With `+48 V` off, recorded tip-to-sleeve and ring-to-sleeve settling below
  `1 mV` within `25 s`, and tip-to-ring settling below `1 mV` within `1 s`.
- Derived an indicated less-than-`10 nA` value from the display limit, then
  retained the more conservative instrument-aware bound of approximately
  `60 nA` after allowing the U1282A `60 V` range's `1 mV` resolution and five-
  count near-zero accuracy term. The corresponding conservative voltage across
  a `1 kohm` divider shunt is less than approximately `60 uV`.
- Passed the off-state stage but retained the overall isolation gate and full-
  dual approval as pending until the `+48 V`-on and final off-again stages pass.

### 11.12 2026-09-01 - Input 2 TRS phantom-isolation gate passed

- Kept the UMC202HD continuously USB-powered and the U1282A in normal DCV mode
  on its `+/-60 V` range, avoiding repetition of the unrelated USB-startup
  transient.
- Monitored tip-to-sleeve, ring-to-sleeve, and tip-to-ring separately while
  switching `+48 V` on and then off for each pair, with several seconds off
  between measurements.
- Recorded no movement from the displayed `0.000 V` on any contact pair during
  its individual phantom-switch cycle.
- Accepted this pair-by-pair switching sequence as a direct test of phantom
  correlation and passed the Input 2 central-TRS isolation gate. Retained the
  inability of normal DCV display sampling to exclude very short transients.
- Kept full-dual approval as `NO` pending construction and commissioning of the
  conforming two-leg protected divider.

### 11.13 2026-09-02 - loopback earth-reference path reviewed

- Recorded the user's observation that the SU-V570 has a two-terminal mains
  connection and no protective-earth conductor, while its speaker negative,
  signal ground, and chassis have measured low-resistance continuity.
- Derived `9.1 kohm + 1.0 kohm = 10.1 kohm` from either speaker terminal to the
  UMC202HD TRS sleeve through the conforming divider. With a connected low-
  resistance loudspeaker linking the two output terminals for common-mode/DC
  analysis, the two nominal paths are approximately `10.1 kohm || 10.1 kohm =
  5.05 kohm`, ignoring interface input impedance and amplifier circuitry.
- Identified the UMC202HD Output 1-to-Technics RCA playback cable as the expected
  lower-resistance signal-ground bond. If its shield wiring and the interface
  grounds are conventional, it earth-references the amplifier through the PC
  before the high-resistance reference divider is added.
- Distinguished a normal external signal-ground reference from protective
  earthing. The divider neither bypasses the amplifier's mains isolation in
  normal operation nor supplies a valid protective-earth conductor.
- Clarified that continuity to earth is not itself current flow. Normal divider
  sample current closes principally through the playback-cable signal return;
  the PC earth branch carries current only when leakage, stray coupling, ground
  potential difference, or another external connection supplies a closed loop.
- Added an unpowered audit of divider-only resistance, interface sleeve/USB/PC
  continuity, and playback-cable ground continuity before powered commissioning.
  Retained the exact paths as open measurements rather than assumptions.

### 11.14 2026-09-02 - reworked two-leg divider provisionally accepted

- Recorded the disconnected attenuator readings made with an Agilent U1282A in
  autoscaling resistance mode: `1.0034 kohm` tip-to-shield, `1.0042 kohm`
  ring-to-shield, `2.0072 kohm` tip-to-ring, `9.111 kohm` input `+`-to-tip,
  `9.109 kohm` input `-`-to-ring, two cross-path readings of `11.056 kohm` and
  `11.066 kohm` both labelled input `+`-to-ring, and `20.122 kohm` input-to-
  input.
- Superseded the former one-leg construction state. The two shunts match within
  approximately `0.080%`, the two series legs within approximately `0.022%`,
  and the tip-to-ring reading agrees with the shunt sum within `0.4 ohm`.
- Derived a provisional standalone/floating differential ratio of `0.09925`,
  or `-20.065 dB`, from the four directly measured resistor paths,
  corresponding to approximately `99.25 mV RMS` for `1.000 V RMS` at the
  divider input before interface loading. In the expected common-ground system,
  the active tip leg predicts `0.099205`, `-20.069 dB`, or `99.21 mV RMS`.
  Retained AC measurement as the actual commissioning gate.
- Kept the continuity pre-check open because input `+`-to-sleeve and input
  `-`-to-sleeve were not reported, one cross-path label is duplicated, and the
  reported cross/end-to-end values are approximately `0.5%` below the sums
  implied by the directly measured branches.
- Required a hands-off, settled repeat on the fixed `60 kohm` range in both
  probe polarities and a record of the installed clamp components/orientation.
  Possible explanations include nonlinear clamp leakage, range/test-current
  changes, surface or finger leakage, and transcription; no cause has yet been
  promoted to a verified conclusion.
- Retained full-dual approval as `NO` pending closure of that continuity check,
  the unpowered system ground-path audit, and low-voltage attenuation,
  polarity, clamp, and frequency-response commissioning.

### 11.15 2026-09-02 - corrected divider resistance-continuity gate passed

- Recorded the corrected, hands-off Agilent U1282A autoscaling-resistance
  repeat: `1.004 kohm` from both tip and ring to sleeve, `2.007 kohm` tip-to-
  ring, `9.117 kohm` input `+`-to-tip, `9.137 kohm` input `-`-to-ring,
  `11.122 kohm` input `+`-to-ring, `11.144 kohm` input `-`-to-tip,
  `20.259 kohm` input-to-input, `10.118 kohm` input `+`-to-sleeve, and
  `10.140 kohm` input `-`-to-sleeve.
- Verified that all six redundant additive identities agree within `0-3 ohm`.
  This is consistent with the U1282A measurement uncertainty and closes the
  former missing-reading, duplicated-label, and unexplained-parallel-path
  concerns without requiring a fixed-range repeat.
- Inferred finger/body leakage as the likely cause of the superseded
  `50-105 ohm` deficits because they disappeared when the user explicitly kept
  fingers out of the circuit. Retained that cause as inferred rather than
  directly measured.
- Passed the reworked attenuator's two-leg resistance-continuity gate. Both
  input leads retain approximately `10.1 kohm` to sleeve and neither is hard-
  grounded.
- Derived unloaded attenuation predictions of `-20.070 dB` for the active tip
  leg in the expected common-ground system, `-20.087 dB` for the ring leg, and
  `-20.078 dB` for the standalone floating divider. The leg-to-leg difference
  is approximately `0.017 dB`; actual interface-loaded AC attenuation remains
  a commissioning measurement.
- Kept full-dual approval as `NO` pending explicit clamp construction/function
  confirmation, the unpowered system ground-path audit, and low-voltage
  attenuation, polarity, clamp, and frequency-response commissioning.

### 11.16 2026-09-02 - divider clamp voltage envelope selected

- Derived the impossible ideal SU-V570 sine-wave bound from the schematic's
  `+/-45.5 V` rails: `32.17 V RMS` at the speaker and, through the measured
  `0.099200` active-leg divider ratio, `3.19 V RMS` or `4.51 V peak` at the
  TRS node.
- Derived more realistic divided peaks of approximately `3.07 V` from the
  published `60 W` into `8 ohm` rating and `3.32 V` from `70 W` into `8 ohm`
  at `1%` THD. Converted the UMC202HD published `+20 dBu` line-input maximum to
  `7.75 V RMS` or `10.96 V peak`; retained it as a performance limit rather
  than an absolute-damage specification.
- Selected, provisionally pending construction and measurement, two `5.1 V`,
  `500 mW` small-signal zeners in series opposition from each TRS signal node
  to sleeve. Vishay `BZX55B5V1` is preferred and `BZX55C5V1` acceptable. This
  supersedes the earlier `3.3 V` proposal because its soft low-current knee was
  unnecessarily close to high-output divided peaks.
- Established that the `9.1 kohm` series resistor is the primary protection.
  With the measured `1.004 kohm` shunt intact, even a `45.5 V DC` rail fault
  produces only `4.50 mA`, `4.51 V` at the node, approximately `0.184 W` in
  the measured `9.117 kohm` series leg, and approximately `0.020 W` in the
  shunt. The higher-voltage zener pair is secondary protection for an open
  shunt or abnormal overvoltage while the series resistor remains intact.
- Added a disconnected bidirectional functional test using a nominal `9 V`
  battery and an external `330 ohm`, at least `0.5 W`, resistor applied directly
  to each TRS node. Installation, four-polarity results, the unpowered system
  ground-path audit, and AC commissioning remain open; full-dual approval
  remains `NO`.

### 11.17 2026-09-02 - complete reference fixture separated and test revised

- Created
  [`rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md`](rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md)
  as the authority for the entire assembly from the rear SU-V570 speaker
  terminals to the UMC202HD Input 2 TRS plug. Recorded the user-reported input
  cable as `2 m` of red/black `1.5 mm^2` two-conductor cable; exact termination,
  enclosure, output-cable, plug, resistor-part, and clamp markings remain open.
- Moved the fixture rationale, schematic, component calculations, phantom-
  isolation evidence, resistor-test history, ground audit, clamp test, and AC
  commissioning out of the acoustic repeatability procedure. Reduced that FRD
  procedure to the channel, geometry, level, capture, window, and repeatability
  steps which consume an already approved fixture.
- Superseded the Section 11.16 direct-node `9 V` battery test. The current test
  uses the PL310QMD in its documented `0-64 V` series mode with both current
  limits set to `10 mA`, drives each complete cable/resistor/shunt/clamp leg in
  both polarities, and leaves the assembled attenuator and clamp intact.
- Defined the current reference plane at the rear amplifier terminals. The
  fixture cable carries only divider current; a copper-resistivity estimate
  gives approximately `0.0229 ohm` per `2 m`, `1.5 mm^2` conductor, whose
  voltage drop is negligible. The separate loudspeaker cable is outside the
  electrical reference and must remain unchanged through a driver set.
- Retained `-20.078 dB` as the unloaded resistor-network prediction, not an
  installed pass value. The published UMC202HD specifications do not state its
  `LINE` input impedance, so the AC gate now measures the interface-loaded
  differential ratio directly and cross-checks it against the REW transfer.
- Retained full-dual approval as `NO` pending the fixture physical record,
  clamp installation and integrated DC outcome, unpowered system ground audit,
  and AC transfer commissioning.

### 11.18 2026-09-02 - post-rebuild complete-fixture resistance gate passed

- Recorded the complete disconnected fixture after the user rebuilt the
  attenuator/clamp as one unit. The Agilent U1282A was used in resistance mode
  on its `60 kohm` range with lead resistance nulled and no body contact with
  the circuit.
- Recorded `1.003 kohm` ring-to-sleeve, `1.002 kohm` tip-to-sleeve,
  `9.125 kohm` from `In+` to tip, `9.139 kohm` from `In-` to ring,
  `10.127 kohm` from `In+` to sleeve, `10.142 kohm` from `In-` to sleeve,
  `2.005 kohm` tip-to-ring, `11.131 kohm` from `In+` to ring,
  `11.145 kohm` from `In-` to tip, and `20.271 kohm` from `In+` to `In-`.
- Verified that the direct tip-ring, input-sleeve, cross-path, and complete
  input-input readings agree with their constituent branch sums within
  `0-2 ohm`. All four inferred resistor paths are within their specified `1%`
  nominal tolerances.
- Recalculated the unloaded active-leg gains as `-20.092 dB` for tip and
  `-20.096 dB` for ring, with only `0.004 dB` mismatch. The standalone
  differential prediction is `-20.094 dB`.
- Passed the post-rebuild resistance gate. The result establishes the intended
  symmetric passive topology and absence of shorts or material low-voltage
  leakage under the meter conditions; it does not establish zener identity,
  orientation in both directions, breakdown voltage, or clamp action.
- Retained full-dual approval as `NO` pending the physical component record,
  four-polarity integrated PL310QMD test, unpowered ground-path audit, and AC
  transfer commissioning.

### 11.19 2026-09-02 - installed clamp evidence accepted for qualification

- Recorded that D1-D4 are marked only `BZX 5V1`; manufacturer, complete family
  suffix, tolerance grade, formal power rating, and capacitance remain unknown.
- Recorded the user's zener-analyser result that every installed-device sample
  gives a plausible voltage close to `5 V` at `2 mA`.
- Recorded that each pair is installed anode-to-anode across its `1 kohm`
  shunt. Confirmed this as a valid series-opposed bidirectional connection: one
  device operates in zener breakdown and the other forward-conducts, with their
  roles exchanging when polarity reverses.
- Recorded user confirmation that both `9.1 kohm` series resistors are rated
  `500 mW` and above `100 V` working voltage.
- At a representative `5.6 V` pair voltage and the `64 V` integrated-test
  point, derived approximately `6.40 mA` through the series resistor,
  `5.59 mA` through the shunt, only `0.81 mA` through the clamp, and about
  `4.1 mW` zener dissipation. An accidental open shunt during the bounded test
  would still limit zener dissipation to approximately `32 mW`.
- Accepted the untraceable suffix for this one-off prototype's controlled
  qualification because the primary resistor/shunt network independently
  bounds a rail-limited SU-V570 output and the required clamp dissipation is
  low. Did not attribute the Vishay `500 mW` rating or B/C tolerance to the
  unidentified installed parts; a reproducible future build should use
  traceable devices.
- Kept bidirectional clamp action as `NOT PERFORMED` pending all four PL310QMD
  curves. Full-dual approval remains `NO` pending that test, the remaining
  physical record, ground-path audit, and AC transfer commissioning.

### 11.20 2026-09-02 - first powered fixture curve establishes tip-positive clamp knee

- **USER-REPORTED MEASUREMENT:** with an Agilent U1282A in DC-voltage mode on
  its `60 V` range measuring tip positive relative to sleeve, and a separate
  Agilent U1272A on its `300 V` range measuring the PL310QMD source, recorded
  source/node pairs of `10.03/0.990 V`, `19.95/1.973 V`, `29.98/2.964 V`,
  `40.07/3.949 V`, `45.56/4.459 V`, `50.06/4.841 V`, `55.10/5.183 V`, and
  `60.21/5.400 V`.
- **DERIVED:** using the measured `9.125 kohm` series path and `1.002 kohm`
  shunt, the first four points depart from the unloaded divider prediction by
  only `-0.24%`, `-0.05%`, `-0.08%`, and `-0.40%`. The `45.56 V` point is
  `-1.08%` below prediction; subsequent departures grow monotonically to
  `-9.36%` at `60.21 V` as the clamp conducts.
- **DERIVED:** at `60.21 V`, the unclamped node prediction is `5.957 V`, while
  the measured node is `5.400 V`. The inferred series current is about
  `6.007 mA`, and the inferred clamp current is about `0.617 mA`. This is a
  smooth, credible low-current zener knee, and it satisfies the high-voltage
  clamp criterion without requiring a higher point for that decision. The
  maximum inferred series-resistor dissipation is about `0.329 W`, or `66%` of
  its stated `0.5 W` rating; modest resistor warmth would therefore be expected.
- **PROVISIONAL DECISION:** mark the tip-positive clamp knee `PASS` and its
  approximately `45.5 V` linearity `BORDERLINE`, because the `-1.08%` result is
  marginally beyond the approximate `1%` target. Do not revise the target or
  call the complete four-polarity gate passed until the opposite-polarity and
  both ring curves establish symmetry.
- **OPEN ITEM AT THIS STAGE:** supply CV/CC indication, actual supply current,
  and thermal observations had not yet been reported. Section 11.21 supersedes
  that incomplete observation record and adds the subsequently supplied nominal
  `64 V` point.

### 11.21 2026-09-02 - tip-positive maximum point and operating observations added

- **USER-REPORTED MEASUREMENT:** at the PL310QMD's nominal `64 V` maximum
  setting, the U1272A measured `64.50 V` and the U1282A measured `5.520 V` from
  tip positive to sleeve. The supply remained in CV mode throughout, indicated
  a maximum `6 mA` subject to uncertain internal-ammeter accuracy, and made the
  fixture only slightly warmer than ambient, with no concerning heating.
- **DERIVED:** the unloaded prediction at `64.50 V` is `6.382 V`; the measured
  node is therefore `0.862 V`, or `13.50%`, lower. The inferred series current
  is `6.464 mA`, the inferred shunt current `5.509 mA`, and the inferred clamp
  current `0.955 mA`. The supply's `6 mA` indication is consistent with this
  result at its available resolution and uncertain accuracy.
- **DERIVED:** inferred dissipation is `0.381 W` in the `9.125 kohm` series path,
  `0.030 W` in the `1.002 kohm` shunt, and only about `5.3 mW` in the clamp
  pair. The slight warmth is therefore expected principally from the series
  resistor; substantial zener self-heating is unlikely, although conducted heat
  and the unknown pair temperature coefficient can move the exact knee slightly.
- **SUPERSEDING DECISION:** this supplements the initial curve in Section 11.20
  and closes its missing CV/current/thermal observations. It strengthens, but
  does not otherwise change, the tip-positive decision: high-voltage clamp,
  current, and thermal behaviour pass; `45.5 V` linearity remains `BORDERLINE`
  pending the tip-negative comparison. Record the nominal `64 V` setting's
  measured `64.50 V` without repeating or intentionally exceeding the `64 V`
  procedural ceiling. The remaining three curves and the ground-path and AC
  gates remain open, so full-dual approval remains `NO`.

### 11.22 2026-09-02 - tip-negative voltage curve passes knee and symmetry checks

- **USER-REPORTED MEASUREMENT:** connected PL310QMD HI to black/input `-` and
  sleeve, and LO to red/input `+`; retained U1282A positive on tip and negative
  on sleeve. Recorded source/node pairs of `9.99/-0.989 V`, `19.92/-1.974 V`,
  `29.96/-2.965 V`, `40.08/-3.948 V`, `45.53/-4.449 V`, `50.05/-4.819 V`,
  `55.10/-5.140 V`, `60.12/-5.351 V`, and `64.49/-5.463 V`.
- **DERIVED:** node magnitudes depart from the unloaded tip-divider prediction
  by `+0.06%`, `+0.15%`, `+0.02%`, `-0.45%`, `-1.24%`, `-2.69%`, `-5.72%`,
  `-10.04%`, and `-14.38%`, respectively. The first three algebraically
  negative inferred clamp currents are sub-`4 uA` uncertainty residuals, not
  physical reverse current.
- **DERIVED:** at `64.49 V`, the unclamped node magnitude would be `6.381 V`;
  the measured `5.463 V` is `0.918 V` lower and remains below `6.2 V`. Inferred
  series, shunt, and clamp currents are `6.469 mA`, `5.452 mA`, and `1.017 mA`;
  inferred series-resistor and clamp-pair dissipation are `0.382 W` and
  `5.6 mW`.
- **DERIVED:** the positive and negative tip node magnitudes differ by only
  `0.057 V` at almost identical maximum source voltages, comfortably inside the
  `0.3 V` investigation threshold. Their near-`45.5 V` departures are similarly
  close at `1.08%` and `1.24%`.
- **PROVISIONAL DECISION:** tip-negative high-voltage clamp action and tip-pair
  symmetry pass. Retain `45.5 V` linearity as `BORDERLINE`, rather than changing
  the acceptance criterion: the repeated, symmetric departure identifies the
  installed pair's soft low-current knee and is not evidence of a construction
  fault. Supply CV/CC state, indicated current, and thermal observations for
  this negative run remain open. Both ring-polarity curves, the ground-path
  audit, and AC commissioning also remain open; full-dual approval stays `NO`.

### 11.23 2026-09-02 - tip-negative observations close and ring-positive curve passes

- **USER-REPORTED OBSERVATION:** for the tip-negative run, both PL310QMD
  current limits were `10 mA`; the supply remained in CV mode, indicated `6 mA`
  maximum, and produced mild heating comparable with the tip-positive run.
  This closes the operating-observation item left open in Section 11.22.
- **USER-REPORTED MEASUREMENT:** for ring positive, connected HI to black/input
  `-`, and LO to red/input `+` and sleeve; measured ring positive relative to
  sleeve. Recorded source/node pairs of `10.05/0.990 V`, `20.09/1.986 V`,
  `30.02/2.969 V`, `40.12/3.955 V`, `45.53/4.454 V`, `50.16/4.849 V`,
  `55.00/5.167 V`, `60.03/5.394 V`, and `64.48/5.515 V`. Both current limits
  were `10 mA`; the supply remained in CV mode, indicated `6 mA` maximum, and
  produced the same mild heating as before.
- **DERIVED:** relative departures from the measured ring-divider prediction
  are `-0.39%`, `-0.04%`, `+0.01%`, `-0.32%`, `-1.08%`, `-2.25%`, `-5.01%`,
  `-9.14%`, and `-13.51%`. At `64.48 V`, the unclamped prediction is `6.377 V`
  and the measured node is `0.862 V` lower. Inferred series, shunt, and clamp
  currents are `6.452 mA`, `5.499 mA`, and `0.954 mA`; inferred series-resistor
  and clamp-pair dissipation are `0.380 W` and `5.3 mW`.
- **DERIVED:** ring positive and tip positive differ by only `0.005 V` at their
  almost identical maximum sources; their relative departures are `-13.51%`
  and `-13.50%`. Both are `1.08%` below prediction near `45.5 V`, showing
  exceptionally close agreement between the two installed clamp pairs.
- **PROVISIONAL DECISION:** ring-positive high-voltage clamp, current, CV, and
  thermal behaviour pass. Retain its `45.5 V` linearity as `BORDERLINE`,
  consistent with the two tip polarities rather than indicative of a fault.
  Ring negative is the sole remaining DC polarity; full-dual approval remains
  `NO` pending that curve and the ground-path and AC gates.

### 11.24 2026-09-02 - ring-negative curve completes four-polarity DC sweep

- **USER-REPORTED MEASUREMENT:** connected PL310QMD HI to red/input `+` and
  sleeve, and LO to black/input `-`; retained U1282A positive on ring and
  negative on sleeve. Recorded source/node pairs of `9.99/-0.990 V`,
  `20.00/-1.978 V`, `29.96/-2.963 V`, `40.09/-3.954 V`, `45.62/-4.467 V`,
  `50.12/-4.846 V`, `55.16/-5.185 V`, `60.16/-5.403 V`, and
  `64.46/-5.515 V`. Both current limits were `10 mA`; the supply remained in
  CV mode, indicated `6 mA` maximum, and produced the same mild heating as the
  preceding runs.
- **DERIVED:** relative departures from the measured ring-divider prediction
  are `+0.21%`, `+0.00%`, `+0.00%`, `-0.27%`, `-0.99%`, `-2.23%`, `-4.95%`,
  `-9.19%`, and `-13.49%`. At `64.46 V`, the measured `5.515 V` node is
  `0.860 V` below its `6.375 V` unclamped prediction. Inferred series, shunt,
  and clamp currents are `6.450 mA`, `5.499 mA`, and `0.951 mA`; inferred
  series-resistor and clamp-pair dissipation are `0.380 W` and `5.2 mW`.
- **DERIVED:** ring positive and negative both measure `5.515 V` at nearly
  identical maximum source voltages. Across all four polarities, maximum node
  magnitudes span only `5.463-5.520 V`, every node is below `6.2 V`, and every
  suppression exceeds the required `0.3 V` by a wide margin.
- **DERIVED:** the four near-`45.5 V` departures are `-1.08%`, `-1.24%`,
  `-1.08%`, and `-0.99%`. Three therefore miss the stated approximate `1%`
  target slightly, although all curves remain within `0.45%` through `40 V`
  before entering the same smooth, symmetric clamp knee. The maximum departure
  corresponds to only about `0.11 dB` at the theoretical rail-bound point and
  is absent at the intended approximately `1 V RMS` operating level.
- **PROVISIONAL DECISION:** pass the four powered curves with an explicit,
  characterized `45.5 V` linearity deviation; do not claim exact compliance or
  silently change the criterion. Clamp action, both polarity-pair symmetry
  checks, current, CV operation, and thermal behaviour pass. The integrated DC
  gate remains open only for the required cooled post-stress resistance matrix.
  Full-dual approval remains `NO` pending that check, physical-record completion,
  the ground-path audit, and AC commissioning.

### 11.25 2026-09-02 - post-stress resistance matrix closes integrated DC gate

- **USER-REPORTED MEASUREMENT:** after the four powered curves and cooling,
  measured the disconnected fixture with the Agilent U1282A in resistance mode
  on its `60 kohm` range, with lead resistance nulled before the first reading.
  Recorded sleeve-to-ring `1.004 kohm`, sleeve-to-tip `1.002 kohm`, sleeve-to-
  In+ `10.130 kohm`, sleeve-to-In- `10.146 kohm`, ring-to-tip `2.006 kohm`,
  ring-to-In+ `11.133 kohm`, ring-to-In- `9.141 kohm`, tip-to-In+
  `9.127 kohm`, tip-to-In- `11.149 kohm`, and In+-to-In- `20.275 kohm`.
  Ambient temperature may have fallen slightly during the evening.
- **DERIVED:** every direct path changed by only `0-4 ohm` from the pre-stress
  matrix. The four independent branch changes are `0-2 ohm`, no more than about
  `0.10%` of a `1 kohm` shunt. The post-stress redundant identities close within
  `0-2 ohm`: ring-tip `0`, In+-sleeve `+1`, In--sleeve `+1`, In+-ring `0`,
  In--tip `+2`, and In+-to-In- `+1 ohm`.
- **INFERRED:** the tiny shifts are compatible with the meter's `1 ohm` display
  resolution, contact repeatability, and the reported environmental change.
  Their common positive direction is not sufficient evidence for a component
  temperature coefficient.
- **DECISION:** pass the post-stress resistance gate. There is no evidence of
  resistor damage, an open clamp, a changed connection, or a new leakage path.
  This closes the integrated PL310QMD DC test as `PASS WITH CHARACTERIZED
  45.5 V LINEARITY DEVIATION`. Full-dual approval remains `NO` pending the
  remaining fixture physical record, unpowered system ground-path audit, and AC
  transfer commissioning.

### 11.26 2026-09-02 - ground-path audit begins with sleeve-to-USB-shell bond

- **USER-REPORTED MEASUREMENT:** with the UMC202HD alone for the first stage of
  the unpowered audit, Input 2 TRS sleeve to the USB connector metal shell
  measured `0.035 ohm`. Sleeve to nominally bare UMC202HD chassis and chassis to
  USB shell both read `OPEN`. Considerable probe pressure was applied in an
  attempt to penetrate oxidation or anodizing.
- **VERIFIED MEASUREMENT:** Input 2 sleeve and USB shield shell have a direct
  low-resistance DC bond within probe/contact uncertainty. This measurement
  does not establish continuity to USB signal contacts, PC chassis, or
  protective earth.
- **INFERRED:** the two open readings are consistent with an enclosure isolated
  from sleeve and USB shield, but do not yet prove it. Applied pressure is not a
  positive demonstration that the probes contacted conductive chassis metal.
- **DECISION:** mark the audit `IN PROGRESS`. Before connecting USB to the
  isolated PC for the next stage, obtain low resistance between two separated
  points on the same nominally bare chassis panel. If that control is open, find
  verified conductive chassis points and repeat the two affected readings.
  Full-dual approval remains `NO` pending that control, the rest of the audit,
  physical-record completion, and AC transfer commissioning.

### 11.27 2026-09-02 - UMC202HD chassis control passes interface-alone stage

- **USER-REPORTED MEASUREMENT:** two separated UMC202HD chassis points measured
  `0.013 ohm`, with very firm pressure applied to both probes.
- **VERIFIED MEASUREMENT:** the low chassis-to-chassis resistance demonstrates
  electrical probe contact at both tested points and continuity through the
  enclosure structure. It validates the two earlier open readings involving
  the chassis.
- **DECISION:** pass the interface-alone portion of the ground-path audit. Under
  the isolated, unpowered test conditions, the chassis is DC-isolated from the
  hard-bonded Input 2 sleeve/USB-shell node. This says nothing about RF coupling
  or paths introduced by USB, playback, or other cables. Map the intended USB
  cable's plug shells next, before connecting it to the isolated PC. Full-dual
  approval remains `NO` pending the rest of the audit, physical-record
  completion, and AC transfer commissioning.

### 11.28 2026-09-02 - intended USB-cable shield continuity passes

- **USER-REPORTED MEASUREMENT:** with the intended USB cable disconnected at
  both ends, metal plug shell to metal plug shell measured `0.130 ohm`.
- **VERIFIED MEASUREMENT:** the intended cable has low-resistance end-to-end
  shield continuity.
- **DERIVED:** together with the UMC202HD's measured `0.035 ohm` Input 2
  sleeve-to-USB-shell bond, the cable carries that sleeve node to the PC-end
  plug shell when connected. Whether the PC then bonds it to chassis and
  protective earth remains a separate measurement.
- **DECISION:** pass the USB-cable portion of the ground-path audit and proceed
  to the isolated-PC stage. Full-dual approval remains `NO` pending the rest of
  the audit, physical-record completion, and AC transfer commissioning.

### 11.29 2026-09-02 - isolated-PC stage confirms protective-earth reference

- **USER-REPORTED MEASUREMENT:** using the Agilent U1282A in auto-ranging
  resistance mode with nulled leads, measured PC USB socket shell to bare PC
  chassis `0.170 ohm`, PC chassis to the protective-earth pin of the free mains
  plug `0.245 ohm`, UMC202HD Input 2 sleeve to PC chassis `0.412 ohm`, and Input
  2 sleeve directly to the free plug's PE pin `0.379 ohm`. Considerable probe
  pressure and a constrained working position make the last digits uncertain.
- **DERIVED:** the separately measured shield-path elements to PC chassis sum
  to `0.035 + 0.130 + 0.170 = 0.335 ohm`, excluding the mated USB contact; the
  direct reading is `0.412 ohm`, a `0.077 ohm` difference. The direct sleeve-to-
  PE result is lower than the `0.657 ohm` sum of the two direct readings through
  the selected chassis probe point. This is not treated as a contradiction:
  remade two-wire contacts, a distributed chassis, and possible parallel USB
  shield/circuit-ground paths prevent precise scalar addition.
- **VERIFIED MEASUREMENT:** all four paths are unambiguously low resistance.
  The PC bonds USB shell to chassis and chassis to PE; with USB connected, Input
  2 sleeve has a directly measured low-resistance path to both PC chassis and
  the free mains plug's PE pin.
- **DECISION:** pass the isolated-PC/PE stage. The original proposed earth-
  reference path is confirmed in substance, although the UMC202HD's bare
  enclosure is not part of it and the USB connection may contain parallel
  shield and circuit-ground routes. These ordinary DMM readings establish
  topology only and do not certify protective-earth resistance or appliance
  safety. The one-off PC shutdown window is complete. Full-dual approval remains
  `NO` pending the playback-path and fixture-alone audit checks, physical-record
  completion, and AC transfer commissioning.

### 11.30 2026-09-02 - mono TS playback cable mapped but placed on hold

- **USER-REPORTED MEASUREMENT:** using the Agilent U1282A in auto-ranging
  resistance mode, measured output-plug tip to RCA centre `0.244 ohm`, tip to
  RCA shell `OPEN`, sleeve to RCA centre `OPEN`, and sleeve to RCA shell
  `0.078 ohm`. The output plug is two-contact mono TS and has no ring contact.
- **VERIFIED MEASUREMENT:** the cable maps cleanly as an ordinary unbalanced
  TS-to-RCA cable, without a tip/sleeve cross-connection.
- **DERIVED:** when inserted into a TRS output jack, the TS plug's long sleeve
  contacts both the jack's sleeve and ring springs. It therefore grounds the
  UMC202HD output jack's ring contact; `N/A` at the loose plug does not
  mean the interface ring remains unconnected in use.
- **EXTERNAL RESEARCH:** Behringer's UMC202HD product page and quick-start guide
  specify `1/4-inch TRS` line outputs. The reviewed manufacturer material does
  not explicitly authorize a TS plug or state that the cold output may be
  shorted to sleeve.
- **DECISION:** pass the cable's continuity map but place it on output-
  compatibility hold. Prefer a TRS-to-RCA cable wired tip-to-centre,
  sleeve-to-shell, and ring open; re-map it before the connected ground audit.
  Alternatively, retain the TS cable only if explicit manufacturer evidence
  establishes short tolerance for this output. Full-dual approval remains `NO`
  pending this resolution, the remaining ground audit, physical-record
  completion, and AC transfer commissioning.

### 11.31 2026-09-02 - unpowered output ring bond narrows TS-cable hold

- **USER-REPORTED MEASUREMENT:** with a genuine TRS breakout plugged into one
  UMC202HD rear output and nothing else connected to the unpowered interface,
  ring to shield/sleeve measured `0.021 ohm`. Cross-checking the breakout loose
  on the bench gave `OPEN` ring-to-shield.
- **VERIFIED MEASUREMENT:** the low resistance arises through the tested output,
  not a permanent short in the breakout.
- **INFERRED:** the tested output ring is deliberately grounded at DC. If that
  remains true with the interface powered, the TS playback cable adds no new
  ring-to-sleeve short. The unpowered result cannot exclude a muting or
  protection circuit that changes state on power-up, and the tested rear-output
  number was not recorded.
- **DECISION:** narrow but do not yet lift the TS-cable hold. With no amplifier,
  fixture, or other analogue cable connected, apply a low-level `1 kHz` signal
  separately to Outputs 1 and 2 and record tip-sleeve, ring-sleeve, and tip-ring
  AC voltage for each. This also resolves whether the current AC commissioning
  assumption that Output 2 supplies two active balanced legs is valid. Full-
  dual approval remains `NO` pending that map and the remaining release gates.

### 11.32 2026-09-02 - powered Output 2 ring-grounded; Output 1 repeat required

- **USER-REPORTED MEASUREMENT:** with the Agilent U1282A in auto-ranging AC-
  millivolt mode, recorded Output 1 tip-sleeve `0.002 mV`, ring-sleeve
  `0.001 mV`, and tip-ring `27.42 mV`; REW had inadvertently sent the signal to
  Output 2 instead of Output 1. The driven Output 2 measured tip-sleeve
  `78.9 mV`, ring-sleeve `0.000 mV`, and tip-ring `78.84 mV`.
- **DERIVED:** for Output 2, tip-ring and tip-sleeve differ by only `0.06 mV`,
  approximately `0.076%`, while ring-sleeve is zero. For Output 1, the phasor
  triangle requires tip-ring to lie between `0.001 mV` and `0.003 mV` when the
  two sleeve-referenced magnitudes are `0.002 mV` and `0.001 mV`; `27.42 mV`
  cannot belong to the same steady measurement state.
- **VERIFIED MEASUREMENT:** powered, driven Output 2 is ring-grounded for this
  purpose. It must drive the fixture asymmetrically from tip to sleeve, not from
  two active balanced legs.
- **DECISION:** pass Output 2 and do not repeat it. Classify the Output 1 row as
  invalid rather than failed because the wrong channel was driven and its
  sequential readings violate the voltage identity. Repeat Output 1 only, with
  channel 1 selected, recording tip-ring both before and after tip-sleeve and
  ring-sleeve. The TS playback-cable hold depends only on that repeat. Full-
  dual approval remains `NO` pending it and the other release gates.

### 11.33 2026-09-03 - driven Output 1 passes; both outputs ring-grounded

- **USER-REPORTED MEASUREMENT:** with the Agilent U1282A in auto-ranging AC-
  millivolt mode and REW routed only to the channel under test, driven Output 1
  measured tip-sleeve `78.69 mV`, ring-sleeve `0.002 mV`, and tip-ring
  `78.73 mV`. Output 2 was not repeated; its valid driven result remains
  `78.9/0.000/78.84 mV`, respectively.
- **DERIVED:** on Output 1, ring-sleeve is approximately `0.0025%` of tip-
  sleeve. Tip-ring differs from tip-sleeve by only `0.04 mV`, approximately
  `0.051%`. Because the three DMM readings are sequential, their `0.038 mV`
  (`0.048%`) excess over the ideal phasor upper bound is consistent with meter
  resolution or slight source drift and lies far inside the `1 mV`/`2%`
  topology tolerance. Output 1 and Output 2 tip-sleeve amplitudes differ by
  only `0.21 mV`, approximately `0.267%` of their mean.
- **VERIFIED MEASUREMENT:** both powered, driven UMC202HD rear outputs are ring-
  grounded for this purpose. Neither output presents two active balanced legs.
- **DECISION:** pass the rear-output topology map and lift the mapped mono TS-
  to-RCA playback cable's compatibility hold. Its sleeve connects Output 1 ring
  to a ground node to which it is already connected, rather than shorting an
  active cold output. Use Output 2 tip and sleeve as the asymmetric source for
  fixture AC commissioning. Full-dual approval remains `NO` pending physical-
  record completion, the connected playback-path ground check, and AC transfer
  commissioning. The existing disconnected post-stress matrix closes the
  fixture-alone ground check with `10.130 kohm` and `10.146 kohm` input-to-
  sleeve paths.
