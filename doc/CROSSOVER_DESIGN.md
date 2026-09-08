# Crossover Design

> - **Lifecycle:** ACTIVE DESIGN AUTHORITY
> - **Owns:** current acoustic direction, driver polarity/topology, NL4 allocation, evidence dependencies, validation gates, and open design decisions
> - **Does not own:** detailed component-bank and inductor construction engineering; installed-driver evidence; measurement procedures
> - **Current decision:** retain the independently derived same-polarity third-order electrical Seed A as the first reversible external-prototype network; its crossing, polarity, sparse directivity, and approximately `3.7 ohm` load gates pass, and a bounded Seed B search found no alternative that improves its shallow woofer upper transition without a worse system trade
> - **Next gate:** complete and measure the three Seed A windings and the selected `1.39149` and `39.000 ohm` resistor banks, then verify the complete practical model before the external prototype measurements
> - **Limitations:** Seed A is not a final crossover; known local woofer early-tail uncertainty near 2.03 kHz; modelled woofer fall is only about `9.1 dB` from `2.1-4.2 kHz`; C2's relative-level correction is derived from the measured protection circuit and REW's calibration convention; positive-side sparse horizontal evidence only; no vertical, negative-angle, full-space power/DI, or distortion data
> - **As of:** 2026-09-08

This file is the active passive-crossover design authority. The project overview is in [README.md](../README.md), current driver evidence and approved impedance sources are in [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md), and detailed prototype-component engineering is in [CROSSOVER_COMPONENT_DEVELOPMENT.md](CROSSOVER_COMPONENT_DEVELOPMENT.md).

The approved woofer-axis C6 capture is retained as a validated phase-bearing
FRD. The common-position woofer capture TW1 has passed at the microphone's new
fixed tweeter-axis position; its windowed source and validated FRD are retained.
The initial summation pair uses TW1 and protected-tweeter C2 from that same
observation point. The raw import, its one required C2 level correction,
topology, software load, and bounded sparse-polar crossing checks now pass.
The slope audit records Seed A's shallow woofer upper transition, but the
subsequent bounded Seed B search found no dominant alternative. Seed A is
therefore suitable for the first reversible external-network iteration, with
that residual output made an explicit measurement question. Distortion remains
a later validation gate.

## 1. Prototype interface and external crossover

The prototype brings the woofer and tweeter out separately through a **Neutrik speakON NL4**.

Pin allocation:

- 1+ : woofer positive;
- 1− : woofer negative;
- 2+ : tweeter positive;
- 2− : tweeter negative.

The robust, keyed four-pole connector keeps the development crossover on the bench, permits easy substitution and polarity reversal, and avoids repeatedly disturbing the cabinet and damping.

The crossover should initially be mounted externally on a board with secure terminals and enough room to swap components. Development-inductor taps must remain accessible so that inductance can be reduced by changing the connected tap rather than cutting off copper. Unused outer winding sections must remain open-circuit, insulated, and mechanically restrained. Do not switch taps with the amplifier energised, and never permit an unused winding section to form a shorted turn.

## 2. Crossover design direction

Design the passive crossover from measured driver responses and impedance in the actual enclosure, not nominal impedances and textbook equations alone.

Current provisional acoustic target:

- crossover region: approximately **2.2–2.4 kHz**, subject to measurement;
- likely target: roughly **fourth-order Linkwitz–Riley acoustic slopes**;
- exact electrical order may differ because the drivers’ natural responses contribute to the final acoustic slopes;
- partial rather than full baffle-step compensation;
- tweeter attenuation required;
- possible woofer impedance equalisation or breakup suppression only if measurements justify it;
- final system impedance and phase must be checked.

Use steeper sixth-order slopes only to solve a measured protection or breakup problem. The normal low-frequency woofer impedance peak does not itself require crossover correction.

### 2.1 Verified measured baseline

