# SU-V570 To UMC202HD Amplifier-Output Reference Fixture

Date prepared: 2026-09-02

Last revised: 2026-09-03

Status: **PRE- AND POST-STRESS RESISTANCE MATRICES PASS; THE INTEGRATED DC TEST
PASSES CLAMP, SYMMETRY, CURRENT, CV, AND THERMAL CHECKS WITH AN ACCEPTED,
CHARACTERIZED 45.5 V LINEARITY DEVIATION; ALL UNPOWERED GROUND-PATH STAGES PASS;
BOTH POWERED REAR OUTPUTS ARE VERIFIED RING-GROUNDED; PHYSICAL RECORD PASSES FOR
CONTROLLED BENCH USE WITH A DOCUMENTED HEAT-SHRINK BODY AND UNSCREENED 5 CM
OUTPUT TAIL; AC TRANSFER/NOISE CHECK REMAINS; NOT APPROVED FOR AMPLIFIER USE**

## 1. Scope And Authority

This file is the detailed authority for the complete electrical-reference
fixture between one Technics SU-V570 speaker-output pair and the Behringer
UMC202HD Input 2 central TRS jack. In this file, *fixture* means all of:

1. the two-conductor cable attached to the selected SU-V570 speaker terminals;
2. the insulated attenuator and voltage-clamp network;
3. the short three-conductor output tail; and
4. the 1/4-inch TRS plug inserted into the central jack of UMC202HD Input 2.

The current amplifier-end cable is user-reported as `2 m` of red-and-black
`1.5 mm^2` two-conductor DC power cable. Red is amplifier positive and black is
the corresponding amplifier negative. It has no printed markings and terminates
in secure, fully inserted bare wire at the SU-V570. The network is individually
insulated and encapsulated in a tapered, approximately `6 cm` multilayer heat-
shrink body. Its output tail is approximately `5 cm` of three twisted `14/0.7`
hookup wires carrying tip, ring, and sleeve to an all-metal TRS plug. Component
part numbers, plug make/model, cable manufacturer, heat-shrink type/rating, and
zener manufacturer/family suffix are unknown and are recorded as such rather
than inferred.

This document owns the fixture rationale, construction, calculations,
inspection, electrical tests, test history, and release gate. Related documents
have narrower authority:

- [`SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md`](SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md)
  establishes whether the amplifier output is suitable in principle;
- [`FRD_MEASUREMENT_SETUP_TEST.md`](FRD_MEASUREMENT_SETUP_TEST.md) consumes an
  already commissioned fixture in the acoustic repeatability test; and
- [`../DRIVER_ANALYSIS.md`](../DRIVER_ANALYSIS.md) retains the dated project
  evidence and decision history.

Never connect this fixture to a powered amplifier until every required gate in
Section 11 is marked `PASS`.

## 2. Functional Rationale

### 2.1 Why An Electrical Reference Is Used

In the preferred full-dual REW measurement:

- UMC202HD Input 1 records the ECM8000 microphone;
- UMC202HD Input 2 records the attenuated amplifier-output voltage; and
- REW uses Input 2 as both response-calibration and timing reference.

This removes the DAC, amplifier gain, and amplifier frequency response from the
derived acoustic transfer function and provides common timing between driver
measurements. The reference is taken after the SU-V570 volume control and power
stage, so a small gain movement or amplifier-response variation does not become
a false driver-response change.

The current fixture attaches at the rear SU-V570 speaker terminals. It therefore
references amplifier-terminal voltage, not voltage at the loudspeaker end of
the separate speaker cable. The true-RMS meter still sets `1.00 V RMS` at the
woofer terminals. A low-resistance, unchanged speaker cable makes the difference
small and repeatable, but its impedance remains part of the measured acoustic
path. If driver-terminal rather than amplifier-terminal normalization later
becomes necessary, connect the same fixture red and black leads at the driver
terminals and document that changed reference plane.

### 2.2 Why The Fixture Uses Two High-Value Legs

The SU-V570 has passed the unpowered common-ground topology gate, but neither
speaker conductor is hard-wired to UMC202HD sleeve inside the fixture. Both are
attenuated symmetrically:

- amplifier positive reaches TRS tip through `9.1 kohm`;
- amplifier negative reaches TRS ring through a separate `9.1 kohm`;
- tip and ring each have `1.0 kohm` to sleeve; and
- each TRS signal node has its own bidirectional clamp to sleeve.

This preserves a balanced two-leg input, avoids manufacturing a second direct
ground bond, and ensures that either speaker lead retains approximately
`10.1 kohm` to sleeve when the fixture is disconnected from the system.

### 2.3 Protection Layers

The protection is deliberately layered:

1. the `9.1 kohm`, at least `0.5 W`, series resistors are the primary current
   limiters;
2. the `1.0 kohm` shunts establish approximately 20 dB attenuation and keep the
   TRS nodes below the UMC202HD input range for any SU-V570 output bounded by
   its supply rails;
3. series-opposed `5.1 V` zeners provide secondary protection against an open
   shunt or abnormal overvoltage while the series resistor remains intact; and
4. construction, DC, ground-path, and AC tests must all pass before use.

The fixture is not a mains-isolation device, protective-earth connection,
speaker load, or substitute for appliance-safety testing. It cannot protect a
misconstruction that bypasses a `9.1 kohm` series resistor.

## 3. Construction Specification

### 3.1 Electrical Schematic

The installed clamp pairs are series-opposed with their anodes joined. A
common-cathode pair would be electrically equivalent. The joined midpoint of
each pair is insulated and connected nowhere else.

```text
         2 m, 1.5 mm^2                    ~5 cm TWISTED T/R/S WIRES
       RED amplifier lead                       TO 1/4-INCH TRS

SU + o================o-- R1 9.1 kohm, 0.5 W --+---------- T (tip)
                                                |
                                                +-- R3 1.0 kohm --+
                                                |                 |
                                                +--K D1 A--A D2 K-+
                                                                  |
                                                                  +------ S (sleeve/shield)
                                                                  |
                                                +--K D3 A--A D4 K-+
                                                |                 |
                                                +-- R4 1.0 kohm --+
                                                |
SU - o================o-- R2 9.1 kohm, 0.5 W --+---------- R (ring)

      BLACK amplifier lead

Fixture sleeve/return is NOT hard-connected to the black amplifier lead.
UMC202HD Input 2 outer XLR contacts 1, 2, and 3 remain unused.
```

### 3.2 Bill Of Materials And Present Evidence

| Ref. | Requirement | Present evidence/status |
| --- | --- | --- |
| Input cable | `2 m`, two-conductor, red/black, `1.5 mm^2`; insulation suitable for the `64 V DC` commissioning test | No printed markings; figure-of-eight insulation remains joined except approximately `5 cm` at the bare-wire speaker end and `2 cm` at the fixture; secure, insulated, strand-free termination; complete fixture passed `64.5 V DC` qualification |
| R1 | `9.1 kohm`, 1%, metal-film, at least `0.5 W`, working voltage at least `100 V` | User-confirmed 1% metal-film, `0.5 W`, working voltage above `100 V`; no retained part number; sourced from Mouser; complete path `9.125 kohm` pre-stress and `9.127 kohm` post-stress |
| R2 | `9.1 kohm`, 1%, metal-film, at least `0.5 W`, working voltage at least `100 V` | User-confirmed 1% metal-film, `0.5 W`, working voltage above `100 V`; no retained part number; sourced from Mouser; complete path `9.139 kohm` pre-stress and `9.141 kohm` post-stress |
| R3 | `1.0 kohm`, 1%, metal-film, at least `0.25 W` | User-confirmed 1% metal-film, `0.25 W`; no retained part number; sourced from Mouser; measured `1.002 kohm` both pre- and post-stress |
| R4 | `1.0 kohm`, 1%, metal-film, at least `0.25 W` | User-confirmed 1% metal-film, `0.25 W`; no retained part number; sourced from Mouser; measured `1.003 kohm` pre-stress and `1.004 kohm` post-stress |
| D1-D4 | Four matched `5.1 V` small-signal zeners in two series-opposed pairs; traceable `BZX55B5V1` or `BZX55C5V1` remains preferred for a reproducible build | Marked `BZX 5V1`; exact manufacturer, family suffix, tolerance, and rating unknown; each individually measured close to `5 V` at `2 mA`; installed anode-to-anode; bidirectional installed function passed |
| Output tail | Shielded balanced two-conductor cable preferred; a very short twisted tip/ring/sleeve tail requires explicit AC noise verification | Approximately `5 cm`; three individually insulated `14/0.7` hookup wires twisted together; no overall electrostatic screen; sleeve wire soldered between the fixture star point and plug sleeve |
| Output plug | 1/4-inch TRS; tip/ring/sleeve wired exactly as shown | Make/model unknown; quality all-metal three-contact plug; internal plastic insulating cylinder; standard cable-clamp jaws; body bonded to sleeve; labelled for UMC202HD Input 2 `LINE`; mapping confirmed electrically |
| Fixture body | Insulating enclosure preferred; strain relief at both cables; no exposed conductive joints | Approximately `6 cm` multilayer heat-shrink cylinder; every component, leg, and junction individually insulated before overall encapsulation; tapered ends and internal wire returns provide strain relief; moderate pull reaches no solder joint; bench-only construction |

Do not substitute a large power TVS without redesigning and remeasuring the
fixture. Its voltage may be specified at a surge current that this network
cannot supply, and its capacitance may disturb the high-frequency reference.

### 3.3 Physical Wiring Rules

1. Keep the red and black input conductors together for their whole run. Do not
   route either conductor separately around the room.
2. Place R1 and R2 where their bodies and leads cannot contact one another,
   the sleeve conductor, enclosure hardware, or the zener network.
3. Make sleeve the local star point for R3, R4, both clamp endpoints, and the
   output-tail sleeve conductor only.
4. Put each clamp pair close to its TRS node and sleeve connection.
5. Insulate the joined zener midpoint. Do not use it as a test point or ground.
6. Provide independent strain relief, or a mechanically equivalent load-
   relieving arrangement, for the heavy input cable and the smaller output
   tail; solder joints must carry no cable tension.
7. Permanently mark the amplifier end `RED +` and `BLACK -`, and mark the TRS
   plug `UMC202HD INPUT 2 - CENTRAL TRS - LINE`.
8. Use fully insulated or shrouded connections during the `64 V DC` test.
9. Use an amplifier-end termination that remains mechanically secure beside
   the separate loudspeaker cable. No loose strand or exposed conductor may
   bridge adjacent binding posts; inspect and pull-test both leads before use.

### 3.4 Recorded Physical-Construction Outcome

**USER-REPORTED INSPECTION - 2026-09-03:** the red and black `1.5 mm^2`
conductors retain their joined figure-of-eight insulation over the complete
`2 m` run except for approximately `5 cm` at the bare-wire speaker-terminal end
and `2 cm` at the fixture end. Colour provides the permanent polarity marking.
The bare-wire termination is secure, insulated, fully captured, and free of
stray strands; the SU-V570 terminals do not accept ring, spade, or banana
terminations.

The components are soldered as a free-air network, each body and exposed lead
is individually heat-shrink insulated, every junction has additional insulation,
and the complete assembly has further overlapping heat-shrink layers forming an
approximately `6 cm` stiff cylinder. Layer count tapers at both ends. Internal
wire returns transfer a moderate cable pull into the encapsulation rather than
the solder joints. All component conductors are inaccessible. The two joined-
anode zener midpoints are separately insulated and connected nowhere else, and
sleeve is confirmed as the common junction for both `1 kohm` shunts, both clamp
endpoints, and the output-tail sleeve conductor.

The output tail is not screened cable. It comprises approximately `5 cm` of
three twisted, individually insulated `14/0.7` hookup wires for tip, ring, and
sleeve. The sleeve conductor is soldered directly between the fixture star and
the TRS sleeve. The all-metal TRS body is intentionally bonded to sleeve; its
tip/ring/sleeve terminals are otherwise separated by the supplied cylindrical
plastic insulator, and the cable is gripped by the plug's normal clamp jaws.
The plug is appropriately labelled.

**ENGINEERING REVIEW:** heat-shrink tubing is legitimately used for electrical
insulation, strain relief, and mechanical protection, but the unknown tubing
identity means no specific dielectric, temperature, abrasion, or flame rating
is claimed. The assembled fixture has nevertheless survived the controlled
`64.5 V DC` test and the post-stress matrix without electrical change, excessive
heating, or observed insulation failure. At the intended approximately `1 V RMS`
amplifier level, internal resistor dissipation is negligible compared with the
already completed DC qualification. The heat-shrink body is therefore accepted
for careful bench handling, not for permanent installation, crushing, abrasion,
unattended use, or use after visible or tactile damage.

