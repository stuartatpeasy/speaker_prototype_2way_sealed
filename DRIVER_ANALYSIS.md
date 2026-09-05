# Driver Analysis and Measurement Record

**Project:** sealed passive two-way loudspeaker prototype  
**Woofer:** SB Acoustics **SB17NRX2C35-8**  
**Tweeter:** SB Acoustics **SB26STWGC-4**  
**Record created:** 2026-08-27  
**Last updated:** 2026-09-05

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
- The SU-V570 reference fixture is electrically released for controlled
  UMC202HD bench use. Its topology, phantom isolation, construction,
  resistance, DC clamp, ground path, connector maps, and proportionate AC
  sanity gate all pass. The full evidence remains in the fixture authority and
  qualification records rather than this driver summary.
- The first UMC202HD checkout passed powered no-signal behaviour and reached a
  clean `1.00 V RMS` at the woofer, but a desktop-specific output-stream dropout
  prevents stable sweeps. The same interface is stable on a Windows 11 laptop;
  extensive desktop controls have closed REW, ASIO, sample rate, tested ports
  and cables, practical peripheral removal, legacy disks, and broad power-plan
  changes as useful causes. The current Microsoft UAC2 binding improved but did
  not eliminate the fault. See
  [`rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md`](rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md)
  for the evidence matrix and deferred live-Linux test.
- **CORRECTED HISTORICAL PROVENANCE - 2026-09-04:** all earlier uninterrupted
  REW impedance sweeps used the StarTech `ICUSBAUDIO2D`, not the UMC22. The
  UMC22's clean evidence comprises extensive ordinary playback plus a current
  matched five-minute music control with zero dropouts; no UMC22 REW full-
  duplex sweep has yet passed.
