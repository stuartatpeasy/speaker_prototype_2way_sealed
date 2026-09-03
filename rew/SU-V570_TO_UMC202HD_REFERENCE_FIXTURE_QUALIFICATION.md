# SU-V570 To UMC202HD Reference-Fixture Qualification Record

Date range: 2026-09-01 to 2026-09-03

Status: **COMPLETED QUALIFICATION EVIDENCE; NOT THE CURRENT OPERATING PROCEDURE**

This record preserves the measurements and reasoning that qualified the
amplifier-output fixture through its phantom-isolation, resistance, DC clamp,
physical-construction, ground-path, and interface-output-topology gates. It
removes the superseded step-by-step dialogue and keeps the evidence needed to
audit the current decisions.

Use:

- [SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md)
  for the construction specification and release state;
- [REFERENCE_FIXTURE_AC_COMMISSIONING.md](REFERENCE_FIXTURE_AC_COMMISSIONING.md)
  for the unfinished AC gate; and
- [SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md](SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md)
  for the SU-V570 common-ground evidence.

Unless stated otherwise, resistance measurements used the battery-powered
Agilent/Keysight U1282A with nulled leads. Reported milliohm values classify
topology; they are not four-wire precision measurements or appliance-safety
certification.

## 1. UMC202HD Input 2 Phantom Isolation

The decision test loaded the central Input 2 TRS contacts with equal
`100 kohm`, 1%, at least `0.25 W` resistors:

```text
Tip  ----- 100 kohm -----+
                         +----- Sleeve
Ring ----- 100 kohm -----+
```

A conventional `48 V` phantom feed through `6.8 kohm` would leave
`48 x 100 / 106.8 = 44.9 V` across either load, so this network cannot hide a
real sustained P48 feed.

**USER-REPORTED MEASUREMENT, 2026-09-01:** with the U1282A in normal DCV mode
on its `+/-60 V` range and `+48 V` off, tip-sleeve and ring-sleeve settled
below `1 mV` within `25 s`; tip-ring settled below `1 mV` within `1 s`.
Without power-cycling the interface, every pair then remained at a displayed
`0.000 V` while `+48 V` was switched on and off separately for that
measurement.

**DECISION - PASS:** no sustained or settling phantom voltage reaches the Input
2 central TRS contacts under the defined load.

An earlier unloaded, high-impedance observation recorded a brief approximately
`3.3 V` power-up peak, rapid fall, slow rise towards `1.5 V`, and
minutes-long decay. That behaviour is retained as evidence of stored charge or
bias/meter interaction, but it was superseded as the decision test by the
loaded result above.

## 2. Complete-Fixture Resistance Qualification

### 2.1 Construction History And Component Evidence

The first physical version was a one-leg attenuator: red reached tip through
`9.1 kohm`, tip had `1 kohm` to sleeve, black was hard-connected to sleeve,
and ring was open. Its approximate `10 kohm` red-black, `1 kohm`
tip-sleeve, ring-open signature exposed that topology; it was rejected and
rebuilt. A first rework check was also superseded because body contact and one
duplicated label produced inconsistent redundant sums. The hands-off
complete-unit matrix below is the accepted pre-stress baseline.

All four resistors are user-reported 1% metal-film axial parts sourced from
Mouser. The `9.1 kohm` series parts are rated `0.5 W` with working voltage
above `100 V`; the `1 kohm` shunts are rated `0.25 W`. Manufacturer and
part numbers were not retained.

The four diodes are marked `BZX 5V1`; exact manufacturer, family suffix,
tolerance grade, and rating are unknown. Each sample measured close to `5 V`
at `2 mA` on the user's zener analyser. Each node uses an anode-to-anode
series-opposed pair, with the joined midpoint insulated and connected nowhere
else. These facts characterize the installed devices without inventing a full
part number.

### 2.2 Accepted Pre-Stress Matrix

**USER-REPORTED MEASUREMENT, 2026-09-02:** after the final rebuild, the
disconnected complete cable-to-TRS unit was measured with the U1282A in
resistance mode on its `60 kohm` range. Leads were nulled and no body part
contacted the circuit. Values are in `kohm`; `In+` is red and `In-` black.

| From / to | Ring | Tip | In+ | In- |
| --- | ---: | ---: | ---: | ---: |
| Sleeve | `1.003` | `1.002` | `10.127` | `10.142` |
| Ring | - | `2.005` | `11.131` | `9.139` |
| Tip | - | - | `9.125` | `11.145` |
| In+ | - | - | - | `20.271` |

