# Crossover Component Development

> - **Lifecycle:** ACTIVE COMPONENT-DEVELOPMENT AUTHORITY
> - **Owns:** current measured component banks, inductor construction and measurement, resistor-bank topology, second-network matching, thermal/mechanical rules
> - **Does not own:** acoustic targets, driver evidence, measurement procedures, or pre-build stock-selection arithmetic
> - **Read when:** procuring, winding, matching, laying out, or building the crossover
> - **Current decision:** Seed A's measured external component set passes; match speaker two to its completed values, then validate the new network acoustically and electrically
> - **Next gate:** recount/procure parts, build the second measured network, and retain both networks externally through pair evidence
> - **Limitations:** holdings have not been recounted; measurements are user-reported; AADE inductance frequency and signed DCR measurement pairs for completed coils are unavailable; PCB/manufacturing release is unqualified; surface temperatures do not reveal winding or voice-coil temperature
> - **As of:** 2026-09-15

The [component-build evidence](history/CROSSOVER_COMPONENT_BUILD_EVIDENCE_2026-09-07_TO_08.md)
holds superseded stock inventories, sample readings, arithmetic, donor-coil
estimates, and reverse-polarity DCR pairs. It is for audit, not routine work.
The active acoustic authority is [CROSSOVER_DESIGN.md](CROSSOVER_DESIGN.md).

## 1. Development rules

- Measure, label, and model every component used.
- Keep substitutions reversible and inductor taps accessible.
- Treat nominal values and winding turns as starting points; direct measurement
  is the acceptance criterion.
- Validate restraint, spacing, temperature, and complete as-built load before
  internal mounting.

## 2. Current Seed A component set

The current practical values are measured completed banks and coils, not sums of
individual samples or winding estimates.

| Part | Completed value | Construction / consequence |
|---|---:|---|
| C(W1) | `17.96 uF`, `0.04 ohm` ESR | within `-0.222%` of `18.0 uF` |
| C(T1) | `12.22 uF`, `0.04 ohm` ESR | within `+0.164%` of `12.2 uF` |
| C(T2) | `22.59 uF`, `0.04 ohm` ESR | within `+0.400%` of `22.5 uF` |
| L(W1) | `724 uH`, `0.292 ohm` DCR | 167 turns, `1.8 mm` ECW |
| L(W2) | `111 uH`, `0.172 ohm` DCR | 78 turns, `1.8 mm` ECW |
| L(T1) | `219 uH`, `0.193 ohm` DCR | 100 turns, `1.8 mm` ECW |
| R(Tser) | `1.401 ohm` | four selected 5R6 resistors in parallel |
| R(Tpar) | `39.032 ohm` | three selected 13R resistors in series |

All reactive values are within `+/-1%` of their Seed A targets. Model these
actual values and parasitics; do not unwind, add turns, trim, or dismantle a
completed bank solely to improve nominal agreement.

## 3. Capacitors

Use polypropylene film capacitors, normally `10%` tolerance and sensible
`100-250 VDC` or higher rating. Measure and label every part before use;
parallel only within its named isolated bank, then measure the completed bank
and enter that value and ESR in the model. The direct reading supersedes
component arithmetic.

For speaker two, recount labelled stock and procure/select a new measured set.
Match the three completed Seed A totals above as closely as practical; `+/-1%`
is preferred and up to `+/-2%` is acceptable for the reversible prototype
after modelling actual values. Check final pad size and lead pitch against
selected physical parts. Do not infer remaining holdings from the 2026-09-07
stock report.

## 4. Inductors

Use air-core coils, actual measured DCR, large-gauge round wire, and physically
separated/approximately orthogonal placement. Foil/ribbon is optional.

### 4.1 Measurement and second-network acceptance

Measure loose coils away from metal and conductive loops at a consistent,
recorded frequency. The reported Seed A method used a PL310QMD at `1 V` with a
`25 mA` limit, a `47 ohm`, `0.5 W` ballast, U1272A current measurement,
and U1282A voltage probes directly across cleaned coil terminals. Reverse
current and voltage without moving those probes and calculate:

```text
R = (Vforward - Vreverse) / (Iforward - Ireverse).
```

The signed-pair subtraction rejects a fixed thermal-EMF/meter offset. For
completed Seed A coils, already-derived DCR is accepted even though signed pairs
were not retained. AADE L/C Meter IIB was nulled before each inductance reading;
its frequency is unknown.

For speaker two, reproduce measured Seed A inductances and DCRs from
measurement, not turn count. Secure incomplete outer layers, retain access to
development taps, keep inductors separated and approximately orthogonal, and
measure the installed network because residual mutual coupling can alter
effective inductance.

### 4.2 Former and layout rules

The current common-former baseline is `1.8 mm` solderable ECW, maximum
outermost-winding OD `70 mm`, `30 mm` wire-bearing barrel OD, and `39 mm`
clear axial length. Inner layers are close-wound; only the outermost may be
incomplete and axial spacers are not used. Use the retained [3D-printed
crossover-coil models](3d_models/Crossover_Coils/README.md) and an ABS former
printed with suitable enclosed-printer ventilation.

## 5. Resistors, thermal, and PCB rules

R(Tser) is four parallel parts and R(Tpar) is three parts in **series**. Do not
copy the old all-parallel L-pad footprint. Match completed Seed A values for
speaker two.

Use one qualified family of flameproof `5 W` parts where practical, at least
`5 mm` body clearance, ventilation, and verified body dimensions, lead
diameter/pitch, mounting, derating, and a second source before manufacturing
release. The exposed Seed A prototype passed a 15-minute nominal `2 V RMS`
CTA-2034 surface check: R(Tser) rose `20.4` to `20.8 degrees C`; L(W1) rose
`20.4` to `20.6 degrees C`; neither rose in the final five minutes. This
does not qualify a different part family or enclosed PCB.

## 6. Completed assembly consequence

Seed A passed coherent point-to-point cold topology checks. With drivers and
the powered-down amplifier connected in verified polarity, input resistance was
`5.929 ohm`; subtracting woofer-filter DCR gives
`5.929 - (0.292 + 0.172) = 5.465 ohm`, consistent with installed woofer
evidence. Powered idle and an initial `0.10 V RMS`, `200-20000 Hz`
commissioning sweep were normal. Detailed commissioning is in the [Seed A
commissioning history](rew/history/SEED_A_EXTERNAL_CROSSOVER_COMMISSIONING_2026-09-08_TO_09.md).

Measured values feed the practical model in [CROSSOVER_DESIGN.md](CROSSOVER_DESIGN.md).
The component, acoustic, load/EPDR, and bounded level/thermal gates pass; retain
the network externally until speaker-two matching and final mounting decisions
are supported by evidence.