The unscreened output tail is a performance deviation rather than a direct
electrical-safety failure. Its `5 cm` length and twisted conductors keep exposed
loop area small, while the approximately `1 kohm` shunts keep both signal nodes
at moderate impedance. It is not electrically equivalent to two conductors
inside an electrostatic shield, so Section 10 must explicitly compare the direct
and fixture-connected no-signal spectra for mains-frequency or other pickup.

**DECISION - PHYSICAL RECORD PASS FOR CONTROLLED BENCH USE:** construction,
polarity marking, insulation, junction isolation, strain relief, component
ratings, plug mapping, and the deliberate output-tail deviation are now
recorded. No rebuild is required on the present evidence. Inspect the bare-wire
termination, outer heat-shrink, both cable exits, and TRS clamp before every use;
stop on looseness, a stray strand, cut, abrasion, softening, discoloration, or
exposed internal structure. Final approval remains gated by AC transfer and
noise commissioning.

## 4. Component-Value Calculations

### 4.1 Input-Cable Resistance

Using copper resistivity `rho ~= 0.0172 ohm mm^2/m`, the calculated resistance
of each `2 m`, `1.5 mm^2` conductor at approximately `20 degrees C` is:

```text
Rlead = rho x length / area
      = 0.0172 ohm mm^2/m x 2 m / 1.5 mm^2
      = 0.0229 ohm per conductor

Rloop = 2 x 0.0229 ohm = 0.0459 ohm
```

This is a material estimate, not a measurement of the finished cable and
contacts. The fixture input cable carries divider current, not loudspeaker
current. At the normal `1.00 V RMS` test point, approximately `99 uA` gives
only about `2.3 uV RMS` drop in one conductor. Even the bounded `4.50 mA` DC
fault current gives about `0.10 mV`. The cable is therefore electrically
negligible in the divider ratio; its large cross-section mainly provides
mechanical robustness.

### 4.2 Nominal And Measured Attenuation

For either nominal leg with sleeve tied to amplifier reference externally:

```text
k = Vout / Vin
  = 1.0 kohm / (9.1 kohm + 1.0 kohm)
  = 0.099010

A = 20 log10(k) = -20.086 dB
```

The post-rebuild complete-unit resistance measurements give:

```text
k_tip  = 1.002 / (9.125 + 1.002) = 0.098943 = -20.092 dB
k_ring = 1.003 / (9.139 + 1.003) = 0.098896 = -20.096 dB
```

With the disconnected fixture driven differentially between red and black, the
four directly measured branch values predict:

```text
k_floating = (1.002 + 1.003)
             / (9.125 + 1.002 + 1.003 + 9.139)
           = 0.098920
           = -20.094 dB
```

These are unloaded fixture predictions. Behringer's published UMC202HD
specifications do not state the `LINE` input impedance, so a defensible
interface-loaded ratio cannot be calculated from published data. Input loading
can only add attenuation to this passive network. The final AC transfer
measurement, not the resistor calculation, decides the installed gain and
frequency response.

### 4.3 Amplifier Loading

With the external playback connection tying sleeve to SU-V570 signal ground,
the active fixture branch is approximately `10.127 kohm`. At `1.00 V RMS`:

```text
Ifixture = 1.00 V / 10.127 kohm = 98.75 uA RMS
Pfixture = (1.00 V)^2 / 10.127 kohm = 98.75 uW
```

In parallel with an ideal `8 ohm` load:

```text
Rcombined = 8 ohm || 10.127 kohm = 7.9937 ohm
```

That is only a `0.079%` reduction and is negligible for the acoustic test.

### 4.4 Maximum Signal And Resistor Power

The SU-V570 schematic marks approximately `+45.5 V`, `0 V`, and `-45.5 V`
rails. An impossible ideal sine reaching both rails would have:

```text
Vamp,peak = 45.5 V
Vamp,RMS  = 45.5 V / sqrt(2) = 32.17 V RMS

Vtip,RMS  = 32.17 V x 0.098943 = 3.18 V RMS
Vtip,peak = 45.5 V x 0.098943  = 4.50 V peak
```

Published output ratings give lower divided peaks:

| SU-V570 condition | Speaker voltage | Fixture-node peak |
| --- | ---: | ---: |
| `60 W` into `8 ohm`, 20 Hz-20 kHz | `21.91 V RMS` | `3.07 V peak` |
| `70 W` into `8 ohm`, 1 kHz at `1%` THD | `23.66 V RMS` | `3.31 V peak` |
| Ideal `+/-45.5 V` rail-bound sine | `32.17 V RMS` | `4.50 V peak` |

The UMC202HD published `+20 dBu` maximum line-input level is:

```text
Vline,RMS  = 0.775 V x 10^(20/20) = 7.75 V RMS
Vline,peak = 7.75 V x sqrt(2)      = 10.96 V peak
```

This is a product performance limit, not an absolute-damage specification, but
the rail-bound fixture output is still approximately `7.7 dB` below it.

For the harsher sustained `45.5 V DC` fault with the shunt intact:

```text
Ifault = 45.5 V / (9.125 kohm + 1.002 kohm) = 4.49 mA
P_R1   = Ifault^2 x 9.125 kohm               = 0.184 W
P_R3   = Ifault^2 x 1.002 kohm               = 0.020 W
Vtip   = Ifault x 1.002 kohm                 = 4.50 V
```

This establishes the `0.5 W` minimum for R1 and R2 with useful margin. The
`0.25 W` shunts have ample margin. Actual component working-voltage and
temperature derating must also be respected.

### 4.5 Clamp Selection

Use two `5.1 V` zeners in series opposition at each node. In either polarity,
one diode is in zener breakdown and the other is forward-biased, so the expected
low-current clamp is broadly:

```text
Vclamp ~= Vz + Vf ~= 5.5 V to 6.2 V peak
```

The exact value depends on diode family, tolerance, current, and temperature.
The installed devices are marked only `BZX 5V1`; their manufacturer and full
part number are unknown. The user's zener analyser reports close to `5 V` at
`2 mA` for every sample. That is useful measured characterization near the
fixture's relevant current range, but it is not evidence for a particular
manufacturer power rating, tolerance curve, or junction capacitance. The
series-opposed pair's forward drop must be added to the measured zener voltage.

The reported anode-to-anode connection is correct. For either node polarity,
one device is reverse-biased into zener operation while the other is forward-
biased. Reversing the voltage swaps those roles.

The earlier provisional `3.3 V` selection is superseded. Its soft low-current
knee is unnecessarily close to the possible `3.1-4.5 V peak` divided output.
The `5.1 V` pair remains inactive for every amplifier-derived waveform bounded
by the rails yet acts well below the UMC202HD's published `10.96 V peak` line-
input figure.

With an open shunt, a `45.5 V` fault clamped at a representative `5.6 V` gives:

```text
Iclamp = (45.5 V - 5.6 V) / 9.125 kohm = 4.37 mA
Pzener ~= 5.0 V x 4.37 mA              = 21.9 mW
```

At the `64 V` commissioning point with the `1.002 kohm` shunt intact, a
representative `5.6 V` pair voltage gives:

```text
Iseries = (64 V - 5.6 V) / 9.125 kohm = 6.40 mA
Ishunt  = 5.6 V / 1.002 kohm          = 5.59 mA
Izener  ~= 6.40 mA - 5.59 mA          = 0.81 mA
Pzener  ~= 5.0 V x 0.81 mA            = 4.1 mW
```

Even an accidental open shunt during that current-limited test would bound the
zener dissipation near `32 mW`. The exact installed power rating remains
unknown, so no `500 mW` rating is attributed to these parts; nevertheless, the
required dissipation is low enough that the controlled, current-limited
qualification can proceed. With the shunt intact and any SU-V570 output bounded
by its rails, the resistors alone hold the node to about `4.50 V`, so the clamp
intentionally remains off. The clamp is secondary protection, not the primary
current limiter.

For this one-off prototype, the missing manufacturer suffix is not itself a
release blocker if the four DC curves demonstrate the required bidirectional
clamp knee and the AC test demonstrates acceptable capacitance and linearity.
Retain the parts as measured, unidentified `BZX 5V1` devices. A reproducible
future build should use fully traceable components.

Do not use anticipated loudness or volume-control position as protection. The
SU-V570 line-input sensitivity is `150 mV` for rated output. The UMC202HD's
published `+3 dBu` maximum output is `1.095 V RMS`, a ratio of `7.30` or
`17.3 dB`, so rated amplifier output is possible with substantial attenuation
at the volume control.

## 5. Verification Order And Global Stop Rules

Perform the following in order:

1. confirm SU-V570 output suitability under the separate topology record;
2. confirm phantom isolation on the actual Input 2 central TRS contacts;
3. inspect and resistance-test the complete unpowered fixture;
4. commission both complete attenuator/clamp legs with the current-limited
   PL310QMD DC test;
5. audit the complete unpowered system ground and cable paths;
6. measure the fixture's AC gain, polarity, and frequency response; and
7. only then connect the fixture to a powered amplifier.

Stop immediately for a shorted series resistor, unexplained continuity, wrong
TRS contact, unstable DC result, unexpected current-limit operation, excessive
component heating, insulation damage, perceptible tingle, visible spark, or an
appliance-safety concern. The fixture remains unapproved until the cause is
understood and every affected test is repeated.

## 6. UMC202HD Input 2 TRS Phantom-Isolation Gate

### 6.1 Decision Test

This is a destination-input prerequisite, not a test of the fixture itself. Use
a separate plain TRS breakout with two equal `100 kohm`, 1%, at least `0.25 W`,
at least `60 V` working-voltage resistors:

```text
Tip  ----- 100 kohm -----+
                         +----- Sleeve
Ring ----- 100 kohm -----+
```

Leave the amplifier, fixture, loudspeaker, microphone, and interface outputs
disconnected. Insert only this breakout into the central Input 2 TRS jack. With
the battery-powered U1282A in normal DCV mode on its `+/-60 V` range, monitor
tip-sleeve, ring-sleeve, and tip-ring while switching USB power and `+48 V` as
specified below:

1. With `+48 V` off, power the interface and allow each reading to settle.
2. For each contact pair separately, switch `+48 V` on while observing, then
   switch it off before moving the probes.
3. Pass only if every settled magnitude is below `0.1 V` and phantom switching
   causes no sustained change.

A conventional `48 V` phantom feed through `6.8 kohm` would produce:

```text
Vloaded = 48 V x 100 kohm / (100 kohm + 6.8 kohm) = 44.9 V
```

The defined load therefore cannot conceal a real P48 feed.

### 6.2 Recorded Outcome

**USER-REPORTED MEASUREMENT, 2026-09-01:** with `+48 V` off, tip-sleeve and
ring-sleeve each settled below `1 mV` within `25 s`; tip-ring settled below
`1 mV` within `1 s`. Without power-cycling the UMC202HD, all three pairs then
remained at a displayed `0.000 V` while `+48 V` was individually switched on
and off for each measurement.

**DECISION - PASS:** the UMC202HD Input 2 central TRS phantom-isolation gate
passes. Normal DCV display sampling cannot exclude a very brief transient, but
it excludes the sustained or settling DC this gate is designed to detect.

**SUPERSEDED DIAGNOSTIC HISTORY:** earlier unloaded measurements showed a brief
approximately `3.3 V` power-up peak, rapid fall, slow rise towards `1.5 V`, and
minutes-long decay. That high-impedance, non-monotonic observation is consistent
with stored charge, changing bias, meter interaction, or multiple time
constants. It is retained as startup evidence but is not the decision test.

## 7. Complete-Fixture Inspection And Resistance Test

### 7.1 Pre-Power Procedure

Disconnect the complete fixture from the amplifier, UMC202HD, PC, power supply,
and every other item. Keep fingers off conductors while readings settle. Inspect
the full cable-to-plug assembly against the schematic, then measure:

| Resistance test | Expected result |
| --- | ---: |
| Tip to sleeve | Approximately `1.0 kohm` |
| Ring to sleeve | Approximately `1.0 kohm` |
| Tip to ring | Approximately `2.0 kohm` |
| Red input to tip | Approximately `9.1 kohm` |
| Black input to ring | Approximately `9.1 kohm` |
| Red input to sleeve | Approximately `10.1 kohm` |
| Black input to sleeve | Approximately `10.1 kohm` |
| Red input to ring | Approximately `11.1 kohm` |
| Black input to tip | Approximately `11.1 kohm` |
| Red input to black | Approximately `20.2 kohm` |

