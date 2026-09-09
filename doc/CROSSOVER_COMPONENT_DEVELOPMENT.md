# Crossover Component Development

> - **Lifecycle:** ACTIVE COMPONENT-DEVELOPMENT AUTHORITY
> - **Owns:** capacitor selection and banks, inductor construction and taps, resistor-bank design, component measurement, thermal constraints, and development implementation
> - **Does not own:** acoustic crossover targets, final topology or polarity, driver evidence, or acoustic validation procedure
> - **Current decision:** the reversible external Seed A crossover is complete; all measured parts pass, and the user-reported cold resistance/topology checks are consistent with the intended woofer, tweeter, common-return, shunt-inductor, and L-pad connections
> - **Next gate:** component construction and on-axis/sparse-horizontal acoustic commissioning are complete; impedance/EPDR, controlled-distortion, and thermal validation continue under CROSSOVER_DESIGN.md
> - **Limitations:** measurements are user-reported; the AADE inductance measurement frequency is unknown; the completed DCRs were supplied as already-derived values without the underlying signed current/voltage pairs; Seed A remains a prototype network rather than a final crossover
> - **As of:** 2026-09-09

This file is the component-engineering companion to [CROSSOVER_DESIGN.md](CROSSOVER_DESIGN.md). Read it for component procurement, winding, PCB layout, thermal design, or construction; it is not required for acoustic modelling alone.

## 1. Development rules

- Measure and label every component before use, and enter measured values into the model.
- Keep development substitutions reversible and the inductor taps accessible.
- Treat nominal textbook values and calculated winding counts as starting points, not acceptance criteria.
- Validate final component restraint, spacing, temperature, and the as-built complete load before moving the network inside the cabinet.

## 2. Component engineering

The following retained values and construction rules define the adjustable prototype component set. They remain subordinate to measured parts and the active acoustic design.

**SUPERSEDED ACOUSTIC SEED / RETAINED COMPONENT PLANNING:** the provisional
fourth-order textbook values below established useful capacitor palettes,
footprints, wire allocations, and adjustable-construction methods. They no
longer define the network to build. The first measured-data candidate is the
same-polarity third-order Seed A in [Crossover design](CROSSOVER_DESIGN.md),
whose first VituixCAD plots were invalidated by response-scale serialisation
misinterpretation and shunt-connectivity entry errors. The retained `verified`
sparse-polar project corrects both errors and has passed the bounded crossing,
directivity, and software-load checks. A slope audit retains its tweeter branch
and records the woofer's approximately `9.1 dB` acoustic fall from
`2.1-4.2 kHz`. The subsequent bounded Seed B comparison found no dominant
alternative: modest extra suppression cost response span, phase/null, and load,
while fourth-order and targeted-notch options became negligible or locally
overfit. That comparison selected Seed A for the reversible external build;
the measured assembly and acoustic result below now supersede this planning
stage.

## 3. Capacitors

Preferred default:

- **10% tolerance polypropylene film capacitors**, selected as the cost-effective prototype default; the marked tolerance is acceptable because the crossover will be built and refined from measured rather than nominal component values;
- sensible voltage rating, typically 100–250 VDC;
- **every capacitor must be measured and labelled with its actual capacitance before insertion into the circuit**;
- parallel combinations and crossover simulations must use the measured capacitances, with the measured total entered into the model; 5% parts may be used when cost-effective, but are not required merely for nominal-value accuracy.

### 3.1 Seed A one-channel capacitor plan

**USER-REPORTED INVENTORY AND UNIT MEASUREMENTS:** the following
definite-provenance polypropylene-film parts were reported on `2026-09-07`.
The quantities are reported holdings, not a physical count performed from this
record. All voltage ratings comfortably exceed the prototype requirement.

| Manufacturer number | Nominal value | Tolerance | Rating | Reported quantity |
|---|---:|---:|---:|---:|
| TDK `B32774H4106K000` | 10 uF | +/-10% | 450 VDC | 4 |
| Panasonic `ECW-FJ60685J` | 6.8 uF | +/-5% | 600 VDC | 4 |
| Panasonic `ECW-FD2W225J` | 2.2 uF | +/-5% | 450 VDC | 10 |
| Panasonic `ECW-FD2W105JC` | 1.0 uF | +/-5% | 450 VDC | 10 |
| Panasonic `ECW-FD2W474J` | 0.47 uF | +/-5% | 450 VDC | 10 |
| Panasonic `ECW-FD2W224KB` | 0.22 uF | +/-10% | 450 VDC | 10 |
| Panasonic `ECW-FD2W104KQ` | 0.10 uF | +/-10% | 450 VDC | 10 |

