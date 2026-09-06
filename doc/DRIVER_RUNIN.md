# Driver Run-in and Stabilisation Procedure

| State | Value |
| --- | --- |
| Lifecycle | **CURRENT PROCEDURE** |
| Owns | Conditioning, cooldown, controlled impedance checks, and repeat/stop rules |
| Does not own | Approved driver baselines, derived parameters, or retention decisions |
| Applies to | SB Acoustics SB17NRX2C35-8 woofer and SB26STWGC-4 tweeter in the sealed prototype cabinet |
| Current evidence authority | [Driver analysis](DRIVER_ANALYSIS.md) |
| Established | 2026-08-31 |

This procedure is intended to reach a reproducible, cooled measurement state before alignment and crossover work. It is not a target-driven attempt to force either driver to match every datasheet value. Stop when the installed measurements stabilise.

## 1. General preparation

1. Mount both drivers in their normal cabinet positions using their normal gaskets and fastening method.
2. Confirm that the rear panel, connector, driver flanges, and every temporary opening are properly sealed.
3. Record the cabinet lining/fill state and do not alter it during a run-in comparison series.
4. Place the cabinet in a stable orientation with the woofer unobstructed. Record ambient temperature and any relevant humidity information.
5. Use the same wiring, driver polarity, measurement jig, 100 Ω sense resistor, interface path, input gains, and REW settings throughout the series.
6. Calibrate the REW impedance rig at **48 kHz**. Repeat open-, short-, and reference-resistor calibration after any sample-rate, interface, gain, lead, sense-resistor, or wiring change.
7. With all equipment unpowered, measure and record the woofer's cold terminal DCR. Use the same meter, nulled leads, connection points, and driver temperature for subsequent checks.
8. Take an initial cooled 48 kHz impedance measurement if one does not already exist under exactly the intended comparison conditions.

## 2. Woofer procedure

### 2.1 Conditioning interval

1. Disconnect the tweeter electrically. Bypass and isolate any crossover so the woofer alone is connected to the conditioning amplifier.
2. Generate a **30 Hz sine wave** and begin with the amplifier level at minimum.
3. Ramp the level up while measuring directly across the woofer terminals. Set **4.00 V RMS at the speaker terminals** using a suitable true-RMS meter.
4. Confirm clean, approximately symmetric motion with no rubbing, knocking, intermittent connection, amplifier clipping, cabinet leak noise, or abnormal heating.
5. Run for **one hour**. Recheck terminal voltage after the first few minutes and after any amplifier adjustment.
6. Do not leave the test unattended. Stop immediately for abnormal mechanical noise, asymmetry, smell, excessive heating, amplifier distress, or a material change in terminal voltage.

The present linear equivalent-circuit estimate is approximately **2.6 mm peak displacement** and **1.9 W real electrical input** at 30 Hz and 4.0 V RMS in the sealed cabinet. These are estimates, not direct displacement or temperature measurements.

### 2.2 Cooldown gate

Thirty minutes is a useful first check, not an adequate standalone definition of "cold". A previous post-conditioning trace contained approximately 0.34 Ω of additional broadband series resistance, equivalent to roughly a 15 °C copper-temperature rise if entirely attributable to the voice coil.

1. Remove the conditioning signal and switch the amplifier off or disconnect it from the woofer.
2. Wait **at least 30 minutes** before the first unpowered DCR check. The default expectation is that approximately **60 minutes or more** may be required.
3. Measure DCR every 10–15 minutes without moving or remounting the driver.
4. Proceed to the REW measurement only when:
   - DCR is within **0.05 Ω or 1%**, whichever is larger, of the pre-run cold reference; and
   - two readings at least 10 minutes apart differ by no more than **0.02 Ω**; and
   - cabinet and driver are close to the original ambient condition.
5. If DCR does not return to the reference, do not reinterpret the higher resistance as a permanent driver change. Check ambient temperature, meter zero, leads, terminals, and connection resistance before continuing.

This gate controls voice-coil temperature. It does not prove that short-term viscoelastic softening of the suspension has fully recovered, so the final baseline also needs the longer rested check in Section 2.4.

If a reliable cold-DCR reference is unavailable, wait at least 60 minutes and use a repeated low-level impedance sweep only as a secondary check that the broad real-impedance offset has stabilised. Do not use repeated sweeps as a shortcut around obvious residual heating.

### 2.3 Controlled REW impedance measurement

1. Keep the driver mounting, cabinet sealing, fill, orientation, and wiring unchanged.
2. Use REW impedance mode with:
   - **48 kHz sample rate**;
   - **1M logarithmic swept sine**;
   - **one sweep at −12 dBFS**;
   - **no smoothing**;
   - **1/96-octave frequency spacing**;
   - the calibrated **100 Ω** sense resistor and the same interface gains/path as the baseline.
3. Check input headroom and confirm neither channel clips.
4. Record the actual driver-terminal sweep voltage if practicable; −12 dBFS alone is not an absolute terminal-voltage specification.
5. Save the REW source and export a ZMA under `rew/`. A suitable filename is:

   `SB17NRX2C35-8 runin 30Hz 4Vrms <cumulative-hours>h 48kHz cooled.zma`

6. Record ambient temperature, cooldown time, cold DCR, conditioning duration, terminal voltage, mounting/fill state, REW calibration state, and any observations.

### 2.4 Analysis and repeat/stop decision