Reverse the meter probes on the diode-containing paths if any result is
polarity-dependent. A normal low-voltage resistance reading cannot prove clamp
action; it can only expose shorts or unexpected leakage. Record the installed
diode markings and visually confirm two series-opposed pairs.

### 7.2 Superseded Construction History

The original fixture had only red-input-to-tip through `9.1 kohm`, tip-to-
sleeve through `1.0 kohm`, and a hard black-input-to-sleeve connection; ring was
open. The reported signature was approximately `10 kohm` red-to-black,
approximately `1 kohm` tip-to-sleeve, and no ring continuity to any terminal.
That one-leg topology was rejected and prohibited from use.

The first measurements after rework strongly indicated both legs, but a
duplicated label and `50-105 ohm` deficits in redundant sums left the formal
gate open. Those results were superseded by the hands-off repeat. Finger/body
leakage is the likely explanation because the deficits disappeared, but the
cause was not directly measured.

The superseded values, retained exactly as reported, were:

| Reported test | Superseded result |
| --- | ---: |
| Tip to sleeve | `1.0034 kohm` |
| Ring to sleeve | `1.0042 kohm` |
| Tip to ring | `2.0072 kohm` |
| Input positive to ring | `11.056 kohm` |
| Input negative to ring | `9.109 kohm` |
| Input positive to tip | `9.111 kohm` |
| Input positive to ring, duplicated label | `11.066 kohm` |
| Input positive to input negative | `20.122 kohm` |

The duplicated cross-path label and inconsistent derived sums are why these
readings do not replace the corrected results below.

### 7.3 Superseded Pre-Rebuild Recorded Outcome

**USER-REPORTED MEASUREMENT, 2026-09-02:** the disconnected fixture's resistor
network was measured with an Agilent U1282A in autoscaling resistance mode,
with the user's fingers kept out of the circuit.

| Resistance test | Result |
| --- | ---: |
| Tip to sleeve | `1.004 kohm` |
| Ring to sleeve | `1.004 kohm` |
| Tip to ring | `2.007 kohm` |
| Red input to ring | `11.122 kohm` |
| Black input to ring | `9.137 kohm` |
| Red input to tip | `9.117 kohm` |
| Black input to tip | `11.144 kohm` |
| Red input to black | `20.259 kohm` |
| Black input to sleeve | `10.140 kohm` |
| Red input to sleeve | `10.118 kohm` |

The redundant identities agree within `0-3 ohm`:

| Identity | Constituent-path sum | Direct reading | Difference |
| --- | ---: | ---: | ---: |
| Tip-ring | `2.008 kohm` | `2.007 kohm` | `-1 ohm` |
| Red-ring | `11.124 kohm` | `11.122 kohm` | `-2 ohm` |
| Black-tip | `11.144 kohm` | `11.144 kohm` | `0 ohm` |
| Red-black | `20.261 kohm` | `20.259 kohm` | `-2 ohm` |
| Red-sleeve | `10.121 kohm` | `10.118 kohm` | `-3 ohm` |
| Black-sleeve | `10.141 kohm` | `10.140 kohm` | `-1 ohm` |

**SUPERSEDED DECISION - RESISTOR NETWORK PASS:** this established the pre-
rebuild two-leg resistance topology. Section 7.4 now supplies the current
post-rebuild baseline.

### 7.4 Post-Rebuild Complete-Unit Resistance Outcome

**USER-REPORTED MEASUREMENT, 2026-09-02:** after rebuilding the attenuator/clamp
as one unit, the complete disconnected fixture was measured with an Agilent
U1282A in resistance mode on its `60 kohm` range. Lead resistance was nulled
before the first measurement, no body part contacted the circuit, and all
reported values are in `kohm`. `In+` is the red amplifier-end lead and `In-` is
the black amplifier-end lead.

| From / to | Ring | Tip | In+ | In- |
| --- | ---: | ---: | ---: | ---: |
| Sleeve | `1.003` | `1.002` | `10.127` | `10.142` |
| Ring | - | `2.005` | `11.131` | `9.139` |
| Tip | - | - | `9.125` | `11.145` |
| In+ | - | - | - | `20.271` |
| In- | - | - | - | - |

The independent path sums close at the meter's displayed `0.001 kohm` or
`1 ohm` resolution:

| Identity | Constituent-path sum | Direct reading | Difference |
| --- | ---: | ---: | ---: |
| Ring-tip | `1.003 + 1.002 = 2.005 kohm` | `2.005 kohm` | `0 ohm` |
| In+ to sleeve | `9.125 + 1.002 = 10.127 kohm` | `10.127 kohm` | `0 ohm` |
| In- to sleeve | `9.139 + 1.003 = 10.142 kohm` | `10.142 kohm` | `0 ohm` |
| In+ to ring | `9.125 + 1.002 + 1.003 = 11.130 kohm` | `11.131 kohm` | `+1 ohm` |
| In- to tip | `9.139 + 1.003 + 1.002 = 11.144 kohm` | `11.145 kohm` | `+1 ohm` |
| In+ to In- | `9.125 + 1.002 + 1.003 + 9.139 = 20.269 kohm` | `20.271 kohm` | `+2 ohm` |

The four branch values are respectively `+0.275%`, `+0.429%`, `+0.200%`, and
`+0.300%` from their nominal `9.1 kohm`, `9.1 kohm`, `1.0 kohm`, and
`1.0 kohm` values. All are inside the specified `1%` tolerances. The two active-
leg calculated gains differ by only approximately `0.004 dB`.

**DECISION - POST-REBUILD RESISTANCE PASS:** the complete assembly has the
required symmetric two-leg passive topology, neither input lead is hard-tied to
sleeve, and there is no evidence of a short or material diode leakage under the
meter's test conditions. The `0-2 ohm` closure errors are negligible for this
decision. The separately reported `BZX 5V1` marking, close-to-`5 V` individual
results at `2 mA`, and anode-to-anode construction add useful component
evidence, but this resistance test cannot establish bidirectional clamp action;
Section 8 remains mandatory.

## 8. Integrated DC Attenuator/Clamp Test With The PL310QMD

### 8.1 Why The Whole Fixture Is Tested

The former `9 V` procedure injected current directly into a TRS node and
bypassed the corresponding `9.1 kohm` resistor. It is superseded. The revised
test drives each complete path from the amplifier-end cable:

```text
PL310QMD -> 2 m input lead -> 9.1 kohm -> TRS node
                                      -> 1.0 kohm and zener pair -> sleeve
```

This verifies cable polarity, series resistance, attenuation, clamp onset, and
post-test resistance integrity as one unit.

The PL310QMD provides two isolated `0-32 V` outputs and an internal series mode
for up to `64 V`. It supports constant-current operation and permits voltage
and current limits to be set with the output isolated. The combined voltage is
high enough to move a healthy `5.1 V` clamp into its low-current knee through
the complete divider. Because the `1.0 kohm` shunt remains installed, it cannot
drive the zener at its `5 mA` data-sheet test current; the purpose is to verify
the real assembled fixture's onset, not to reproduce the manufacturer's diode
characterization.

### 8.2 Safety And Instrument Preparation

This test uses up to `64 V DC`. Current limiting reduces fault energy but does
not make exposed conductors touch-safe or remove energy already stored in the
power supply. Use shrouded leads, an insulated TRS breakout, and an uncluttered
bench. Do not touch, probe-reposition, or rewire the circuit with the output on.

1. Disconnect the fixture from the SU-V570, UMC202HD, PC, and every other item.
2. Fit the PL310QMD's normal local-sense links; remote sense is unnecessary.
3. Select the instrument's documented `SERIES` mode and use its designated
   combined series-output terminals. Do not improvise external links while the
   supply is energized.
4. With both outputs isolated/off, set both sections' current limits to
   `10 mA`. The lower limit controls the common series current. Verify the
   setting from the supply indication before attaching the fixture.
5. Set both voltage controls to zero. Before attaching the fixture, use the
   U1282A in DCV autorange or a fixed range above `64 V` across the combined
   output to verify the total voltage and the relationship to the two supply
   meters. The U1282A's fixed `+/-60 V` range is too low for the maximum point.
   Once verified, the two supply indications may be summed for the sweep so the
   U1282A can remain fixed on the active node. Otherwise use a second suitably
   rated meter; never move the only meter between source and node while the
   output is enabled.
6. Insert the fixture TRS plug only into an insulated, unpowered breakout so
   tip, ring, and sleeve are accessible. Never insert it into the UMC202HD for
   this test.

The healthy fixture draws only about `64 V / 10.1 kohm = 6.3 mA`, so the supply
should remain in constant-voltage mode. Entry into current limit, a node that
remains near zero, or rapid or localized heating is a stop condition. Near the
maximum source voltage, a series resistor can dissipate approximately:

```text
P_Rseries ~= (6.4 mA)^2 x 9.1 kohm = 0.37 W
```

That is within the specified `0.5 W` rating but can make a small resistor
perceptibly warm if held there. Treat `55-64 V` as brief measurement points,
not a soak test; allow cooling between polarity runs and investigate smell,
discoloration, or heating inconsistent with this calculated dissipation.

### 8.3 Four Test Connections

Switch the output off and confirm zero volts before making each connection.
`HI` and `LO` below are the verified combined series-output terminals. The
input lead not being tested is tied to sleeve so the hookup reproduces the
fixture's common-ground operating condition without changing its construction.

| Test | PL310QMD HI | PL310QMD LO | Measure |
| --- | --- | --- | --- |
| Tip positive | Red | Black and sleeve | Tip relative to sleeve |
| Tip negative | Black and sleeve | Red | Tip relative to sleeve |
| Ring positive | Black | Red and sleeve | Ring relative to sleeve |
| Ring negative | Red and sleeve | Black | Ring relative to sleeve |

For each connection:

1. connect the U1282A from the active TRS node to sleeve in DCV mode, on a range
   that safely includes `6.5 V`, then start with the combined output at `0 V`;
2. enable the output and record actual source voltage, active-node voltage, and
   supply current at approximately `10`, `20`, `30`, `40`, `45.5`, `50`, `55`,
   `60`, and the highest available value not exceeding `64 V`;
3. increase voltage slowly, watching for constant-current indication, unstable
   readings, smell, or rapid or localized heating;
4. return to `0 V`, switch the output off, and verify zero before rewiring; and
5. allow the fixture to cool before the next polarity if a series resistor
   became warm at the highest-voltage points.

### 8.4 Predicted Curve And Acceptance Criteria

With the clamp inactive, the active node should follow the measured divider
ratio. For the tip leg:

| Applied DC | Unclamped tip prediction (`0.098943 x V`) |
| ---: | ---: |
| `10.0 V` | `0.989 V` |
| `20.0 V` | `1.979 V` |
| `30.0 V` | `2.968 V` |
| `40.0 V` | `3.958 V` |
| `45.5 V` | `4.502 V` |
| `50.0 V` | `4.947 V` |
| `55.0 V` | `5.442 V` |
| `60.0 V` | `5.937 V` |
| `64.0 V` | `6.332 V` |

The ring prediction is `0.098896 x V`, only about `3 mV` lower at `64 V`.

Pass the integrated DC test only when all of the following hold:

1. Both legs and both polarities remain linear within approximately `+/-1%`
   of their measured resistor ratios through `45.5 V`.
2. Near the maximum available `60-64 V`, every node shows a clear clamp knee:
   its magnitude is at least `0.3 V` below its individual unclamped prediction
   and does not exceed `6.2 V`.
3. The positive and negative curves for a node are reasonably symmetric. The
   installed tolerance grade is unknown, so investigate a high-voltage
   difference greater than approximately `0.3 V` against the individual
   analyser results rather than assigning an unverified B- or C-grade limit.
4. Total current remains below `10 mA`, the supply does not enter constant-
   current mode, and there is no rapid, localized, or otherwise unexplained
   heating beyond the calculated series-resistor dissipation.
5. After the test, all Section 7.4 resistance readings remain consistent and
   neither shunt nor series resistor has changed materially.

A node that continues to follow the straight unclamped prediction at maximum
voltage indicates an open, absent, or wrongly connected clamp. A prematurely
flattened curve indicates a wrong zener voltage, wrong orientation, leakage, or
an unintended path. Do not compensate by changing the acceptance limits.

### 8.5 Results Record

Record every available diode identifier, the body markings, analyser result,
and whether the pairs are common-cathode or common-anode before testing. Mark
unavailable manufacturer or family information explicitly as `unknown`; do not
invent a suffix from the measured voltage.

