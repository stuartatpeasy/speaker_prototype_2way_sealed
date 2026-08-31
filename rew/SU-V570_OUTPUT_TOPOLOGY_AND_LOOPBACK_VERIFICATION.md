# Technics SU-V570 Output Topology And Loopback Verification

Date prepared: 2026-08-31

Status: **SCHEMATIC ASSESSMENT ONLY - EXTERNAL VERIFICATION PENDING**

## 1. Purpose

Determine whether the Technics SU-V570 loudspeaker outputs are conventional
common-ground outputs suitable for the protected UMC202HD driver-terminal
reference described in
[`FRD_MEASUREMENT_SETUP_TEST.md`](FRD_MEASUREMENT_SETUP_TEST.md).

This document deliberately separates:

- what the supplied schematic strongly indicates;
- what must still be established by external measurements;
- the optional powered confirmation that may follow a successful unpowered
  test;
- the connection that remains prohibited even if the amplifier passes.

## 2. Preserved Schematic Evidence

The supplied full-resolution image is preserved as:

[`SU-V570_power_amp_output_schematic.png`](SU-V570_power_amp_output_schematic.png)

SHA-256:

`35ED76E0E52DA1F5121D4609889CAB8289AD34F67FD5C9897FE1CB3A8E637D7C`

![Technics SU-V570 power amplifier and speaker output schematic](SU-V570_power_amp_output_schematic.png)

## 3. Provisional Schematic Conclusion

The drawing strongly indicates a conventional common-signal-ground amplifier,
not a bridged or floating loudspeaker output.

Evidence:

1. Each negative speaker terminal at `JK501` is connected to a signal-ground
   symbol.
2. The left-channel active output reaches the positive terminals through
   output inductor `L503` and the speaker-protection relay.
3. The right-channel active output similarly reaches its positive terminals
   through `L504` and the relay.
4. Only one terminal of each loudspeaker output is actively driven. A bridged
   output would show a second power stage driving the nominal negative terminal.
5. The output stages operate from approximately `+45.5 V`, `0 V`, and `-45.5 V`.
   The loudspeaker return is the amplifier's signal `0 V`, associated with the
   midpoint of the split supply and its reservoir capacitors, not external
   earth.
6. The heavy vertical line through the connector circles appears to denote the
   connector or mechanical boundary. Electrical connections enter individual
   terminals horizontally.

This is strong evidence, but the conclusion must remain provisional until the
unpowered resistance measurements in Section 6 have been recorded.

## 4. What C712 Does Not Mean

`C712` is marked `0.01`, interpreted as `0.01 uF = 10 nF`. It appears to bond
signal ground to chassis or external ground at high frequency. It is not in the
loudspeaker-current return path.

Its reactance is:

```text
Xc = 1 / (2 pi f C)
```

At 1 kHz:

```text
Xc = 1 / (2 pi x 1000 x 10e-9)
   = 15.9 kohm
```

A capacitor with `15.9 kohm` reactance cannot carry ampere-scale loudspeaker
return current. At 1 MHz its reactance is approximately `15.9 ohm`, which is
consistent with an RF, interference, or electrostatic ground bond.

The absence of a DC bond between signal ground and chassis ground is therefore
not evidence of a floating or bridged speaker output. Signal `0 V`, chassis,
protective earth, and speaker negative are related concepts but need not be the
same physical node.

## 5. Safety Conditions For External Testing

For all resistance and continuity measurements:

1. Unplug the SU-V570 from the mains.
2. Disconnect every external cable, including speakers, RCA leads, and any
   measurement-interface connection. This prevents an external cable from
   manufacturing the continuity being tested.
3. Leave the amplifier disconnected long enough for its reservoir capacitors to
   discharge.
4. Use a battery-powered handheld multimeter.
5. Put the leads in `COM` and `V/ohm`, never the current socket.
6. Select resistance or continuity mode only after confirming that the
   amplifier is de-energised.
7. Do not open the case or probe internal mains or supply-rail nodes for this
   test.

Fluke's resistance-measurement guidance likewise requires circuit power to be
off and capacitors to be discharged:
<https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-measure-resistance>

## 6. Required Unpowered Measurements

### 6.1 Establish meter-lead resistance

Short the probes firmly together and record the reading. If the meter has a
relative or zero function, it may be used, but retain the original reading in
the table.

```text
R_lead = __________ ohm
```

### 6.2 Measure the speaker-return network

Use the exposed metal of the binding posts, not paint or oxidised surfaces.

| Test | Measured resistance | Expected result |
| --- | ---: | --- |
| Left A negative to Left B negative |  | Approximately `R_lead` |
| Left A negative to Right A negative |  | Approximately `R_lead` |
| Left A negative to Right B negative |  | Approximately `R_lead` |
| Any speaker negative to AUX/CD RCA outer shell |  | Approximately `R_lead` |
| Any speaker negative to bare metal chassis |  | May rise or show `OL` |