**VERIFIED MODEL CONFIGURATION:**
[`vituixcad/Prototype loudspeaker measured baseline verified 2026-09-07.vxp`](../vituixcad/Prototype%20loudspeaker%20measured%20baseline%20verified%202026-09-07.vxp)
is `10,825` bytes with SHA-256
`a456b8c2773cf0412394c75811aa6fdb41c2047a15f5f193f130904a7fb85645`.
It contains the correct TW1 and C2 FRDs at `0 degrees`, both current installed
ZMA files, TW1 scale `0.00 dB`, C2 scale `+11.14 dB`, zero response delays,
native unsmoothed phase, no polarity inversion or minimum-phase conversion,
and zeroed driver-instance coordinates. Its two unfiltered branches are
connected directly to the source. This is the preserved raw software baseline,
not a listening network.

### 2.2 Derived exploratory Seed A

**DERIVED / PROVISIONAL MODEL SEED — NOT A CONSTRUCTION RELEASE:** an
independent complex nodal fit compared second-, third-, and fourth-order
electrical scaffolds in both polarities against the native TW1/C2 FRDs and
installed ZMAs. It included estimated winding DCR and penalised phase mismatch,
low system impedance, inadequate tweeter high-pass attenuation, and residual
woofer breakup. A same-polarity third-order network was the simplest useful
starting point. Use these rounded values for the next VituixCAD check:

| Branch | Ordered topology from source to driver | Seed A value |
| --- | --- | ---: |
| Woofer | series L(W1) | `0.72 mH`, model DCR `0.165 ohm` |
| Woofer | shunt C(W1) after L(W1) | `18.0 uF`, model ESR `0.01 ohm` |
| Woofer | series L(W2), then woofer | `0.11 mH`, model DCR `0.097 ohm` |
| Tweeter | series C(T1) | `12.2 uF`, model ESR `0.01 ohm` |
| Tweeter | shunt L(T1) after C(T1) | `0.22 mH`, model DCR `0.083 ohm` |
| Tweeter | series C(T2), then R(Tser), then tweeter | `22.5 uF`, `0.01 ohm` ESR; `1.40 ohm` series |
| Tweeter | R(Tpar) directly across tweeter | `39 ohm` |
| Polarity | both drivers | normal / same polarity |

The model DCRs are winding-geometry estimates, not measured component values.
Use the listed values exactly for software comparison before rounding to
available measured parts. At the retained response scale, this seed predicts:

- acoustic-magnitude equality near `2.12 kHz`, with about `16.8 degrees`
  relative phase and a `16.6 dB` reverse-polarity null;
- minimum system impedance about `3.71 ohm` near `2.66 kHz`, with approximately
  `-10 degrees` phase there;
- approximately `-24.8 dB` tweeter attenuation at `1 kHz` relative to its
  `8-10 kHz` level; and
- woofer output about `15.4 dB` below the tweeter at `5 kHz`, despite the raw
  woofer breakup peak.

These are independent calculated checks over the retained data range, not
VituixCAD results or measured filtered responses. The equality point is below
the provisional `2.2-2.4 kHz` direction and the predicted null is useful rather
than exceptional. Inspect the actual VituixCAD curves before deciding whether
to refine phase, move the crossover, or add any equalisation. Do not optimise
the old fourth-order values: with the measured inputs, that former scaffold
placed equality near `2.77 kHz` with roughly `102 degrees` relative phase and
did not sum correctly.

Further on-axis fitting is parked. The sparse `+20/+40/+60 degree` horizontal
directivity set supplied the proportionate discriminator against fitting local
gated-response structure. The user confirms that the vertical pivot lay in the
front baffle plane on the horizontal driver centreline; positive rotation was
anti-clockwise viewed from above. This supports the retained constant-radius
angle interpretation without a translation correction.

