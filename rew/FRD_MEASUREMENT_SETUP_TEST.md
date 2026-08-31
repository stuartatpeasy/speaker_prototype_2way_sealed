# FRD Measurement Setup Repeatability Test - UMC202HD

Date prepared: 2026-08-30

Last revised: 2026-08-31

Status: provisional setup-validation procedure, revised for the Behringer
UMC202HD. This procedure validates the woofer measurement chain. It is not yet
the full polar procedure and must not be used for an unprotected tweeter sweep.

## 1. Purpose

Use three repeated, unmoved woofer measurements to establish whether the
UMC202HD, ECM8000, Technics SU-V570, REW, protected electrical reference, and
room setup provide repeatable magnitude, phase, and timing around the intended
crossover region.

Pass criteria over 1-5 kHz:

- magnitude spread no greater than approximately 0.2 dB;
- system-delay spread preferably no greater than 5 us;
- phase traces nearly coincident, with no unexplained jumps or drift;
- no clipping indication on either REW input.

Passing this test permits the same measurement chain to be used for the first
installed-driver FRD measurements. Tweeter protection and sweep limits remain a
separate prerequisite.

## 2. Chosen Reference Topology

The preferred UMC202HD arrangement is a full-dual-channel acoustic measurement:

- Input 1 records the ECM8000 microphone;
- Input 2 records a protected, attenuated sample of the voltage at the driver
  terminals;
- Output 1 drives the Technics line input;
- Output 2 is not part of the analogue measurement path.

The reference is therefore taken after the DAC, amplifier, volume control, and
speaker cable. REW measures acoustic output relative to the voltage actually
applied to the driver, while also obtaining a common timing reference.

Use REW's `Use loopback as cal and timing reference` mode with `Merge loopback
response into IR` enabled. This is different from the earlier UMC22 procedure,
which used Output 2 directly looped to Input 2 for timing only.

### 2.1 Safe fallback

If the protected divider has not passed its commissioning checks, or the
Technics output topology has not been verified, do not connect either speaker
terminal to the UMC202HD. Temporarily use the semi-dual connection instead:

```text
UMC202HD Output 2 -> UMC202HD Input 2, set to LINE
```

For that fallback, select `Use loopback as timing reference`. It provides valid
common timing but leaves the amplifier response in the acoustic measurement.
Do not mix semi-dual and full-dual data in one final driver set without first
showing that the two arrangements produce equivalent results.

## 3. UMC202HD Signal-Path Reference

The UMC202HD provides two independent USB capture channels, two independent USB
playback channels, and two similar microphone/line input stages.

### 3.1 Front and rear controls

- `INPUT 1` and `INPUT 2` are separate USB capture channels.
- `GAIN 1` and `GAIN 2` control their respective input stages independently.
- The `LINE/INST` selector for Input 2 must be set to `LINE` when accepting the
  electrical reference through a 1/4-inch TRS plug.
- Start with both `PAD` switches disengaged. Reduce gain before engaging a pad.
- `OUTPUT` controls the two rear line outputs together.
- `PHONES` controls only the headphone output.
- Keep `DIRECT MONITOR` OFF. It is unnecessary and could create feedback during
  commissioning.
- The rear `+48 V` switch supplies phantom power for the ECM8000 through its XLR
  connection. Connect the microphone before enabling phantom power.
- Connect the electrical reference to Input 2 by TRS, never by XLR.

### 3.2 Channel assignments

| UMC202HD channel | Assignment |
| --- | --- |
| Input 1 / USB input L | ECM8000 measurement microphone |
| Input 2 / USB input R | Protected driver-terminal reference |
| Output 1 / USB output L | Technics amplifier and driver under test |
| Output 2 / USB output R | Unconnected during full-dual measurement |

## 4. Protected Driver-Terminal Divider

Never connect a speaker output directly to either UMC202HD input. Behringer
specifies a maximum line-input level of +20 dBu, approximately 7.75 V RMS. That
is a measurement headroom specification, not a safe fault limit.

Use a fixed, enclosed, approximately 20 dB divider with a balanced TRS output.
The following provisional network attenuates both speaker terminals relative to
the interface reference ground rather than hard-grounding either terminal:

```text
Driver + ---- 9.1 kohm, 0.5 W ----+---- TRS tip
                                  |
                               1.0 kohm
                                  |