- **PROVISIONAL DECISION - 2026-09-05:** pursue the risk-accepted UMC22 route so
  FRD is no longer blocked on the UMC202HD diagnosis. At `1.00 V RMS` across the
  woofer the fixture predicts `0.09892 V RMS`, about `19.9 dB` below the UMC22
  instrument input's published `+2 dBu` maximum. A rail-bounded fault can exceed
  that published level by about `10.3 dB`; the user accepts the unquantified
  possibility of UMC22 damage. Powered use remains unapproved until the contact,
  phantom, ground-path, and low-voltage full-duplex gates in
  [`rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md`](rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md)
  pass. Direct user-observed PCB inspection has established that both UMC22
  rear outputs are two-node unbalanced sources: tip is signal and ring/sleeve
  share one copper return. The unpowered `INST 2` contact map also passes: tip
  is open to ring, sleeve, and USB shell, while those three returns are mutually
  connected at sub-ohm resistance. Gate B phantom isolation passes: all
  readings with phantom off and on remained at or below approximately
  `0.0020 V DC` and settled to zero. Gate C's amplifier-positive isolation also
  passes with `9125 ohm` to tip and `10127 ohm` to ring, sleeve, and USB shell;
  its stable return paths are `0.290-0.311 ohm` and complete the intended common
  bond. Gates A-C now pass. The amplifier-disconnected low-voltage full-duplex
  checkout's no-signal stage also passes: `0.0015 V DC` settled to zero with no
  clipping or abnormality. REW device enumeration also passes with Java
  exclusive-mode UMC22 input/output, independent L/R channels, `48 kHz`, and
  calibration `None`. The initial no-excitation UI assignment used measurement
  output/input L, reference input R, reference output R, loopback calibration/
  timing, IR merge, and zero offset. Unity
  input scaling, the UMC22-specific measurement name, and the `20-20000 Hz`
  first-checkout range are now confirmed. The bounded amplifier-disconnected
  `1 kHz` level also passes at `0.0207 V RMS`, with slow `0.0205-0.0210 V RMS`
  movement and no clipping, dropout, or abnormality. Live REW reference capture
  initially failed because a non-exclusive input endpoint was selected. Choosing
  the `EXCL:` variant immediately restored linear `GAIN 2` response; Input 2 is
  now set to `-20.88 dBFS` at a steady external `0.0218 V RMS`. Input 1 also
  responds normally to its gain control and nearby sound without clipping. The
  controlled headphone-to-microphone setup also passes with main `In` at
  `-19.5 dBFS`, `Ref In` at `-20.84 dBFS`, and a steady `0.0230 V RMS` external
  reference. The first amplifier-disconnected `1M` full-duplex sweep then
  completed without warning, error, clipping, audible discontinuity, or
  abnormality and produced one clear dominant impulse arrival. It is valid
  dropout-free stream evidence but not timing evidence: the stored timing index
  is `N/A` and System Delay is unavailable because reference output R was
  physically unconnected while the fixture sensed output L. A second sweep
  corrected both outputs to L and completed without clipping or dropout at
  `0.0222 V AC`, but its Info panel stored reference input L rather than R. Its
  almost-flat response is an invalid self-reference and timing remains `N/A`.
  Selecting reference input R then raised a REW beta 133 `Index 1 out of bounds
  for length 1` exception. After restart the exact-`EXCL:`, `48 kHz`, L/L/L/R
  setup passes visual audit. One exact-routing repeat with Java `Stereo only`
  selected then completes without the exception and stores reference output L
  and input R, but timing index remains `N/A` and System Delay unavailable. Its
  `0.5100 ms` peak and `0.4792 ms` IR start are physically plausible but do not
  prove repeatable reference timing. REW Scope cannot retrieve the preceding
  measurement's captures. The subsequent amplifier-disconnected `256k` timing-
  only sweep passed with reference index `47970.52`, System Delay `0.6141 ms`,
  IR start `0.5208 ms`, exact L/L/L/R routing, and no warning, clipping, dropout,
  or exception. Gate D now passes for hardware, stream, routing, and ordinary
  loopback timing. The IR-merge treatment remains excluded;
  the subsequent calibration-data diagnostic passed with `Soundcard: Loopback
  cal`, reference index `47975.52`, System Delay `0.5100 ms`, and no warning or
  abnormality. Use that treatment for the UMC22. Load the ECM8000 calibration
  before treating any response as design evidence.
  UMC22 Output 1 reuses the already-mapped TS-to-RCA cable into SU-V570 `AUX`
  left. The complete switched-off Gate E assembly now passes with the woofer
  and fixture in parallel at B-left with correct polarity and all unintended
  sockets empty. The subsequent UMC22-only USB/phantom no-signal observation
  also passes: the phantom indicator illuminated, neither channel clipped, and
  there was no unexpected sound, instability, heating, smell, or other
  abnormality. The following minimum-volume SU-V570 no-signal stage also passes
  after approximately one minute: the woofer remained silent, neither channel
  clipped, and there was no transient or persistent hum/buzz, instability,
  heating, smell, smoke, or other abnormality. The controlled woofer level now
  passes with `1.0000 V AC` indicated on the Agilent U1282A at the SU-V570's
  `-38 dB` volume-scale mark. The gross protected-reference voltage also passes
  at a stable `98.53 mV AC`, giving a measured transfer of `0.09853`
  (`-20.129 dB`), only `-0.39%` (`-0.034 dB`) from prediction. Generator was
  stopped; neither channel clipped; and there was no dropout, instability, or
  other abnormality. The breakout has now been removed, the fixture is
  connected directly to `INST 2`, the U1282A is back across the woofer, and the
  powered final connection shows no abnormality. Reference-input gain also
  passes at a stable `-20.87 dBFS` (`+/-0.01 dB`) with `GAIN 2` approximately
  2 o'clock, the woofer at `1.0003 V AC`, at least `6 dB` peak headroom, and no
  clipping, dropout, or anomaly. The supplied generic `0-degree` ECM8000
  response has now been identified as
  `calibration/ECM8000_calibration_data.csv`; its orientation matches the
  microphone aimed at the cabinet. The CSV itself is now REW-compatible: spaces
  were added after its commas without changing numeric values, and the redundant
  `.cal` derivative was removed at the user's request. This is not a unit-
  specific or absolute-sensitivity calibration, so its unquantified sample
  error must remain attached to any resulting magnitude/phase evidence.
  User-reported geometry is `1000 mm` capsule-to-baffle, at woofer-centre height
  and baffle horizontal centre, with the cabinet on a secured 10-degree rotation
  jig.
  The pre-consolidation derivative loaded without warning and persisted only on
  microphone input L, with input R showing `None`. The retained canonical CSV
  has now also been selected and persists under its new filename on exact
  `EXCL:` UMC22 input L only; R remains `None`. The bounded Check Levels
  observation was clean with `GAIN 1` approximately 4 o'clock, main `In`
  approximately `-15.5 dBFS`, and `Ref In` approximately `-33.8 dBFS`; both
  varied by less than about `+/-1 dB`. The subsequent sweep evidence narrows
  both conclusions. At `-10 dBFS` REW raised distortion and inadequate-headroom
  warnings. A user-initiated `-20 dBFS` repeat removed the warning but still
  approached about `3.8 dB` headroom. Its Info panel proves the microphone file
  was not applied (`Mic: No cal file`): the Preferences screenshot associates
  the CSV with `Default Input`, while the selected measurement input is
  `MICROPHONE (Master Volume), L`. The repeat does pass as a routing/timing
  diagnostic with `Soundcard: Loopback cal`, reference index `47850.03`, System
  Delay and peak `3.1243 ms`, SNR `43.8 dB`, correct L/R reference routing, one
  dominant arrival, and a grossly woofer-like response. At that checkpoint
  signals were stopped pending correction of the active-input calibration
  association and microphone gain.
  The CSV has now been associated with the exact active `EXCL:` UMC22
  `MICROPHONE (Master Volume), L` selector and persists across Preferences
  close/reopen. Measure's Calibration data display now also names
  `ECM8000_calibration_data.csv` for the pending microphone input L while the
  Measure dialog explicitly uses `MICROPHONE (Master Volume) L` and retains R
  as the timing-reference input. The pre-measurement calibration-application
  check therefore passes. The subsequent `-20 dBFS` Check Levels adjustment
  moved main `In` from approximately `-15.5` to `-19.3 dBFS`, an actual
  `3.8 dB` reduction, with only a few degrees of knob movement and no meaningful
  change to its approximate 4 o'clock description. This predicts approximately
  `7.6 dB` minimum sweep headroom. `Ref In` remained stable at `-33.58 dBFS`
  with only `+/-0.01 dB` fluctuation, and there was no warning, clipping,
  dropout, or other abnormality. Retain the new `GAIN 1` position. One
  calibrated `-20 dBFS` verification sweep was then approved while reusable
  acoustic capture remained held pending its result. That sweep completed without
  warning or anomaly but directly showed only `3.6 dB` main-input headroom,
  while reference headroom was `32.9 dB`. The main channel therefore still
  fails the `6 dB` target and the prior `7.6 dB` prediction is superseded.
  Measurement Info nevertheless passes the diagnostic metadata: microphone CSV
  and loopback calibration are stored, L/L/R routing and numeric timing are
  correct, SNR is `44.4 dB`, and signal-to-distortion is `34.3 dB`. The highest
  response peak is `6.07 kHz`. A short `6070 Hz`, `-20 dBFS` output-L tone then
  reduced main-input peak from approximately `-2` to `-10.3 dBFS` when only
  `GAIN 1` was moved to approximately 2 o'clock. This directly establishes
  `10.3 dB` main-input headroom at the measured worst-case frequency; no
  equipment or signal abnormality occurred. One final calibrated verification
  sweep then passed with main/reference peaks `-10.7`/`-33 dBFS`, both green,
  and no warning or abnormality. Measurement Info stores the mic CSV, loopback
  cal, correct route, timing index `47849.96`, System Delay `3.1257 ms`, SNR
  `43.5 dB`, and signal-to-distortion `62.5 dB`. It is accepted as
  repeatability run 1. Runs 2 and 3 also stayed green without warning or
  abnormality and pass stored calibration, routing, timing, and signal-quality
  metadata. Their three System Delays are
  `3.1257`/`3.1267`/`3.1264 ms`, a total spread of only `1.0 us`, passing the
  preferred `5 us` limit. The raw session is saved. Its first native-grid API
  comparison under the stored long default IR windows is room-dominated and
  does not pass, but the corresponding three IR peak amplitudes span only
  `0.037 dB`. The superseding raw-IR comparison uses one common derived
  `2.0 ms` left / `1.0 ms` right direct window. Over `1-5 kHz`, maximum
  magnitude spread is `0.0743 dB` and maximum circular phase spread is
  `1.931 degrees`; at `2.3 kHz` they are `0.0735 dB` and `0.697 degrees`.
  Together with the clean live runs and delay result, this passes Gate E and
  qualifies the UMC22 route for controlled installed-woofer FRD. The short
  derived window is adequate for qualification, not adopted as a final stored
  REW window. Generic microphone-calibration and absolute-SPL limitations
  remain; the result does not release raw-tweeter or polar work.

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