**PARTIAL DIRECTIVITY RESULT — TWEETER RAW BATCH PASSED:** the protected
tweeter `+20/+40/+60 degree` archive has passed identity, timing, impulse, and
window-sensitivity review. With its matched polar-only `1.5 ms` right window,
the tweeter remains broad through approximately `2.1-2.4 kHz`; progressive
narrowing is clear above about `4 kHz`. This supports retaining the present
crossover region as a candidate but does not yet choose among it or validate
Seed A. The now-completed woofer raw family supplies the necessary comparison
once its FRDs are exported and verified.

The four tweeter polar FRDs pass native-response verification and are preserved
separately. The root C2 `3.5 ms` design FRD has returned exactly to its previous
verified size and checksum, so the measured baseline and Seed A dependencies
are safe. The remaining discriminator is the combined woofer/tweeter polar
comparison, not another capture.

**DIRECTIVITY RESULT — BOTH SPARSE RAW FAMILIES VERIFIED:** the completed
`+20/+40/+60 degree` woofer traces and exports pass UUID, timing, metadata,
impulse-envelope, reflection, window, and native-response review. A common `3.5 ms`
right window is stable enough for the crossover question: changing it to
`3.0 ms` changes derived directivity over `1.8-2.6 kHz` by `0.13-0.53 dB RMS`
across the three angles. The woofer is already materially directional through
the candidate crossover region: at `2.4 kHz`, approximate changes from on-axis
are `-0.94`, `-1.80`, and `-4.39 dB` at `+20`, `+40`, and `+60 degrees`;
at `3.0 kHz` they are `-1.63`, `-4.20`, and `-9.75 dB`. A local `+40 degree`
feature near `2.2 kHz` carries about `0.8 dB` window-choice uncertainty and
must not drive fine optimisation. VituixCAD reproduction and combined
modelling, not more acoustic sweeps, are the proportionate next steps.

One-sixth-octave band means put the smallest RMS woofer/tweeter directivity
mismatch across the three measured angles at approximately `2.2-2.3 kHz`:
`1.99 dB` at `2.2 kHz` and `2.05 dB` at `2.3 kHz`, compared with `3.32 dB`
at `2.1 kHz`, `3.10 dB` at `2.4 kHz`, and about `3.8 dB` at
`2.5-2.6 kHz`. This supports the existing handover region and argues against
moving it materially higher; it does not define a crossover frequency to the
nearest hundred hertz.

**DERIVED PRELIMINARY SEED A POLAR MODEL:** applying Seed A's documented
component values and DCR/ESR, the installed complex impedances, native polar
phase, and the common protected-tweeter `+11.14 dB` scale gives off-axis
extrema over `1.8-3.0 kHz` of approximately `-1.74/+0.29 dB` at
`+20 degrees`, `-1.94/+2.11 dB` at `+40 degrees`, and `-3.12/+0.43 dB` at
`+60 degrees`. The positive `+40 degree` feature is near `2.2 kHz`, appears in
both raw drivers, and overlaps the woofer's approximately `0.8 dB` local
window-choice uncertainty. Seed A therefore remains a useful first candidate.
Its angle mappings and summation were subsequently reproduced in VituixCAD;
the signal-free slope audit below now owns the remaining construction-release
question.

**VERIFIED VITUIXCAD SPARSE-POLAR ASSIGNMENT / PLOT CHECK PASSED:**
[`vituixcad/Prototype loudspeaker crossover Seed A sparse polar verified 2026-09-07.vxp`](../vituixcad/Prototype%20loudspeaker%20crossover%20Seed%20A%20sparse%20polar%20verified%202026-09-07.vxp)
is `25,484` bytes with SHA-256
`6dd951a5b89040418841887a365d3e8e0a3e1fbb2634a7e084240fd10eea8e2b`.
Direct XML comparison against Seed A confirms that its complete `CROSSOVER`
subtree is unchanged, as are both installed ZMA assignments, response scales,
delays, polarity, smoothing, and minimum-phase settings. Each driver now has
explicit horizontal `0/+20/+40/+60 degree` response entries pointing to its
verified `polar/` FRDs. The project is set to horizontal-only, `20 degree`
angular steps, with vertical inclusion disabled.