| Item | Recorded value |
| --- | --- |
| PL310QMD serial/calibration status |  |
| D1-D4 identity and characterization | Marked `BZX 5V1`; exact part number and manufacturer unknown; each close to `5 V` at `2 mA` on zener analyser |
| Pair orientation | Anode-to-anode, both pairs |
| Maximum combined source voltage | `64.50 V` measured (`64 V` nominal setting) |
| Current-limit setting, both sections | `10 mA` |

Record every step here; add rows if the actual maximum or clamp knee requires
an intermediate point.

| Test | Nominal source | Actual source | Node voltage | Supply current | CV/CC and observations |
| --- | ---: | ---: | ---: | ---: | --- |
| Tip positive | `10 V` | `10.03 V` | `0.990 V` | `~0.991 mA` derived | CV throughout run |
| Tip positive | `20 V` | `19.95 V` | `1.973 V` | `~1.970 mA` derived | CV throughout run |
| Tip positive | `30 V` | `29.98 V` | `2.964 V` | `~2.961 mA` derived | CV throughout run |
| Tip positive | `40 V` | `40.07 V` | `3.949 V` | `~3.958 mA` derived | CV throughout run |
| Tip positive | `45.5 V` | `45.56 V` | `4.459 V` | `~4.504 mA` derived | CV throughout run |
| Tip positive | `50 V` | `50.06 V` | `4.841 V` | `~4.956 mA` derived | CV throughout run |
| Tip positive | `55 V` | `55.10 V` | `5.183 V` | `~5.470 mA` derived | CV throughout run |
| Tip positive | `60 V` | `60.21 V` | `5.400 V` | `~6.007 mA` derived | CV throughout run |
| Tip positive | maximum, nominal `64 V` | `64.50 V` | `5.520 V` | `6 mA` indicated; `~6.464 mA` derived | CV; fixture only slightly warmer than ambient; no concerning heating |
| Tip negative | `10 V` | `9.99 V` | `-0.989 V` | `~0.986 mA` derived | CV throughout run |
| Tip negative | `20 V` | `19.92 V` | `-1.974 V` | `~1.967 mA` derived | CV throughout run |
| Tip negative | `30 V` | `29.96 V` | `-2.965 V` | `~2.958 mA` derived | CV throughout run |
| Tip negative | `40 V` | `40.08 V` | `-3.948 V` | `~3.960 mA` derived | CV throughout run |
| Tip negative | `45.5 V` | `45.53 V` | `-4.449 V` | `~4.502 mA` derived | CV throughout run |
| Tip negative | `50 V` | `50.05 V` | `-4.819 V` | `~4.957 mA` derived | CV throughout run |
| Tip negative | `55 V` | `55.10 V` | `-5.140 V` | `~5.475 mA` derived | CV throughout run |
| Tip negative | `60 V` | `60.12 V` | `-5.351 V` | `~6.002 mA` derived | CV throughout run |
| Tip negative | maximum, nominal `64 V` | `64.49 V` | `-5.463 V` | `6 mA` indicated; `~6.469 mA` derived | CV; mild heating comparable with tip positive; no concern |
| Ring positive | `10 V` | `10.05 V` | `0.990 V` | `~0.991 mA` derived | CV throughout run |
| Ring positive | `20 V` | `20.09 V` | `1.986 V` | `~1.981 mA` derived | CV throughout run |
| Ring positive | `30 V` | `30.02 V` | `2.969 V` | `~2.960 mA` derived | CV throughout run |
| Ring positive | `40 V` | `40.12 V` | `3.955 V` | `~3.957 mA` derived | CV throughout run |
| Ring positive | `45.5 V` | `45.53 V` | `4.454 V` | `~4.495 mA` derived | CV throughout run |
| Ring positive | `50 V` | `50.16 V` | `4.849 V` | `~4.958 mA` derived | CV throughout run |
| Ring positive | `55 V` | `55.00 V` | `5.167 V` | `~5.453 mA` derived | CV throughout run |
| Ring positive | `60 V` | `60.03 V` | `5.394 V` | `~5.978 mA` derived | CV throughout run |
| Ring positive | maximum, nominal `64 V` | `64.48 V` | `5.515 V` | `6 mA` indicated; `~6.452 mA` derived | CV; mild heating comparable with earlier runs; no concern |
| Ring negative | `10 V` | `9.99 V` | `-0.990 V` | `~0.985 mA` derived | CV throughout run |
| Ring negative | `20 V` | `20.00 V` | `-1.978 V` | `~1.972 mA` derived | CV throughout run |
| Ring negative | `30 V` | `29.96 V` | `-2.963 V` | `~2.954 mA` derived | CV throughout run |
| Ring negative | `40 V` | `40.09 V` | `-3.954 V` | `~3.954 mA` derived | CV throughout run |
| Ring negative | `45.5 V` | `45.62 V` | `-4.467 V` | `~4.503 mA` derived | CV throughout run |
| Ring negative | `50 V` | `50.12 V` | `-4.846 V` | `~4.954 mA` derived | CV throughout run |
| Ring negative | `55 V` | `55.16 V` | `-5.185 V` | `~5.468 mA` derived | CV throughout run |
| Ring negative | `60 V` | `60.16 V` | `-5.403 V` | `~5.992 mA` derived | CV throughout run |
| Ring negative | maximum, nominal `64 V` | `64.46 V` | `-5.515 V` | `6 mA` indicated; `~6.450 mA` derived | CV; mild heating comparable with earlier runs; no concern |

#### 8.5.1 Tip-Positive Partial Outcome

**USER-REPORTED MEASUREMENT, 2026-09-02:** the Agilent U1282A measured tip
positive relative to sleeve in DC-voltage mode on its `60 V` range. A separate
Agilent U1272A measured the PL310QMD combined output on its `300 V` range. All
reported values are DC volts. The supply remained in CV mode throughout, its
maximum indicated current was `6 mA` subject to uncertain internal-ammeter
accuracy, and the fixture became only slightly warmer than ambient with no
concerning heating.

| Supply | Measured node | Unclamped prediction | Difference | Relative difference |
| ---: | ---: | ---: | ---: | ---: |
| `10.03 V` | `0.990 V` | `0.992 V` | `-0.002 V` | `-0.24%` |
| `19.95 V` | `1.973 V` | `1.974 V` | `-0.001 V` | `-0.05%` |
| `29.98 V` | `2.964 V` | `2.966 V` | `-0.002 V` | `-0.08%` |
| `40.07 V` | `3.949 V` | `3.965 V` | `-0.016 V` | `-0.40%` |
| `45.56 V` | `4.459 V` | `4.508 V` | `-0.049 V` | `-1.08%` |
| `50.06 V` | `4.841 V` | `4.953 V` | `-0.112 V` | `-2.26%` |
| `55.10 V` | `5.183 V` | `5.452 V` | `-0.269 V` | `-4.93%` |
| `60.21 V` | `5.400 V` | `5.957 V` | `-0.557 V` | `-9.36%` |
| `64.50 V` | `5.520 V` | `6.382 V` | `-0.862 V` | `-13.50%` |

The series current inferred from `(Vsupply - Vnode) / 9.125 kohm` rises from
approximately `0.991 mA` to `6.464 mA`. Subtracting the `1.002 kohm` shunt
current suggests increasing zener current of approximately `17 uA` at
`40.07 V`, `54 uA` at `45.56 V`, `124 uA` at `50.06 V`, `298 uA` at
`55.10 V`, `617 uA` at `60.21 V`, and `955 uA` at `64.50 V`. Treat the few-
microamp results below `40 V` as dominated by combined meter and resistor
uncertainty; the monotonic high-voltage trend is the meaningful evidence. The
PL310QMD's `6 mA` maximum indication is consistent with the derived `6.464 mA`
given its resolution and uncertain ammeter accuracy.

At the highest measured point, the series-resistor dissipation inferred from
`I^2 R` is approximately `(6.464 mA)^2 x 9.125 kohm = 0.381 W`, about `76%` of
its stated `0.5 W` rating. The reported slight warmth is therefore expected
from the series resistor; rapid or localized heating would not be. The clamp-
pair current and total dissipation at that point are only approximately
`0.955 mA` and `5.3 mW`, respectively, so substantial zener self-heating is
unlikely. Conducted heat and an unknown pair temperature coefficient can still
move the exact knee slightly; begin each polarity run from a comparable cooled
state.

**PARTIAL DECISION:** the tip-positive curve is linear well within `1%` through
`40.07 V` and shows a smooth, credible zener knee. At `64.50 V`, the measured
node is `0.862 V` below its unclamped prediction and remains below `6.2 V`, so
the high-voltage clamp criterion passes comfortably. The actual source was
`0.50 V` above the procedural `64 V` ceiling because the nominal maximum setting
measured high; record it, but do not intentionally exceed `64 V` on later runs.
At `45.56 V`, the `-1.08%` deviation is marginally beyond the
approximate `1%` linearity target. Record this as `BORDERLINE`, not a failure or
an adjusted criterion. Section 8.5.2 subsequently establishes close negative-
polarity symmetry and retains the `BORDERLINE` label. The departure has
negligible consequence at the intended approximately `1 V RMS` acoustic-
measurement level, but it characterizes the clamp's soft low-current knee.

#### 8.5.2 Tip-Negative Partial Outcome

**USER-REPORTED MEASUREMENT, 2026-09-02:** PL310QMD HI was connected to black
input `-` and sleeve, and LO to red input `+`. The Agilent U1282A remained with
its positive lead on tip and negative lead on sleeve, so the reported node
voltages are correctly negative. The U1272A measured positive source magnitude.
Both PL310QMD current limits were `10 mA`; it remained in CV mode, indicated
`6 mA` maximum, and produced mild heating comparable with the tip-positive run.

| Supply magnitude | Measured node magnitude | Unclamped prediction | Difference | Relative difference |
| ---: | ---: | ---: | ---: | ---: |
| `9.99 V` | `0.989 V` | `0.988 V` | `+0.001 V` | `+0.06%` |
| `19.92 V` | `1.974 V` | `1.971 V` | `+0.003 V` | `+0.15%` |
| `29.96 V` | `2.965 V` | `2.964 V` | `+0.001 V` | `+0.02%` |
| `40.08 V` | `3.948 V` | `3.966 V` | `-0.018 V` | `-0.45%` |
| `45.53 V` | `4.449 V` | `4.505 V` | `-0.056 V` | `-1.24%` |
| `50.05 V` | `4.819 V` | `4.952 V` | `-0.133 V` | `-2.69%` |
| `55.10 V` | `5.140 V` | `5.452 V` | `-0.312 V` | `-5.72%` |
| `60.12 V` | `5.351 V` | `5.948 V` | `-0.597 V` | `-10.04%` |
| `64.49 V` | `5.463 V` | `6.381 V` | `-0.918 V` | `-14.38%` |

The first three points agree with the unloaded prediction within `0.16%`;
their algebraically negative inferred clamp currents are sub-`4 uA` residuals
from meter and resistance uncertainty, not physical reverse current. At
`64.49 V`, the inferred series current is `6.469 mA`, shunt current is
`5.452 mA`, and clamp current is `1.017 mA`. Inferred series-resistor and clamp-
pair dissipation are approximately `0.382 W` and `5.6 mW`, respectively.

The positive and negative tip curves are closely matched. At the almost
identical maximum sources of `64.50 V` and `64.49 V`, their node magnitudes are
`5.520 V` and `5.463 V`, a difference of only `0.057 V`, comfortably below the
`0.3 V` investigation threshold. The magnitude difference rises smoothly from
approximately `1 mV` below `40 V` to `10 mV` at `45.5 V`, `43 mV` at `55.10 V`,
and `57 mV` at maximum source.

**PARTIAL DECISION:** tip-negative high-voltage clamp action and tip-pair
symmetry pass. At `45.53 V`, the node is `1.24%` below its unclamped prediction,
which closely reproduces the tip-positive `1.08%` departure and supports a
normal, symmetric soft zener knee rather than a wiring or component fault. It
nevertheless remains outside the stated approximate `1%` linearity target, so
retain the tip pair's `45.5 V` linearity status as `BORDERLINE`; do not alter the
criterion. The `10 mA` limits, CV operation, `6 mA` indication, and expected mild
heating close this polarity's operating observations.

#### 8.5.3 Ring-Positive Partial Outcome