Use the bandwidth-derived sealed-system resonance $F_c$, not merely the discrete frequency bin containing maximum impedance. The reproducible method is defined in [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md).

For successive **cooled, controlled 48 kHz** measurements:

$$
\Delta F_c(\%)=100\frac{F_{c,n}-F_{c,n-1}}{F_{c,n-1}}.
$$

1. If $F_c$ decreases by **1% or more**, and the trace remains otherwise healthy, perform another one-hour interval starting at Section 2.1.
2. If the magnitude of the change is **less than 1%**, do not add another conditioning hour automatically. Repeat the low-level impedance sweep after at least 10 minutes with no further drive; if the traces overlay within normal measurement scatter, stop the conditioning loop.
3. At the first stop decision—and before promoting a new crossover baseline—leave the driver unpowered for **12–24 hours** at a reasonably stable ambient temperature, recheck DCR, and repeat the 48 kHz sweep. Treat this rested result as the evidence of durable change. If it differs materially from the short-cool result, base any future run/stop comparison on similarly rested measurements.
4. Stop and investigate rather than continuing automatically if:
   - $F_c$ rises materially;
   - a second resonance, phase discontinuity, or unexpected trace-shape change appears;
   - cooled DCR does not recover;
   - rubbing, knocking, asymmetry, compression, or amplifier clipping occurs.
5. After **four total one-hour 30 Hz sine intervals**, stop the automatic loop and review the accumulated trend even if $F_c$ is still moving. Do not pursue the published 36.5 Hz value as a conditioning target.
6. Append the new measurement and conclusion to [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md). Promote a new woofer ZMA to crossover-baseline status only after the rested trace is reproducible.

## 3. Tweeter procedure

### 3.1 Default decision: no dedicated run-in

No dedicated tweeter run-in is presently required.

Reasons:

- the installed SB26STWGC-4 impedance already agrees closely with its published resonance and Q values;
- the project has no evidence that deliberate conditioning would materially improve crossover accuracy or long-term stability;
- its published **120 W** statement is conditional on an **IEC high-pass Butterworth filter at 2.6 kHz, 12 dB/octave** and is not an unconditional bare-driver or sine-wave rating;
- the tweeter has only approximately **1.2 mm peak-to-peak linear coil travel**, making unnecessary low-frequency or high-level conditioning disproportionately risky;
- normal protected acoustic measurements and later listening will provide any incidental low-level mechanical use without an objectionable sustained high-frequency tone.

### 3.2 Tweeter baseline and later check

1. Mount and seal the tweeter in its normal cabinet position.
2. Take a cooled, low-level **48 kHz, −12 dBFS** REW impedance measurement under the same calibrated-jig discipline used for the woofer.
3. Do not apply an unfiltered sine, broadband signal, or programme material directly to the bare tweeter.
4. Once a validated protective high-pass/crossover is installed, carry out normal low- and moderate-level acoustic measurements and listening checks.
5. Recheck tweeter impedance after the initial protected development/listening period only to establish whether a repeatable change occurred. If there is no material change, no further action is required.

### 3.3 Contingency only if future evidence shows drift

If repeatable cooled measurements later show that deliberate tweeter stabilisation is necessary:

1. Use the actual validated crossover or a separately verified protective high-pass meeting or exceeding the manufacturer's 2.6 kHz, 12 dB/octave test condition.
2. Use low-level broadband noise or ordinary programme material, not a sustained single-frequency tone.
3. Begin at a modest listening level and monitor filtered tweeter voltage, amplifier clipping, distortion, and heating.
4. Stop for any audible distress or unexpected impedance change.
5. Do not choose a target wattage until the complete filter transfer function and actual tweeter terminal voltage have been measured.

This contingency is not authorised by the present evidence and should not be performed merely for procedural symmetry with the woofer.

## 4. Run-in log template

| Field | Record |
|---|---|
| Date and operator | |
| Driver and serial/sample identity | |
| Cabinet and mounting state | |
| Fill/lining state | |
| Ambient temperature / humidity | |
| Pre-run cold DCR | |
| Signal / frequency | |
| Terminal voltage | |
| Conditioning duration / cumulative duration | |
| First cooldown check time and DCR | |
| Final cooldown time and DCR | |
| REW sample rate / level / sweep length | |
| Calibration status | |
| ZMA filename | |
| $Z_{max}$, peak-bin frequency | |
| Bandwidth-derived $F_c$ | |
| $Q_{mc}$, $Q_{ec}$, $Q_{tc}$ | |
| Change from previous cooled $F_c$ | |
| Noise, smell, asymmetry, or other observations | |
| Decision: repeat / confirm / stop / investigate | |

## 5. Primary references

- [SB Acoustics SB17NRX2C35-8 datasheet](https://sbacoustics.com/wp-content/uploads/2020/02/6in-SB17NRX2C35-8.pdf)
- [SB Acoustics SB26STWGC-4 datasheet](https://sbacoustics.com/wp-content/uploads/2020/05/SB26STWGC-4.pdf)
- [KLIPPEL, Mechanical Fatigue and Load-Induced Aging of Loudspeaker Suspension](https://www.klippel.de/fileadmin/klippel/Bilder/Know-How/Literature/Papers/Aging%20of%20loudspeaker%20suspension_Klippel.pdf)
- [REW impedance-measurement documentation](https://www.roomeqwizard.com/help/help_en-GB/html/impedancemeasurement.html)