The `2.2-10 uF` samples were measured with a Peak Electronics Atlas ESR+ and
include its ESR reading in ohms. The `0.10-0.22 uF` samples were measured for
capacitance with an AADE L/C Meter IIB, which does not report ESR. The readings
are user reports; the test frequency and equivalent-circuit convention of the
ESR+ reading were not recorded.

| Sample | Measured capacitance | Measured ESR |
|---|---:|---:|
| 10-A | 10.43 uF | 0.08 ohm |
| 10-B | 10.16 uF | 0.09 ohm |
| 10-C | 10.32 uF | 0.08 ohm |
| 10-D | 10.13 uF | 0.07 ohm |
| 6.8-A | 6.72 uF | 0.08 ohm |
| 6.8-B | 6.60 uF | 0.08 ohm |
| 6.8-C | 6.70 uF | 0.08 ohm |
| 6.8-D | 6.69 uF | 0.08 ohm |
| 2.2-A | 2.19 uF | 0.07 ohm |
| 2.2-B | 2.21 uF | 0.06 ohm |
| 2.2-C | 2.17 uF | 0.06 ohm |
| 2.2-D | 2.16 uF | 0.06 ohm |
| 2.2-E | 2.21 uF | 0.06 ohm |
| 2.2-F | 2.17 uF | 0.06 ohm |
| 2.2-G | 2.16 uF | 0.06 ohm |
| 2.2-H | 2.20 uF | 0.06 ohm |
| 2.2-I | 2.20 uF | 0.07 ohm |
| 2.2-J | 2.14 uF | 0.06 ohm |
| 0.22-A | 0.2214 uF | not available |
| 0.22-B | 0.2196 uF | not available |
| 0.22-C | 0.2167 uF | not available |
| 0.22-D | 0.2240 uF | not available |
| 0.10-A | 0.0993 uF | not available |
| 0.10-B | 0.1019 uF | not available |
| 0.10-C | 0.0983 uF | not available |
| 0.10-D | 0.0989 uF | not available |

Additional film capacitors up to `2.2 uF` have adequate reported voltage
ratings but less certain provenance. They are not needed for the initial plan;
they may be used later only after capacitance and ESR measurement if a useful
trim value is missing.

The joint nominal allocation for one Seed A network is:

| Seed A bank | Nominal target | Starting combination | Nominal total |
|---|---:|---|---:|
| C(W1) | 18.0 uF | 6.8 + 6.8 + 2.2 + 2.2 uF | 18.00 uF |
| C(T1) | 12.2 uF | 10 + 2.2 uF | 12.20 uF |
| C(T2) | 22.5 uF | 10 + 10 + 2.2 + 0.22 + 0.10 uF | 22.52 uF |

This consumes three of four `10 uF`, two of four `6.8 uF`, four of ten
`2.2 uF`, one `0.22 uF`, and one `0.10 uF` part. It deliberately allocates the
scarce `10 uF` parts across the whole network rather than optimising one bank in
isolation. The `0.10 uF` C(T2) trim is optional after measurement: without it,
the marked-value sum is `22.42 uF`, already only `0.36%` below target. Do not
populate it merely because the nominal arithmetic is closer.

Selecting the three banks jointly from those readings gives:

| Bank | Selected samples | Calculated total | Error from Seed A |
|---|---|---:|---:|
| C(W1) | 6.8-A + 6.8-C + 2.2-A + 2.2-C + 0.22-B | 17.9996 uF | -0.0004 uF; -0.0022% |
| C(T1) | 10-D + 2.2-J | 12.27 uF | +0.07 uF; +0.574% |
| C(T2) | 10-B + 10-C + 2.2-D | 22.64 uF | +0.14 uF; +0.622% |

This is a deliberately whole-network selection. The lowest `10 uF` sample is
used in C(T1), where a high sample cannot be offset by subtracting capacitance;
C(T2) then accepts a still-small positive error. Sample `10-A` remains unused.
C(W1)'s fifth, small capacitor trims the otherwise-low measured main-part sum
to essentially exact target. No `0.10 uF`, `1.0 uF`, `0.47 uF`, or
uncertain-provenance part is needed.

Parallel the selected parts only within their named isolated bank, label the
bank, and measure its completed capacitance and ESR before connecting it to the
crossover. One stable reading is enough; repeat only an anomalous result. The
direct completed-bank reading supersedes the arithmetic total in VituixCAD.

**USER-REPORTED COMPLETED-BANK MEASUREMENTS — CURRENT VALUES:**