The six independently redundant sums close within `0-2 ohm`. For example,
`9.125 + 1.002 = 10.127 kohm` exactly for In+-sleeve, while the largest
closure is `20.271 - (9.125 + 1.002 + 1.003 + 9.139) = 2 ohm`. The measured
`9.125`, `9.139`, `1.002`, and `1.003 kohm` branches are respectively
`0.275%`, `0.429%`, `0.200%`, and `0.300%` above nominal, all within
1%. The calculated unloaded differential gain is `-20.094 dB`.

**DECISION - PASS:** the complete unit has the required symmetric two-leg
topology, neither input lead is hard-connected to sleeve, and the meter reveals
no short or material low-voltage diode leakage.

## 3. Integrated PL310QMD DC Clamp Qualification

### 3.1 Test Configuration

The TTi PL310QMD was used in its series mode to drive one complete
amplifier-end-to-TRS branch at a time. Both section current limits were
`10 mA`. The Agilent U1272A measured supply magnitude in DCV mode on its
`300 V` range; the U1282A measured node-to-sleeve voltage in DCV mode on its
`60 V` range. The UMC202HD and SU-V570 were absent.

| Curve | PL310QMD HI | PL310QMD LO | Measured node |
| --- | --- | --- | --- |
| Tip positive | Red | Black and sleeve | Tip relative to sleeve |
| Tip negative | Black and sleeve | Red | Tip relative to sleeve |
| Ring positive | Black | Red and sleeve | Ring relative to sleeve |
| Ring negative | Red and sleeve | Black | Ring relative to sleeve |

With no clamp current, the measured divider ratios predict
`Vtip = 0.098943 Vsupply` and `Vring = 0.098896 Vsupply`. The test required a
clear high-voltage knee, node magnitude no greater than `6.2 V`, positive/
negative symmetry within approximately `0.3 V`, current below `10 mA`, CV
operation, no abnormal heating, and an unchanged cooled resistance matrix. The
original linearity target was approximately `+/-1%` through the amplifier's
`45.5 V` rail envelope.

### 3.2 Raw Four-Curve Results

All values below are DC volts. Each cell gives actual supply magnitude / signed
node voltage.

| Nominal source | Tip positive | Tip negative | Ring positive | Ring negative |
| ---: | ---: | ---: | ---: | ---: |
| `10 V` | `10.03 / 0.990` | `9.99 / -0.989` | `10.05 / 0.990` | `9.99 / -0.990` |
| `20 V` | `19.95 / 1.973` | `19.92 / -1.974` | `20.09 / 1.986` | `20.00 / -1.978` |
| `30 V` | `29.98 / 2.964` | `29.96 / -2.965` | `30.02 / 2.969` | `29.96 / -2.963` |
| `40 V` | `40.07 / 3.949` | `40.08 / -3.948` | `40.12 / 3.955` | `40.09 / -3.954` |
| `45.5 V` | `45.56 / 4.459` | `45.53 / -4.449` | `45.53 / 4.454` | `45.62 / -4.467` |
| `50 V` | `50.06 / 4.841` | `50.05 / -4.819` | `50.16 / 4.849` | `50.12 / -4.846` |
| `55 V` | `55.10 / 5.183` | `55.10 / -5.140` | `55.00 / 5.167` | `55.16 / -5.185` |
| `60 V` | `60.21 / 5.400` | `60.12 / -5.351` | `60.03 / 5.394` | `60.16 / -5.403` |
| nominal `64 V` | `64.50 / 5.520` | `64.49 / -5.463` | `64.48 / 5.515` | `64.46 / -5.515` |

The supply remained in constant-voltage mode throughout every run. It indicated
at most `6 mA`, consistent with derived maximum series currents of
`6.450-6.469 mA` given its display accuracy. Heating was assessed tactually,
not instrumentally: the fixture became only mildly warmer than ambient, with no
smell, discoloration, rapid hot spot, or other concern. The calculated maximum
series-resistor dissipation is approximately `0.380-0.382 W`, so mild warming
of a `0.5 W` part is expected. Derived maximum clamp current is approximately
`0.951-1.017 mA`, only about `5.2-5.6 mW` in a pair.

### 3.3 Curve Decision

| Curve | Departure at approximately `45.5 V` | Node at maximum | Unclamped prediction | Clamp reduction |
| --- | ---: | ---: | ---: | ---: |
| Tip positive | `-1.08%` | `5.520 V` | `6.382 V` | `0.862 V` |
| Tip negative | `-1.24%` | `-5.463 V` | `-6.381 V` | `0.918 V` |
| Ring positive | `-1.08%` | `5.515 V` | `6.377 V` | `0.862 V` |
| Ring negative | `-0.99%` | `-5.515 V` | `-6.375 V` | `0.860 V` |

