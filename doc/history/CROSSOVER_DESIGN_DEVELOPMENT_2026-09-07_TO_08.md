# Crossover Design Development - 2026-09-07 to 2026-09-08

> - **Lifecycle:** HISTORY / SUPERSEDED DESIGN DEVELOPMENT
> - **Owns:** exploratory Seed A and Seed B modelling, predecessor VXP review, and resolved VXP serialisation/connectivity errors
> - **Does not own:** current Seed A decision, measured-component model, or validation gate
> - **Read when:** auditing why Seed A was selected, reproducing a historic calculation, or diagnosing an old VXP
> - **Current consequence:** retain measured same-polarity third-order Seed A; current evidence is in [Crossover design](../CROSSOVER_DESIGN.md)
> - **Last reviewed:** 2026-09-15

This record retains dated calculations and superseded VXP interpretation. They
were useful selection evidence, not measured filtered-system evidence.

## 1. Exploratory Seed A

An independent complex nodal fit compared second-, third-, and fourth-order
scaffolds in both polarities against native TW1/C2 FRDs and installed ZMAs,
penalising phase mismatch, low impedance, tweeter attenuation, and woofer
breakup. The simplest useful seed was same-polarity third order:

| Branch | Source-to-driver order | Seed value |
|---|---|---:|
| Woofer | L(W1), shunt C(W1), L(W2) | `0.72 mH` / `18.0 uF` / `0.11 mH` |
| Tweeter | C(T1), shunt L(T1), C(T2), R(Tser) | `12.2 uF` / `0.22 mH` / `22.5 uF` / `1.40 ohm` |
| Tweeter shunt | R(Tpar) directly across tweeter | `39 ohm` |
| Polarity | both drivers | normal / same |

Estimated DCRs (`0.165`, `0.097`, `0.083 ohm`) and capacitor ESRs
(`0.01 ohm`) were planning inputs, not measurements. The longer-window
calculation predicted `2.12 kHz` equality, `16.8 degrees` relative phase,
`16.6 dB` reverse null, `3.71 ohm` minimum near `2.66 kHz`, `-24.8 dB`
tweeter attenuation at `1 kHz`, and woofer output `15.4 dB` below tweeter at
`5 kHz`. The former fourth-order scaffold predicted `2.77 kHz`,
approximately `102 degrees`, and poor summation, so it was superseded.

The positive `+20/+40/+60 degree` raw-driver data supported a handover region
near `2.2-2.3 kHz` without defining it to the nearest hundred hertz. The
woofer's local `+40 degree`, `2.2 kHz` feature carried approximately
`0.8 dB` window-choice uncertainty. The vertical pivot was in the front-baffle
plane on the horizontal driver centreline; positive rotation was anti-clockwise
viewed from above. Use only the measured positive side; no full-space/directivity
conclusion follows.

## 2. Nominal sparse-polar VXP and correction

[`vituixcad/Prototype loudspeaker crossover Seed A sparse polar verified 2026-09-07.vxp`](../../vituixcad/Prototype%20loudspeaker%20crossover%20Seed%20A%20sparse%20polar%20verified%202026-09-07.vxp)
was `26,630` bytes with SHA-256
`e8235831de072724d95ad0a5d1b84fb57bc4235693953d717626b5fadb8d3538` at
review. It contains two drivers, eight electrical components, twelve sources,
and explicit horizontal `0/+20/+40/+60 degree` entries per driver; the current
practical VXP retains sources/settings and substitutes measured values.

The stored C2 scale `3.6057864302164244` is a linear multiplier, displayed by
VituixCAD as `20 log10(3.6057864302164244) = 11.140 dB`. Intermediate files
that stored `11.14` applied about `+20.94 dB`, over-weighting the tweeter by
about `9.80 dB`; their acoustic plots are invalid. Separately, R2=`39 ohm`
was initially in series below D2 rather than across it. The retained verified
VXP has R2 in parallel and R1=`1.4 ohm` in series; the later R(Tpar) symbol
move was cosmetic. Earlier source, level-corrected, corrected, and redundant
on-axis variants were deleted at the user's request after their reconstruction
inputs and failure modes were recorded. None validates Seed A.

The verified sparse-polar VXP uses the tweeter's `1.5 ms` polar window rather
than the `3.5 ms` on-axis design FRD. Its calculation gives `2.101 kHz`,
`6.4 degrees`, and a `25.1 dB` reverse null; the longer-window seed's
`2.12 kHz`, `16.8 degrees`, and `16.6 dB` are an analysis-window
difference, not a physical timing change. Its calculated `3.705 ohm` minimum
near `2.655 kHz` at `-10.4 degrees` was later superseded for hardware
judgement by the as-built load measurement.