**USER-REPORTED MEASUREMENT, 2026-09-02:** PL310QMD HI was connected to
black/input `-`, and LO to red/input `+` and sleeve. The U1282A measured ring
positive relative to sleeve; the U1272A measured positive source magnitude.
Both supply current limits were `10 mA`; the supply remained in CV mode,
indicated `6 mA` maximum, and produced the same mild, non-concerning heating as
the tip runs.

| Supply | Measured node | Unclamped prediction | Difference | Relative difference |
| ---: | ---: | ---: | ---: | ---: |
| `10.05 V` | `0.990 V` | `0.994 V` | `-0.004 V` | `-0.39%` |
| `20.09 V` | `1.986 V` | `1.987 V` | `-0.001 V` | `-0.04%` |
| `30.02 V` | `2.969 V` | `2.969 V` | `+0.000 V` | `+0.01%` |
| `40.12 V` | `3.955 V` | `3.968 V` | `-0.013 V` | `-0.32%` |
| `45.53 V` | `4.454 V` | `4.503 V` | `-0.049 V` | `-1.08%` |
| `50.16 V` | `4.849 V` | `4.961 V` | `-0.112 V` | `-2.25%` |
| `55.00 V` | `5.167 V` | `5.439 V` | `-0.272 V` | `-5.01%` |
| `60.03 V` | `5.394 V` | `5.937 V` | `-0.543 V` | `-9.14%` |
| `64.48 V` | `5.515 V` | `6.377 V` | `-0.862 V` | `-13.51%` |

At `64.48 V`, the measured `9.139 kohm` series and `1.003 kohm` shunt paths
imply `6.452 mA` series current, `5.499 mA` shunt current, and `0.954 mA` clamp
current. Inferred series-resistor and clamp-pair dissipation are approximately
`0.380 W` and `5.3 mW`, matching the observed mild heating and `6 mA` supply
indication.

Ring positive also matches tip positive exceptionally closely. Their maximum
node voltages differ by only `0.005 V` at `64.48-64.50 V` source, and their
relative departures from the respective unloaded dividers are `-13.51%` and
`-13.50%`. At approximately `45.5 V`, both are `1.08%` below prediction. This
agreement checks not merely the nominal component values but the installed
low-current knee of the two separate clamp pairs.

**PARTIAL DECISION:** ring-positive high-voltage clamp, current, CV, and thermal
behaviour pass. Its `45.5 V` linearity is `BORDERLINE`, consistently with both
tip polarities, rather than evidence of a ring-leg fault. Ring negative remains
the only unmeasured DC polarity; its comparison will decide ring-pair symmetry
and complete the four voltage curves.

#### 8.5.4 Ring-Negative And Four-Curve Outcome

**USER-REPORTED MEASUREMENT, 2026-09-02:** PL310QMD HI was connected to
red/input `+` and sleeve, and LO to black/input `-`. The U1282A retained its
positive lead on ring and negative lead on sleeve, so the reported node voltages
are correctly negative. Both current limits were `10 mA`; the supply remained
in CV mode, indicated `6 mA` maximum, and produced the same mild,
non-concerning heating as the preceding runs.

| Supply magnitude | Measured node magnitude | Unclamped prediction | Difference | Relative difference |
| ---: | ---: | ---: | ---: | ---: |
| `9.99 V` | `0.990 V` | `0.988 V` | `+0.002 V` | `+0.21%` |
| `20.00 V` | `1.978 V` | `1.978 V` | `+0.000 V` | `+0.00%` |
| `29.96 V` | `2.963 V` | `2.963 V` | `+0.000 V` | `+0.00%` |
| `40.09 V` | `3.954 V` | `3.965 V` | `-0.011 V` | `-0.27%` |
| `45.62 V` | `4.467 V` | `4.512 V` | `-0.045 V` | `-0.99%` |
| `50.12 V` | `4.846 V` | `4.957 V` | `-0.111 V` | `-2.23%` |
| `55.16 V` | `5.185 V` | `5.455 V` | `-0.270 V` | `-4.95%` |
| `60.16 V` | `5.403 V` | `5.950 V` | `-0.547 V` | `-9.19%` |
| `64.46 V` | `5.515 V` | `6.375 V` | `-0.860 V` | `-13.49%` |

At `64.46 V`, the ring paths imply `6.450 mA` series current, `5.499 mA`
shunt current, and `0.951 mA` clamp current. Inferred series-resistor and clamp-
pair dissipation are approximately `0.380 W` and `5.2 mW`, consistent with the
`6 mA` indication and mild heating.

Ring polarity symmetry is exceptionally close: both polarities measure exactly
`5.515 V` to the reported precision at `64.48 V` and `64.46 V` sources. Across
all four curves, the maximum node magnitudes span only `5.463-5.520 V`, a total
spread of `0.057 V`, while every node is `0.860-0.918 V` below its unclamped
prediction and below the `6.2 V` ceiling.

At the approximately `45.5 V` points, departures are `-1.08%` tip positive,
`-1.24%` tip negative, `-1.08%` ring positive, and `-0.99%` ring negative. The
stated approximate `+/-1%` criterion is therefore not met exactly by three
curves, with the largest miss only `0.24` percentage point. Because all four
curves remain within `0.45%` through `40 V`, then enter the same smooth knee,
the deviation is attributable to the intended low-current clamp behaviour and
not divider nonlinearity or a construction fault. At `45.5 V` it represents at
most approximately `0.11 dB` of compression; at the intended approximately
`1 V RMS` measurement level the clamp is inactive.

**FOUR-CURVE DECISION:** `PASS WITH CHARACTERIZED LINEARITY DEVIATION`. Do not
rewrite or claim exact compliance with the original approximate `1%` target;
accept the measured `0.99-1.24%` soft-knee departure explicitly because clamp
action, four-way symmetry, current, CV operation, and thermal behaviour all
pass with wide margins and the deviation has no material effect in the intended
operating range. At this stage the integrated DC gate remained administratively
`IN PROGRESS` until the required cooled post-stress Section 7.4 resistance
matrix confirmed that no component or connection had changed; Section 8.5.5
records that subsequent pass.

Then summarize the decision values:

| Test | Node at `45.5 V` | Node at maximum source voltage | Unclamped maximum prediction | Maximum current | Result |
| --- | ---: | ---: | ---: | ---: | --- |
| Tip positive | `4.459 V` at `45.56 V` source | `5.520 V` at `64.50 V` source | `6.382 V` | `6 mA` indicated; `~6.464 mA` derived | CLAMP KNEE, CV/CURRENT, AND THERMAL BEHAVIOUR PASS; 45.5 V LINEARITY BORDERLINE |
| Tip negative | `-4.449 V` at `45.53 V` source | `-5.463 V` at `64.49 V` source | `-6.381 V` | `6 mA` indicated; `~6.469 mA` derived | CLAMP KNEE, TIP-PAIR SYMMETRY, CV/CURRENT, AND THERMAL BEHAVIOUR PASS; 45.5 V LINEARITY BORDERLINE |
| Ring positive | `4.454 V` at `45.53 V` source | `5.515 V` at `64.48 V` source | `6.377 V` | `6 mA` indicated; `~6.452 mA` derived | CLAMP KNEE, CV/CURRENT, AND THERMAL BEHAVIOUR PASS; 45.5 V LINEARITY BORDERLINE |
| Ring negative | `-4.467 V` at `45.62 V` source | `-5.515 V` at `64.46 V` source | `-6.375 V` | `6 mA` indicated; `~6.450 mA` derived | CLAMP KNEE, RING-PAIR SYMMETRY, CV/CURRENT, AND THERMAL BEHAVIOUR PASS; 45.5 V LINEARITY WITHIN 1% |

**CURVE-SET DECISION:** all four powered curves pass clamp action, polarity
symmetry, current, CV, and thermal checks. The curve set passes with the
explicitly characterized `45.5 V` linearity deviation above; it does not meet
the approximate `1%` target exactly. Section 8.5.5 records the subsequently
completed post-stress resistance check and final integrated-DC decision.

#### 8.5.5 Cooled Post-Stress Resistance Check

After the fixture has returned to ambient temperature, disconnect it from the
PL310QMD and every other device. With the U1282A in the same nulled-lead,
`60 kohm` resistance setup used for Section 7.4, repeat the complete nine-value
matrix and compare it directly with the pre-stress baseline. Pass when every
path remains consistent with the original `0.001 kohm` display resolution and
all redundant sums still close without a new unexplained path. A material
change, open path, or new low resistance is a stop condition.

**USER-REPORTED MEASUREMENT, 2026-09-02:** after the powered sweep and cooling,
the complete fixture was measured with the Agilent U1282A in resistance mode on
its `60 kohm` range. Lead resistance was nulled before the first reading. The
user noted that room temperature may have fallen slightly during the evening.

| From / to | Ring | Tip | In+ | In- |
| --- | ---: | ---: | ---: | ---: |
| Sleeve | `1.004` | `1.002` | `10.130` | `10.146` |
| Ring | - | `2.006` | `11.133` | `9.141` |
| Tip | - | - | `9.127` | `11.149` |
| In+ | - | - | - | `20.275` |
| In- | - | - | - | - |

Every direct path changed by only `0-4 ohm` from its pre-stress value:

| Path | Pre-stress | Post-stress | Change |
| --- | ---: | ---: | ---: |
| Sleeve-ring | `1.003 kohm` | `1.004 kohm` | `+1 ohm` |
| Sleeve-tip | `1.002 kohm` | `1.002 kohm` | `0 ohm` |
| Sleeve-In+ | `10.127 kohm` | `10.130 kohm` | `+3 ohm` |
| Sleeve-In- | `10.142 kohm` | `10.146 kohm` | `+4 ohm` |
| Ring-tip | `2.005 kohm` | `2.006 kohm` | `+1 ohm` |
| Ring-In+ | `11.131 kohm` | `11.133 kohm` | `+2 ohm` |
| Ring-In- | `9.139 kohm` | `9.141 kohm` | `+2 ohm` |
| Tip-In+ | `9.125 kohm` | `9.127 kohm` | `+2 ohm` |
| Tip-In- | `11.145 kohm` | `11.149 kohm` | `+4 ohm` |
| In+-In- | `20.271 kohm` | `20.275 kohm` | `+4 ohm` |

The post-stress redundant identities remain closed within `0-2 ohm`:

| Identity | Constituent-path sum | Direct reading | Difference |
| --- | ---: | ---: | ---: |
| Ring-tip | `1.004 + 1.002 = 2.006 kohm` | `2.006 kohm` | `0 ohm` |
| In+ to sleeve | `9.127 + 1.002 = 10.129 kohm` | `10.130 kohm` | `+1 ohm` |
| In- to sleeve | `9.141 + 1.004 = 10.145 kohm` | `10.146 kohm` | `+1 ohm` |
| In+ to ring | `9.127 + 1.002 + 1.004 = 11.133 kohm` | `11.133 kohm` | `0 ohm` |
| In- to tip | `9.141 + 1.004 + 1.002 = 11.147 kohm` | `11.149 kohm` | `+2 ohm` |
| In+ to In- | `9.127 + 1.002 + 1.004 + 9.141 = 20.274 kohm` | `20.275 kohm` | `+1 ohm` |

The largest direct change is `4 ohm`, only about `0.04%` of a `10.1 kohm`
path. The branch changes are `0-2 ohm`, at most approximately `0.10%` of a
`1 kohm` shunt. These shifts are negligible relative to component tolerance and
are compatible with the meter's `1 ohm` display resolution, contact variation,
and the reported ambient change. Their all-positive sign is not used to infer a
temperature coefficient.

**DECISION - POST-STRESS RESISTANCE PASS:** there is no evidence of resistor
damage, an open clamp, a changed connection, or a new leakage path. Together
with the four powered curves, this closes the complete integrated PL310QMD DC
test as `PASS WITH CHARACTERIZED 45.5 V LINEARITY DEVIATION`.

## 9. Unpowered System Ground-Path Audit

The fixture does not hard-connect a speaker terminal to sleeve. In isolation,
each terminal has approximately `10.1 kohm` to sleeve; with a loudspeaker
connected between them, the two common-mode paths can approach
`10.1 kohm || 10.1 kohm = 5.05 kohm`.

The likely lower-resistance bond is the UMC202HD Output 1-to-SU-V570 RCA
playback cable. It normally connects interface output sleeve/shield to the RCA
outer shell, which the amplifier measurements place near speaker-negative and
chassis potential. USB and the PC may then reference this audio ground to
protective earth. That is a signal-reference path, not protective earthing.