The user reports that the retained project opened without warnings and that
each driver showed the intended four responses. In the final user-supplied
screenshots, the normal-polarity branches cross near `2.1 kHz` and sum
constructively; temporary tweeter inversion produces a deep cancellation near
that crossing, visually consistent with the independently predicted
approximately `25.1 dB` null. The normalised measured-angle plot shows the
expected progressive narrowing and no broad discontinuity that justifies
rejecting or finely re-optimising Seed A. The user confirms that the tweeter is
restored to normal polarity. This is application-rendered corroboration of the
saved assignment and passes the bounded software acoustic gate; it is not a
filtered-system measurement.

Only the measured positive side is evidence. Do not treat interpolation, any
mirrored negative side, or the project's inherited power/directivity settings
as a measured full-space result; full CTA-2034 or sound-power conclusions
require substantially more angular coverage.

**RESOLVED VXP SERIALISATION AND CONNECTIVITY ERRORS:** the initial project
opened without warning and both driver lists contained the intended angles, but
its screenshots exposed a main branch crossing inconsistent with the independent
model. The saved `3.6057864302164244` response-scale value was initially
misdiagnosed as dB. VituixCAD displays acoustic scale in dB but serialises this
field as a linear multiplier:

```text
20 log10(3.6057864302164244) = 11.140 dB.
```

The original stored scale was therefore correct. Intermediate files that store
`11.14` apply approximately `+20.94 dB` and over-weight the tweeter by about
`9.80 dB`; those superseded acoustic screenshots exhibit the resulting low
crossing.
Separately, the initial Seed A files placed `R2=39 ohm` in series below D2
instead of across it. Screenshots made that schematic error visible. The user
then repositioned the corrected parallel branch for clarity; its two terminals
still visibly share the tweeter's upper node and ground, so the change is
cosmetic and functionally correct.

The retained `verified` files combine the original correct stored multiplier
with graph-verified parallel R2 connectivity and series `R1=1.4 ohm`. Earlier
source, `level-corrected`, `corrected`, and redundant on-axis Seed A variants
were deleted at the user's request after their failure mode and reconstruction
inputs were recorded here; none of their acoustic plots validates Seed A. The
latest impedance plot uses the intended parallel topology and is unaffected by
acoustic response scale, so it remains valid. The user confirmed that the
tweeter was returned to uninverted state after each temporary reverse-polarity
screenshot.

The verified sparse-polar project uses the tweeter's shorter `1.5 ms` polar
window rather than the retained `3.5 ms` on-axis design FRD.
Independent calculation predicts its main branch equality at about `2.101 kHz`,
approximately `6.4 degrees` relative phase, and an approximately `25.1 dB`
reverse-polarity null. The final screenshots agree with those checks. The
earlier `2.12 kHz`, `16.8 degree`, `16.6 dB` figures remain the corresponding
prediction from the longer `3.5 ms` on-axis design response. This distinction
is an analysis-window consequence, not a physical timing change.

For the retained Seed A project, the intended passive topology has a
derived minimum input impedance of approximately `3.705 ohm` near `2.655 kHz`
at approximately `-10.4 degrees`. This value was calculated from the installed
ZMAs and intended circuit. The latest VituixCAD impedance plot uses the same
parallel topology and agrees visually, so the proportionate software load gate
passes; final as-built impedance and EPDR remain later measurement gates.

### 2.3 Signal-free Seed A design audit

**DERIVED RESULT — PROVISIONAL HOLD, SUPERSEDED BY SECTION 2.4:** complex
evaluation of the documented network against the retained `3.5 ms` TW1/C2
design FRDs and installed ZMAs reproduces the main Seed A checks after
one-sixth-octave local averaging: branch equality at approximately `2.102 kHz`,
approximately `16.1 degrees` relative phase, `5.71 dB` constructive addition
over the louder branch, and an approximately `16.84 dB` normal-to-reverse
difference. The system minimum remains approximately `3.705 ohm` near
`2.654 kHz` at `-10.4 degrees`. These are model-derived values, not filtered-
system measurements.

