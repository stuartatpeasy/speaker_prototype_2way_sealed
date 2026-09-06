# Amplifier-Output Reference Fixture — Specification

Lifecycle: **CURRENT SPECIFICATION**
Owns: electrical design, construction requirements, component evidence,
attenuation/loading/fault calculations, and redesign constraints.
Does not own: operating sequence or completed test evidence.
Use procedure: [`REFERENCE_FIXTURE_USE.md`](REFERENCE_FIXTURE_USE.md)
Qualification:
[`../qualification/REFERENCE_FIXTURE_QUALIFICATION_2026-09-01_TO_03.md`](../qualification/REFERENCE_FIXTURE_QUALIFICATION_2026-09-01_TO_03.md)
Last reviewed: 2026-09-06

## 1. Functional Definition

The fixture derives a protected electrical reference from one Technics SU-V570
speaker-output pair for a two-channel REW measurement. It comprises:

1. a `2 m`, red/black, `1.5 mm^2` two-conductor input cable;
2. two symmetric `9.1 kohm` series and `1.0 kohm` shunt divider legs;
3. two independent bidirectional `5.1 V` zener clamp pairs;
4. an approximately `5 cm` twisted tip/ring/sleeve output tail; and
5. a 1/4-inch TRS plug.

The electrical reference removes DAC/amplifier gain and response from the
derived acoustic transfer function and supplies common timing. The current
connection references amplifier terminals, not the driver end of the separate
speaker cable. The true-RMS meter remains the authority for setting driver
voltage.

The SU-V570 has passed the unpowered common-ground topology gate, but neither
speaker conductor is hard-wired to fixture sleeve. Both legs are attenuated.
This preserves a floating symmetric network when disconnected and avoids
building an additional direct ground bond into the fixture.

The protection layers are:

- R1/R2 `9.1 kohm`, minimum `0.5 W`, as primary current limiters;
- R3/R4 `1.0 kohm` shunts, providing approximately 20 dB attenuation;
- series-opposed `5.1 V` zener pairs as secondary open-shunt/overvoltage
  protection; and
- construction, resistance, DC, ground-path, and proportionate AC tests.

The fixture is not mains isolation, protective earth, a speaker load, or a
substitute for amplifier safety testing. It cannot protect a construction error
that bypasses a series resistor.

## 2. Electrical Schematic

The installed clamp pairs are series-opposed with anodes joined. A
common-cathode pair is electrically equivalent. Each midpoint is individually
insulated and connected nowhere else.

```text
         2 m, 1.5 mm^2                    ~5 cm TWISTED T/R/S WIRES
       RED amplifier lead                       TO 1/4-INCH TRS

SU + o================o-- R1 9.1 kohm, 0.5 W --+---------- T (tip)
                                                |
                                                +-- R3 1.0 kohm --+
                                                |                 |
                                                +--K D1 A--A D2 K-+
                                                                  |
                                                                  +------ S
                                                                  |
                                                +--K D3 A--A D4 K-+
                                                |                 |
                                                +-- R4 1.0 kohm --+
                                                |
SU - o================o-- R2 9.1 kohm, 0.5 W --+---------- R (ring)

      BLACK amplifier lead
```

Fixture sleeve is not directly connected to the black amplifier lead.
UMC202HD Input 2 outer XLR contacts remain unused. UMC22 use is controlled by
its separate risk acceptance and qualification.

## 3. Bill Of Materials And Retained Evidence

| Ref. | Requirement | Present evidence and limitation |
| --- | --- | --- |
| Input cable | `2 m`, joined red/black `1.5 mm^2`; insulation suitable for completed `64.5 V DC` test | No printed manufacturer/rating; complete fixture passed; secure bare-wire amplifier end |
| R1 | `9.1 kohm`, 1%, metal film, at least `0.5 W`, working voltage above `100 V` | User-confirmed Mouser part, part number unretained; complete path `9.125 kohm` pre-stress, `9.127 kohm` post-stress |
| R2 | Same as R1 | Complete path `9.139 kohm` pre-stress, `9.141 kohm` post-stress |
| R3 | `1.0 kohm`, 1%, metal film, at least `0.25 W` | `1.002 kohm` pre/post-stress |
| R4 | Same as R3 | `1.003 kohm` pre-stress, `1.004 kohm` post-stress |
| D1-D4 | Four matched `5.1 V` small-signal zeners, two opposed pairs; traceable `BZX55B5V1` or `BZX55C5V1` preferred for a reproducible build | Marked `BZX 5V1`; manufacturer, suffix, tolerance, and rating unknown; each near `5 V` at `2 mA`; installed bidirectional behaviour passed |
| Output tail | Shielded balanced pair preferred; very short twisted T/R/S allowed with noise check | Approximately `5 cm` of three twisted, insulated `14/0.7` hookup wires; no overall screen |
| Plug | 1/4-inch TRS, contacts exactly as schematic | Unknown make/model; all-metal body bonded to sleeve; internal insulator and cable clamp; mapping passed |
| Body | Insulating enclosure and strain relief; no exposed joints | Approximately `6 cm` multilayer heat-shrink body; individually insulated parts/junctions; bench-use limitation |