| Bank | Completed capacitance | Error from Seed A | Completed ESR |
|---|---:|---:|---:|
| C(W1) | 17.96 uF | -0.04 uF; -0.222% | 0.04 ohm |
| C(T1) | 12.22 uF | +0.02 uF; +0.164% | 0.04 ohm |
| C(T2) | 22.59 uF | +0.09 uF; +0.400% | 0.04 ohm |

These direct bank readings supersede the calculated totals for modelling. All
three remain comfortably inside the preferred `+/-1%` window; no capacitor
substitution or further trimming is justified.

Aim initially for these measured-total windows:

| Bank | Preferred +/-1% window | Proportionate fallback |
|---|---:|---|
| C(W1) | 17.82-18.18 uF | Up to +/-2% is acceptable for the reversible prototype after entering the actual value in the model. |
| C(T1) | 12.078-12.322 uF | Same. |
| C(T2) | 22.275-22.725 uF | Same. |

**DERIVED SENSITIVITY CHECK:** with the other documented Seed A values fixed,
all eight simultaneous `+/-1%` capacitor-bank corners put predicted branch
equality between approximately `2.107` and `2.118 kHz`, versus `2.112 kHz`
nominal. The deliberately pessimistic simultaneous `+/-2%` corners span about
`2.101-2.123 kHz`; their predicted minimum system impedance spans about
`3.58-3.83 ohm`. This supports the `+/-1%` selection aim and shows that trimming
to hundredths of a microfarad is not useful. The final decision still uses the
model with the actual three bank values, because the corner combinations also
move the predicted reverse-polarity difference by several decibels.

Using the retained `3.5 ms` on-axis design responses and the completed-bank
capacitance and ESR readings gives branch equality near
`2.112 kHz`, approximately `15.6 degrees` relative phase, an approximately
`17.3 dB` normal-to-reverse difference, and minimum input impedance about
`3.699 ohm` near `2.654 kHz`. The corresponding nominal Seed A figures are
`2.112 kHz`, `16.7 degrees`, `16.7 dB`, and `3.705 ohm`. This is a
signal-free derived check, not a filtered-system measurement. It confirms that
the completed capacitor banks do not materially disturb Seed A.

The definite-provenance stock is sufficient for this one-channel development
network, not for two identical copies of the nominal allocation: a pair would
require six `10 uF` parts and only four are reported. Defer any pair-matching
purchase until the prototype values are acoustically accepted.

For parallel ideal capacitors, capacitance adds directly:

```text
Cbank = C1 + C2 + ...
```

ESR does not add this way and should preferably be measured on the completed
bank. At frequencies where each branch's ESR is small relative to its
capacitive reactance, a useful check is

```text
Rbank approximately equals sum(Ri * Ci^2) / (sum(Ci))^2.
```

The squared-capacitance weighting occurs because the larger capacitors carry a
larger fraction of the bank current. It is neither the arithmetic sum of the
individual ESRs nor, for unequal capacitances, their ordinary resistor-parallel
value.

### 3.2 Retained general capacitor palette

The superseded 2.4 kHz textbook LR4 network and retained prototype tuning envelopes are:

| Capacitor | Textbook value | Prototype tuning envelope |
|---|---:|---:|
| C(W1) | 13.188 µF | approximately 10–20 µF |
| C(W2) | 2.931 µF | approximately 2.2–4.4 µF |
| C(T1) | 8.792 µF | approximately 6.6–11.9 µF |
| C(T2) | 17.584 µF | approximately 13.2–23.7 µF |

Use the following shared nominal-value palette for prototype capacitor banks:

| Nominal value | Intended role |
|---:|---|
| 10 µF | main |
| 6.8 µF | main |
| 2.2 µF | coarse trim or small main |
| 1.0 µF | coarse trim |
| 0.47 µF | medium trim |
| 0.22 µF | fine trim |
| 0.10 µF | fine trim |

With no more than four populated capacitors per position, this seven-value E6 subset covers a 2.5%-spaced adjustment grid across the stated envelopes with a calculated maximum nominal miss of approximately 1.27% and a mean nominal miss of approximately 0.33%. The apparent nominal accuracy is secondary: selected parts must be chosen by measured values. The palette is retained because it provides broad adjustment, fine trimming, extensive value reuse, and a simpler development BOM.

Nominal starting combinations for the textbook network are:

| Capacitor | Starting combination | Nominal total |
|---|---|---:|
| C(W1) | 10 + 2.2 + 1.0 µF | 13.20 µF |
| C(W2) | 1.0 + 1.0 + 0.47 + 0.47 µF | 2.94 µF |
| C(T1) | 6.8 + 1.0 + 1.0 µF | 8.80 µF |
| C(T2) | 10 + 6.8 + 0.47 + 0.22 µF | 17.49 µF |

These combinations are selection seeds, not mandatory marked values. Choose the actual combination from the measured capacitor inventory, use the measured parallel sum in simulation, and match completed left/right banks by measured total capacitance.

Provide **four general parallel capacitor footprints plus a fifth small trim footprint at every capacitor position**. The expected normal population is no more than four capacitors; the fifth position is reserved primarily for a 0.10–0.47 µF measured trim capacitor so that fine adjustment does not require replacing a main capacitor. Final pad sizes and lead pitches must be checked against the selected capacitor families before PCB layout.

Alternatives:

- polyester film may be acceptable in less critical positions;
- bipolar electrolytics may be used for very large shunt values if size/cost requires it and their ESR is included in the model;
- ceramic X7R/X5R/Y5V parts should not be used in the signal path;
- boutique paper-in-oil parts are unnecessary.

## 4. Inductors

Preferred default:

- air-core inductors;
- actual DCR measured and included in simulation;
- low DCR particularly important in the woofer series path;
- large-gauge round wire is adequate;
- foil/ribbon inductors are optional, not required;
- orient adjacent inductors at 90° and separate them physically to reduce magnetic coupling.

### 4.1 Seed A mapping from available coils

**USER-REPORTED AVAILABLE FINISHED COILS:** all four are wound on the common
air-core former discussed below. Inductance, construction, and polarity-reversed
DC measurements were reported on `2026-09-08`; the inductance measurement
instrument/frequency remains open.

| Reported inductance | Turns | Wire | Present Seed A use |
|---:|---:|---:|---|
| 1.2 mH | 215 | 1.8 mm ECW | Approved donor candidate for 0.72 mH L(W1), subject to DCR. |
| 902 uH | 195 | 1.4 mm ECW | No preferred direct use; retain intact as a development spare. |
| 550 uH | 170 | 1.4 mm ECW | No preferred direct use; retain intact as a development spare. |
| 207 uH | 97 | 1.8 mm ECW | Approved donor candidate for 220 uH L(T1), subject to DCR. |

For a bounded estimate on one former and wire size, write the empirical winding
law as

```text
L = k * N^p
```

The two 1.8 mm observations give

```text
p = ln(1.200 / 0.207) / ln(215 / 97) = 2.21.
```

Therefore the estimated turn counts are

```text
N[0.72 mH] = 215 * (0.72 / 1.20)^(1 / 2.21) = 170.6 turns;
N[0.22 mH] = 97 * (0.22 / 0.207)^(1 / 2.21) = 99.7 turns.
```

The corrected turn count for the `902 uH` 1.4 mm coil is `195`, not `215`.
Together with the `550 uH`/170-turn coil this gives a local two-point exponent
of `3.61`. That is a warning that layer geometry and/or winding construction
strongly affects these two observations; it is not credible for extrapolation
down to `0.11 mH`. The earlier provisional 79-turn 1.4 mm estimate is therefore
withdrawn.

For L(W2), the better-bounded 1.8 mm relation gives

```text
N[0.11 mH] = 97 * (0.11 / 0.207)^(1 / 2.21) = 72.9 turns.
```

Use a new 1.8 mm winding starting near 73 turns. This remains an extrapolation
below the `207 uH` coil, so the meter, not turn count, is the stopping rule.

The resulting provisional implementation is therefore:

| Seed A part | Target | Provisional implementation |
|---|---:|---|
| L(W1) | 0.72 mH | Unwind the approved 1.2 mH/215-turn 1.8 mm donor towards approximately 171 turns, stopping on measured inductance. |
| L(W2) | 0.11 mH | Wind a new 1.8 mm coil towards approximately 73 turns, stopping on measured inductance. |
| L(T1) | 0.22 mH | Add about three turns to the approved 207 uH/97-turn 1.8 mm donor, stopping on measured inductance. |

The user confirms that both donor coils may be modified and that replacement
formers and ECW are readily available. Preserve the removed 1.8 mm wire if
L(W1) is unwound.

**USER-REPORTED DCR METHOD / DERIVED ACCEPTANCE:** use the isolated coil as the
DUT in this circuit:

```text
PL310QMD at 1 V, 25 mA limit
  -> 47 ohm, 0.5 W ballast
  -> U1272A in DC mA mode
  -> coil DUT
  -> supply return

U1282A in DC voltage mode directly across the coil terminals
```