Repeat questionable readings after reversing the probes and improving contact.
An in-circuit capacitor can cause a changing reading while it charges. That is
particularly relevant to the chassis measurement and is not itself a failure.

### 6.3 Unpowered decision gate

Treat the common-ground topology as externally supported if:

- all four negative speaker terminals are mutually continuous at approximately
  the meter-lead resistance; and
- a speaker negative is continuous to an input RCA outer shell at approximately
  the meter-lead resistance.

The speaker-negative-to-chassis reading is not a pass criterion. A high,
changing, or open DC reading is compatible with the `C712` RF bond.

Stop and reassess the schematic if:

- left and right negative terminals are not mutually continuous;
- speaker negative is not continuous with RCA signal ground; or
- a reading changes materially with the speaker-bank selector in a way not
  explained by contact resistance.

Do not proceed to a powered test until the unpowered readings have been reviewed.

## 7. Optional Low-Voltage Powered Confirmation

This section is optional and should be performed only after Section 6 passes.
Keep the amplifier closed and use a battery-powered, electrically isolated
multimeter.

1. Reconnect one woofer or a suitable load to one selected speaker output.
2. Connect a line-level source and apply a 1 kHz sine wave.
3. Establish approximately `1.00 V RMS` across the speaker terminals.
4. Keep the meter in AC-voltage mode with its leads in `COM` and `V/ohm`.
5. Put the black probe on the outer shell of the selected line-input RCA socket.
6. Measure AC voltage from speaker negative to the RCA shell.
7. Measure AC voltage from speaker positive to the RCA shell.
8. Finally, measure directly across speaker positive and negative.

Expected common-ground result:

| Test | Expected result |
| --- | --- |
| Speaker negative to RCA shell | Near the meter's noise floor |
| Speaker positive to RCA shell | Approximately `1.00 V RMS` |
| Speaker positive to speaker negative | Approximately `1.00 V RMS` |

Calculate:

```text
r = V(negative to RCA ground) / V(positive to negative)
```

For a conventional common-ground output, `r` should be at the meter's noise
floor and comfortably below `0.01` or 1%. A bridged amplifier would normally
show substantial AC voltage on both speaker terminals relative to signal ground.

As a separate amplifier-health observation, measure DC voltage directly across
the speaker terminals with no signal. Low tens of millivolts are unsurprising;
hundreds of millivolts warrant stopping and investigating the amplifier. This DC
offset check is not, by itself, a topology test.

### 7.1 Powered-test record

| Quantity | Result |
| --- | ---: |
| Test frequency |  Hz |
| Speaker-terminal voltage |  V RMS |
| Negative-to-RCA-shell voltage |  V RMS |
| Positive-to-RCA-shell voltage |  V RMS |
| Ratio `r` |  |
| DC offset across speaker output |  mV DC |

## 8. Prohibited Test Connections

Do not:

- connect a speaker output directly to a UMC202HD input;
- place a multimeter in current mode across any speaker or supply output;
- use a USB-connected meter for the powered topology check;
- attach an earth-grounded oscilloscope ground clip to either speaker terminal;
- infer a safe connection merely because the amplifier plays normally;
- bypass the divider's voltage clamps or commissioning measurements.

## 9. Consequence For The UMC202HD Loopback

If Section 6 passes, the SU-V570 is suitable in principle for the protected
full-dual reference. Continue to use the two-leg high-value divider specified in
[`FRD_MEASUREMENT_SETUP_TEST.md`](FRD_MEASUREMENT_SETUP_TEST.md), rather than
hard-connecting speaker negative to the UMC202HD sleeve.

That choice remains preferable even for a common-ground amplifier because the
UMC202HD-output-to-Technics-RCA cable already provides a signal-ground
connection. The two high-value divider legs avoid adding a second low-resistance
ground path and exploit the UMC202HD balanced line input.

The divider and interface must still pass the low-voltage electrical
commissioning procedure before the reference is connected across a driven
loudspeaker.

## 10. Final Status Record

Complete this only after reviewing the measurements.

```text
Schematic assessment:       LIKELY COMMON-GROUND
Unpowered measurements:     PENDING
Powered confirmation:       NOT PERFORMED
Divider commissioning:      NOT PERFORMED
Approved for full-dual use: NO

Reviewed by: _______________
Date:        _______________
Notes:
________________________________________________________________________
________________________________________________________________________
```

## 11. Supporting Source

Behringer specifies two XLR/TRS microphone/line/instrument inputs and a maximum
line-input level of approximately `+20 dBu` for the UMC202HD. That headroom does
not remove the requirement for an attenuating and fault-protected divider:
<https://mediadl.musictribe.com/media/sys_master/h1f/h9b/8849476255774.pdf>