The tweeter branch is not a `-6 dB` L-pad. At the measured approximately
`3.48 ohm` tweeter impedance near `2.3 kHz`, `39 ohm` in parallel gives about
`3.20 ohm`; with `1.40 ohm` in series its resistive divider is approximately
`-3.15 dB`. The complete high-pass is approximately `-3.88 dB` at `2.3 kHz`
and its `8-10 kHz` electrical passband is approximately `-2.70 dB`. Combined
with the measured raw tweeter response, filtered tweeter output at `1 kHz` is
about `24.4 dB` below its `8-10 kHz` output. The approximately `15-17 dB/oct`
measured acoustic rise over representative one-octave intervals below the
crossing is reasonably close to the `18.6 dB` crossing-to-half-frequency change
of an ideal LR4 high-pass; no fourth tweeter reactance is presently justified.

The woofer is the unresolved branch. From `2.1` to `4.2 kHz` its filtered
measured output falls only about `9.1 dB`, compared with approximately
`18.6 dB` from the crossing to twice the crossing frequency for an ideal LR4
low-pass. The raw breakup region counteracts much of the electrical roll-off;
at `5 kHz` the woofer remains only about `14.8 dB` below the tweeter and changes
the modelled total by about `1.4 dB`. This is a material upper-stopband question
even though the overall one-sixth-octave-smoothed `1.5-5 kHz` total spans only
about `3.65 dB` and the sparse directivity plot showed no broad discontinuity.

A bounded check adding `1-22 uF` as the conventional fourth shunt capacitor
after the existing second woofer inductor, without retuning the other values,
did not cure the problem: the `2.1-4.2 kHz` fall became progressively shallower,
from approximately `-8.5 dB` at `1 uF` to rising output at `22 uF`, while the
crossing moved downward. Increasing the existing second inductor improved
upper attenuation but progressively worsened phase alignment, reverse-null
depth, and total-response span. Component count alone is therefore not the
answer. This result provisionally held construction for the bounded multi-value
comparison recorded in Section 2.4; it is retained to explain that
discriminator rather than as the current decision.

For resistor planning only, the pad-alone model assigns approximately `30%` of
its real input power to the `1.40 ohm` series resistor and approximately `6%`
to the `39 ohm` shunt over `2.3-10 kHz`. If `20 W` reaches the complete pad,
that is approximately `6.0 W` and `1.2 W` respectively; the final bank design
must use the selected network and measured parts.

### 2.4 Bounded Seed B search

**DERIVED DECISION — NO SEED B PROMOTED:** a deterministic bounded search held
the verified Seed A tweeter branch fixed and compared retuned three-reactance
and four-reactance woofer ladders over the installed complex impedance and
phase-bearing acoustic data. Hard gates retained a `2.05-2.25 kHz` equality
region, at most `20 degrees` relative phase, at least `15 dB` normal-to-reverse
difference, no worse than a `4.2 dB` robust `1-5 kHz` total-response span, and
at least `3.5 ohm` minimum impedance. Approximate inductor DCR scaled with the
square root of inductance from the Seed A winding estimates; candidate values
therefore remain comparative rather than construction specifications.

The strongest constrained three-reactance result used approximately
`0.739 mH / 15.34 uF / 0.320 mH`. Relative to Seed A it improved woofer fall
from `-8.89` to `-12.15 dB` over `2.1-4.2 kHz` and woofer/tweeter separation at
`5 kHz` from `-15.50` to `-17.36 dB`. That modest improvement was not dominant:
the robust `1-5 kHz` total span worsened from `3.46` to `4.20 dB`, relative
phase from `16.93` to `19.52 degrees`, reverse difference from `16.52` to
`15.27 dB`, and minimum impedance from `3.707` to `3.599 ohm`.