A reproducible future build should use fully traceable resistors, zeners, cable,
plug, and enclosure. Do not infer missing manufacturer ratings from generic
part-family expectations.

## 4. Construction Requirements

1. Keep red and black input conductors together for their full route. Do not
   form separate loops around the room.
2. Prevent R1/R2 bodies or leads contacting one another, sleeve, enclosure
   hardware, or clamp parts.
3. Use sleeve as the local star point only for R3, R4, clamp endpoints, and the
   output-tail sleeve.
4. Put each clamp pair close to its signal node and sleeve connection. Insulate
   the joined midpoint; do not use it as a ground or test point.
5. Provide independent strain relief for the heavy input cable and output tail.
   Solder joints must carry no cable tension.
6. Permanently mark the amplifier end `RED +` and `BLACK -`, and mark the TRS
   plug `UMC202HD INPUT 2 - CENTRAL TRS - LINE` where that interface is used.
7. Use fully insulated/shrouded connections for high-voltage DC qualification.
8. Ensure the bare-wire amplifier termination is fully captured and cannot
   bridge adjacent binding posts. Inspect and pull-test before use.

**RECORDED CONSTRUCTION — 2026-09-03:** joined figure-of-eight insulation
continues over the `2 m` input cable except approximately `5 cm` at the
amplifier end and `2 cm` at the fixture. Components form a free-air soldered
network with individually heat-shrunk bodies/leads, additional junction
insulation, and overlapping overall heat-shrink. Tapered layers and internal
wire returns transfer moderate pull into encapsulation. All conductors and both
zener midpoints are inaccessible. Sleeve is the verified local star.

The output tail is deliberately unscreened. Its short twisted construction and
approximately `1 kohm` shunts keep loop area and node impedance moderate, but it
is not electrostatically equivalent to screened balanced cable. Actual
full-system no-signal noise and movement sensitivity are therefore required
measurement-quality checks.

Unknown heat-shrink identity means no specific dielectric, abrasion,
temperature, or flame rating is claimed. Passing the `64.5 V DC` test and
post-stress matrix supports careful bench use only—not permanent installation,
crushing, abrasion, unattended operation, or use after damage.

## 5. Cable Resistance And Attenuation

At approximately `20 degrees C`, with copper resistivity
`rho ~= 0.0172 ohm mm^2/m`, each `2 m`, `1.5 mm^2` conductor is estimated at:

```text
Rlead = rho x length / area
      = 0.0172 ohm mm^2/m x 2 m / 1.5 mm^2
      = 0.0229 ohm
Rloop = 0.0459 ohm
```

At `1.00 V RMS`, divider current is about `99 uA`, so one lead drops only
about `2.3 uV`. Even `4.50 mA` fault current drops about `0.10 mV`; cable
resistance is negligible in the divider ratio.

Nominal one-leg transfer, with sleeve externally tied to amplifier reference:

```text
k = 1.0 kohm / (9.1 kohm + 1.0 kohm) = 0.099010
A = 20 log10(k) = -20.086 dB
```

Measured pre-stress branch values give:

```text
k_tip  = 1.002 / (9.125 + 1.002) = 0.098943 = -20.092 dB
k_ring = 1.003 / (9.139 + 1.003) = 0.098896 = -20.096 dB

k_floating = (1.002 + 1.003)
             / (9.125 + 1.002 + 1.003 + 9.139)
           = 0.098920 = -20.094 dB
```