Reference ground -----------------+---- TRS sleeve

Driver - ---- 9.1 kohm, 0.5 W ----+---- TRS ring
                                  |
                               1.0 kohm
                                  |
Reference ground -----------------+---- TRS sleeve
```

Use 1% metal-film resistors. Add a bidirectional voltage clamp from tip to
sleeve and another from ring to sleeve. Each clamp must remain inactive at the
normal reference level but limit its node to less than approximately 5 V peak.
A provisional implementation is two 3.3 V low-power zener diodes connected in
series opposition for each clamp. Verify the finished divider by measurement;
do not assume its attenuation or high-frequency response from nominal values.

For either leg, ignoring UMC202HD loading:

```text
k = 1.0 / (9.1 + 1.0) = 0.0990
attenuation = 20 log10(k) = -20.09 dB
```

Therefore 1.00 V RMS at the driver produces approximately 99 mV RMS at the
reference input. A hypothetical 28.3 V RMS amplifier output produces about
2.80 V RMS, still below the published line-input maximum. At 28.3 V RMS, the
resistor dissipation in a driven leg is only about 79 mW in total; 0.5 W parts
provide ample normal margin.

Construction requirements:

- use an insulated enclosure or insulated terminals in a metal enclosure;
- provide strain relief and fully cover all live solder joints;
- connect the divider input in parallel with the driver at the driver terminals;
- use a shielded TRS cable from the divider to UMC202HD Input 2;
- label input, output, and ground connections permanently;
- complete the unpowered checks in
  [`SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md`](SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md)
  before connecting the divider. If the output is bridged, floating, or
  otherwise unsuitable for a ground-referenced high-value divider, use the
  semi-dual fallback until a suitable isolated reference is designed.

## 5. Known Measurement Geometry

Nominal values:

- microphone distance from the baffle-plane reference point: 1000 mm;
- preferred microphone and woofer-centre height: 1040 mm;
- room height: 2080 mm;
- cabinet reference point to wall behind cabinet: 670 mm;
- microphone to wall behind microphone: 970 mm;
- source/microphone line to nearest side wall: 1530 mm.

At 1040 mm height, the first calculated floor and ceiling reflections arrive at
approximately 3.81 ms. The wall behind the cabinet follows at approximately
3.91 ms. Begin with a right IR window of 3.5-3.7 ms, then use the measured ETC to
place the window before the actual first reflection.

If the setup remains at 950 mm height, the floor reflection is calculated at
3.34 ms. Begin with a right IR window of 3.0-3.2 ms instead.

## 6. Equipment And Cabling

Required:

- Behringer ECM8000 microphone and XLR cable;
- Behringer U-Phoria UMC202HD and USB cable;
- current Behringer Windows driver for the UMC202HD;
- suitable cable from UMC202HD Output 1 (L) to a Technics line input;
- commissioned protected divider from Section 4 and a balanced TRS cable;
- short TRS patch cable for electronic commissioning only;
- Technics SU-V570 amplifier;
- loudspeaker cable from one Technics speaker channel to the installed woofer;
- true-RMS voltmeter suitable at 1 kHz;
- microphone stand, tape or laser measure, and cabinet support;
- PC running REW.

Do not use the headphone output to drive either loudspeaker.

## 7. Install And Configure The UMC202HD

1. Install the current UMC202HD Windows driver from Behringer.
2. Connect the UMC202HD directly to a reliable USB port.
3. In REW select the manufacturer's ASIO driver, not the old UMC22 endpoint or
   a generic shared-mode Windows device.
4. Select 24-bit operation and a sample rate of 88.2 kHz.
5. Confirm that REW exposes two inputs and two outputs independently.
6. Prevent Windows and other applications from sending notifications or other
   audio to the UMC202HD during the test.
7. Clear any soundcard calibration file made for the UMC22. It is not valid for
   the UMC202HD or for a different sample rate.
8. Load the ECM8000 calibration file for Input 1, if one is available.

The 88.2 kHz rate supports a nearly full-band 5 Hz to 41 kHz sweep for clean
loopback-response merging. It does not improve the low-frequency resolution of
the short reflection-free window; that resolution remains set mainly by the
window duration. There is no useful reason to use 176.4 or 192 kHz here.

## 8. Commission The Electrical Channels And Divider

Perform this section before connecting the Technics speaker output.

1. Set `DIRECT MONITOR` OFF, both pads OFF, both gains fully down, and `OUTPUT`
   fully down.
2. Set Input 2 to `LINE`.
3. Connect Output 2 directly to Input 2 with the short TRS patch cable.
4. Set a low digital level, raise `OUTPUT` to maximum, and raise `GAIN 2` only
   enough to obtain a clean direct-loopback trace without clipping.
5. In REW, make and save a 5 Hz to 41 kHz direct-loopback measurement at
   88.2 kHz. Confirm that output R appears only on input R, without dropout.
6. Stop the signal and disconnect the direct patch cable without changing
   `OUTPUT`, `GAIN 2`, the digital level, or the measurement settings.
7. Feed the same Output 2 signal through the divider and connect the divider's
   TRS output to Input 2.
8. Repeat the measurement. Relative to the direct trace it should be close to
   20 dB lower, with smooth magnitude, stable phase, and correct polarity.
9. Increase the test level carefully until the divider output approaches its
   intended approximately 100 mV RMS operating level. Confirm that the clamp is
   inactive and the response remains linear.
10. Record the measured attenuation at 1 kHz and save both traces together.
11. Verify the divider ratio with a true-RMS voltmeter before exposing it to an
   amplifier output.

Stop here if channel identity, polarity, attenuation, or frequency response is
not as expected.

## 9. Safety And Initial Acoustic-Test State

1. Switch the Technics off and turn its volume fully down.
2. Set UMC202HD `OUTPUT`, `GAIN 1`, and `GAIN 2` fully down.
3. Set both inputs to `LINE`, both pads OFF, and `DIRECT MONITOR` OFF. Input 1's
   line/instrument choice is irrelevant to its XLR microphone connection.
4. Set phantom power OFF while connecting the microphone.
5. Connect only the woofer to the selected Technics speaker output.
6. Leave the tweeter electrically disconnected.
7. Select only one Technics speaker bank, A or B, not both.
8. Disable loudness and tone processing, or use Power Amp Direct if appropriate.
9. Confirm the protected divider passed Section 8 and that the Technics output
   is suitable for the connection before proceeding.

## 10. Cable The Full-Dual Acoustic System

1. Connect the ECM8000 to UMC202HD Input 1 by XLR.
2. Connect UMC202HD Output 1 (L) to one Technics line input channel.
3. Connect the matching Technics speaker output channel to the woofer.
4. Connect the divider input across the woofer terminals, in parallel with the
   woofer and voltmeter.
5. Connect the divider's balanced TRS output to UMC202HD Input 2.
6. Leave UMC202HD Output 2 physically unconnected.
7. Connect the UMC202HD to the PC and enable +48 V phantom power.
8. Recheck that Input 2 is in `LINE` mode and `DIRECT MONITOR` remains OFF.

Signal paths:

```text
ECM8000 -> UMC202HD Input 1 / USB input L -> REW measurement input