The strongest four-reactance searches drove their added final shunt capacitor
to approximately `0.06-0.14 uF`, hundreds of ohms near crossover and therefore
electrically negligible. They collapse toward the same three-reactance result
rather than justify another filter pole. A separate Seed A plus series-RLC
shunt search could produce a narrow dip near `4.2 kHz`, but no candidate met
both `-14 dB` or better woofer fall over `2.1-4.2 kHz` and at least `20 dB`
woofer/tweeter separation at `5 kHz` while retaining all system gates. That is
the signature of fitting one local feature rather than solving the broad
transition.

The ideal LR4 octave comparison remains a useful diagnostic, not an absolute
component-order requirement. Seed A's residual woofer output changes the
modelled total by only about `1.3 dB` at `5 kHz`, and its verified sparse polar
plot showed no broad discontinuity. With no model alternative providing a
clear whole-system improvement, further optimisation against gated raw data is
more likely to fit measurement structure than to improve the loudspeaker. Seed
A is therefore released for a reversible external build. Promote a Seed B only
if measured filtered branches reproduce a broad, design-relevant weakness.

**PRACTICAL CAPACITOR MAPPING PASSED:** the assembled one-channel banks measure
`17.96 uF` for C(W1), `12.22 uF` for C(T1), and `22.59 uF` for C(T2), each with
reported `0.04 ohm` ESR. All are within `0.4%` of Seed A. An independent complex
check against the retained `3.5 ms` on-axis design responses leaves predicted
equality near `2.112 kHz`, normal-to-reverse difference near `17.3 dB`, and
minimum input impedance near `3.699 ohm`; these are immaterial changes from
nominal Seed A.

The reported finished-coil inventory provides plausible donor routes for
L(W1) and L(T1), plus a new-wind route for L(W2); the user confirms that the
test coils may be modified and that replacement formers and ECW are readily
available. Cold DCR remains open. Directly substituting the existing `207 uH`
coil for L(T1) fails the bounded phase and reverse-null gates; it should be
trimmed to measured `220 uH`, not accepted unchanged. Exact component
assignments, winding derivation, and measurement requirements are owned by
[Crossover component development](CROSSOVER_COMPONENT_DEVELOPMENT.md).

Definite-provenance 5 W metal-oxide stock also gives exact nominal Seed A
resistor constructions: four `5.6 ohm` parts in parallel for `1.40 ohm`, and
three `13 ohm` parts in series for `39 ohm`. Their conservative predicted bank
dissipations are approximately `6.0 W` and `1.2 W`, respectively, so individual
parts remain well below their 5 W ratings. Measured selection gives
`1.391494 ohm` from 5R6 samples E/F/I/J in parallel and exactly `39.000 ohm`
from 13R samples B/D/E in series. Completed-bank checks remain open.

Polarity-reversed DC measurements give the available coils DCRs from
`0.18812-0.42174 ohm`. The corrected `902 uH` coil count is `195`, not `215`,
which invalidates the earlier 79-turn 1.4 mm L(W2) extrapolation. The current
route retains the 1.8 mm donors for L(W1) and L(T1) and uses a new approximately
73-turn 1.8 mm starting winding for L(W2), with measured inductance as the
stopping criterion. A representative higher-DCR sensitivity case retains the
crossing, phase, reverse-null, and load gates; final values still require the
completed windings.

**INTENTIONAL RETENTION BOUNDARY:** `vituixcad/` now contains only the verified
measured baseline and the verified sparse-polar Seed A project. The latter is
the sole current Seed A software authority and preserves the widest useful
model; the longer-window on-axis Seed A can be reconstructed from the measured
baseline, the documented component table, and the retained FRD/ZMA sources.
Superseded intermediate projects and three legacy `.mdat` files formerly kept
under `vituixcad/` were deleted at the user's request. The current raw
measurement authorities remain under `rew/`; the deleted tracked legacy files
also remain recoverable from Git history if provenance is ever required.

