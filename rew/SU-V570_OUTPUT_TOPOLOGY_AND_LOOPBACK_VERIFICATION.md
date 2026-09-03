# Technics SU-V570 Output Topology And Loopback Verification

Date prepared: 2026-08-31

Last revised: 2026-09-03

Status: **UNPOWERED COMMON-GROUND CHECK PASSED - COMPLETE FIXTURE NOT YET APPROVED**

## 1. Purpose

Determine whether the Technics SU-V570 loudspeaker outputs are conventional
common-ground outputs suitable for the protected amplifier-output reference
fixture specified in
[`SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md`](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md).

This document deliberately separates:

- what the supplied schematic strongly indicates;
- what has now been established by external measurements;
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

This was strong schematic evidence. The 2026-09-01 resistance measurements in
Section 6 now externally support the common-ground conclusion. That result does
not by itself approve connection to the UMC202HD; the complete fixture has its
own construction, test, and release gates.

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

**VERIFIED MEASUREMENT, 2026-09-01:** with the meter lead resistance nulled,
speaker negative measured approximately `0.10 ohm` to exposed bare-metal
chassis. If that was the settled reading after any charging transient, the
complete amplifier presents an effective low-resistance DC path between those
points in the tested, fully disconnected condition. The measurement does not
identify that path, and it does not change `C712` into the loudspeaker-current
return; a `10 nF` capacitor cannot explain a settled `0.10 ohm` DC result.

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
the table. If the reading is then nulled, compare subsequent measurements with
approximately `0 ohm`, not with the original lead reading.

```text
R_lead = 0.050 ohm
Math Null applied before the measurements in Section 6.2: YES
```

### 6.2 Measure the speaker-return network

Use the exposed metal of the binding posts, not paint or oxidised surfaces.

| Test | Measured resistance | Expected result |
| --- | ---: | --- |
| Left A negative to Left B negative | `0.002 ohm` after null | Approximately `0 ohm` after null |
| Left A negative to Right A negative | `0.045 ohm` after null | Approximately `0 ohm` after null |
| Left A negative to Right B negative | `0.045 ohm` after null | Approximately `0 ohm` after null |
| Any speaker negative to AUX/CD RCA outer shell | `0.120-0.150 ohm`; mean `0.130 ohm`, after null | Low, stable DC resistance after null |
| Any speaker negative to bare metal chassis | `0.100 ohm` after null | May be low, rise, or show `OL`; not a pass criterion |

Repeat questionable readings after reversing the probes and improving contact.
An in-circuit capacitor can cause a changing reading while it charges. That is
particularly relevant to the chassis measurement and is not itself a failure.

### 6.3 Unpowered decision gate

Treat the common-ground topology as externally supported if:

- all four negative speaker terminals are mutually continuous at very low,
  stable resistance; and
- a speaker negative has similarly unambiguous low-resistance DC continuity to
  an input RCA outer shell.

Without a meter null, very low readings should be approximately the meter-lead
resistance plus contact and internal path resistance. With a meter null, as in
the 2026-09-01 measurements, the displayed result should instead be near zero
plus contact and internal path resistance.

The speaker-negative-to-chassis reading is not a pass criterion. A high,
changing, or open DC reading is compatible with the `C712` RF bond.

Stop and reassess the schematic if:

- left and right negative terminals are not mutually continuous;
- speaker negative is not continuous with RCA signal ground; or
- a reading changes materially with the speaker-bank selector in a way not
  explained by contact resistance.

Do not proceed to a powered test until the unpowered readings have been reviewed.

### 6.4 2026-09-01 review result

**VERIFIED MEASUREMENT:** all speaker-negative terminals are mutually
continuous. The `0.002 ohm` same-channel A-to-B result is effectively zero for
this two-wire measurement. The `0.045 ohm` cross-channel results are still a
very low metallic path and may include binding-post contact, internal wiring,
PCB trace, and probe-contact resistance.

**VERIFIED MEASUREMENT:** every speaker negative has stable low-resistance DC
continuity to AUX/CD RCA signal ground. The `0.120-0.150 ohm` range is far below
a value that could plausibly represent only capacitive coupling or incidental
leakage. Its small spread is consistent with ordinary two-wire contact and path
variation.

The Keysight U1282A `60 ohm` range has `0.001 ohm` resolution and specified
accuracy of `+/- (0.15% of reading + 20 counts)` after Math Null, or about
`+/-0.020 ohm` for these readings under the datasheet conditions. The exact
milliohm differences should therefore not be over-interpreted; the topology
distinction is nevertheless decisive.

**DECISION:** Section 6 passes. The measurements externally support a
conventional common-signal-ground output and rule against treating the SU-V570
as a bridged or floating-output amplifier for this measurement plan.

## 7. Optional Low-Voltage Powered Confirmation

This section is optional and should be performed only after Section 6 passes.
Keep the amplifier closed and use a battery-powered, electrically isolated
multimeter.

**USER DECISION, 2026-09-01:** this optional confirmation is waived. The
successful unpowered gate is accepted as sufficient evidence for the present
measurement plan. Waiving this test does not waive the UMC202HD phantom-
isolation or complete-fixture construction and commissioning gates.

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
- bypass the fixture's voltage clamps or commissioning measurements.