These are unloaded predictions. Published UMC202HD material does not state the
`LINE` input impedance, so installed loading cannot be calculated defensibly.
Actual full-dual reference level owns installed gain; sub-decibel agreement is
not itself a safety condition.

## 6. Amplifier Loading And Fault Calculations

With external playback commoning sleeve to SU-V570 signal ground, the active
branch is approximately `10.127 kohm`. At `1.00 V RMS`:

```text
Ifixture = 1.00 V / 10.127 kohm = 98.75 uA
Pfixture = 98.75 uW
8 ohm || 10.127 kohm = 7.9937 ohm
```

The fixture changes an ideal `8 ohm` load by only `0.079%`.

The SU-V570 schematic shows approximately `+45.5 V`, `0 V`, and `-45.5 V`
rails. An ideal rail-limited sine gives `32.17 V RMS`. Divided output is
`3.18 V RMS`, `4.50 V peak`. Published amplifier conditions are lower:

| Condition | Speaker voltage | Fixture-node peak |
| --- | ---: | ---: |
| `60 W` into `8 ohm`, 20 Hz-20 kHz | `21.91 V RMS` | `3.07 V` |
| `70 W` into `8 ohm`, 1 kHz at 1% THD | `23.66 V RMS` | `3.31 V` |
| Ideal `+/-45.5 V` rail-bound sine | `32.17 V RMS` | `4.50 V` |

UMC202HD `+20 dBu` maximum line level corresponds to `7.75 V RMS` or
`10.96 V peak`; the rail-bound divided output is approximately `7.7 dB` below
that performance limit. The UMC22's lower instrument-input limit is handled by
its separate accepted-risk record.

For sustained `45.5 V DC` with shunt intact:

```text
Ifault = 45.5 V / (9.125 kohm + 1.002 kohm) = 4.49 mA
P_R1 = (4.49 mA)^2 x 9.125 kohm = 0.184 W
P_R3 = (4.49 mA)^2 x 1.002 kohm = 0.020 W
Vtip = 4.50 V
```

This supports the `0.5 W` series and `0.25 W` shunt minimums with useful
margin, subject to working-voltage and temperature derating.

## 7. Clamp Design And Redesign Constraints

Two series-opposed `5.1 V` zeners at each node produce a low-current clamp
approximately equal to zener plus forward drop:

```text
Vclamp approximately Vz + Vf approximately 5.5 to 6.2 V peak
```

The reported anode-to-anode installation is correct; polarity swaps which
device is in zener breakdown. The earlier provisional `3.3 V` choice is
superseded because its soft knee lies too close to possible `3.1-4.5 V peak`
normal divided output.

With an open shunt and `45.5 V` fault, using `5.6 V` clamp:

```text
Iclamp = (45.5 - 5.6) V / 9.125 kohm = 4.37 mA
Pzener approximately 5.0 V x 4.37 mA = 21.9 mW
```

At `64 V` commissioning with shunt intact:

```text
Iseries = (64 - 5.6) V / 9.125 kohm = 6.40 mA
Ishunt = 5.6 V / 1.002 kohm = 5.59 mA
Izener approximately 0.81 mA
Pzener approximately 4.1 mW
```

Even accidental open shunt during that current-limited test bounds zener
dissipation near `32 mW`. No `500 mW` rating is attributed to the unidentified
parts; completed four-polarity curves provide the one-off prototype evidence.

Do not substitute a power TVS without redesign and remeasurement: its rated
surge voltage may assume unavailable current and its capacitance may disturb
the audio-band reference. Do not change resistor values, clamp family,
topology, cable/reference plane, or enclosure and inherit this qualification.
A redesign must re-check attenuation, interface loading, rail/fault current,
resistor power/voltage, clamp current/knee/capacitance, construction, complete
resistance matrix, both polarities of both legs, ground paths, and low-voltage
AC behaviour.

Do not use anticipated loudness or volume position as protection. UMC202HD
`+3 dBu` output is `1.095 V RMS`; against SU-V570 `150 mV` sensitivity for
rated output, the ratio is `7.30` or `17.3 dB`, so rated amplifier output is
possible with substantial volume attenuation.

## 8. Primary Component References

- [Vishay BZX55 data sheet](https://www.vishay.com/docs/85604/bzx55.pdf)
- [Thurlby Thandar PL-series data](https://www.farnell.com/datasheets/99860.pdf)