## 3. Signal-free audit and bounded Seed B comparison

The longer-window replay gave `2.102 kHz`, `16.1 degrees`, `5.71 dB`
constructive addition, `16.84 dB` normal-to-reverse difference, and a
`3.705 ohm` minimum. It showed a reasonable tweeter rise but only about
`9.1 dB` woofer fall from `2.1-4.2 kHz`; raw breakup counteracted electrical
roll-off. A conventional added woofer shunt capacitor (`1-22 uF`) made that
fall progressively shallower, while a larger second inductor worsened phase,
null, and response span. This was a provisional hold, not a construction gate.

The deterministic Seed B search fixed the Seed A tweeter branch and required
`2.05-2.25 kHz` equality, at most `20 degrees`, at least `15 dB` reverse
difference, at most `4.2 dB` robust `1-5 kHz` span, and at least `3.5 ohm`
minimum impedance. DCR scaled with square-root inductance, so comparisons were
not construction specifications. The strongest three-reactance result
(`0.739 mH / 15.34 uF / 0.320 mH`) improved woofer fall `-8.89` to
`-12.15 dB` and `5 kHz` separation `-15.50` to `-17.36 dB`, but worsened
span `3.46` to `4.20 dB`, phase `16.93` to `19.52 degrees`, reverse
difference `16.52` to `15.27 dB`, and minimum impedance `3.707` to
`3.599 ohm`. Four-reactance searches reduced their added capacitor to
`0.06-0.14 uF`, electrically negligible. A series-RLC shunt could fit a
narrow `4.2 kHz` dip but did not meet all system gates. No Seed B was promoted.

This comparison selected Seed A for a reversible build. Measured construction,
acoustic evidence, load, and bounded level/thermal evidence subsequently
replaced the signal-free work as the current authority.

## 4. Retained sparse-polar directivity detail

The protected-tweeter `+20/+40/+60 degree` archive passed identity, timing,
impulse, and window-sensitivity review. With its matched `1.5 ms` right
window, it remained broad through approximately `2.1-2.4 kHz` and narrowed
progressively above about `4 kHz`. The completed woofer family passed UUID,
metadata, impulse-envelope, reflection, window, and native-response review.
A common `3.5 ms` right window was stable enough: changing to `3.0 ms`
changed derived directivity over `1.8-2.6 kHz` by `0.13-0.53 dB RMS`.

At `2.4 kHz`, woofer changes from on-axis were `-0.94`, `-1.80`, and
`-4.39 dB` at `+20`, `+40`, and `+60 degrees`; at `3.0 kHz` they were
`-1.63`, `-4.20`, and `-9.75 dB`. One-sixth-octave mismatch between
woofer and tweeter was lowest near `2.2-2.3 kHz`: `1.99 dB` at `2.2 kHz`
and `2.05 dB` at `2.3 kHz`, against `3.32 dB` at `2.1 kHz`,
`3.10 dB` at `2.4 kHz`, and about `3.8 dB` at `2.5-2.6 kHz`.

The preliminary Seed A polar calculation gave extrema over `1.8-3.0 kHz` of
`-1.74/+0.29 dB` at `+20 degrees`, `-1.94/+2.11 dB` at `+40 degrees`,
and `-3.12/+0.43 dB` at `+60 degrees`. The positive `+40 degree` feature
near `2.2 kHz` appeared in both drivers and overlapped the approximately
`0.8 dB` local woofer window uncertainty. It did not justify fine
optimisation or further raw sweeps.

## 5. Retained signal-free branch detail

At the measured approximately `3.48 ohm` tweeter impedance near `2.3 kHz`,
`39 ohm` in parallel gives about `3.20 ohm`; with `1.40 ohm` series its
resistive divider is about `-3.15 dB`. The complete high-pass was about
`-3.88 dB` at `2.3 kHz` and its `8-10 kHz` passband about `-2.70 dB`;
filtered tweeter output at `1 kHz` was about `24.4 dB` below `8-10 kHz`.
The ideal LR4 reference was diagnostic, not an order requirement.

For resistor planning only, the pad-only model assigned approximately `30%`
of real input power to the `1.40 ohm` series resistor and `6%` to the
`39 ohm` shunt over `2.3-10 kHz`. If `20 W` reached the pad, that was
about `6.0 W` and `1.2 W`; actual selected-bank construction superseded
this planning calculation.