All curves agree with the unloaded divider within `0.45%` through `40 V`,
then enter the same smooth knee. At maximum source, magnitudes span only
`5.463-5.520 V`; the ring pair both read `5.515 V`. Three curves narrowly
miss the approximate 1% criterion at `45.5 V`, with the worst miss only
`0.24` percentage point. This is no more than about `0.11 dB` compression
at the rail envelope and has no material consequence near the intended
`1 V RMS` amplifier output, where the clamp is inactive.

**DECISION - PASS WITH CHARACTERIZED 45.5 V LINEARITY DEVIATION:** the four
curves verify correct polarity, bidirectional clamp action, close symmetry,
bounded current, CV operation, and expected thermal behaviour. The decision
does not misstate the three `0.99-1.24%` results as exact compliance.

### 3.4 Cooled Post-Stress Matrix

**USER-REPORTED MEASUREMENT, 2026-09-02:** after cooling, the disconnected unit
was remeasured with the same U1282A `60 kohm` setup and nulled leads. The room
may have cooled slightly during the evening.

| From / to | Ring | Tip | In+ | In- |
| --- | ---: | ---: | ---: | ---: |
| Sleeve | `1.004` | `1.002` | `10.130` | `10.146` |
| Ring | - | `2.006` | `11.133` | `9.141` |
| Tip | - | - | `9.127` | `11.149` |
| In+ | - | - | - | `20.275` |

Every direct path changed by only `0-4 ohm`; all post-stress redundant sums
close within `0-2 ohm`. The largest change is approximately `0.04%` of a
`10.1 kohm` path and the branch changes are at most `0.10%` of a `1 kohm`
shunt. Their all-positive sign is not used to infer a temperature coefficient.

**DECISION - PASS:** there is no evidence of resistor damage, open clamp,
changed connection, or new leakage path. This closes the integrated DC gate.

## 4. Physical-Construction Qualification

**USER-REPORTED INSPECTION, 2026-09-03:** the unmarked `2 m`, `1.5 mm^2`
red/black figure-of-eight input cable remains joined except for approximately
`5 cm` at its secure, insulated, strand-free bare-wire speaker termination
and `2 cm` at the fixture. Red denotes positive and black negative.

Every component, exposed lead, and junction is individually heat-shrink
insulated before overlapping outer layers form an approximately `6 cm`,
normally inflexible body. Tapered layers and internal wire returns provide
strain relief; a moderate pull reaches no solder joint. The joined-anode diode
midpoints are separately insulated. Sleeve is the common junction for both
`1 kohm` shunts, both clamp endpoints, and the output-tail sleeve conductor.

The approximately `5 cm` output tail uses three twisted, individually
insulated `14/0.7` hookup wires rather than screened cable. The unknown-make
all-metal TRS plug has distinct contacts, a plastic cylindrical terminal
insulator, clamp-jaw strain relief, a sleeve-bonded body, and an appropriate
Input 2 `LINE` label.

**DECISION - PASS FOR CONTROLLED BENCH USE:** the construction has also
survived the `64.5 V DC` sweeps and post-stress resistance check. No
heat-shrink dielectric, temperature, flame, or abrasion rating is claimed, so
this is not approval for permanent, crushed, abraded, unattended, or production
use. The unscreened tail is a performance uncertainty, not a demonstrated
safety fault; the remaining AC test must compare matched no-signal spectra.

## 5. Unpowered System Ground-Path Audit

### 5.1 Measured Paths

Every device was unpowered and disconnected as required. The one PC stage was
performed with the PC shut down, mains plug removed from the wall, every other
cable removed, and only its Class-I power cord retained to expose the free
plug's protective-earth pin. Considerable probe pressure was needed on chassis
metal, so the last digit is not treated as precision data.

| Stage | Measurement | Result |
| --- | --- | ---: |
| UMC202HD alone | Input 2 sleeve to bare chassis | `OPEN` |
| UMC202HD alone | Input 2 sleeve to USB shell | `0.035 ohm` |
| UMC202HD alone | Bare chassis to USB shell | `OPEN` |
| Chassis contact control | Two separated bare chassis points | `0.013 ohm` |
| Intended USB cable alone | Plug shell to plug shell | `0.130 ohm` |
| PC alone | USB socket shell to bare chassis | `0.170 ohm` |
| PC alone | Chassis to free mains-plug PE pin | `0.245 ohm` |
| PC plus USB and UMC202HD | Input 2 sleeve to PC chassis | `0.412 ohm` |
| PC plus USB and UMC202HD | Input 2 sleeve to free-plug PE pin | `0.379 ohm` |
| Playback cable | Two-contact TS tip to RCA centre / shell | `0.244 ohm` / `OPEN` |
| Playback cable | TS sleeve to RCA centre / shell | `OPEN` / `0.078 ohm` |
| Isolated UMC202HD output | Ring to sleeve through verified TRS breakout | `0.021 ohm`; breakout alone `OPEN` |
| Joined only by intended dual playback cable | Input 2 sleeve to corresponding SU-V570 RCA shell | `0.061 ohm` |
| Same connected state | Input 2 sleeve to corresponding speaker negative | `0.174 ohm` |
| Fixture alone, evidence reused from post-stress matrix | In+ / In- to sleeve | `10.130 / 10.146 kohm` |