Perform the following with every item unplugged from the wall and discharged,
using only the battery-powered meter in resistance mode. Unless a step says
otherwise, remove USB and every other interconnect as well. Null the meter leads
before the low-resistance readings. Use a verified, unpowered central-TRS
breakout to expose Input 2 sleeve; its tip/ring load resistors may remain fitted,
but connect nothing else to it.

1. With the UMC202HD alone, unpowered, and disconnected from USB and every other
   cable, measure Input 2 TRS sleeve to a known bare-metal chassis point, sleeve
   to the USB connector's metal shell, and bare chassis to USB shell. Do not
   probe the small USB signal contacts unless a safe mapped breakout is already
   available. If a chassis reading is open, do not infer isolation from applied
   probe pressure alone. Prove both chassis contacts by obtaining a low-resistance
   reading between two separated points on the same nominally bare chassis
   panel, without deliberately damaging its finish. If that control is also
   open, move to verified conductive points such as an uncoated chassis edge or
   metal fixing that is known to contact the panel, then repeat all affected
   chassis measurements.
2. With the intended USB cable disconnected at both ends, measure metal plug
   shell to metal plug shell. Do not probe any USB signal or power contacts.
3. Perform the following as one PC-shutdown window; no later fixture test
   requires the PC to be stripped down again. Shut the PC down, disconnect its
   mains plug from the wall, and remove every other cable, including displays,
   network, audio, and peripherals. If it has a detachable Class-I power cord,
   leave the PC end connected so the protective-earth pin of the free wall plug
   remains available; never probe a wall socket.

   1. With USB still disconnected, measure the selected PC USB socket's metal
      shell to a verified bare-metal PC-chassis point.
   2. If the PC is Class I, measure that chassis point to the protective-earth
      pin of its disconnected mains plug. Record `N/A` for a Class-II PC with no
      protective-earth contact.
   3. Connect only the already mapped USB cable and the otherwise isolated,
      unpowered UMC202HD. Measure Input 2 sleeve to the PC chassis point.
   4. If the PC is Class I, also measure Input 2 sleeve directly to the
      protective-earth pin of the disconnected mains plug.

   If any expected chassis result is open, validate the PC probe contact by
   measuring between two separated bare-metal points on the same PC chassis.
4. Resistance-map the intended Output 1-to-RCA playback cable. First identify
   whether its output plug is three-contact TRS or two-contact TS, then record
   every available plug contact to RCA centre and shell. A TS plug is not a TRS
   plug with an omitted ring: its long sleeve also contacts the UMC202HD output
   jack's ring spring and therefore grounds that contact, which would be the
   cold leg if the output were actively balanced.
   Unless the manufacturer explicitly confirms that operation as safe or the
   powered no-load check in Section 10.1 shows that ring is already inactive or
   grounded, use a TRS-to-RCA cable wired tip to RCA centre, sleeve to RCA shell,
   and ring open.
5. With both devices still unplugged, connect that cable and measure Input 2
   sleeve to the selected SU-V570 RCA shell and corresponding speaker negative.
6. Remove the playback cable. Confirm that the fixture alone still gives
   approximately `10.1 kohm` from each amplifier lead to sleeve, or about
   `5.05 kohm` only when the two leads are joined through a low-resistance load.

Record the audit in stages:

| Stage | Measurement | Result |
| --- | --- | --- |
| Interface alone | Input 2 sleeve to UMC202HD bare chassis | `OPEN`; validated by chassis control |
| Interface alone | Input 2 sleeve to UMC202HD USB shell | `0.035 ohm`; low-resistance bond verified |
| Interface alone | UMC202HD bare chassis to USB shell | `OPEN`; validated by chassis control |
| Interface-alone control | Two separated points on the same nominally bare chassis panel | `0.013 ohm`; probe contact and chassis continuity verified |
| USB cable alone | Metal plug shell to metal plug shell | `0.130 ohm`; shield continuity verified |
| PC alone, mains disconnected | Selected PC USB socket shell to bare PC chassis | `0.170 ohm`; low-resistance bond verified |
| PC alone, mains disconnected | Bare PC chassis to mains-plug protective earth, if Class I | `0.245 ohm`; low-resistance bond verified |
| USB and PC, mains disconnected | Input 2 sleeve to bare PC chassis | `0.412 ohm`; end-to-end low-resistance bond verified |
| USB and PC, mains disconnected | Input 2 sleeve to mains-plug protective earth, if Class I | `0.379 ohm`; complete earth-reference path verified |
| Playback cable map | Plug type | Two-contact mono TS; no ring contact |
| Playback cable map | TS tip to RCA centre / shell | `0.244 ohm` / `OPEN` |
| Playback cable map | TS sleeve to RCA centre / shell | `OPEN` / `0.078 ohm` |
| Isolated UMC202HD, unpowered | Tested rear output ring to sleeve/shield through verified TRS breakout | `0.021 ohm`; breakout alone reads `OPEN` |
| Playback cable output compatibility | TS sleeve grounds the UMC202HD TRS jack's ring contact when inserted | PASS - both powered, driven outputs are ring-grounded, so the TS plug adds no new cold-leg short |
| UMC202HD and SU-V570 joined only by playback cable | Input 2 sleeve to RCA shell and corresponding speaker negative | PASS - `0.061 ohm` to RCA shell; `0.174 ohm` to speaker negative |
| Fixture alone | Each amplifier lead to sleeve | PASS - post-stress matrix gives In+ `10.130 kohm` and In- `10.146 kohm` to sleeve |

**PASS:** every path is explained by the measured cable map; the playback path
provides the one expected low-resistance SU-V570-to-UMC202HD signal-ground bond;
and the fixture alone retains kilo-ohm isolation from both amplifier leads.

**STOP:** either fixture lead is hard-connected to sleeve, a path cannot be
explained, or there is a tingle, visible spark, damaged mains wiring, or other
appliance-safety concern. Never defeat PC protective earth to cure hum.

**USER-REPORTED MEASUREMENT - 2026-09-02:** with the UMC202HD isolated as
specified, Input 2 sleeve to the USB connector metal shell measured
`0.035 ohm`. Input 2 sleeve to nominally bare UMC202HD chassis and that chassis
point to USB shell both read `OPEN`. Considerable probe pressure was applied in
an attempt to penetrate oxidation or anodizing.

**INFERRED:** the `0.035 ohm` result verifies a direct low-resistance DC bond
between Input 2 sleeve and USB shield shell, within probe/contact uncertainty.
It does not by itself establish a connection to the USB signal contacts, PC
chassis, or protective earth. The two open chassis readings are mutually
consistent with an enclosure isolated from sleeve and USB shield, but remain
conditional: an open measurement cannot prove that either probe made electrical
contact through a surface finish.

**USER-REPORTED CONTROL MEASUREMENT - 2026-09-02:** two separated chassis
points measured `0.013 ohm` with very firm pressure applied to both probes.

**DECISION - INTERFACE-ALONE STAGE PASS:** the control proves that both probes
reached conductive enclosure metal and that the tested chassis points belong to
one low-resistance metal structure. The earlier open readings therefore establish
DC isolation of that chassis from the hard-bonded Input 2 sleeve/USB-shell node
under the isolated, unpowered test conditions. This result does not establish
isolation at RF or while other cables are connected.

**USER-REPORTED USB-CABLE MEASUREMENT - 2026-09-02:** metal-shell to metal-shell
resistance along the disconnected intended USB cable measured `0.130 ohm`.

**DECISION - USB-CABLE STAGE PASS:** the cable provides low-resistance
end-to-end shield continuity. Combined with the UMC202HD's `0.035 ohm`
sleeve-to-USB-shell bond, this carries the Input 2 sleeve node to the metal shell
of the PC-end USB plug when the cable is connected. It does not by itself prove
that the PC bonds its USB shell to chassis or protective earth.

**USER-REPORTED ISOLATED-PC MEASUREMENTS - 2026-09-02:** using the Agilent
U1282A in auto-ranging resistance mode with its leads nulled, measured PC USB
socket shell to bare PC chassis `0.170 ohm`, PC chassis to the protective-earth
pin of the free mains plug `0.245 ohm`, UMC202HD Input 2 sleeve to PC chassis
`0.412 ohm`, and Input 2 sleeve to the free plug's protective-earth pin
`0.379 ohm`. Considerable and somewhat variable probe pressure was required at
the PC chassis while working in a constrained position; the last digits are not
treated as precision results.

An idealized sum of the separately measured shell path to PC chassis is

```text
0.035 + 0.130 + 0.170 = 0.335 ohm
```

before allowing for the mated USB connector. The direct `0.412 ohm` reading is
only `0.077 ohm` higher. The direct sleeve-to-PE reading need not equal
`0.412 + 0.245 = 0.657 ohm`: probe contacts were remade, the chassis is a
distributed conductor rather than a single mandatory series junction, and USB
shield and circuit-ground bonds can provide parallel routes. The four readings
are therefore used to classify topology, not to assign precise milliohm
resistances.

**DECISION - ISOLATED-PC/PE STAGE PASS:** the PC bonds its USB connector shell
to chassis and chassis to protective earth. With the intended USB cable fitted,
the UMC202HD Input 2 sleeve has a directly measured low-resistance path to both
PC chassis and the protective-earth pin. This confirms an earth-reference path;
it is not a protective-conductor resistance test and does not certify appliance
or installation safety.

**USER-REPORTED PLAYBACK-CABLE MAP - 2026-09-02:** using the Agilent U1282A in
auto-ranging resistance mode, measured the two-contact mono output plug's tip to
RCA centre `0.244 ohm`, tip to RCA shell `OPEN`, sleeve to RCA centre `OPEN`,
and sleeve to RCA shell `0.078 ohm`. There is no ring contact. These results map
the cable cleanly as a conventional TS-to-RCA unbalanced cable.

**INITIAL OUTPUT-COMPATIBILITY HOLD:** the official UMC202HD documentation identifies
Outputs 1 and 2 as `1/4-inch TRS` line outputs but does not explicitly authorize
grounding the ring/cold output with a TS plug. Insertion of this two-contact plug
would make exactly that connection inside the jack. Cable continuity therefore
passes, but this particular cable is not approved for the powered playback path
on the available evidence. The conservative replacement is a TRS-to-RCA cable
wired tip-to-centre and sleeve-to-shell with ring left open. Re-map that final
cable before continuing the connected ground-path audit.

**USER-REPORTED FOLLOW-UP - 2026-09-02:** with a verified TRS breakout inserted
into one otherwise completely disconnected and unpowered UMC202HD rear output,
ring to shield/sleeve measured `0.021 ohm`. The same breakout measured `OPEN`
ring-to-shield while unplugged on the bench.

**INFERRED:** this is strong evidence that the tested output ring is deliberately
bonded to ground at DC, rather than being shorted by the breakout. If that bond
also exists while powered, inserting the TS playback cable adds no new ring-to-
sleeve short and the compatibility hold can be lifted for that output. The
unpowered result alone is not conclusive because an output-muting or protection
circuit could ground a conductor only while power is absent. The user did not
identify which rear output was tested, and Section 10 currently depends on the
topology of Output 2 as well as the playback path's Output 1.

**USER-REPORTED POWERED OUTPUT FOLLOW-UP - 2026-09-03:** with REW routed only to
the channel under test, driven Output 1 measured `78.69 mV` tip-sleeve,
`0.002 mV` ring-sleeve, and `78.73 mV` tip-ring. The earlier correctly driven
Output 2 results remain `78.9 mV`, `0.000 mV`, and `78.84 mV`, respectively.

**DECISION - PLAYBACK-CABLE COMPATIBILITY PASS:** both powered outputs are
ring-grounded. Inserting the mapped mono TS playback plug therefore connects
Output 1 ring to a sleeve node to which it is already connected; it does not
short an active cold leg. Lift the TS-cable compatibility hold. This conclusion
is specific to the measured UMC202HD and mapped cable, and does not generalize
to an arbitrary TRS output.

**EVIDENCE REUSE - FIXTURE-ALONE PASS:** the cooled post-stress complete-unit
matrix was taken with the fixture disconnected and records `10.130 kohm` from
input `+` to sleeve and `10.146 kohm` from input `-` to sleeve. Those are the
same two paths required by audit step 6. Repeating them without an intervening
wiring change would add no information, so the existing matrix closes the
fixture-alone stage.