This is an appropriate Kelvin-style voltage measurement provided the voltage
probes contact the cleaned coil terminals inside the current-lead contacts. The
ammeter burden changes the current but not the calculated resistance because
the actual current is measured. With a nearly zero-ohm DUT, the ballast limits
current to approximately

```text
I = 1 V / 47 ohm = 21.3 mA,
```

below the `25 mA` supply limit. Its approximate dissipation is only
`I^2 R = 21 mW`, and expected coil heating is negligible.

For better rejection of thermal EMF and meter-zero offsets, take readings in
both polarities without moving the voltage contacts. Treat reverse current and
voltage as signed values and calculate

```text
R = (Vforward - Vreverse) / (Iforward - Ireverse).
```

This follows from `Vmeasured = Voffset + I*R`: subtraction cancels the same
`Voffset`.

**USER-REPORTED DCR RESULT — METHOD PASSED:**

| Coil | Forward I / V | Reverse I / V | Derived DCR |
|---|---:|---:|---:|
| 550 uH, 170 turns, 1.4 mm | 19.888 mA / 6.659 mV | -19.870 mA / -6.648 mV | 0.33470 ohm |
| 902 uH, 195 turns, 1.4 mm | 19.703 mA / 8.317 mV | -19.843 mA / -8.361 mV | 0.42174 ohm |
| 207 uH, 97 turns, 1.8 mm | 19.800 mA / 3.727 mV | -20.041 mA / -3.768 mV | 0.18812 ohm |
| 1.2 mH, 215 turns, 1.8 mm | 19.934 mA / 7.274 mV | -19.928 mA / -7.266 mV | 0.36476 ohm |

For example, the 550 uH result is

```text
R = [6.659 - (-6.648)] mV / [19.888 - (-19.870)] mA
  = 13.307 mV / 39.758 mA
  = 0.33470 ohm.
```

The units check directly: millivolts divided by milliamperes are ohms. The
forward and reverse ratios also agree closely, so there is no evidence of a
material polarity-dependent offset.

The donor DCRs are higher than the first geometric estimates, but this does not
block the prototype. With final inductances held at Seed A targets, a
representative post-winding DCR tuple of `0.30/0.13/0.19 ohm` for
L(W1)/L(W2)/L(T1) predicts equality near `2.123 kHz`, about `12.7 degrees`
relative phase, about `19.0 dB` normal-to-reverse difference, and minimum
impedance about `3.82 ohm`. This is a sensitivity case, not a prediction of the
unfinished coils. Final measured DCRs still replace it in the model.

The existing `207 uH` coil should not be accepted unchanged merely because it
is close in percentage terms. With the completed capacitor banks and the other
Seed A values fixed, substituting `207 uH` for `220 uH` moves predicted equality
from about `2.112` to `2.127 kHz`, relative phase from `15.6` to `22.2 degrees`,
normal-to-reverse difference from `17.3` to `14.2 dB`, and minimum impedance
from `3.699` to about `3.53 ohm`. That misses the bounded phase and reverse-null
gates, so trimming this coil to measured `220 uH` has practical value.

**USER-REPORTED COMPLETED INDUCTORS / DERIVED PASS — 2026-09-08:** the AADE
L/C Meter IIB was nulled before each inductance reading; its measurement
frequency is unknown. Cold DCR was reported from the established
polarity-reversed four-point method. Supplying an already-derived DCR rather
than its signed current/voltage pairs is an explicitly accepted input route,
so those pairs are not a missing acceptance datum.

| Seed A part | Target | Measured inductance | Error | Turns | Cold DCR | Wire |
|---|---:|---:|---:|---:|---:|---:|
| L(W1) | `720 uH` | `724 uH` | `+4 uH`; `+0.556%` | 167 | `0.292 ohm` | `1.8 mm` |
| L(W2) | `110 uH` | `111 uH` | `+1 uH`; `+0.909%` | 78 | `0.172 ohm` | `1.8 mm` |
| L(T1) | `220 uH` | `219 uH` | `-1 uH`; `-0.455%` | 100 | `0.193 ohm` | `1.8 mm` |

For example, L(W1)'s percentage error is

```text
(724 uH - 720 uH) / 720 uH * 100% = +0.556%.
```

Microhenries cancel in the ratio, as required for a percentage. All three
inductors are within `+/-1%` of their Seed A targets. Their resistance ordering
is also physically coherent for the reported windings: the 78-turn coil is
lowest, the 100-turn coil next, and the 167-turn coil highest. The higher than
initially estimated DCRs are not silently discarded; they are direct practical-
model inputs. No further unwinding, added turn, or repeat measurement is
justified solely to improve nominal agreement. The unknown AADE test frequency
limits exact comparison with another LCR instrument but does not block this
reversible prototype.

