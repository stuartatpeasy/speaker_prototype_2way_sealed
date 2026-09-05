# SU-V570 To UMC202HD Amplifier-Output Reference Fixture

Date prepared: 2026-09-02

Last revised: 2026-09-05

Status: **ALL PROPORTIONATE SAFETY/CONNECTIVITY GATES PASS; APPROVED FOR
CONTROLLED POWERED-AMPLIFIER BENCH USE**

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

This document owns the fixture rationale, construction specification,
calculations, current qualification state, and release gate. Related documents
have narrower authority:

- [`SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md`](SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md)
  establishes whether the amplifier output is suitable in principle;
- [`SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md`](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md)
  retains completed test readings and qualification reasoning;
- [`REFERENCE_FIXTURE_AC_COMMISSIONING.md`](REFERENCE_FIXTURE_AC_COMMISSIONING.md)
  retains the low-voltage observations and completed proportional AC release
  decision;
- [`FRD_MEASUREMENT_SETUP_TEST.md`](FRD_MEASUREMENT_SETUP_TEST.md) consumes an
  already commissioned fixture in the acoustic repeatability test; and
- [`../DRIVER_ANALYSIS.md`](../DRIVER_ANALYSIS.md) retains the dated project
  evidence and decision history.

The release in this file is explicitly for UMC202HD Input 2. Reusing the
passive fixture with a UMC22 does not transfer the UMC202HD contact, phantom, or
input-level qualification. That bounded alternative is controlled by
[`UMC22_RISK_ACCEPTED_FRD_FALLBACK.md`](UMC22_RISK_ACCEPTED_FRD_FALLBACK.md).

Never connect this fixture to a powered amplifier until Section 7 explicitly
says `Approved for amplifier use: YES`.

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
becomes necessary, connect the same clamp/attenuator `In+` (red) and `In-`
(black) leads at the driver terminals and document that changed reference
plane.

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
inside an electrostatic shield. Check actual no-signal reference-channel noise
in the first powered full-dual setup, where the amplifier and final cable
placement are present; this is a measurement-quality check rather than a
standalone electrical-release gate.

**DECISION - PHYSICAL RECORD PASS FOR CONTROLLED BENCH USE:** construction,
polarity marking, insulation, junction isolation, strain relief, component
ratings, plug mapping, and the deliberate output-tail deviation are now
recorded. No rebuild is required on the present evidence. Inspect the bare-wire
termination, outer heat-shrink, both cable exits, and TRS clamp before every use;
stop on looseness, a stray strand, cut, abrasion, softening, discoloration, or
exposed internal structure. The later proportionate AC sanity/release review
passed; actual powered no-signal behaviour is a measurement-quality check.

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
can only add attenuation to this passive network. The actual full-dual reference
level decides the installed gain for measurement purposes; sub-decibel
agreement with the unloaded calculation is not a safety condition.

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
the rail-bound clamp/attenuator output is still approximately `7.7 dB` below it.

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
required dissipation was low enough for the completed controlled,
current-limited qualification. With the shunt intact and any SU-V570 output
bounded by its rails, the resistors alone hold the node to about `4.50 V`, so
the clamp intentionally remains off. The clamp is secondary protection, not
the primary current limiter.

For this one-off prototype, the missing manufacturer suffix is not a release
blocker because the four completed DC curves demonstrate the required
bidirectional clamp knee. Audio-band response and repeatability are checked in
the first complete full-dual measurement chain rather than by further low-level
DMM metrology. Retain the parts as measured, unidentified `BZX 5V1` devices. A
reproducible future build should use fully traceable components.

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
6. complete the proportionate AC sanity and release review; and
7. only then connect the fixture to a powered amplifier under the documented
   controlled startup.

Stop immediately for a shorted series resistor, unexplained continuity, wrong
TRS contact, unstable DC result, unexpected current-limit operation, excessive
component heating, insulation damage, perceptible tingle, visible spark, or an
appliance-safety concern. The fixture remains unapproved until the cause is
understood and every affected test is repeated.

## 6. Completed Qualification And Current Gate

The detailed raw readings, intermediate calculations, superseded diagnostics,
and test conditions are retained in
[SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md).
This section is the concise current state; do not repeat a completed test unless
the fixture, relevant interconnect, interface, PC grounding, or amplifier wiring
changes.

| Gate | Current result |
| --- | --- |
| SU-V570 unpowered topology | PASS - common-signal-ground output, 2026-09-01 |
| Optional powered SU-V570 confirmation | WAIVED, 2026-09-01 |
| UMC202HD Input 2 central-TRS phantom isolation | PASS - all loaded pairs displayed `0.000 V` through individual `+48 V` switching, 2026-09-01 |
| Complete-unit pre-stress resistance matrix | PASS - symmetric two-leg network; redundant sums close within `0-2 ohm`, 2026-09-02 |
| Physical construction | PASS for controlled bench use - heat-shrink body and unscreened `5 cm` output tail recorded, 2026-09-03 |
| Four-polarity PL310QMD clamp test | PASS with characterized `45.5 V` soft-knee deviation, 2026-09-02 |
| Cooled post-stress resistance matrix | PASS - every path changed by only `0-4 ohm`, 2026-09-02 |
| Unpowered system ground-path audit | PASS - all stages, 2026-09-03 |
| UMC202HD rear-output topology | PASS - mechanically TRS, electrically TS; R/S pads share PCB copper, 2026-09-03 |
| Straight-through cable map | PASS - T/T `0.345 ohm`, R/R `0.337 ohm`, S/S `0.320 ohm`; all cross-paths open, 2026-09-03 |
| Output 2 source adaptor map | PASS - TRS with ring unconnected; T/`In+` `0.400 ohm`, S/`In-` `0.370 ohm`; all prohibited paths open, 2026-09-03 |
| Breakout-cable map | PASS - through passed straight-through cable: T/T `0.345 ohm`, R/R `0.328 ohm`, S/S `0.328 ohm`; all cross-paths open; breakout residual below approximately `0.01 ohm` comparison repeatability, 2026-09-03 |
| [AC sanity and proportionality review](REFERENCE_FIXTURE_AC_COMMISSIONING.md) | PASS FOR RELEASE - corrected low-voltage path gives raw `-20.45 dB`, consistent with the calculated `-20.094 dB`; precision DMM/noise work moved to practical full-dual checks, 2026-09-03 |
| Approved for amplifier use | **YES - controlled bench use under the documented startup and stop rules** |