**USER-REPORTED CONNECTED-PLAYBACK MEASUREMENT - 2026-09-03:** with the Agilent
U1282A in auto-ranging resistance mode and its leads nulled, the UMC202HD and
SU-V570 were unpowered and disconnected from mains. The UMC202HD had no USB or
other external connection apart from the intended dual analogue playback cable
to the corresponding SU-V570 RCA input channels and the breakout used to reach
Input 2 sleeve. Input 2 sleeve measured `0.061 ohm` to the corresponding RCA
shell and `0.174 ohm` to the corresponding SU-V570 speaker-negative terminal.
The user's reference to UMC202HD rear "inputs 1 and 2" is interpreted here as
rear **Outputs 1 and 2**, because those are the rear analogue sockets connected
to the amplifier's RCA inputs.

**DERIVED:** the resistance attributable beyond the measured RCA shell is
approximately

```text
0.174 ohm - 0.061 ohm = 0.113 ohm.
```

That agrees closely with the earlier direct `0.120-0.150 ohm` speaker-negative-
to-RCA-shell range (mean `0.130 ohm`). The `0.007 ohm` difference from the
earlier minimum and `0.017 ohm` difference from its mean are immaterial beside
remade probe contacts and the U1282A's low-ohms uncertainty. With both channels
of a dual playback cable fitted, parallel shield and common signal-ground paths
can also make the end-to-end value slightly lower than a simple sum of isolated
measurements.

**DECISION - UNPOWERED SYSTEM GROUND-PATH AUDIT PASS:** both connected readings
are stable low-resistance metallic paths and agree with the independently mapped
playback cable and SU-V570 common-signal-ground measurements. Every audit path
is now explained, while the fixture-alone matrix still proves that neither
amplifier lead is hard-connected to sleeve. This closes Section 9. It does not
approve powered amplifier use: Section 10 AC transfer/noise commissioning
remains open.

## 10. AC Transfer, Polarity, And Linearity Commissioning

### 10.1 Rear-Output Topology Prerequisite

Before using the playback cable or treating Output 2 as a balanced source,
determine both rear outputs' powered no-load topology. Do not connect the
SU-V570, playback cable, reference fixture, microphone, or any other analogue
cable during this check.

1. Connect the UMC202HD only to the PC by USB and insert the verified TRS
   breakout into Output 1.
2. Set `DIRECT MONITOR` off and the `OUTPUT` knob fully down. In REW, select only
   Output 1 and generate a `1 kHz`, approximately `-20 dBFS` sine wave.
3. Put the U1282A in AC-voltage mode. Slowly raise `OUTPUT` only until the
   largest reading is approximately `50-100 mV RMS`.
4. Without moving the output control, record tip-to-sleeve, ring-to-sleeve, and
   tip-to-ring. Stop the generator before moving probes or the breakout. If a
   result fails the voltage-identity check below, repeat tip-to-ring before and
   after the two sleeve-referenced measurements without changing level.
5. Stop the generator, route REW to Output 2 only, move the breakout to Output
   2, and repeat. Never use resistance mode on the powered interface.

The channel-to-jack correspondence is mandatory: measure Output 1 only while
REW is driving Output 1, and measure Output 2 only while REW is driving Output
2. An idle jack's readings do not classify that output's topology. Keep REW
frequency and level and the physical `OUTPUT`-knob position unchanged between
the two driven-output tests.

| Powered no-load output | Tip-sleeve | Ring-sleeve | Tip-ring | Classification |
| --- | ---: | ---: | ---: | --- |
| Output 1 | `78.69 mV` | `0.002 mV` | `78.73 mV` | PASS - driven output is ring-grounded |
| Output 2 | `78.9 mV` | `0.000 mV` | `78.84 mV` | PASS - driven output is ring-grounded |

For a stable simultaneous measurement, the phasor magnitudes must satisfy

```text
abs(|Vtip-sleeve| - |Vring-sleeve|) <= |Vtip-ring|
|Vtip-ring| <= |Vtip-sleeve| + |Vring-sleeve|
```

The DMM readings are sequential rather than simultaneous. Apply the identity
within the documented meter resolution and any small source-level drift; a
sub-`1 mV` closure residual that also lies well inside the classification
criteria below is not a failure. A large residual remains an invalid result.

**SUPERSEDED DIAGNOSTIC HISTORY - 2026-09-02:** with REW inadvertently driving
Output 2, the idle Output 1 was recorded as `0.002 mV` tip-sleeve, `0.001 mV`
ring-sleeve, and `27.42 mV` tip-ring. Its sleeve-referenced readings would
constrain tip-ring to `0.001-0.003 mV`, so that row could not describe one
steady circuit state and was correctly classified as invalid rather than as an
output fault. The correctly driven Output 2 measured `78.9 mV` tip-sleeve,
`0.000 mV` ring-sleeve, and `78.84 mV` tip-ring.

**USER-REPORTED OUTPUT 1 REPEAT - 2026-09-03:** with the Agilent U1282A in
auto-ranging AC-millivolt mode and REW routed only to Output 1, measured
`78.69 mV` tip-sleeve, `0.002 mV` ring-sleeve, and `78.73 mV` tip-ring. Output 2
was not repeated; its table row retains the valid 2026-09-02 driven result.

**DERIVED:** on Output 1, ring-sleeve is only approximately `0.0025%` of tip-
sleeve, while tip-ring differs from tip-sleeve by `0.04 mV`, approximately
`0.051%`. The sequential values exceed the ideal phasor upper bound by only
`0.038 mV`, approximately `0.048%`, which is negligible beside the `1 mV`/
`2%` classification allowance and is consistent with meter resolution or
minor source drift. On Output 2, tip-ring differs from tip-sleeve by `0.06 mV`,
approximately `0.076%`, while ring-sleeve is zero. Output 1 and Output 2 tip-
sleeve magnitudes differ by only `0.21 mV`, approximately `0.267%` of their
mean.

**DECISION - OUTPUT MAP PASS:** classify both powered outputs as ring-grounded.
The mapped mono TS-to-RCA playback cable is compatible with Output 1 because it
adds no new short of an active conductor. For the Section 10.2 source, drive
fixture red from Output 2 tip and black from sleeve; do not treat Output 2 as a
two-active-leg balanced source.

**USER-REPORTED INTERNAL PCB INSPECTION - 2026-09-03:** both rear output
sockets are physical three-contact TRS parts with three soldered through-hole
clip terminals. On both footprints, the separate ring and sleeve pads connect
through four-spoke thermal reliefs to the same PCB copper fill; all four R/S
pads share that fill. This agrees independently with the `0.021 ohm` unpowered
ring-to-sleeve reading and both powered AC output maps. The copper connection
also removes the former possibility that a muting or protection state created
the bond only under particular power conditions.

**SUPERSEDING TOPOLOGY WORDING:** call these mechanically TRS sockets with
electrically TS, tip-plus-common output topology. They are not literally
two-contact sockets: a TRS plug still contacts ring and sleeve separately, but
the PCB joins those contacts permanently. A TS plug therefore creates no new
output connection. The temporary asymmetric source adaptor may use a TS plug,
or a TRS plug with ring either unused or joined to sleeve. The direct baseline
must remain TRS-to-TRS because the front Input 2 ring is a distinct balanced-
input signal contact.

With tip-to-sleeve adjusted into the `50-100 mV RMS` region, classify an output
as single-ended or ring-grounded for this purpose if ring-to-sleeve is no more
than `1 mV RMS` and tip-to-ring agrees with tip-to-sleeve within the greater of
`1 mV` or `2%`. A TS plug then creates no additional cold-leg short. If tip and
ring both carry substantial signal and tip-to-ring is larger, retain the TS-
cable hold and use the ring-open TRS-to-RCA cable. Stop on any unstable,
ambiguous, or unexpectedly large reading.

### 10.2 Fixture Transfer Procedure

#### 10.2.1 Measurement Principle

This is a low-voltage fixture characterization, not a rehearsal of the complete
amplifier/loudspeaker setup. UMC202HD Output 2 temporarily substitutes for the
SU-V570 speaker output and drives the fixture at a safe signal level. The
SU-V570, loudspeaker, microphone, and normal playback path are deliberately
absent.

Let `O(f)` represent the UMC202HD Output 2 path, `I(f)` the Input 2 path,
`P(f)` the direct TRS patch cable, `B(f)` the inline measurement breakout,
`A(f)` the asymmetric source adaptor, and `Hfixture(f)` the complete fixture.
With the same breakout left at Input 2 and unchanged interface and REW settings,
the two measurements are approximately:

```text
Direct run:   D(f) = O(f) x P(f) x B(f) x I(f)
Fixture run:  F(f) = O(f) x A(f) x Hfixture(f) x B(f) x I(f)

Therefore:    F(f) / D(f) = Hfixture(f) x A(f) / P(f)
```

Equivalently, subtract the direct trace from the fixture trace in decibels and
subtract their phases. The common UMC202HD output, inline-breakout, and input
responses cancel. The short, mapped source adaptor and direct patch cable do
not algebraically cancel, but their small residual difference is bounded by
construction and the interconnect preflight; investigate it if the measured
transfer approaches a pass limit.

This establishes the fixture's actual attenuation while loaded by Input 2,
frequency and phase flatness, polarity, linearity at the intended reference
level, clamp inactivity, and susceptibility to pickup from its unscreened tail.
It does not test the SU-V570 response, loudspeaker, microphone, acoustic path,
or hum that may arise only when the complete amplifier/PC system is powered.
Those belong to the later full-dual setup check; the amplifier is absent here so
it cannot obscure a fixture fault or expose the interface to amplifier voltage
before this final fixture gate passes.

#### 10.2.2 Connections And Procedure

Perform this only after Sections 7-9 pass. Keep the SU-V570, loudspeaker, and
microphone disconnected. Keep UMC202HD phantom power off.

Two different temporary signal paths are used sequentially; do not combine
them:

1. **Direct baseline:** a conventional male-to-male balanced TRS patch cable
   connects UMC202HD Output 2 to the female end of the inline measurement
   breakout. The breakout's male plug connects to the central TRS of Input 2.
   The fixture is completely absent from this path.
2. **Fixture measurement:** remove that patch cable. A source adaptor connects
   Output 2 tip/sleeve to fixture red/black, while the fixture's existing male
   TRS plug connects to the same breakout female socket. Leave the breakout's
   male plug connected to Input 2 throughout both measurements.

The male-to-male patch cable is therefore not an extension for the fixture and
must not be interposed between its plug and Input 2. The inline breakout is a
common temporary measurement accessory, not a permanent part of the fixture.

Output 2 is verified ring-grounded. Use an insulated temporary source adaptor
in which Output 2 tip drives fixture red and sleeve drives fixture black; do not
describe or wire it as a balanced source. Use an insulated inline TRS
breakout comprising a female TRS socket for the fixture plug and a male TRS
plug for Input 2, wired straight through, so tip, ring, and sleeve can be
measured under load. Source and reference sleeves must follow the measured
interface-ground arrangement. Do not short an output conductor to sleeve unless
that exact mapping has been separately shown safe for the UMC202HD output.

**PROVISIONAL BREAKOUT CONSTRUCTION DECISION - 2026-09-03:** the proposed
female TRS socket -> screened cable -> three-node tip/ring/sleeve test junction
-> screened cable -> male TRS plug topology is electrically acceptable with
the following construction controls:

- use two-insulated-core screened cable: tip and ring use the two cores, while
  the screens from both cable sections join only the sleeve node;
- keep both cable sections and every stripped or unscreened length as short as
  practical; approximately `0.5 m` maximum total cable is a construction target,
  not a separately verified electrical limit;
- mount the three independent junctions on a restrained, insulating terminal
  block and provide strain relief on both cable sections. A conductive
  enclosure is optional rather than required; if later used, bond it only to
  sleeve and insulate tip and ring from it;
- ensure no screw, enclosure surface, cable screen, or loose strand can bridge
  tip to ring or either signal contact to sleeve; and
- attach and remove insulated meter leads only with the signal stopped. Do not
  leave hand-held probes or exposed clip leads where movement can short the
  contacts during a powered measurement.

The terminal block's resistance and capacitance are not expected to limit this
audio-band test. From the post-stress values, the driven fixture presents
approximately `1.002 kohm || 9.127 kohm = 0.903 kohm` at tip and
`1.004 kohm || 9.141 kohm = 0.905 kohm` at ring, or about `1.808 kohm`
differential source resistance. As an intentionally conservative illustration,
an added `100 pF` directly between tip and ring would place the corresponding
single-pole corner near:

```text
f = 1 / (2 pi x 1.808 kohm x 100 pF) = 880 kHz
```