## 9. Consequence For The UMC202HD Loopback

If Section 6 passes, the SU-V570 is suitable in principle for the protected
full-dual reference. Continue to use the complete two-leg high-value fixture
specified in
[`SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md`](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md),
rather than hard-connecting speaker negative to the UMC202HD sleeve.

That fixture file is the detailed authority for its cable-to-TRS construction,
component calculations, phantom prerequisite, ground-path audit, integrated DC
clamp test, AC transfer commissioning, and release gate. The remainder of this
section records only the amplifier-topology consequences.

That choice remains preferable even for a common-ground amplifier. Its two
high-value legs avoid creating a second low-resistance ground bond and use the
UMC202HD balanced line input. The playback cable may already reference the
amplifier's audio ground to the PC, but the actual system bonds must be measured
rather than inferred from connector shells. The fixture record owns that audit
and explains the earth-reference consequence.

**VERIFIED MEASUREMENT, 2026-09-02:** the interface/USB/PC portion of that audit
now confirms low-resistance bonds from UMC202HD Input 2 sleeve to PC chassis and
to the protective-earth pin of the PC's disconnected mains plug. The existing
disconnected post-stress matrix also closes the fixture-alone check.

**PLAYBACK-CABLE COMPATIBILITY PASS, 2026-09-03:** the proposed cable maps
correctly as mono TS-to-RCA, and powered driven-channel measurements verify
that both UMC202HD rear outputs are ring-grounded. Output 1 measured
`78.69/0.002/78.73 mV` and Output 2 measured `78.9/0.000/78.84 mV` tip-sleeve/
ring-sleeve/tip-ring. Its TS sleeve therefore adds no new short of an active
cold output when used on Output 1. Output 2 must supply the fixture-transfer
test from tip and sleeve rather than as two active balanced legs.

**USER-REPORTED INTERNAL PCB INSPECTION, 2026-09-03:** each rear output uses a
physical three-contact TRS socket with all three through-hole terminals
soldered. On both socket footprints, the separate ring and sleeve terminals
connect through four-spoke thermal reliefs to the same copper fill. Combined
with the unpowered `0.021 ohm` ring-to-sleeve reading and the powered AC maps,
this verifies a permanent tip-plus-common, electrically TS output topology; it
is not a state-dependent grounded cold output. The connectors remain
mechanically TRS and may still accept a TRS cable. A TS plug merely contacts two
PCB nodes—tip and the already-common R/S node—and is therefore compatible with
these specific inspected outputs.

**CONNECTED PLAYBACK-PATH PASS, 2026-09-03:** with the UMC202HD and SU-V570
unpowered, isolated from mains, USB disconnected, and the intended dual analogue
playback cable fitted, Input 2 sleeve measured `0.061 ohm` to the corresponding
SU-V570 RCA shell and `0.174 ohm` to the corresponding speaker-negative
terminal. The implied `0.113 ohm` RCA-shell-to-speaker-negative portion agrees
with the earlier `0.120-0.150 ohm` direct measurements within low-resistance
contact uncertainty and possible parallel dual-cable ground paths. The fixture
authority therefore marks the complete unpowered ground-path audit `PASS`.

The amplifier's approximately `+/-45.5 V` rails define the fixture's design
envelope. The dedicated fixture record derives its attenuation, component
ratings, and clamp choice from that envelope.

**CURRENT GATE, 2026-09-03:** the amplifier topology gate has passed and the
optional powered confirmation has been waived. This document makes no separate
approval of the attenuator, clamps, interface, or complete loopback. Complete
the fixture AC transfer/noise commissioning and release gate before using the
acoustic procedure. Its physical construction record now passes for controlled
bench use with the heat-shrink body and short unscreened output tail explicitly
documented.

## 10. Final Status Record

Complete this only after reviewing the measurements.

```text
Schematic assessment:       LIKELY COMMON-GROUND
Unpowered measurements:     PASS - 2026-09-01
Powered confirmation:       WAIVED - optional, 2026-09-01
Complete-fixture authority: SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md
Fixture release status:     NO
Approved for full-dual use: NO

Reviewed by: Codex review of user-reported readings and ground-path analysis
Date:        2026-09-03
Notes:
Section 6 passes and externally supports the schematic common-ground
assessment. The optional powered confirmation was waived. All fixture-specific
evidence and remaining gates are maintained in the separate fixture record.
```

## 11. Supporting Sources

Keysight specifies the U1282A low-resistance range, resolution, accuracy after
Math Null, and null procedure in the U1280 Series data sheet:
<https://www.keysight.com/us/en/assets/7018-04867/data-sheets/5992-0847.pdf>

The Technics operating instructions show normal line-level interconnection and
direct users to connect the AC power cord only after the other cables:
<https://www.manualslib.com/manual/3432378/Technics-Su-V570.html?page=5>

The Technics SU-V570 service manual gives the power-amplifier rail notation and
output topology used in the schematic assessment:
<https://audiocircuit.dk/downloads/technics/Technics-SUV570-int-sm.pdf>