### 4.2 Retained former and superseded textbook windings

Retained construction choices and current common-former baseline:

- the superseded textbook allocation used **1.8 mm diameter solderable enamelled copper wire (ECW) for L(W1) and L(T1)** and **1.4 mm diameter solderable ECW for L(W2) and L(T2)**; Seed A's current three-inductor mapping above instead uses 1.8 mm wire throughout;
- preferred supplier: **wires.co.uk / Scientific Wire Company**, with **SX1800** and **SX1400** solderable ECW ranges as current reference products;
- maximum outside diameter of the **outermost winding layer: 70 mm**; bobbin flanges may also be up to 70 mm diameter, and the winding may occupy the full radial envelope;
- wire-bearing barrel outside diameter: **30 mm** for the common former family;
- clear axial winding length: **39 mm** for all four inductors;
- every inner layer is close-wound across the available axial length; only the outermost layer may be incomplete, and axial spacers are not used;
- air-core construction using purpose-designed 3D-printed bobbins/formers that may also contribute to mechanical restraint on the crossover PCB;
- bobbin/former material: **ABS**, printed on an enclosed printer with suitable ventilation, selected for its thermal margin over PLA and PETG.

Calculated nominal windings for the provisional 2.4 kHz textbook network are:

| Inductor | Provisional target | Wire | Turns per full layer | Nominal winding estimate | Nominal winding OD | Approx. nominal wire length | Approx. nominal copper mass | Calculated nominal DCR at 20 °C |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| L(W1) | 1.000 mH | 1.8 mm | 20 | 9 full layers + 11 outer turns; 191 total | 68.2 mm | 29.0 m | 658 g | 0.195 Ω |
| L(W2) | 0.500 mH | 1.4 mm | 25 | 6 full layers + 1 outer turn; 151 total | 51.0 mm | 18.5 m | 254 g | 0.206 Ω |
| L(T1) | 0.1668 mH | 1.8 mm | 20 | 4 full layers + 8 outer turns; 88 total | 49.1 mm | 10.6 m | 242 g | 0.072 Ω |
| L(T2) | 0.7504 mH | 1.4 mm | 25 | 7 full layers + 5 outer turns; 180 total | 54.0 mm | 23.1 m | 316 g | 0.256 Ω |

The previous two-turn over-wind was sufficient only for manufacturing trim to a known target. It did not provide a credible development range: even an otherwise similar textbook network moved from 2.4 kHz to 2.2 kHz requires approximately 9.1% more inductance, before allowing for measured driver behaviour, topology refinement, or winding-model error. Development coils will therefore be wound towards a **measured ceiling approximately 25% above each provisional target** and provided with accessible taps. This is a practical tuning range around the present topology, not a guarantee that every redesign can be accommodated.

Suggested initial development wind-to values are:

| Inductor | Suggested initial development wind-to | Suggested measured wind-to inductance | Occupied winding OD implied by count | Development implementation |
|---|---:|---:|---:|---|
| L(W1) | approximately 218 turns | approximately 1.250 mH | approximately 72.0 mm on current geometry | **Does not fit the current 70 mm envelope**; use a revised development former or a 200-turn main coil plus a separate tapped series-trim inductor. |
| L(W2) | approximately 178 turns | approximately 0.625 mH | approximately 54.0 mm | Fits the current former. |
| L(T1) | approximately 103 turns | approximately 0.2085 mH | approximately 52.9 mm | Fits the current former. |
| L(T2) | approximately 217 turns | approximately 0.938 mH | approximately 57.0 mm | Fits the current former. |

The suggested turn counts are **planning estimates, not stopping criteria**. They use the present fill-adjusted geometry model provisionally calibrated against earlier reported inductance-per-turn measurements; that calibration remains subject to the loose-coil measurement audit. Measure delivered insulated-wire diameter before finalising a former. During winding, measure each loose coil in free air, away from metal, conductive loops, and other inductors, using a compensated fixture and consistent test frequency. Stop when the required measured wind-to inductance is reached, even if actual turn count differs, and record actual turn count, inductance, test frequency, and cold DCR.

Bring out and label taps at useful measured values across approximately 80%, 90%, 100%, 110%, 120%, and 125% of the provisional target, or at the closest practical turns. Measure inductance and DCR at every tap rather than deriving them from turn count alone. During crossover refinement, select taps and measured capacitor combinations, enter selected measured values into VituixCAD, and repeat filtered-driver, summed-response, reverse-polarity-null, impedance, and off-axis checks. Keep unused outer winding open-circuit and insulated, and do not cut off excess copper until the acoustic design is stable.