REW output L -> UMC202HD Output 1 -> Technics -> woofer

Woofer terminals -> protected divider -> UMC202HD Input 2 / USB input R
                                      -> REW cal and timing reference
```

## 11. Position The Loudspeaker And Microphone

1. Put the microphone capsule 1000 mm from the baffle-plane reference point.
2. If practical, set the microphone capsule and woofer centre to 1040 mm above
   the floor. Raise the cabinet rather than changing microphone position between
   later driver batches.
3. Aim the microphone according to the orientation required by its calibration
   file. If no calibration file exists, record that fact in the results.
4. Keep the woofer centre, microphone capsule, and baffle reference point on one
   line for the zero-degree measurement.
5. Do not move the cabinet, microphone, stands, cables, or nearby objects between
   the three repeat measurements.

## 12. Configure REW For The Acoustic Test

Use these initial settings:

| Setting | Value |
| --- | --- |
| Driver | Behringer UMC ASIO driver |
| Sample format | 24 bit |
| Sample rate | 88.2 kHz |
| Measurement input | UMC202HD input L / Input 1 |
| Measurement output | UMC202HD output L / Output 1 |
| Reference input | UMC202HD input R / Input 2 |
| Reference output | UMC202HD output R / Output 2 |
| Timing mode | Use loopback as cal and timing reference |
| Merge loopback response into IR | Enabled |
| Separate soundcard calibration file | None |
| Timing offset | 2.915 ms for 1000 mm at 343 m/s |
| Sweep range | 5 Hz to 41 kHz |
| Sweep level | -20 dBFS initially; -10 dBFS after voltage setting |
| Sweep length | 1M |
| Repetitions | 1 |
| Abort if heavy input clipping occurs | Enabled |

REW sends the same sweep to the measurement and reference outputs when a
loopback reference is selected. Output 2 remains physically unconnected in this
full-dual arrangement; Input 2 receives the reference from the amplifier-driven
woofer terminals instead.

The timing offset removes the nominal 1000 mm propagation time while retaining
the driver's real acoustic delay relative to the baffle reference plane. Do not
independently align the woofer and tweeter impulse peaks later.

## 13. Establish 1.00 V RMS At The Woofer

1. Leave the Technics volume fully down.
2. With the Technics still off, set the UMC202HD `OUTPUT` fully clockwise. This
   gives a repeatable setting and keeps the interface output stage well above
   its noise floor; the Technics volume will set the driver voltage.
3. In REW Generator, select a 1 kHz sine wave, output L, at -10 dBFS.
4. Put the voltmeter across the woofer terminals.
5. Start the generator.
6. Switch on the Technics and select the intended input and speaker bank.
7. Slowly raise the Technics volume until the meter reads 1.00 V RMS.
8. Stop the generator immediately.
9. Confirm that the divider output is approximately 99 mV RMS and is not clipped.
10. Mark the Technics volume position with removable tape.
11. Do not move the UMC202HD `OUTPUT` or Technics volume for the remainder of the
    measurement series.

The divider reference is not a substitute for the true-RMS meter when setting
the absolute driver voltage. Its exact attenuation is removed by REW's reference
normalisation, but the target voltage must still be established independently.

## 14. Set Measurement And Reference Input Levels

1. Open REW's measurement dialog with the settings from Section 12.
2. Run `Check Levels`.
3. Raise `GAIN 1` only as needed for a clean microphone signal with comfortable
   headroom. Aim initially for peaks around -12 to -18 dBFS.
4. Raise `GAIN 2` from minimum until the electrical reference is detected
   reliably with at least 6 dB headroom. Do not engage the pad unless minimum
   gain still leaves insufficient headroom.
5. Confirm that neither input clips and both front-panel `CLIP` LEDs remain off.
6. Do not alter either gain after this point.

Absolute SPL calibration is not required for this repeatability test. When the
SL-200 is available, calibrate REW with the meter on C weighting, SLOW response,
and its appropriate range, without changing `GAIN 1` afterward.

## 15. Capture Three Repeats

1. Name the first measurement `SB17 UMC202HD repeat 1`.
2. Run one sweep and note REW's reported System Delay.
3. Without moving or touching anything, repeat as `SB17 UMC202HD repeat 2`.
4. Repeat once more as `SB17 UMC202HD repeat 3`.
5. Save all three measurements together as:

   `rew/SB17NRX2C35-8_UMC202HD_full_dual_repeatability.mdat`

## 16. Apply A Common IR Window

1. Select the first measurement and inspect its Impulse and ETC views.
2. Locate the actual first reflection rather than relying only on calculation.
3. Use a 2.0 ms left window with Tukey 0.5 as an initial setting.
4. End the right window immediately before the first reflection:
   - start at 3.5-3.7 ms if measuring at 1040 mm height;
   - start at 3.0-3.2 ms if measuring at 950 mm height.
5. Apply exactly the same IR windows to all three measurements.
6. Save the `.mdat` file again after windowing.

## 17. Evaluate Repeatability

1. Overlay all three magnitude traces over 1-5 kHz.
2. Use identical smoothing for all traces; 1/24 octave or no smoothing is
   suitable for the comparison.
3. Overlay phase and confirm that the traces nearly coincide.
4. Record the System Delay shown for each measurement.
5. Calculate delay spread as maximum delay minus minimum delay.
6. At 2.3 kHz, a 5 us timing difference corresponds to approximately 4.1 degrees:

   `360 x 2300 x 5e-6 = 4.14 degrees`

7. Record the largest visible magnitude separation over 1-5 kHz.

Results:

| Run | System Delay (ms) | Difference from Run 1 (us) | Notes |
| --- | ---: | ---: | --- |
| 1 |  | 0 |  |
| 2 |  |  |  |
| 3 |  |  |  |

| Check | Result | Pass target |
| --- | --- | --- |
| Delay spread |  | Preferably no more than 5 us |
| Magnitude spread, 1-5 kHz |  | No more than about 0.2 dB |
| Phase overlay |  | Nearly coincident |
| Microphone clipping |  | None |
| Reference clipping/dropout |  | None |

## 18. If The Test Fails

Check, in this order:

1. `DIRECT MONITOR` is OFF.
2. REW has input L assigned to the microphone and input R to the reference.
3. Input 2 is in `LINE` mode and the divider polarity is correct.
4. `Use loopback as cal and timing reference` and `Merge loopback response into
   IR` are both selected.
5. Both input traces have adequate level and neither is clipping.
6. Sample rate, ASIO device, and channel selections did not change.
7. UMC202HD output, both input gains, and Technics volume did not move.
8. The microphone, cabinet, divider, cable, or stand did not move.
9. The divider has the expected attenuation and a smooth 5 Hz to 41 kHz response.
10. The impulse response does not contain multiple comparable peaks caused by a
    synchronisation or sweep problem.
11. Repeat with a 512k single sweep if acoustic noise or the long sweep caused a
    problem.
12. Repeat once with the safe semi-dual connection. If semi-dual is repeatable
    but full-dual is not, investigate the divider and amplifier reference path.

## 19. Deferred Work

Do not proceed to the raw tweeter, full polar series, near-field merge, or final
FRD export until this repeatability test passes. The tweeter measurement requires
a separately agreed sweep range, voltage, and protective high-pass component.

## 20. Primary References

- SU-V570 schematic assessment and external verification record:
  [`SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md`](SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md)
- Behringer UMC202HD product information and quick-start guide:
  <https://www.behringer.com/en/products/0805-AAR>
- REW measurement and loopback-reference documentation:
  <https://www.roomeqwizard.com/help/help_en-GB/html/makingmeasurements.html>
- VituixCAD measurement guide for REW:
  <https://kimmosaunisto.net/Software/VituixCAD/VituixCAD_Measurement_REW.pdf>