## 3. Evidence and model dependencies

Use only the approved installed ZMA sources identified in [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md). Phase-bearing FRD data must share a valid electrical timing reference and fixed measurement geometry; use the current method and runbook routed by [MEASUREMENT_WORKFLOW.md](MEASUREMENT_WORKFLOW.md).

The useful present crossover-region loads near 2.30 kHz are approximately:

- woofer: 7.98 ohm at +10.8 degrees;
- tweeter: 3.48 ohm at -5.0 degrees.

These complex loads replace nominal driver impedances in every exploratory
model. The approved C6 installed-woofer source is
[`rew/frd/SB17NRX2C35-8/000deg_1m_UMC22_2026-09-06.frd`](../rew/frd/SB17NRX2C35-8/000deg_1m_UMC22_2026-09-06.frd).
It remains useful woofer-axis evidence. The designated common-position TW1 FRD path is
[`rew/frd/SB17NRX2C35-8/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd`](../rew/frd/SB17NRX2C35-8/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd).
The protected tweeter C2 response at the same fixed point is retained and its
windowed FRD passes native-data verification. TW1's FRD was restored exactly
after the recoverable export-path collision, so the common-position pair is
ready for initial acoustic summation after one scalar correction. REW defines
each generated loopback-calibration response as `0 dB` at `1 kHz`. With the
measured `10.13 uF`, `0.08 ohm` protection capacitor and installed tweeter ZMA,
the tweeter-terminal/source ratio at `1.001 kHz` is `0.27744`, or `-11.14 dB`.
The post-capacitor reference removes the capacitor's frequency-dependent
magnitude and phase, but that `1 kHz` normalisation leaves the same constant
level reduction in C2. Set C2 response scale to `+11.14 dB`; leave TW1 at
`0.00 dB`, both response delays at `0 us`, minimum-phase conversion off, and
polarity uninverted for the raw baseline. Do not add another geometric or
acoustic-centre delay because the common-timed FRDs already contain it.

Include measured component capacitance,
inductance, DCR,
tolerances, driver spacing, baffle diffraction, and the complete system
impedance/phase in the model. Treat textbook tables and optimiser output as
seeds, particularly if optimisation produces extreme or implausible values.

## 4. Excursion and power philosophy

Do not design for routine operation at rated Xmax:

- normal use well below Xmax;
- loud passages remain below Xmax through most of the operating band;
- brief peaks may approach Xmax;
- Xmech/Xlim remain emergency limits, not operating targets.

Account for $Bl$, suspension and inductance variation, harmonic and intermodulation distortion, and thermal compression. The sealed near-wall alignment is not intended to extract heroic deep bass from one 6.5-inch midwoofer.

Tweeter power ratings must always be read with their specified high-pass condition. Do not apply an unfiltered broadband or low-frequency signal to the bare tweeter.

## 5. Required validation before freezing the crossover

1. Use only current, valid installed ZMA and phase-bearing FRD sources identified in [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md).
2. Optimise for acoustic slopes, summed magnitude, directivity, impedance, and component constraints rather than textbook electrical values.
3. Build the crossover externally with measured component values and accessible taps.
4. Measure individual filtered drivers, normal-polarity sum, reverse-polarity null, horizontal off-axis response, distortion, and system impedance/EPDR.
5. Update the model with as-built component values and repeat one controlled change at a time.
6. Move the network inside only after the complete measured assembly is stable and thermally acceptable.

## 6. Open crossover items

- exact crossover frequency and topology;
- exact component values and acoustic polarity;
- final L(W1) development implementation: revised former or separate tapped trim inductor;
- inductor interlock, outer-layer binding, and PCB restraint;
- final system impedance classification and amplifier headroom;
- final crossover mounting position;
- whether DSP remains development-only or is used in the finished system.