1. Acquire the first reusable installed-woofer FRD series with the qualified
   UMC22 route under
   [the fallback procedure](rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md). Keep the
   final gains, `-20 dBFS` sweep level, fixed `1000 mm` geometry, common timing,
   and generic non-unit-specific microphone-calibration limitation. Select and
   record a REW-native IR window suitable for the actual response bandwidth.
   Continue the UMC202HD live-Linux diagnosis independently rather than blocking
   FRD on it.
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
- The UMC22 Input 2 contact map, phantom-isolation gate, complete Gate C ground
  audit, full-duplex stream execution, ordinary loopback timing, and loopback-
  generated electrical-reference calibration now pass. The IR-merge treatment
  remains excluded. A generic, REW-compatible `0-degree` ECM8000 CSV is now
  retained. Its former `Default Input` association did not apply to the selected
  measurement source; the file now persists against the exact active
  `MICROPHONE (Master Volume), L` selector, and Measure's Calibration data
  display and the final measurement metadata confirm its application to input
  L. Its unit-to-unit uncertainty remains unquantified. The microphone gain
  passed the initial pink-noise Check Levels but failed to
  provide adequate sweep headroom. Targeted gain setting at `6.07 kHz`, the
  final calibrated checkout, and two unchanged repeats now pass. All three
  stayed green without warning or abnormality. Delay spread is `1.0 us`; under
  a common conservative direct window the `1-5 kHz` maximum spreads are
  `0.0743 dB` magnitude and `1.931 degrees` phase. Gate E and the controlled
  installed-woofer route therefore pass. The fixture itself is released; the
  fallback record owns the controlled powered gate. Final measurements still
  require a documented REW-native window, and the raw tweeter requires its own
  protection and procedure.
  Keep the loudspeaker cable fixed because the reference plane is at the
  amplifier terminals, not the driver terminals.
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
- [Behringer U-PHORIA series quick-start guide, including UMC22 specifications](https://mediadl.musictribe.com/media/PLM/data/docs/UMC/QSG_BE_0805-AAR_U-PHORIA-Series_WW.pdf)
- [Klippel, *Mechanical Fatigue and Load-Induced Aging of Loudspeaker Suspension*](https://www.klippel.de/fileadmin/klippel/Bilder/Know-How/Literature/Papers/Aging%20of%20loudspeaker%20suspension_Klippel.pdf)
- [REW impedance-measurement documentation](https://www.roomeqwizard.com/help/help_en-GB/html/impedancemeasurement.html)

### 10.3 Acoustic-measurement procedures and evidence

- [`DRIVER_RUNIN.md`](DRIVER_RUNIN.md)
- [`rew/FRD_MEASUREMENT_SETUP_TEST.md`](rew/FRD_MEASUREMENT_SETUP_TEST.md)
- [`rew/SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md`](rew/SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md)
- [`rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md`](rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md)
- [`rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md`](rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md)
- [`rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md`](rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md)
- [`rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md`](rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md)
- [`rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md`](rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md)
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

### 11.6 2026-09-01 to 2026-09-04 - reference-path qualification and checkout

- Passed SU-V570 common-ground topology, UMC202HD Input 2 phantom isolation,
  fixture construction/resistance, four-polarity DC clamp, full ground-path,
  rear-output topology, and interconnect maps. Raw evidence is retained in the
  fixture qualification record.
- Established the rear outputs as mechanically TRS but electrically TS and
  corrected the installed amplifier input to `AUX` left, speaker bank `B` left.
- Accepted the corrected low-voltage `105.3 mV` input / `10.0 mV` output
  observation as a proportionate approximately `-20 dB` AC sanity check. The
  detailed fixture release basis is retained in the AC commissioning record.
- Passed the powered no-signal observation and reached a clean `1.00 V RMS` at
  the woofer, then stopped sweeps because of recurring UMC202HD source-stream
  dropouts. The complete compact test matrix, closed causes, privacy treatment,
  and live-Linux next discriminator are retained only in
  [`rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md`](rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md).

### 11.7 2026-09-05 - risk-accepted UMC22 FRD fallback

- Accepted a pragmatic UMC22 route in principle so the desktop-specific
  UMC202HD dropout does not indefinitely block acoustic development.
- Derived approximately `19.9 dB` of normal reference-input headroom at the
  established `1.00 V RMS` woofer level, but recorded that the fixture's
  approximately `4.50 V peak` rail-bounded result is about `10.3 dB` above the
  UMC22 instrument input's published `+2 dBu` maximum.
- Recorded the user's explicit acceptance of possible UMC22 damage without
  extending that acceptance to person, amplifier, PC, loudspeaker, or
  measurement-integrity hazards.
- Added
  [`rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md`](rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md)
  with only the interface-specific contact, phantom, ground-path, low-voltage
  full-duplex, and controlled woofer gates still required. Powered-amplifier
  use remains unapproved until those gates pass.
- Recorded direct user-observed PCB inspection of both UMC22 rear outputs:
  their separate mechanical TRS ring and sleeve/shield pads share one copper
  fill, making each a tip-plus-common, TS-equivalent unbalanced source. This
  reduces uncertainty in the future playback-cable map but does not advance
  the Input 2 or full-duplex gates.
- Passed the unpowered UMC22 `INST 2` contact map with tip-to-ring,
  tip-to-sleeve, and tip-to-USB-shell all open; ring-to-sleeve `0.314 ohm`,
  ring-to-shell `0.050 ohm`, and sleeve-to-shell `0.030 ohm`; and no observed
  polarity sensitivity. The sub-ohm values are used topologically rather than
  as precision resistance data because they do not close as a resistance
  triangle. At that checkpoint Gate B phantom isolation was next; powered-
  amplifier use remained unapproved.
- Passed the phantom-off half of Gate B with the UMC22 connected only to USB
  and the `INST 2` breakout: tip-to-sleeve `0.0005 V DC`, ring-to-sleeve
  `0.0000 V DC`, and tip-to-ring `0.0004 V DC`. The `0.0005 V DC` maximum is
  `200` times below the `0.1 V DC` stop threshold. The phantom-on comparison is
  still required before Gate B can pass.
- Passed the phantom-on half and therefore all of Gate B. Enabling phantom with
  the meter across tip-to-sleeve caused no movement beyond `0.001 V DC`; all
  three pairs initially displayed approximately `0.0020 V DC` when probed and
  settled to `0.0000 V DC` in approximately `10 s`. This is at least `50`
  times below the stop threshold and materially unchanged from phantom off.
  The final unpowered ground-path audit is next; powered-amplifier use remains
  unapproved.
- Selected UMC22 Output 1 to SU-V570 `AUX` left through the same mapped
  TS-to-RCA playback cable used in the UMC202HD checkout. Because both
  interfaces have the same tip-plus-common source topology, its existing
  `0.244 ohm` signal, `0.078 ohm` return, and open cross-path evidence is reused;
  only the complete UMC22 assembled ground path remains to be measured.
- Passed Gate C amplifier-positive isolation in the final unpowered assembly:
  speaker-bank `B` left positive measured `9125 ohm` to breakout tip and
  `10127 ohm` to breakout ring, breakout sleeve, and USB shell. The exact
  `10127 - 9125 = 1002 ohm` difference reconstructs R3 and proves that no mapped
  return bypasses R1. The low-resistance return-node map remains before Gate C
  can pass.
- Passed the Gate C return map in the unchanged unpowered assembly. Speaker-
  bank `B` left negative measured `0.137 ohm` to the `AUX` left RCA shell and
  `0.311`, `0.290`, and `0.299 ohm` to breakout ring, breakout sleeve, and USB
  shell respectively, with no instability. The local result matches the prior
  `0.12-0.15 ohm` amplifier range; the complete paths coherently include the
  `0.078 ohm` cable return and remade contacts. Gate C therefore passes. The
  amplifier-disconnected low-voltage full-duplex checkout is next; SU-V570
  power remains unapproved.
- Passed the Gate D amplifier-disconnected no-signal check through the source
  adaptor, complete clamp/attenuator, and breakout. Tip-to-sleeve began at
  `0.0015 V DC` and settled to `0.0000 V DC` after approximately `15 s`, with
  no clipping indication or abnormality. The initial magnitude is about `66.7`
  times below the stop threshold. REW may now be opened without excitation to
  establish the UMC22 `48 kHz` full-duplex routing; amplifier power remains
  unapproved.
- Passed REW device enumeration with driver type `Java`, input and output both
  `EXCL: Behringer UMC22 (USB Audio CODEC)`, output choices `L`/`R`/`L+R`,
  input choices `L`/`R`, rate `48 kHz`, and soundcard calibration `None`.
  Channel and timing-reference assignments remain to be confirmed before any
  signal is generated.
- Passed the no-excitation channel/timing assignment from screenshots:
  measurement output/input `L`, reference output/input `R`, loopback-as-cal-and-
  timing enabled, loopback response merged into the IR, and offset `0.0000 ms`.
  The user then confirmed input scalar `1.00`, measurement name `UMC22
  low-voltage loopback 1`, and range `20-20000 Hz`, while retaining `-20 dBFS`,
  `1M`, one repetition, and zero timing offset. The pre-excitation configuration
  therefore passes; the bounded amplifier-disconnected `1 kHz` level setting is
  next.
- Passed the controlled `1 kHz`, `-20 dBFS` amplifier-disconnected level check.
  Breakout tip-to-sleeve was `0.0207 V RMS` with `OUTPUT` at approximately
  3 o'clock, wandering slowly over only `0.0205-0.0210 V RMS` (`0.21 dB`
  end-to-end). There was no clipping, dropout, or abnormality. This establishes
  the analogue level but not REW full-duplex stability; setting Input 2's
  reference-channel gain is next.
- Held the live reference-gain step after `Ref In` remained at approximately
  `-93.72 dBFS` while physical `GAIN 2` was moved across its full range, despite
  the DMM-proved tone at `INST 2`. The screenshot shows measurement input `L`
  and loopback input `R`, with both input meters at the noise floor; it also
  shows the input device without the intended `EXCL:` prefix. This does not
  revoke the analogue-level pass, but the live Java/USB input endpoint and
  channel map remain unproved. Restoring or disproving the exclusive input
  endpoint is next; a reversible main-input `R` test follows only if needed.
- Resolved the live reference-capture hold by selecting the missing `EXCL:`
  input endpoint. `Ref In` immediately responded linearly in decibels to
  `GAIN 2` and is now set to a stable `-20.88 dBFS`, fluctuating by only about
  `0.01 dB`; the corresponding tip-to-ring voltage is a steady `0.0218 V RMS`.
  Ring and sleeve are the mapped common return, so this remains consistent with
  the protected Input 2 path. The reference-channel level passes; Input 1's
  microphone channel is next.
- Passed the Input 1 microphone-channel check. With `GAIN 1` at minimum, room
  sound indicated about `-83 dBFS`, generally moving by about `+/-3 dB`; at the
  approximately 2-o'clock gain setting it averaged roughly `-56 dBFS`, with
  nearby speech at approximately `-18 dBFS`. Speech, finger clicks, and other
  local sounds produced normal responses; no clipping or abnormality occurred.
  Continuous PC-fan noise plus intermittent birds and aircraft mean these are
  functional channel observations rather than intrinsic electronic-noise data.
  Both input channels now pass; controlled headphone-to-microphone full-duplex
  setup is next.
- Passed the controlled headphone-to-microphone full-duplex level setup with
  main `In` at `-19.5 dBFS`, `Ref In` at `-20.84 dBFS`, and breakout tip-to-ring
  at a steady `0.0230 V RMS`. `GAIN 1` was between 2 and 3 o'clock, `GAIN 2`
  remained between 3 and 4 o'clock, and the left earpiece was approximately
  `150 mm` from the microphone. No clipping, dropout, or abnormality occurred.
  The two channel levels differ by only `1.34 dB`; one controlled `1M` sweep is
  next.
- Passed execution of the first UMC22 REW full-duplex sweep: one amplifier-
  disconnected `1M`, `20-20000 Hz`, `-20 dBFS` measurement completed without
  warning, error, clipping, audible discontinuity, or abnormality. The Impulse
  view contains one unmistakable dominant arrival near zero and no comparable
  later peak. This is functional headphone-path evidence, not driver FRD.
  Its Info panel subsequently showed timing-reference index `N/A`, System Delay
  `Not available`, offset `N/A`, clock adjustment `0.0 ppm`, mode `Loopback as
  cal ref`, output R, and input R. The fixture actually receives measurement
  output L while physical output R is empty, so the result remains a valid
  dropout-free stream test but fails timing validity. The documented reference-
  output assignment was the error, not the user's wiring. Repeat once with both
  measurement and timing-reference outputs L.
- Passed stream execution, but not response/timing validity, on the second
  amplifier-disconnected UMC22 sweep. With both output selectors corrected to
  L and the external level confirmed as `0.0222 V AC`, the `1M`, `20-20000 Hz`,
  `-20 dBFS` sweep completed without unexpected warning, clipping, or dropout.
  Its Info panel nevertheless stores `Timing ref input: MICROPHONE (Master
  Volume) L`, the same Input 1/L used for the measurement, rather than fixture-
  fed Input 2/R. The almost-flat magnitude and phase are therefore an invalid
  self-reference, and timing index remains `N/A` with System Delay unavailable.
  At that checkpoint one exact-routing repeat was next: outputs L, measurement
  input L, reference input R; no wiring or gain change was required.
- Held the next exact-routing attempt when selecting reference input R caused
  REW V5.40 beta 133 to throw `ArrayIndexOutOfBoundsException: Index 1 out of
  bounds for length 1`. After restarting REW, screenshots show the exact
  `EXCL:` UMC22 endpoints, `48 kHz`, `32k` buffers, output/reference-output L,
  measurement input L, reference input R, loopback calibration/timing and merge,
  zero offset, and the established sweep fields. Relevant Analysis settings are
  also coherent. The exception is consistent with a stale mono Java capture
  object but the obfuscated stack does not prove that inference. One controlled
  retry is authorised after selecting Java `Stereo only`; if the exception
  recurs, stop and retain a REW debug file rather than repeating measurements.
- Completed the Java `Stereo only` exact-routing sweep without recurrence of
  the beta 133 channel-index exception. The Info panel stores timing-reference
  output L and `MICROPHONE (Master Volume) R`, with measurement input L. It
  nevertheless reports timing index `N/A`, System Delay `Not available`, timing
  offset `N/A`, and clock adjustment `0.0 ppm`. The acoustic peak is
  `0.5100 ms` and IR start `0.4792 ms` (`164 mm`); both are physically plausible
  for the nominal `150 mm` test spacing but do not prove stable loopback timing.
  The subsequent proposed inspection of retained `Captured` and `Ref Captured`
  traces was based on a mistaken interpretation of REW Scope; the current Scope
  is a live two-channel instrument and cannot display the preceding measurement
  buffers. One short `256k` amplifier-disconnected timing-only sweep is now the
  bounded A/B test. It retains L/L/L/R routing and all physical settings while
  isolating ordinary loopback timing from loopback calibration and IR merging.
- Passed that amplifier-disconnected `256k` timing-only diagnostic. The current
  physical setup was confirmed as the known-good USB path; Output 1/L through
  the complete source-adaptor/clamp/attenuator/breakout path to `INST 2`;
  ECM8000 on `MIC / LINE 1`; headphones connected; and phantom active. REW
  stored reference index `47970.52`, System Delay and peak `0.6141 ms`, IR start
  `0.5208 ms`, timing mode `Loopback`, output L, reference input R, and clock
  adjustment `0.0 ppm`. The user observed no warning, clipping, dropout, or
  exception. This closes Gate D for UMC22 hardware, two-channel stream, routing,
  and ordinary loopback timing while leaving the combined calibration/IR-merge
  path excluded. The screenshot also records no microphone or soundcard
  calibration file. That was immaterial to this diagnostic, but the ECM8000
  calibration and a valid UMC22/electrical-reference magnitude-calibration route
  are required before any powered response becomes crossover evidence.
- Passed the final unchanged `256k` calibration-data diagnostic. With the
  headphone held by hand at approximately `150 mm`, REW stored `Soundcard:
  Loopback cal`, timing mode `Loopback as cal ref`, reference output L/input R,
  reference index `47975.52`, System Delay and peak `0.5100 ms`, IR start
  `0.4375 ms` (`150 mm`), and clock adjustment `0.0 ppm`. No warning or
  abnormality was reported. The hand-held source makes centimetre-scale inferred
  distance differences immaterial. This qualifies `Make calibration data from
  loopback response`, with IR merging excluded, as the UMC22 candidate mode for
  Gate E. Load the ECM8000 calibration before reusable acoustic capture. The raw
  qualification session is retained as
  `rew/UMC22 loopback-cal-data diagnostic.mdat` and was committed with the
  completed qualification record at the user's request.
- Recorded the first switched-off Gate E assembly report: UMC22 USB disconnected,
  phantom off, all three gain/output controls at minimum, Direct Monitor off,
  ECM8000 on Input 1, protected fixture reference on Input 2, and Output 1/L to
  SU-V570 `AUX` left; SU-V570 off at minimum volume with tone defeat, loudness
  off, centred balance, `AUX`, and bank B only. Those states pass, but power is
  held until the woofer-only load, fixture red/black polarity, breakout
  insulation, and unused headphone/output/right-input sockets are confirmed.
- Passed the complete switched-off Gate E assembly after confirming B-left
  positive to both woofer positive and fixture `In+`, B-left negative to both
  woofer negative and fixture `In-`, no other load, insulated/restrained
  breakout, and empty UMC22 headphone, Output 2, and SU-V570 AUX-right sockets.
  At that checkpoint the UMC22-only USB/phantom no-signal observation was next
  and SU-V570 power remained held.
- Passed the UMC22-only USB/phantom no-signal observation with the complete
  assembly unchanged and the SU-V570 off at minimum volume. The phantom
  indicator illuminated; neither channel showed a clip indication; and there
  was no unexpected sound, instability, heating, smell, or other abnormality.
  At that checkpoint minimum-volume SU-V570 no-signal power-up was next and
  signal generation remained held.
- Passed the SU-V570 minimum-volume no-signal power-up. With the documented
  controls and wiring retained and every REW signal stopped, the amplifier was
  powered for approximately one minute. The woofer remained silent, neither
  UMC22 channel clipped, and there was no transient or persistent hum/buzz,
  instability, heating, smell, smoke, or other abnormality. The controlled
  woofer/reference voltage check was next; no acoustic sweep was approved.
- Passed the controlled woofer-voltage target with `1.0000 V AC` indicated on
  the Agilent U1282A at the SU-V570's `-38 dB` scale mark. Generator was then
  stopped and the system was silent. The scale mark is only a setup landmark;
  future restoration still requires the meter.
- Passed the gross protected-reference voltage at a stable `98.53 mV AC`
  tip-to-ring with the same level controls. The measured transfer is `0.09853`
  (`-20.129 dB`), only `-0.39%` (`-0.034 dB`) from the resistance-derived
  `0.09892`. Generator was stopped; neither UMC22 channel clipped; and there
  was no dropout, instability, or other abnormality.
- Passed the final direct-reference no-signal state after removing the
  breakout, connecting the fixture directly to `INST 2`, and returning the
  U1282A to the woofer. The specified configuration was confirmed and no
  abnormality was reported after SU-V570 power-up.
- Passed final reference-input gain setting at a stable `Ref In` RMS level of
  `-20.87 dBFS`, fluctuating by approximately `+/-0.01 dB`, with `GAIN 2` near
  2 o'clock and U1282A woofer voltage stable at `1.0003 V AC`. At least `6 dB`
  peak headroom was confirmed; no numeric peak value was recorded. Neither
  channel clipped, and there was no dropout or other anomaly. Generator was
  stopped.
- Identified `calibration/ECM8000_calibration_data.csv` as a generic
  `0-degree` ECM8000 response with `124` strictly ascending rows from `20` to
  `21999 Hz`, frequency-response values from `-4.920` to `+1.015 dB`, and a
  phase column. The as-supplied SHA-256 was
  `c64553a2ff0e2f2799bf1bd8a275ea649c3a1aae7ff2dd39fba1b572953b4d6d`.
  Because its commas lacked REW's documented following whitespace, spaces were
  added after the commas without changing any numeric value. The retained,
  directly REW-compatible CSV now has SHA-256
  `bb8fba5b6ae58b5a84d4ba47807ca61d49cc291325a0c3b43fae7294407c5e23`;
  the redundant `.cal` derivative was removed at the user's request. The file
  is generic rather than unit-specific and contains no microphone sensitivity;
  it may improve nominal response correction but does not establish calibrated
  absolute SPL or unit-specific magnitude/phase accuracy.
- Recorded the user-reported initial acoustic geometry: microphone tip
  `1000 mm` from the baffle plane, microphone aimed normally at the cabinet,
  capsule level with the woofer centre and horizontally centred on the baffle.
  The loudspeaker is on a sturdy-table jig that rotates about the horizontal
  centre of the baffle plane and is marked at 10-degree increments. The
  microphone orientation matches the generic `0-degree` file.
- Passed the calibration parser and per-channel assignment check using the
  pre-consolidation derivative: REW displayed no warning, and closing and
  reopening Preferences showed the file persisted only for the left channel of
  the exact `EXCL:` UMC22 input while its right channel showed `None`. Because
  the user's requested consolidation then removed that derivative, reselect the
  retained CSV on input L and reconfirm persistence before setting `GAIN 1`;
  no acoustic sweep is yet approved.
- Passed canonical-file assignment: after selecting the retained
  `calibration/ECM8000_calibration_data.csv`, closing and reopening Preferences
  showed that the new filename persisted for the left channel only of the exact
  `EXCL:` UMC22 microphone input; the right channel remained `None`. Set
  microphone `GAIN 1` with the bounded Check Levels observation next; no
  measurement sweep is yet approved.
- Passed microphone Check Levels with `GAIN 1` approximately 4 o'clock. The
  Levels tool showed main `In` near `-15.5 dBFS` and `Ref In` near
  `-33.8 dBFS`, each moving by less than approximately `+/-1 dB`. Neither UMC22
  clip indicator illuminated, and there was no dropout or other anomaly. The
  main level lies within REW's documented acceptable `-30` to `-12 dBFS` RMS
  range for an analogue microphone/preamp input. Retain `GAIN 1` and the
  previously qualified `GAIN 2`; do not raise the latter to match the pink-noise
  reading because the direct `1 kHz` reference was already established at
  `-20.87 dBFS`, and REW uses the loopback's 1 kHz level as its calibration
  reference. One `256k` acoustic checkout is approved next; reusable repeats
  remain held pending its review.
- **SUPERSEDING ACOUSTIC-CHECKOUT RESULT:** the first `256k`, `20-20000 Hz`,
  `-10 dBFS` powered woofer sweep raised a distortion warning and indicated
  inadequate headroom. The user stopped progressing and repeated at
  `-20 dBFS`; that suppressed the warning, but the Measure dialog still showed
  minimum headroom of approximately `3.8 dB` (the limiting channel was not
  captured). No hardware clip, dropout, or other abnormality occurred.
- Screenshot review establishes that the `-20 dBFS` repeat is useful only as a
  diagnostic. It used REW V5.40 beta 133, exact UMC22 input L, output L,
  reference output L/input R, `48 kHz`, one `256k` sweep, and loopback as
  calibration/timing reference. `Soundcard: Loopback cal`, reference index
  `47850.03`, System Delay `3.1243 ms`, peak `3.1243 ms`, IR start `3.0000 ms`,
  SNR `43.8 dB`, and signal-to-distortion `23.1 dB` were stored. The impulse has
  one clear dominant arrival and the magnitude is grossly woofer-like rather
  than self-referenced/flat.
- **CALIBRATION-APPLICATION CORRECTION:** the same Info panel states
  `Mic: No cal file`. The Cal files screenshot shows the CSV persisted for the
  exact device's `Default Input`, whereas Soundcard and measurement metadata use
  `MICROPHONE (Master Volume), L`. The earlier persistence result therefore
  proves REW retained a per-channel preference but not that it applied to the
  active measurement source. No acoustic magnitude from either sweep is
  reusable. At that checkpoint signals were stopped pending association of the
  CSV with the exact active input selector.
- Passed the corrected active-source Preferences association with all signals
  stopped. Soundcard shows exact input device
  `EXCL: Behringer UMC22 (USB Audio CODEC)`, selector
  `MICROPHONE (Master Volume)`, and channel L. The ECM8000 CSV is assigned to
  that specific input on L only and persists across Preferences close/reopen.
  This passed the Preferences half of the correction while signal remained
  held.
- Passed the pending-measurement calibration check. Measure's Calibration data
  display identifies the UMC22 `MICROPHONE (Master Volume)` source and names
  `ECM8000_calibration_data.csv` under Mic calibration files for L. The pending
  measurement explicitly uses that source's L channel, while its electrical
  timing-reference input is R. REW did not show a separate microphone-
  calibration row for R in this view. The next bounded step is `-20 dBFS`
  Check Levels with only `GAIN 1` reduced enough to lower the main indication
  by approximately `4 dB`; this predicts about `7.8 dB` sweep headroom but does
  not establish it until a subsequent sweep.
- Passed the controlled microphone-gain correction. At `-20 dBFS`
  Check Levels, reducing only `GAIN 1` moved main `In` from approximately
  `-15.5` to `-19.3 dBFS`, a `3.8 dB` change. The knob moved only a few degrees
  and is still approximately at 4 o'clock. This predicts about `7.6 dB` minimum
  sweep headroom. `Ref In` was stable at `-33.58 dBFS` with `+/-0.01 dB`
  fluctuation; there was no warning, clipping, dropout, or other abnormality.
  The gain correction therefore passes, and one calibrated `-20 dBFS` sweep is
  approved to verify actual headroom and the stored microphone-calibration
  entry.
- The calibrated `-20 dBFS` headroom checkout completed without warning or
  anomaly, but its direct Measure display showed only `3.6 dB` main-input
  headroom in red versus `32.9 dB` reference headroom in green. The microphone
  path remains the sole limiter and the earlier `7.6 dB` prediction is
  superseded. The broadband Check Levels adjustment did not predict the sweep's
  narrow worst-case peak. Measurement Info confirms the ECM8000 CSV, loopback
  calibration, exact routing, timing-reference index `47849.89`, System Delay
  `3.1273 ms`, SNR `44.4 dB`, and signal-to-distortion `34.3 dB`. The user
  located the highest response peak at `6.07 kHz`.
- Passed the targeted worst-case gain setting. With a `6070 Hz`, `-20 dBFS`
  sine, reducing only `GAIN 1` to approximately 2 o'clock moved main-input peak
  from about `-2` to `-10.3 dBFS`, an `8.3 dB` reduction. No equipment or
  signal abnormality occurred. The prior full sweep's `32.9 dB` reference
  headroom remains applicable because `GAIN 2` and the output path are
  unchanged. One final calibrated headroom-verification sweep was approved.
- Passed the final calibrated headroom checkout. Highest displayed levels were
  main `-10.7 dBFS` and reference `-33 dBFS`, both green, and no warning or
  abnormality occurred. Measurement Info confirms
  `Mic: ECM8000_calibration_data.csv`, `Soundcard: Loopback cal`, exact L/L/R
  routing, timing-reference index `47849.96`, System Delay and IR peak
  `3.1257 ms`, IR start `3.0000 ms`, SNR `43.5 dB`, signal-to-distortion
  `62.5 dB`, and clock adjustment `0.0 ppm`. This final-settings capture is
  repeatability run 1; make only identical runs 2 and 3 before review.
- Passed repeatability-run metadata and delay. Runs 2 and 3 retain the mic CSV,
  loopback calibration, exact route, `48 kHz`, `3.0000 ms` IR start, and
  `0.0 ppm` clock adjustment. System Delays are `3.1257`, `3.1267`, and
  `3.1264 ms`, giving a `1.0 us` total spread against the preferred `5 us`
  maximum. SNR is `43.5`, `44.3`, and `44.3 dB`; signal-to-distortion is
  `62.5`, `60.2`, and `64.0 dB`.
- Retained the unique raw repeatability session as
  `rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat`, `19138881` bytes,
  SHA-256 `b47e6aca826a4a95d77dfcab731edac95c2c6bf21be56f8bf249fcf23bd5e3c1`.
  It was committed with the completed qualification record at the user's
  request and must not be deleted or ignored.
- Extracted the saved session successfully through REW's API with no manifest
  warning, `None` smoothing, and a common native grid. The initial `1-5 kHz`
  pointwise comparison fails under the stored `311.9167 ms` left and `500 ms`
  right default IR windows: magnitude range median `1.056 dB`, 95th percentile
  `4.354 dB`, maximum `32.364 dB`; circular phase range median
  `7.045 degrees`, 95th percentile `33.742 degrees`, maximum
  `179.819 degrees`. The worst magnitude point is a narrow `1339.23 Hz` null,
  while IR peak amplitudes differ by only `0.037 dB`. This is provisionally
  attributed to room-reflection cancellation, not promoted to a hardware
  failure.
- Confirmed that repeatability runs 2 and 3 stayed green throughout with no
  warning, clipping, dropout, or other abnormality.
- Extracted the three final-setting raw impulses by explicit UUID through the
  REW API client: measurement IDs `22`/`23`/`24`, `131072` samples each at
  `48 kHz`, no manifest warnings, and source hash/size matching the retained
  `.mdat`.
- **SUPERSEDING UMC22 REPEATABILITY DECISION - PASS:** applying the same derived
  `2.0 ms` left / `1.0 ms` right direct window relative to each impulse peak,
  with raised-cosine tapers over the outer halves, gives `1-5 kHz` magnitude
  spread median `0.0635 dB`, 95th percentile `0.0736 dB`, maximum
  `0.0743 dB`, and circular phase spread median `0.994 degrees`, 95th percentile
  `1.815 degrees`, maximum `1.931 degrees`. At `2.3 kHz`, the corresponding
  spreads are `0.0735 dB` and `0.697 degrees`. The full-length FFT preserved
  each impulse's time origin and the `1.0 us` measured delay spread. Gate E and
  the controlled installed-woofer FRD route pass.
- **LIMITATION:** the `3.0 ms` total derived window has approximately `333 Hz`
  nominal resolution. It is adequate for the `1-5 kHz` qualification and
  `2.2-2.4 kHz` crossover region, but it neither modifies the raw `.mdat` nor
  establishes the final REW-native production window. Generic microphone-
  calibration and uncalibrated absolute SPL also remain attached to subsequent
  woofer data. Raw-tweeter and polar work are not released by this result.
