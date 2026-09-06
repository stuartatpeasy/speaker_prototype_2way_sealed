# UMC22 Installed-Woofer FRD Runbook

Lifecycle: **CURRENT PROCEDURE**
Current approved action: perform the no-excitation audit, report it for review,
then—only after authorisation—make one reusable 0-degree woofer capture and
stop for review.
Required qualification: **PASS**, recorded in
[`../qualification/UMC22_FRD_QUALIFICATION.md`](../qualification/UMC22_FRD_QUALIFICATION.md).
Do not proceed to: repeat captures, cabinet rotation, FRD export, raw-tweeter
measurement, or polar work.
Last verified state report: 2026-09-06

## 1. Scope And Risk Boundary

This procedure governs the qualified UMC22, SU-V570, protected electrical
reference, and ECM8000 route for the installed SB17 woofer only. It does not
qualify another interface, a changed fixture, the tweeter, or a polar series.

**USER DECISION — 2026-09-05:** the user accepts a known but unquantified
possibility of damage to the approximately GBP 25 UMC22 during an amplifier
fault. The normal reference level has ample nominal input margin, but the
worst amplifier-derived fixture voltage can exceed the UMC22's published
instrument-input maximum. This acceptance does not waive checks protecting the
person, SU-V570, PC, loudspeaker, or data validity. It cannot guarantee that a
destructive UMC22 failure would be perfectly contained, although the fixture's
high series resistance makes wider damage unlikely.

The qualified fixture remains mandatory. Never connect an amplifier output
directly to `INST 2`. Use the current fixture operating instructions in
[`../fixtures/REFERENCE_FIXTURE_USE.md`](../fixtures/REFERENCE_FIXTURE_USE.md).

## 2. Qualified Physical And Software State

The released signal path is:

```text
REW output L -> UMC22 Output 1 -> mapped TS-to-RCA cable
             -> SU-V570 AUX left -> speaker bank B left -> installed woofer

SU-V570 B-left terminals -> qualified clamp/attenuator -> UMC22 INST 2
ECM8000 -> UMC22 Input 1 XLR
```

The woofer and fixture are in parallel at B-left with `In+`/red on positive and
`In-`/black on negative. Headphones, Output 2, and AUX right remain empty.
`DIRECT MONITOR` is off. The ECM8000 is connected before phantom is enabled.
The microphone capsule is `1000 mm` from the baffle plane, on the woofer axis,
aimed at the cabinet to match the generic 0-degree calibration. The microphone
is fixed and the cabinet is secured on the 10-degree-marked rotation jig.

Qualified final controls/settings are:

- UMC22 `OUTPUT` fully clockwise;
- `GAIN 1` approximately 2 o'clock;
- `GAIN 2` approximately 2 o'clock;
- phantom on for the ECM8000;
- SU-V570 input `AUX`, tone `DEFEAT`, loudness off, `POWER AMP DIRECT` off;
- speaker bank B left only;
- SU-V570 volume at its documented `-38 dB` scale mark;
- Agilent U1282A across the woofer when confirming level.

**USER-REPORTED CURRENT STATE — 2026-09-06:** the user reported that the whole
system remained identical to the passed qualification, with the qualified
wiring, controls, `1000 mm` geometry, enclosure/room state, and stopped-signal
condition unchanged and no anomaly observed. This supports staging the
no-excitation audit. It is not a fresh electrical or acoustic measurement.

If any cable, control, power state, geometry, enclosure state, or nearby
reflective object has changed since that report, stop and report the current
state. Do not assume that the earlier report covers a changed setup.

## 3. Cold Connection And Startup

Use this section after any disconnection, uncertain state, or deliberate cold
restart. If the qualified assembly is genuinely unchanged and already powered,
do not disturb it merely to repeat commissioning; proceed to Section 4.

1. Stop REW Generator, Check Levels, and Measure; stop all other application
   audio. Switch the SU-V570 off and set its volume fully down. Disconnect UMC22
   USB and turn phantom off.
2. Inspect the fixture, plugs, strain relief, insulation, and cable restraint.
   Stop for exposed conductors, loose terminals, damaged insulation, heat
   damage, or an altered component/cable.
3. Set UMC22 `OUTPUT`, `GAIN 1`, and `GAIN 2` fully down and `DIRECT MONITOR`
   off. Leave Output 2 and headphones empty.
4. Connect Output 1 through the passed TS-to-RCA cable to SU-V570 `AUX` left.
   Keep AUX right empty. Select tone `DEFEAT`, loudness off, and `POWER AMP
   DIRECT` off.
5. Connect only the installed woofer to speaker bank B left. At the same
   terminals connect fixture red/`In+` to positive and black/`In-` to negative.
   Connect the fixture output directly to `INST 2`; do not retain a breakout in
   the measurement path.
6. Connect the ECM8000 to Input 1 by XLR. Connect USB, then enable phantom.
   Confirm the phantom indicator is normal, neither channel clips, and there is
   no sound, instability, heating, or smell.