That illustrative capacitance would cause only about `0.009 dB` magnitude loss
at `41 kHz`. It is not a claim about the unknown cable capacitance: the actual
continuity map and direct-versus-fixture sweep remain the acceptance evidence.
Keeping the breakout unchanged in both runs removes most of its response from
the comparison; the no-signal comparison still exposes pickup that becomes
material with the fixture's higher output impedance.

**SUPERSEDING PROPORTIONALITY REVIEW - 2026-09-03:** a machined screened
enclosure is not required for the proposed approximately `5 cm` compact
terminal-block break. The earlier enclosure preference over-weighted a
plausible but directly testable electrostatic-pickup risk. Even an intentionally
pessimistic `1 ohm` of added series resistance in each signal conductor would
add only `2 ohm` to the differential loop and lose about `0.017 dB` into a
hypothetical `1 kohm` load; the actual mapped resistance should be much smaller,
and the unchanged breakout is common to both traces. For an illustrative
effective differential loop area of `1 cm^2`, sinusoidal magnetic pickup at
`50 Hz` is:

```text
Vinduced = 2 pi f A B

B =   1 uT:  Vinduced = 0.031 uV  (-130 dB relative to 100 mV)
B =  10 uT:  Vinduced = 0.314 uV  (-110 dB relative to 100 mV)
B = 100 uT:  Vinduced = 3.14  uV  ( -90 dB relative to 100 mV)
```

These values scale directly with loop area and field strength. A normal
conductive screening box would chiefly screen electric fields and RF; unless
made from suitable high-permeability material, it would not eliminate this
low-frequency magnetic term.

Electrostatic pickup is harder to predict because it depends on placement and
capacitance imbalance. A deliberately severe model, coupling a `230 V RMS`,
`50 Hz` conductor through unequal capacitance to one approximately `0.9 kohm`
leg, gives:

```text
Vhum = 2 pi f R Vline delta-C

delta-C = 0.01 pF:  Vhum =  0.65 uV  (-104 dB relative to 100 mV)
delta-C = 0.10 pF:  Vhum =  6.5  uV  ( -84 dB relative to 100 mV)
delta-C = 1.00 pF:  Vhum = 65    uV  ( -64 dB relative to 100 mV)
```

That is a sensitivity illustration, not a prediction that the terminal block
will see the full mains potential or those capacitances. Keep tip and ring
compact and geometrically similar, keep the breakout away from mains leads,
power bricks, and transformers, and restrain it on a non-conductive surface.
Proceed first with the simple unenclosed block. Add a removable insulated,
sleeve-bonded electrostatic screen only if the matched no-signal test reveals
material hum or position/hand-sensitive pickup. This empirical stop condition
is more proportionate than requiring a screened enclosure in advance.

Before connecting USB or generating a signal, resistance-map the AC-test
interconnects while every item is loose on the bench. With nulled meter leads:

- the direct-baseline male-to-male balanced TRS patch cable must give low
  resistance from tip to tip, ring to ring, and sleeve to sleeve, with every
  cross-contact path open;
- the temporary source adaptor, tested by itself, must give low resistance from
  its Output 2 plug tip to its red fixture-side contact and from its output-
  common contact to its black fixture-side contact, with no red-black or other
  unintended cross-contact short. For a TS plug, the long sleeve is output
  common; for a TRS plug, ring may be open or deliberately joined to sleeve but
  must never connect to red. Record which implementation was built; and
- the female-to-male inline fixture-output breakout must carry tip, ring, and
  sleeve straight through independently at low resistance, with every cross-
  contact path open.

An unsecured exposed clip-lead arrangement is not acceptable while energized.
Insulate every permanent joint; keep the three intended terminal-block test
points physically separated, and attach insulated meter leads only while the
signal is stopped. Do not reuse the phantom-isolation adaptor containing the
`100 kohm` loads as a straight-through AC breakout. Record the actual mapping
before proceeding.

The loose-bench interconnect preflight is being recorded as follows:

| Interconnect | Same-contact resistance | Cross-contact paths | Decision |
| --- | --- | --- | --- |
| Direct-baseline male-to-male TRS patch cable | Tip `0.345 ohm`; ring `0.337 ohm`; sleeve/shield `0.320 ohm` | All open | PASS (`2026-09-03`) |
| Output 2 source adaptor | PENDING | PENDING | PENDING |
| Female-to-male inline fixture-output breakout | PENDING | PENDING | PENDING |

For the first row, the user reports an approximately `1 m`, lightweight Sony
headphone-extension cable, measured with nulled Agilent U1282A leads. The three
conductors average `0.334 ohm` and span only `0.025 ohm`. The direct signal loop
uses the tip and ring conductors, so its measured series resistance is
`0.345 + 0.337 = 0.682 ohm`; even against a deliberately conservative
hypothetical `1 kohm` load, this would cause only about `0.068%` or `0.0059 dB`
of attenuation. It is therefore negligible relative to the `0.1 dB` transfer-
flatness criterion, and every unintended path being open establishes the
required contact topology. The cable passes; the other two adaptor maps remain
required before USB connection or signal generation.

1. Set Input 2 to `LINE`, `PAD` off, `GAIN 2` fully down, `DIRECT MONITOR` off,
   and `OUTPUT` fully down.
2. Connect Output 2 through the normal balanced TRS patch cable and the mapped
   inline breakout to Input 2. Leave the breakout connected to Input 2 for both
   runs.
3. At low level, capture and save a direct `5 Hz-41 kHz`, `88.2 kHz` REW trace.
   Confirm correct channel identity and no clipping. Stop the generator and,
   without changing any gain or output setting, also save a direct-cable Input 2
   no-signal spectrum using fixed RTA/FFT settings that can be repeated.
4. Stop the signal. Without changing digital level, Output, Gain 2, REW
   settings, or the breakout-to-Input 2 connection, remove the direct patch
   cable. Connect the complete fixture through the temporary asymmetric source
   adaptor, and insert the fixture TRS plug into the breakout female socket.
5. Capture a second trace.
6. With the generator stopped and all gain/output settings unchanged, use REW's
   spectrum or RTA view to record the Input 2 no-signal spectrum with the
   fixture connected. Compare it with a direct-cable no-signal capture made
   under the same settings. In particular, inspect `50 Hz`, `100 Hz`, their
   harmonics, broadband noise, and any movement-sensitive spikes. The fixture's
   approximately `5 cm` output tail has no electrostatic screen, so this is a
   required installed-performance check rather than an optional diagnostic.
7. At `1 kHz`, use the true-RMS meter to measure differential input voltage
   from red to black and differential output voltage from tip to ring. Calculate
   the interface-loaded ratio and gain:

   ```text
   k_loaded = V(tip-ring) / V(red-black)
   A_loaded = 20 log10(k_loaded)
   ```

8. Confirm correct polarity, smooth relative magnitude and phase, and no
   unexpected high-frequency roll-off or resonance. The loaded gain should not
   exceed the unloaded `-20.094 dB` prediction beyond measurement uncertainty;
   extra attenuation is possible because the UMC202HD `LINE` input impedance is
   unpublished. Investigate more than approximately `1 dB` of extra attenuation
   and account for it explicitly rather than adjusting the resistor model.
9. Increase only far enough to approach the intended approximately `100 mV RMS`
   fixture output. Confirm linear scaling and no clamp conduction.
10. Record the DMM-derived and REW-relative `1 kHz` attenuation, their agreement,
    the largest relative transfer variation over `5 Hz-41 kHz`, and the direct-
    versus-fixture noise comparison. Save the direct, fixture, and no-signal
    traces together.

Provisional pass targets are correct polarity, DMM and REW `1 kHz` attenuation
agreeing within `0.2 dB`, no gain above the passive unloaded prediction beyond
measurement uncertainty, adequate reference headroom at the normal test level,
no discontinuity, and no unexplained relative magnitude variation greater than
`0.1 dB` over `20 Hz-20 kHz`. Review actual phase and ultrasonic behaviour
before accepting the `5 Hz-41 kHz` endpoints; the clamp junction capacitance is
part of what this test must measure. The unscreened tail also passes only if it
adds no material `50/100 Hz` family or other coherent pickup, no intermittent
movement-sensitive noise, and leaves enough reference-channel signal-to-noise
margin to meet the transfer-repeatability targets. Review the measured spectra
rather than assigning an unsupported microvolt limit in advance.

| AC check | Result |
| --- | --- |
| Direct trace filename |  |
| Fixture trace filename |  |
| Unloaded resistor prediction at `1 kHz` | `-20.094 dB` |
| DMM-loaded gain at `1 kHz` | PENDING |
| REW-relative gain at `1 kHz` | PENDING |
| DMM/REW agreement | PENDING |
| Relative variation, `20 Hz-20 kHz` | PENDING |
| Direct-versus-fixture no-signal spectrum | PENDING |
| `50/100 Hz` family or movement-sensitive pickup | PENDING |
| Polarity | PENDING |
| Clamp inactive near `100 mV RMS` | PENDING |
| Overall AC decision | NOT PERFORMED |

## 11. Installation And Release Gate

When every preceding gate passes:

1. switch the SU-V570 off and turn its volume fully down;
2. connect fixture red to the positive and black to the negative of the same
   channel and speaker bank used by the woofer, at the rear amplifier terminals;
3. connect the loudspeaker separately to that same output pair; the fixture
   cable must not carry loudspeaker current;
4. insert the fixture TRS plug only into the central jack of UMC202HD Input 2;
5. set Input 2 to `LINE`, begin with Gain 2 fully down, and leave its outer XLR
   contacts unused;
6. connect the approved, measured Output 1-to-RCA playback cable: the mapped TS
   cable only if Section 10.1 classifies Output 1 as ring-grounded, otherwise a
   ring-open TRS-to-RCA cable; and
7. establish the acoustic-test level under
   [`FRD_MEASUREMENT_SETUP_TEST.md`](FRD_MEASUREMENT_SETUP_TEST.md).

Do not use a different channel or speaker bank for the reference. Do not move
the fixture between amplifier and driver reference planes without recording the
change. Make or remove every amplifier, loudspeaker, fixture, and TRS connection
with the amplifier off.

Current gate:

```text
SU-V570 unpowered topology:       PASS - 2026-09-01
Powered topology confirmation:   WAIVED - optional, 2026-09-01
Input 2 TRS phantom isolation:   PASS - 2026-09-01
Pre-stress resistance matrix:    PASS - complete unit, 2026-09-02
Fixture physical record:         PASS - CONTROLLED BENCH USE; HEAT-SHRINK BODY AND UNSCREENED 5 CM TAIL RECORDED, 2026-09-03
Clamp component evidence:        PASS - BZX 5V1, ~5 V AT 2 mA, A-A PAIRS, INSTALLED FUNCTION VERIFIED
Bidirectional clamp function:    PASS - BOTH LEGS, BOTH POLARITIES, 2026-09-02
Four powered DC curves:          PASS WITH CHARACTERIZED 45.5 V LINEARITY DEVIATION
Post-stress resistance matrix:   PASS - ALL PATHS WITHIN 0-4 OHM OF BASELINE, 2026-09-02
Integrated PL310QMD DC test:     PASS WITH CHARACTERIZED 45.5 V LINEARITY DEVIATION
Unpowered system ground audit:   PASS - ALL STAGES, 2026-09-03
Rear-output topology:            PASS - BOTH POWERED, DRIVEN OUTPUTS RING-GROUNDED, 2026-09-03
AC transfer commissioning:       NOT PERFORMED
Approved for amplifier use:      NO
```

## 12. Primary References

- SU-V570 output-topology evidence and gate:
  [`SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md`](SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md)
- Acoustic repeatability procedure that consumes the commissioned fixture:
  [`FRD_MEASUREMENT_SETUP_TEST.md`](FRD_MEASUREMENT_SETUP_TEST.md)
- Technics SU-V570 service manual, including output ratings, input sensitivity,
  and the power-amplifier schematic:
  <https://audiocircuit.dk/downloads/technics/Technics-SUV570-int-sm.pdf>
- Behringer UMC202HD quick-start guide, including maximum line input and output:
  <https://mediadl.musictribe.com/media/PLM/data/docs/UMC/QSG_BE_0805-AAR_U-PHORIA-Series_WW.pdf>
- Vishay `BZX55` small-signal zener data sheet:
  <https://www.vishay.com/docs/85604/bzx55.pdf>
- Thurlby Thandar PL-series data, including PL310QMD `0-64 V` series operation,
  current limiting, output isolation, metering, and output switching:
  <https://www.farnell.com/datasheets/99860.pdf>
- Keysight U1280 Series data sheet:
  <https://www.keysight.com/us/en/assets/7018-04867/data-sheets/5992-0847.pdf>