The `0.013 ohm` chassis control validates both open UMC202HD enclosure
readings. Thus Input 2 sleeve is hard-bonded to USB shell but DC-isolated from
the tested enclosure metal. The idealized separate shell-path sum to PC chassis
is `0.035 + 0.130 + 0.170 = 0.335 ohm`, only `0.077 ohm` below the directly
measured `0.412 ohm`. Exact scalar addition is not expected from remade
two-wire contacts, a distributed chassis, mated connectors, and possible
parallel shield/circuit-ground paths.

The PC measurements verify a low-resistance route from interface sleeve through
USB shell/cable and PC chassis to protective earth. This is an ordinary
signal-reference topology result, not a protective-conductor resistance test.
Never defeat PC protective earth to cure hum.

The connected result leaves approximately
`0.174 - 0.061 = 0.113 ohm` beyond the RCA shell. This agrees with the
independent SU-V570 `0.120-0.150 ohm` speaker-negative-to-RCA-shell range
(mean `0.130 ohm`) within contact uncertainty and possible parallel paths
through the dual cable.

**DECISION - PASS:** every low-resistance path is explained. The playback cable
provides the expected single signal-ground bond between UMC202HD sleeve and the
SU-V570 common signal ground; the fixture independently retains kilo-ohm
isolation from both amplifier leads.

## 6. UMC202HD Rear-Output Topology

The official connector description alone did not establish whether a TS plug
could safely ground a rear output's ring. Three independent observations now
do:

1. an otherwise isolated, unpowered rear output measured `0.021 ohm` from
   ring to sleeve through a breakout that was open when unplugged;
2. powered `1 kHz` measurements, with REW driving only the channel under
   test, gave:

   | Output | Tip-sleeve | Ring-sleeve | Tip-ring |
   | --- | ---: | ---: | ---: |
   | 1 | `78.69 mV` | `0.002 mV` | `78.73 mV` |
   | 2 | `78.9 mV` | `0.000 mV` | `78.84 mV` |

3. internal inspection found physical three-contact TRS sockets with all three
   through-hole terminals soldered; on both footprints, the separate ring and
   sleeve pads connect through four-spoke thermals to the same PCB copper fill.

An earlier Output 1 row taken while REW accidentally drove Output 2 gave
`0.002/0.001/27.42 mV`. It violates the voltage triangle for one steady
circuit state and was discarded as invalid, not treated as a hardware fault.
Output 2's correctly driven row remained valid and was not repeated.

**DECISION - PASS:** both rear sockets are mechanically TRS but electrically
tip plus a permanent ring/sleeve common, equivalent to TS signal topology. The
mapped mono TS-to-RCA playback cable therefore adds no new short of an active
cold leg. The Output 2 fixture-test adaptor may be TS, or TRS with ring open or
joined to sleeve; tip drives red and common drives black. The direct Output
2-to-front-Input 2 baseline must remain TRS-to-TRS because the front input ring
is a distinct balanced-input contact.

## 7. Qualification Summary

| Gate | Decision |
| --- | --- |
| SU-V570 common-ground prerequisite | PASS under separate topology record |
| UMC202HD Input 2 phantom isolation | PASS |
| Complete-unit pre-stress resistance | PASS |
| Physical construction | PASS for controlled bench use |
| Four-polarity DC clamp function | PASS with characterized `45.5 V` deviation |
| Cooled post-stress resistance | PASS |
| Complete unpowered ground-path audit | PASS |
| UMC202HD rear-output topology | PASS; mechanically TRS, electrically TS |
| AC transfer/noise commissioning | NOT PERFORMED |
| Approved for powered-amplifier use | **NO** |

The next work is not another completed-gate repeat. Continue at the source-
adaptor and inline-breakout maps in
[REFERENCE_FIXTURE_AC_COMMISSIONING.md](REFERENCE_FIXTURE_AC_COMMISSIONING.md).