7. With the generator still stopped, power the SU-V570 at minimum volume.
   Confirm the woofer remains silent and there is no transient or persistent
   hum/buzz, clipping, instability, heating, smell, or smoke.
8. Restore only the qualified control positions listed in Section 2. If level
   must be re-established, use a `1 kHz`, output-L tone at the qualified source
   setting and raise amplifier volume slowly to `1.00 V RMS` across the woofer;
   stop the tone immediately. Do not infer broadband voltage from a changing
   meter indication during a sweep.

The historical gross protected-reference result was `98.53 mV AC` at
`1.0000 V AC` woofer voltage. Repeating it is unnecessary unless the fixture,
cable, or level path changed. If repeated through a restrained breakout, accept
only `80-120 mV RMS`; stop the tone before touching the connection and restore
the direct fixture-to-`INST 2` path afterward.

## 4. Mandatory No-Excitation Audit

Do not generate a signal during this section. Report every displayed item and
any discrepancy before a capture is authorised.

1. Confirm Generator, Check Levels, and Measure are stopped and no other
   application audio is active.
2. Confirm REW `V5.40 beta 133` and Java `Stereo only`.
3. Confirm both input and output are the exact exclusive endpoint
   `EXCL: Behringer UMC22 (USB Audio CODEC)` and sample rate is `48 kHz`.
4. Confirm input-volume scaling is `1.00` and no separate soundcard-calibration
   file is loaded.
5. Confirm the complete channel matrix:

   | Role | Selection |
   | --- | --- |
   | Measurement output | L |
   | Timing-reference output | L |
   | Measurement input | `MICROPHONE (Master Volume) L` |
   | Reference input | `MICROPHONE (Master Volume) R` |

   This is `L/L/L/R`. Reference output R is invalid because physical Output 2
   is empty; reference input L would self-reference the microphone channel.
6. Confirm `Use loopback as cal and timing reference` and `Make calibration
   data from loopback response`.
7. Confirm `Merge loopback response into IR` is **off** and timing offset is
   `0.0000 ms`.
8. In Measure's Calibration data display, confirm
   `ECM8000_calibration_data.csv` for the exact active measurement input L.
   Confirm the electrical reference input R has no microphone calibration.
   A file shown only against `Default Input` does not pass this check.
9. Confirm both UMC22 clip indicators are off and the idle system is silent,
   stable, and free of new heat, smell, or other abnormality.
10. Prepare—but do not start—one SPL sweep:

   | Field | Required value |
   | --- | --- |
   | Name | `SB17 installed 0deg 1000mm UMC22 2026-09-06 capture 1` |
   | Range | `20-20000 Hz` |
   | Level | `-20 dBFS` |
   | Length | `256k` |
   | Repetitions | `1` |
   | Clipping abort | enabled |

Stop at this gate and report the complete audit. A prepared dialog is not
authorisation to run it.

## 5. One-Capture Gate

After the no-excitation audit has been reviewed and the single capture is
explicitly authorised:

1. Reconfirm that no setting, control, wiring, or physical position changed.
2. Run exactly the prepared sweep while watching both input levels and the
   hardware clip indicators.
3. Stop immediately for a clipping or distortion warning, hardware clip,
   severe rubbing/buzzing, dropout, instability, unusual heating, smell, smoke,
   perceptible tingle, spark, or any other abnormality.
4. After the sweep, generate nothing further and change no control or position.
5. Record both input headrooms, every warning/anomaly, and Measurement Info:
   microphone calibration, soundcard calibration, input/output routing,
   timing-reference index, System Delay, IR start, timing offset, clock
   adjustment, SNR, and signal-to-distortion.
6. Inspect and retain the direct impulse and ETC. Identify the first material
   reflection and propose a REW-native left/right window under
   [`../FRD_MEASUREMENT_METHOD.md`](../FRD_MEASUREMENT_METHOD.md).

Then stop for review. Do not make a second capture, rotate the cabinet, export
an FRD, or copy the qualification's derived window into REW before approval.

## 6. Global Stop Rules And Limitations

Stop and de-energise safely for unexpected continuity, the wrong connector
contacts, an open protective path, sustained DC above a stated gate, clipping,
dropout, instability, abnormal sound, visible damage, heating, smell, smoke,
sparks, or perceptible tingle. Stop data work for missing calibration, wrong
endpoint/channel, absent numeric timing, inadequate headroom, moved geometry,
or a multi-arrival/ambiguous impulse. Preserve the failed capture and label it
diagnostic; do not repair its status by editing metadata.

The supplied ECM8000 CSV is a generic 0-degree response, not a serial-number-
specific calibration and not an absolute-sensitivity calibration. Results are
therefore not absolute-SPL evidence. The qualification's derived `2.0 ms` left
/ `1.0 ms` right window was suitable for a `1-5 kHz` repeatability gate; it is
not a final production window. Each reusable series must store a suitable
REW-native window selected from its own impulse/ETC.

This release is for controlled installed-woofer FRD only. Raw-tweeter sweeps
need an agreed protected band, level, and series high-pass. Polar measurements
need a separate rotation and position-control procedure. Neither is released.