For L(W1), the current 30 mm-barrel, 39 mm-long former accommodates at most 200 turns within the 70 mm winding-OD limit; turn 201 starts an eleventh layer and increases occupied OD to approximately 72.0 mm. If a separate series-trim inductor is used during development, keep it well separated from and approximately orthogonal to L(W1), and measure both combined inductance and total DCR: residual mutual coupling can make inductance differ from simple series addition, while winding resistances add and affect crossover response. Once crossover values are stable, wind or trim clean left/right final inductors to matched measured values rather than treating oversized tapped development coils as automatically production-ready.

All winding patterns assume conservative enamelled-wire diameters of 1.909 mm and 1.502 mm. Nominal wire lengths, masses, and DCRs exclude lead-outs and purchasing allowance. Secure every incomplete outer layer. Completed inductance and cold DCR must be measured and entered into the crossover model; tabulated values remain manufacturing and development starting points, not substitutes for measurement. Interlocking details and PCB restraint remain to be designed.

## 5. Resistors

### 5.1 Seed A resistor plan

**USER-REPORTED DEFINITE-PROVENANCE STOCK:** ten each of `3.6`, `4.7`, `5.1`,
`5.6`, `6.8`, `7.5`, `8.2`, `9.1`, `10`, `11`, `13`, `15`, `18`, and
`22 ohm` 5 W metal-oxide resistors are available. Broad 1% E24 coverage is also
available at 0.25 and 0.5 W; assorted 1-5 W resistors below about `10 ohm` have
less certain provenance. Neither lower-power nor uncertain-provenance stock is
needed for the initial Seed A plan.

The simplest definite-provenance constructions are:

| Seed A part | Construction | Nominal result | Continuous 20 W-pad case |
|---|---|---:|---|
| R(Tser) | four `5.6 ohm`, 5 W resistors in parallel | 1.400 ohm | Approximately 6 W bank total, 1.5 W per equal resistor; 30% of individual rating. |
| R(Tpar) | three `13 ohm`, 5 W resistors in series | 39.0 ohm | Approximately 1.2 W string total, 0.4 W per equal resistor; 8% of individual rating. |

The arithmetic is

```text
R(Tser) = 5.6 ohm / 4 = 1.4 ohm;
R(Tpar) = 13 + 13 + 13 = 39 ohm.
```

This solution is exact at marked values, uses one known resistor family, and
has ample thermal margin.

**USER-REPORTED RESISTOR MEASUREMENTS:** the U1282A was used in resistance mode
on its `60 ohm` range, with the leads nulled before the first reading.

| Sample | 5.6 ohm population | 13 ohm population |
|---|---:|---:|
| A | 5.535 ohm | 12.898 ohm |
| B | 5.398 ohm | 13.034 ohm |
| C | 5.543 ohm | 12.924 ohm |
| D | 5.543 ohm | 12.986 ohm |
| E | 5.559 ohm | 12.980 ohm |
| F | 5.584 ohm | 12.999 ohm |
| G | 5.520 ohm | 12.878 ohm |
| H | 5.527 ohm | 12.925 ohm |
| I | 5.554 ohm | 12.919 ohm |
| J | 5.567 ohm | 12.881 ohm |

Select these populations:

| Seed A part | Selected samples | Calculated value | Error from target |
|---|---|---:|---:|
| R(Tser) | 5R6-E || 5R6-F || 5R6-I || 5R6-J | 1.391494 ohm | -0.008506 ohm; -0.608% |
| R(Tpar) | 13R-B + 13R-D + 13R-E | 39.000 ohm | 0.000 ohm; 0.000% |

The R(Tser) selection uses the four highest measured 5R6 values because every
sample is below its marking; this produces the highest and therefore closest
four-way parallel result. Under the conservative 6 W bank case, predicted
individual powers are `1.502`, `1.495`, `1.503`, and `1.500 W`, respectively.
The three R(Tpar) readings sum exactly to target and share the conservative
1.2 W string power at approximately `0.401`, `0.400`, and `0.399 W`.

Assemble and directly measure both completed banks. The shunt bank is a
**series string**, so its PCB footprints and links must not be copied from the
earlier all-parallel L-pad concept.

**USER-REPORTED COMPLETED RESISTOR BANKS / DERIVED PASS — 2026-09-08:** the
Agilent U1282A was used in resistance mode with auto-ranging, and its leads
were nulled before the first bank measurement.

