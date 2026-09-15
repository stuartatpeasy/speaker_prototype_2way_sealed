# Crossover Component Build Evidence - 2026-09-07 to 2026-09-08

> - **Lifecycle:** HISTORY / RETAINED COMPONENT-BUILD EVIDENCE
> - **Owns:** dated stock, sample selection, arithmetic, donor-coil estimates, and pre-build DCR readings
> - **Does not own:** active measured component specification or speaker-two procurement decision
> - **Read when:** auditing a completed Seed A value, historic material provenance, or selection arithmetic
> - **Current consequence:** use completed measurements in [Crossover component development](../CROSSOVER_COMPONENT_DEVELOPMENT.md)
> - **Last reviewed:** 2026-09-15

These user-reported dated records explain how Seed A was built. They do not
state present stock. Direct completed-bank and completed-coil readings supersede
all arithmetic and estimates below.

## 1. Capacitor stock and selection

On `2026-09-07`, reported definite-provenance holdings were four each of
`10 uF` TDK B32774H4106K000 (`450 VDC`) and `6.8 uF` Panasonic ECW-FJ60685J
(`600 VDC`), ten each of `2.2 uF` ECW-FD2W225J, `1.0 uF` ECW-FD2W105JC,
`0.47 uF` ECW-FD2W474J (`450 VDC`), `0.22 uF` ECW-FD2W224KB, and
`0.10 uF` ECW-FD2W104KQ. The `2.2-10 uF` samples used a Peak Atlas ESR+;
smaller parts used an AADE L/C Meter IIB without ESR. Test frequency and
equivalent-circuit convention were not recorded. Lesser-provenance capacitors
were not selected.

The nominal banks were C(W1) `18.0 uF`, C(T1) `12.2 uF`, C(T2) `22.5 uF`.
Whole-network selection gave C(W1) `6.8-A + 6.8-C + 2.2-A + 2.2-C + 0.22-B =
17.9996 uF`; C(T1) `10-D + 2.2-J = 12.27 uF`; and C(T2) `10-B + 10-C +
2.2-D = 22.64 uF`. The `0.10 uF` trim was deliberately omitted. Completed
measurements were C(W1) `17.96 uF`, C(T1) `12.22 uF`, and C(T2) `22.59 uF`,
each `0.04 ohm` ESR; they are the active values.

The reported stock was sufficient for one channel, not a pair: six `10 uF`
parts would be needed but only four were reported before speaker one. Recount
rather than subtracting from this record for speaker two. For a parallel bank,
`Cbank = C1 + C2 + ...`; measure ESR directly rather than summing it. A useful
small-ESR check is `Rbank approximately equals sum(Ri * Ci^2) / (sum(Ci))^2`.

## 2. Donor coils, estimates, and pre-build DCR

Available finished coils were reported as `1.2 mH`, 215 turns, `1.8 mm` ECW;
`902 uH`, 195 turns, `1.4 mm`; `550 uH`, 170 turns, `1.4 mm`; and
`207 uH`, 97 turns, `1.8 mm`. The first and last were approved donors, while
the two `1.4 mm` coils remained spares. An empirical `L = k N^p` estimate
from the `1.8 mm` observations gave `p = 2.21`; it suggested about 171 turns
for `0.72 mH`, 73 for `0.11 mH`, and 100 for `0.22 mH`. The `1.4 mm` pair
produced an implausible local exponent `3.61`, so its earlier 79-turn estimate
was withdrawn. The meter, not the estimate, was the stopping rule.

The polarity-reversed four-point method used a `1 V`, `25 mA`-limited
PL310QMD, `47 ohm` ballast, U1272A current measurement, and U1282A coil
voltage. Results were `0.33470 ohm` (550 uH), `0.42174 ohm` (902 uH),
`0.18812 ohm` (207 uH), and `0.36476 ohm` (1.2 mH). The raw signed I/V
pairs and illustrative `0.30/0.13/0.19 ohm` sensitivity tuple are dated
planning evidence only; complete-coil DCRs `0.292/0.172/0.193 ohm` for
L(W1)/L(W2)/L(T1) supersede them.

## 3. Resistor stock and selection

Dated definite-provenance stock was ten each of `3.6`, `4.7`, `5.1`,
`5.6`, `6.8`, `7.5`, `8.2`, `9.1`, `10`, `11`, `13`, `15`,
`18`, and `22 ohm` `5 W` metal-oxide resistors. Lower-power E24 and mixed
lesser-provenance stock were not selected. Nominal construction was four
`5.6 ohm` parts in parallel for `1.400 ohm` R(Tser), and three `13 ohm`
parts in series for `39.0 ohm` R(Tpar). At a conservative `20 W` pad case
this corresponded to about `6.0 W` and `1.2 W` bank dissipation.

The U1282A was lead-nulled on the `60 ohm` range. Selected 5R6 E/F/I/J gave a
calculated `1.391494 ohm`; 13R B/D/E summed to `39.000 ohm`. Completed banks
measured `1.401 ohm` and `39.032 ohm`; these supersede sample arithmetic.
R(Tpar) is a series string, so early all-parallel L-pad footprints are invalid.

## 4. Detailed sample readings retained from the build record

The unit readings below are user-reported. They are retained to reconstruct the
dated whole-network selection, not to select a second network.

### 4.1 Capacitor samples

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

### 4.2 Pre-build reverse-polarity DCR pairs

| Coil | Forward I / V | Reverse I / V | Derived DCR |
|---|---:|---:|---:|
| 550 uH, 170 turns, 1.4 mm | 19.888 mA / 6.659 mV | -19.870 mA / -6.648 mV | 0.33470 ohm |
| 902 uH, 195 turns, 1.4 mm | 19.703 mA / 8.317 mV | -19.843 mA / -8.361 mV | 0.42174 ohm |
| 207 uH, 97 turns, 1.8 mm | 19.800 mA / 3.727 mV | -20.041 mA / -3.768 mV | 0.18812 ohm |
| 1.2 mH, 215 turns, 1.8 mm | 19.934 mA / 7.274 mV | -19.928 mA / -7.266 mV | 0.36476 ohm |

The derivation is `R = (Vforward - Vreverse) / (Iforward - Ireverse)`.
For the 550 uH coil, `13.307 mV / 39.758 mA = 0.33470 ohm`; millivolts
divided by milliamperes give ohms. The near agreement of forward and reverse
ratios did not suggest a material polarity-dependent offset.

### 4.3 Resistor sample readings and selection

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

| Seed A part | Selected samples | Calculated value | Error from target |
|---|---|---:|---:|
| R(Tser) | 5R6-E / F / I / J in parallel | 1.391494 ohm | -0.008506 ohm; -0.608% |
| R(Tpar) | 13R-B + D + E in series | 39.000 ohm | 0.000 ohm; 0.000% |

The four highest measured 5R6 parts gave the closest parallel bank because
every sample was below its marking. At the conservative 6 W bank case, the
predicted individual powers were 1.502, 1.495, 1.503, and 1.500 W; the 1.2 W
R(Tpar) string divided to about 0.401, 0.400, and 0.399 W.
