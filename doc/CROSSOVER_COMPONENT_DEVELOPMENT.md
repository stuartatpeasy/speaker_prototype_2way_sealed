# Crossover Component Development

> - **Lifecycle:** ACTIVE COMPONENT-DEVELOPMENT AUTHORITY
> - **Owns:** capacitor selection and banks, inductor construction and taps, resistor-bank design, component measurement, thermal constraints, and development implementation
> - **Does not own:** acoustic crossover targets, final topology or polarity, driver evidence, or acoustic validation procedure
> - **Current decision:** build an adjustable external prototype from measured components; all tabulated values are development seeds
> - **Next gate:** select physical component families, verify dimensions, build measured/tapped parts, and feed as-built values back into the active design
> - **Limitations:** final values depend on valid installed FRD and crossover optimisation; winding estimates remain subordinate to measured inductance and DCR
> - **As of:** 2026-09-06

This file is the component-engineering companion to [CROSSOVER_DESIGN.md](CROSSOVER_DESIGN.md). Read it for component procurement, winding, PCB layout, thermal design, or construction; it is not required for acoustic modelling alone.

## 1. Development rules

- Measure and label every component before use, and enter measured values into the model.
- Keep development substitutions reversible and the inductor taps accessible.
- Treat nominal textbook values and calculated winding counts as starting points, not acceptance criteria.
- Validate final component restraint, spacing, temperature, and the as-built complete load before moving the network inside the cabinet.

## 2. Component engineering

The following retained values and construction rules define the adjustable prototype component set. They remain subordinate to measured parts and the active acoustic design.

## 3. Capacitors

Preferred default:

- **10% tolerance polypropylene film capacitors**, selected as the cost-effective prototype default; the marked tolerance is acceptable because the crossover will be built and refined from measured rather than nominal component values;
- sensible voltage rating, typically 100–250 VDC;
- **every capacitor must be measured and labelled with its actual capacitance before insertion into the circuit**;
- parallel combinations and crossover simulations must use the measured capacitances, with the measured total entered into the model; 5% parts may be used when cost-effective, but are not required merely for nominal-value accuracy.

The provisional 2.4 kHz textbook LR4 network and agreed prototype tuning envelopes are:

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

Locked construction choices and current common-former baseline:

- winding-conductor allocation: **1.8 mm diameter solderable enamelled copper wire (ECW) for L(W1) and L(T1)**, and **1.4 mm diameter solderable ECW for L(W2) and L(T2)**; this hybrid allocation places heavier wire where its DCR reduction is most useful relative to the associated driver impedance without using it indiscriminately;
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

The prototype tweeter L-pad implementation baseline is:

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

Selected measured values, DCR, and tolerances feed back into [CROSSOVER_DESIGN.md](CROSSOVER_DESIGN.md). Final acceptance requires the filtered-driver, summed-response, reverse-polarity-null, off-axis, distortion, impedance/EPDR, and thermal gates in that active design authority.
