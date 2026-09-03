# Technics SU-V570 Output Topology And Loopback Verification

Date prepared: 2026-08-31

Last revised: 2026-09-03

Status: **UNPOWERED COMMON-GROUND CHECK PASSED; OPTIONAL POWERED CHECK WAIVED;
REFERENCE-FIXTURE AC GATE PENDING**

## 1. Purpose

Determine whether the Technics SU-V570 loudspeaker outputs are conventional
common-ground outputs suitable for the protected amplifier-output reference
fixture specified in
[`SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md`](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md).

This document deliberately separates:

- what the supplied schematic strongly indicates;
- what has now been established by external measurements;
- the optional powered confirmation, which was subsequently waived; and
- the connection that remains prohibited even though the amplifier passes.

## 2. Preserved Schematic Evidence

The supplied full-resolution image is preserved as:

[`SU-V570_power_amp_output_schematic.png`](SU-V570_power_amp_output_schematic.png)

SHA-256:

`35ED76E0E52DA1F5121D4609889CAB8289AD34F67FD5C9897FE1CB3A8E637D7C`

![Technics SU-V570 power amplifier and speaker output schematic](SU-V570_power_amp_output_schematic.png)

## 3. Schematic Assessment

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

## 7. Optional Powered Confirmation - Waived

**USER DECISION, 2026-09-01:** the successful unpowered gate is accepted as
sufficient evidence for this measurement plan, so the optional low-voltage
powered topology confirmation will not be performed. This does not waive the
separate UMC202HD, fixture, or AC release gates. No blank result sheet or
superseded procedure is retained.

## 8. Prohibited Test Connections

Do not:

- connect a speaker output directly to a UMC202HD input;
- place a multimeter in current mode across any speaker or supply output;
- use a USB-connected meter for the powered topology check;
- attach an earth-grounded oscilloscope ground clip to either speaker terminal;
- infer a safe connection merely because the amplifier plays normally;
- bypass the fixture's voltage clamps or commissioning measurements.

## 9. Consequence For The UMC202HD Reference

The passed Section 6 gate makes the SU-V570 suitable in principle for the
protected amplifier-output reference. It does not authorize a direct
speaker-output-to-interface connection. Use the symmetric two-leg high-value
fixture in
[SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md);
neither speaker lead is hard-connected to UMC202HD sleeve.

That arrangement remains preferable for this common-ground amplifier because it
avoids a second low-resistance bond through the reference input. The separately
audited playback path already provides the expected SU-V570-to-UMC202HD signal
ground and references it through USB and the Class-I PC to protective earth.
These are signal-path findings, not an appliance-safety or protective-conductor
test.

The completed ground readings, UMC202HD rear-output tests, PCB inspection, and
TS playback-cable decision are retained without duplication in
[the qualification record](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md).
The rear sockets are mechanically TRS but electrically tip plus a permanent
ring/sleeve common, so the mapped TS-to-RCA playback cable is compatible with
these specific outputs. The amplifier's approximately `+/-45.5 V` rails define
the fixture design envelope.

**CURRENT GATE, 2026-09-03:** amplifier topology passes and the optional powered
confirmation is waived. Complete
[the fixture AC transfer/noise gate](REFERENCE_FIXTURE_AC_COMMISSIONING.md)
before powered-amplifier or full-dual use.

## 10. Final Status Record

```text
Schematic assessment:       LIKELY COMMON-GROUND
Unpowered measurements:     PASS - 2026-09-01
Powered confirmation:       WAIVED - optional, 2026-09-01
Complete-fixture authority: SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md
Completed evidence:          SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md
Remaining electrical gate:  REFERENCE_FIXTURE_AC_COMMISSIONING.md
Fixture release status:     NO
Approved for full-dual use: NO

Reviewed by: Codex review of user-reported readings and ground-path analysis
Date:        2026-09-03
Notes:
Section 6 passes and externally supports the schematic common-ground
assessment. The optional powered confirmation was waived. Fixture construction,
completed evidence, and remaining AC work are separated into the three records
named above.
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