| Seed A part | Construction | Measured bank | Error from target |
|---|---|---:|---:|
| R(Tser) | 5R6 E/F/I/J in parallel | `1.401 ohm` | `+0.001 ohm`; `+0.071%` |
| R(Tpar) | 13R B/D/E in series | `39.032 ohm` | `+0.032 ohm`; `+0.082%` |

The direct completed-bank measurements supersede the component-arithmetic
values of `1.391494` and `39.000 ohm` for modelling. R(Tser)'s direct result is
`0.009506 ohm`, or `0.683%`, above its component-derived value; R(Tpar)'s is
`0.032 ohm`, or `0.082%`, above its component-derived value. For R(Tser)'s
error from the Seed A target,

```text
(1.401 ohm - 1.400 ohm) / 1.400 ohm * 100% = +0.071%.
```

The small differences from the pre-assembly arithmetic are not large enough to
indicate a wiring error or justify dismantling either bank. Both measured banks
pass and are the values to use in the practical crossover.

### 5.2 Retained earlier L-pad planning

The earlier general L-pad implementation baseline was:

- use **5 W flameproof axial resistors in E24 values**; metal-oxide parts are acceptable, as are preferably low-inductance or non-inductive wirewound parts;
- use one resistor technology and series within each parallel bank where practicable, rather than mixing parts with substantially different thermal behaviour;
- provide PCB footprints for **five parallel resistors for R(ser)** and **three parallel resistors for R(par)**; expected normal population is four and two respectively, with additional positions retained for value selection and thermal flexibility;
- base continuous thermal calculations on the conservative assumption of **20 W into the complete L-pad**, representing 40% of the provisional 50 W system input; 50 W continuously directed into the L-pad is a test/fault-survival case rather than normal music design;
- at selected attenuation, aim to keep each resistor below **70% of its datasheet-derated rating** in the 20 W case, and preferably near or below 60%; populate the spare position if required by chosen value, tolerance analysis, or temperature testing;
- maintain at least **5 mm clearance from each resistor body to the PCB and to every other component body**, keep banks ventilated and clear of heat-sensitive parts, and verify temperatures on the assembled crossover under the conservative test condition;
- before final PCB layout, approve at least two candidate resistor families and verify body length, body diameter, lead diameter, lead pitch, mounting/derating requirements, and second-source compatibility; “5 W axial” is not a standard mechanical package.

Detailed 3–10 dB value exploration remains in **`L pad.xlsx`**. Two corrected E24 reference combinations are:

- 7 dB R(ser): **8.2 Ω || 9.1 Ω || 9.1 Ω || 9.1 Ω = 2.214 Ω**;
- 8 dB: **R(ser) = 9.1 Ω || 9.1 Ω || 10 Ω || 11 Ω = 2.435 Ω** and **R(par) = 5.1 Ω || 5.6 Ω = 2.669 Ω**.

These are prototype population candidates, not final acoustic attenuation values. Final values depend on measured in-enclosure driver responses, impedance data, and measurement-led crossover optimisation.


## 6. Handoff to acoustic design

**USER-REPORTED ASSEMBLY / COLD GATE — PASS (2026-09-08):** the completed
external crossover passed coherent point-to-point resistance checks for the
woofer path, capacitor-blocked tweeter path, L(T1) shunt, common return, and
both L-pad combinations. With the crossover, drivers, and powered-down
amplifier output connected in the verified polarities, the lead-nulled Agilent
U1272A input reading was `5.929 ohm`. Removing the two woofer-inductor DCRs gives

```text
Rwoofer = 5.929 ohm - (0.292 + 0.172) ohm
        = 5.465 ohm.
```

The result is dimensionally sound and reasonably close to the installed
woofer's approximately `5.645 ohm` curve-consistent low-frequency resistance;
the latter is not an exact DC four-wire value. Powered-idle and the initial
`0.10 V RMS`, `200-20000 Hz` audible commissioning sweep subsequently passed.
Detailed commissioning and diagnostic chronology is retained in the [Seed A
commissioning history](rew/history/SEED_A_EXTERNAL_CROSSOVER_COMMISSIONING_2026-09-08_TO_09.md).

The completed measured values and parasitics now feed the practical model in
[CROSSOVER_DESIGN.md](CROSSOVER_DESIGN.md). The component gate is complete, and
the filtered-driver, summed-response, physical reverse-polarity-null, and
sparse-horizontal gates now pass. Final crossover acceptance still requires
distortion, impedance/EPDR, and thermal gates in that active design authority.