The current resistance baseline after DC stress is:

| From / to | Ring | Tip | In+ | In- |
| --- | ---: | ---: | ---: | ---: |
| Sleeve | `1.004 kohm` | `1.002 kohm` | `10.130 kohm` | `10.146 kohm` |
| Ring | - | `2.006 kohm` | `11.133 kohm` | `9.141 kohm` |
| Tip | - | - | `9.127 kohm` | `11.149 kohm` |
| In+ | - | - | - | `20.275 kohm` |

At the approximately `64.5 V` DC endpoints, all four clamp-node magnitudes
were `5.463-5.520 V`; the supply stayed in CV mode, indicated at most `6 mA`,
and produced only mild expected resistor warming. Near `45.5 V`, the four
departures from the unloaded resistor predictions were `0.99-1.24%`; this
smooth, symmetric soft-knee behaviour is accepted explicitly rather than
misreported as exact compliance with the approximate `1%` target.

The ground audit establishes the intended low-resistance signal-reference route
from Input 2 sleeve through USB and the Class-I PC to protective earth, and
through the mapped playback cable to SU-V570 signal ground. It is not a
protective-conductor test. The fixture itself retains approximately `10.1 kohm`
from either amplifier lead to sleeve and does not create a second hard ground
bond.

Internal inspection of this UMC202HD found both rear output sockets to be
mechanically three-contact TRS parts whose separate ring and sleeve pads share
the same PCB copper fill. Together with the `0.021 ohm` unpowered R/S reading
and powered AC maps, this verifies permanent tip-plus-common, electrically TS
outputs. The Output 2 source adaptor may therefore use TS, or TRS with ring
unused or joined to sleeve. The direct baseline remains TRS-to-TRS because
front Input 2 ring is a distinct signal-return contact.

## 7. Installation And Release Gate

Current release state: **Approved for amplifier use: YES, for controlled bench
use under the connection, startup, inspection, and stop rules below**.

The proportionality review in
[REFERENCE_FIXTURE_AC_COMMISSIONING.md](REFERENCE_FIXTURE_AC_COMMISSIONING.md)
closes the standalone electrical gate. The resistance and DC evidence establish
the protection function, and the corrected low-voltage result is an adequate
gross AC sanity check. Exact attenuation, powered-system noise, headroom, and
dropout behaviour are measurement-quality checks in the first full-dual setup.
That checkout subsequently reached a clean `1.00 V RMS` at the woofer but found
brief recurring source-stream mutes. Sweeps are paused for REW/ASIO/USB/UMC
diagnosis; the passive fixture's controlled-use safety release remains valid.

After release, make every amplifier, loudspeaker, fixture, and TRS connection
with the SU-V570 switched off:

1. turn SU-V570 volume fully down;
2. connect clamp/attenuator `In+` (red) to positive and `In-` (black) to
   negative on the same channel and speaker bank as the woofer;
3. connect the loudspeaker separately to that output pair; the fixture cable
   must not carry loudspeaker current;
4. insert the clamp/attenuator output plug only into the central TRS jack of
   UMC202HD Input 2, directly for normal use or through the passed breakout
   cable for the first gross reference-level check;
5. set Input 2 to `LINE`, `PAD` off, and `GAIN 2` fully down; leave its XLR
   contacts unused;
6. connect the verified Output 1 TS-to-RCA playback cable; and
7. establish the acoustic-test level under
   [FRD_MEASUREMENT_SETUP_TEST.md](FRD_MEASUREMENT_SETUP_TEST.md).

Do not use a different channel or speaker bank for the reference. Do not move
between amplifier-terminal and driver-terminal reference planes without
recording the change. Inspect the bare-wire termination, fixture insulation,
cable exits, and TRS strain relief before every use.

## 8. Primary References

- Completed fixture qualification evidence:
  [SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md)
- Completed AC commissioning and release rationale:
  [REFERENCE_FIXTURE_AC_COMMISSIONING.md](REFERENCE_FIXTURE_AC_COMMISSIONING.md)
- SU-V570 output-topology evidence:
  [SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md](SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md)
- Acoustic procedure that consumes the released fixture:
  [FRD_MEASUREMENT_SETUP_TEST.md](FRD_MEASUREMENT_SETUP_TEST.md)
- Technics SU-V570 service manual:
  <https://audiocircuit.dk/downloads/technics/Technics-SUV570-int-sm.pdf>
- Behringer UMC202HD quick-start guide:
  <https://mediadl.musictribe.com/media/PLM/data/docs/UMC/QSG_BE_0805-AAR_U-PHORIA-Series_WW.pdf>
- Vishay `BZX55` data sheet:
  <https://www.vishay.com/docs/85604/bzx55.pdf>
- Thurlby Thandar PL-series data:
  <https://www.farnell.com/datasheets/99860.pdf>
- Keysight U1280 Series data sheet:
  <https://www.keysight.com/us/en/assets/7018-04867/data-sheets/5992-0847.pdf>
