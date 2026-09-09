# Crossover Design

> - **Lifecycle:** ACTIVE DESIGN AUTHORITY
> - **Owns:** current acoustic direction, driver polarity/topology, NL4 allocation, evidence dependencies, validation gates, and open design decisions
> - **Does not own:** detailed component-bank and inductor construction engineering; installed-driver evidence; measurement procedures
> - **Current decision:** retain the same-polarity third-order Seed A as the reversible external prototype; its measured components, practical model, on-axis filtered branches, normal sum, physical reverse null, and sparse `0/+20/+40/+60 degree` horizontal responses pass proportionately, with a moderate crossover-region directivity flare retained as a possible refinement rather than grounds for an immediate component change
> - **Next gate:** establish and run a qualified as-built full-system impedance/phase measurement before higher-level distortion or thermal testing; no further unchanged acoustic sweep is presently required
> - **Limitations:** Seed A is not a final crossover; the user's stated cosmetic R(Tpar) move in the reopened/saved practical VXP was accepted without inspection; the AADE inductance test frequency is unknown; known local woofer early-tail uncertainty near 2.03 kHz; modelled woofer fall is only about `9.1 dB` from `2.1-4.2 kHz`; C2's relative-level correction is derived; the threshold-triggered persistent `1 kHz` distortion is now strongly associated with the undamped tweeter-only load but its exact mechanism is unproved and ultrasonic behaviour remains outside the UMC22/48 kHz observation band; the overnight Windows restart means the current software/process state does not reproduce the discovery state; positive-side sparse horizontal evidence only; no vertical, negative-angle, full-space power/DI, or controlled sweep distortion data
> - **As of:** 2026-09-09

This file is the active passive-crossover design authority. The project overview is in [README.md](../README.md), current driver evidence and approved impedance sources are in [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md), and detailed prototype-component engineering is in [CROSSOVER_COMPONENT_DEVELOPMENT.md](CROSSOVER_COMPONENT_DEVELOPMENT.md).

The approved installed impedance and phase-bearing acoustic sources remain the
model baseline. Their raw import, C2 level correction, topology, software load,
and sparse-polar assignments pass. The completed measured-component Seed A
network then passed physical filtered-branch, normal-sum, reverse-polarity, and
positive-horizontal acoustic validation. Its broad measured equality near
`1.83 kHz` is lower than the practical model prediction, and its shallow woofer
upper transition plus moderate horizontal flare remain possible refinement
targets. Neither currently outweighs the successful summation and load-model
gates. Controlled full-system distortion and as-built load/thermal validation
remain open; the earlier undamped tweeter-only fault investigation is parked.

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

**ORIGINAL PROVISIONAL TARGET / CURRENT MEASURED CONSEQUENCE:** the initial
design region was approximately `2.2-2.4 kHz` with roughly fourth-order
Linkwitz-Riley-like acoustic slopes. The completed Seed A prototype instead
crosses broadly near `1.83 kHz` with essentially coincident phase and passes its
physical normal/reverse summation gates. Retain the following design principles
for any later controlled refinement:

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
starting point. These rounded values defined the first VituixCAD check:

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

The model DCRs were winding-geometry estimates, not measured component values.
At the retained response scale, this seed predicted:

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
than exceptional. The later VituixCAD and physical results are recorded below.
The old fourth-order values remain superseded: with the measured inputs, that
former scaffold
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
narrowing is clear above about `4 kHz`. At that stage this supported retaining
the candidate region but did not yet choose among it or validate Seed A; the
subsequently completed woofer family provided the required comparison.

The four tweeter polar FRDs pass native-response verification and are preserved
separately. The root C2 `3.5 ms` design FRD has returned exactly to its previous
verified size and checksum, so the measured baseline and Seed A dependencies
were preserved. The combined woofer/tweeter polar comparison subsequently
completed the discriminator without another raw capture.

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
modelling were therefore selected instead of more acoustic sweeps.

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

**VERIFIED VITUIXCAD SPARSE-POLAR ASSIGNMENT / NOMINAL PREDECESSOR:**
[`vituixcad/Prototype loudspeaker crossover Seed A sparse polar verified 2026-09-07.vxp`](../vituixcad/Prototype%20loudspeaker%20crossover%20Seed%20A%20sparse%20polar%20verified%202026-09-07.vxp)
has a committed verified reference at `25,484` bytes with SHA-256
`6dd951a5b89040418841887a365d3e8e0a3e1fbb2634a7e084240fd10eea8e2b`.
It was application-verified on 2026-09-07. Direct XML comparison then
confirmed its complete nominal Seed A topology, installed ZMA assignments, response
scales, delays, polarity, smoothing, and minimum-phase settings. Each driver
had explicit horizontal `0/+20/+40/+60 degree` entries pointing to its verified
`polar/` FRDs, with horizontal-only `20 degree` steps and vertical inclusion
disabled. The current practical project retains those sources and settings and
changes only the documented component values, parasitics, aggregate resistor-
bank power fields, and description.

The user reported that the nominal predecessor opened without warnings and
that each driver showed the intended four responses. In its final user-supplied
screenshots, the normal-polarity branches crossed near `2.1 kHz` and summed
constructively; temporary tweeter inversion produced a deep cancellation near
that crossing, visually consistent with the independently predicted
approximately `25.1 dB` null. The normalised measured-angle plot shows the
expected progressive narrowing and no broad discontinuity that justifies
rejecting or finely re-optimising Seed A. The user confirmed that the tweeter
was restored to normal polarity. This remains application-rendered
corroboration of the unchanged source assignment and topology; it is not
verification of the new practical values or a filtered-system measurement.

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

**AS-BUILT COMPONENT AND COLD-ASSEMBLY PASS — 2026-09-08:** the practical
Seed A network uses the directly measured completed values below. Detailed
construction, instrument, calculation, and limitation records remain in
[Crossover component development](CROSSOVER_COMPONENT_DEVELOPMENT.md).

| Part | Practical measured value | Parasitic / construction |
|---|---:|---|
| C(W1) | `17.96 uF` | `0.04 ohm` ESR |
| L(W1) | `724 uH` | `0.292 ohm` DCR; 167 turns; 1.8 mm wire |
| L(W2) | `111 uH` | `0.172 ohm` DCR; 78 turns; 1.8 mm wire |
| C(T1) | `12.22 uF` | `0.04 ohm` ESR |
| L(T1) | `219 uH` | `0.193 ohm` DCR; 100 turns; 1.8 mm wire |
| C(T2) | `22.59 uF` | `0.04 ohm` ESR |
| R(Tser) | `1.401 ohm` | four selected 5R6 parts in parallel |
| R(Tpar) | `39.032 ohm` | three selected 13R parts in series |

All reactive values are within approximately `1%` of target. The AADE
inductance frequency is unknown, and the reported already-derived DCRs do not
retain their signed current/voltage pairs; neither limitation blocks the
reversible prototype. Cold topology checks passed, including the expected
`0.464 ohm` woofer-filter DCR contribution, DC-open tweeter path, correct
common return/shunt/L-pad relationships, verified driver and amplifier
polarities, and `5.929 ohm` complete input resistance. Powered-idle behaviour
and a first `0.10 V RMS`, `200-20000 Hz` audible commissioning sweep were
normal.

**MEASURED ACOUSTIC VALIDATION — PROPORTIONATE PASS (2026-09-08 TO
2026-09-09):** the raw retained authority is
[`rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat`](../rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat).
The detailed capture conditions, identities, intermediate diagnostics, and
derived comparisons are retained in
[Seed A commissioning history](rew/history/SEED_A_EXTERNAL_CROSSOVER_COMMISSIONING_2026-09-08_TO_09.md).

The current design consequences are:

- WF1 and TF1 place broad measured branch equality near `1.83 kHz`,
  approximately `13-14%` below the practical model's `2.116 kHz`, with
  essentially coincident relative phase.
- After exact voltage correction, SUM1 correlates `0.99566` with the measured
  WF1+TF1 vector sum; residual RMS is `20.62 dB` below the measured sum.
- REV1 correlates `0.99463` with WF1-TF1. At `1/12` octave, measured
  normal-to-reverse difference peaks at `25.31 dB` near `1.636 kHz` and is
  `15.82 dB` near `1.83 kHz`, passing the established physical polarity
  gate. The earlier `32.5/44.1 dB` separately smoothed branch-subtraction
  figures are qualitative only, not physical-null predictions.
- The approximately `5.3 dB` axial dip near `11 kHz` is already present in
  the protected-tweeter source and partly fills/moves off axis. It is an
  angle-dependent tweeter/waveguide/baffle or very-early local-diffraction
  feature, not a Seed A or woofer-summation fault, and does not justify EQ.
- The measured `0/+20/+40/+60 degree` full-system set has no broad crossover
  hole and only about `+1.36 dB` maximum off-axis excess. A moderate roughly
  `2.5-3.1 dB` beamwidth change across `1.5-2.5 kHz` remains a possible
  controlled-refinement target; above `3 kHz`, narrowing progresses coherently
  with angle.

The intermittent distorted `1 kHz` tone seen only with the undamped
tweeter-only load is closed/parked after clean resistor-dummy, damped real-
tweeter, and complete-system tests through the relevant bounded levels. A
real-tweeter-dependent amplifier/load interaction remains the leading inference,
but its exact mechanism and possible ultrasonic content were not proved. This
closed diagnostic is distinct from the pending controlled full-system
distortion/compression gate.

Together, the physical branch, sum, polarity, and horizontal evidence support
retaining Seed A unchanged as the reversible prototype. They do not freeze the
final crossover. The next gate is a qualified as-built system impedance-and-
phase measurement; higher-level distortion/compression and thermal validation
remain later gates. No unchanged acoustic sweep is presently justified.

### 2.5 Practical measured-component model

**DERIVED PRACTICAL MODEL / SIGNAL-FREE GATES PASSED:**
[`vituixcad/Prototype loudspeaker crossover Seed A practical measured 2026-09-08.vxp`](../vituixcad/Prototype%20loudspeaker%20crossover%20Seed%20A%20practical%20measured%202026-09-08.vxp)
retains the verified sparse-polar source assignments, topology, normal
polarity, and C2 scale multiplier `3.605786`, while replacing every Seed A
component with the completed measured value:

| Part | Practical model value |
|---|---:|
| L(W1) | `0.724 mH`, `0.292 ohm` DCR, `1.8 mm` wire |
| C(W1) | `17.96 uF`, `0.04 ohm` ESR |
| L(W2) | `0.111 mH`, `0.172 ohm` DCR, `1.8 mm` wire |
| C(T1) | `12.22 uF`, `0.04 ohm` ESR |
| L(T1) | `0.219 mH`, `0.193 ohm` DCR, `1.8 mm` wire |
| C(T2) | `22.59 uF`, `0.04 ohm` ESR |
| R(Tser) | `1.401 ohm`; aggregate bank power field `20 W` |
| R(Tpar) | `39.032 ohm`; aggregate bank power field `15 W` |

The initially generated practical file passed an XML parse covering both
drivers, all eight measured component entries, four
horizontal responses per driver, installed ZMA paths, and the unchanged
tweeter scale. Independent complex nodal replay against the retained longer-
window TW1/C2 design pair gives branch equality near `2.116 kHz`, relative
phase about `13.2 degrees`, normal-to-reverse difference about `18.6 dB`, and
minimum input impedance `3.805 ohm` near `2.792 kHz` at approximately
`-9.4 degrees`. These pass the bounded `2.05-2.25 kHz`, `20 degree`, `15 dB`,
and `3.5 ohm` gates.

Using the actual sparse-polar zero-degree files stored by the VXP gives native-
curve equality near `2.119 kHz`, relative phase about `3.74 degrees`, and
normal-to-reverse difference about `29.7 dB`; input impedance is unchanged.
The difference from the longer-window figures is the already documented
tweeter polar-window effect, not a hardware inconsistency. The user subsequently
reopened and saved the practical file after moving R(Tpar) solely to avoid a
schematic overlap, and explicitly identified the change as cosmetic. That
report is accepted without inspecting, comparing, hashing, backing up, or
restoring the saved file. The application reopen/save gate is therefore
complete without promoting the change into new electrical evidence.

**INTENTIONAL RETENTION BOUNDARY:** `vituixcad/` contains the verified measured
baseline, the committed verified nominal sparse-polar Seed A reference, and its practical
measured-component successor. Other superseded intermediate projects remain
recoverable from Git history; the longer-window on-axis cases can be
reconstructed from the measured baseline, documented components, and retained
FRD/ZMA sources. Current raw measurement authorities remain under `rew/`.

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

## 5. Validation state before freezing the crossover

1. **Passed:** current installed ZMA and phase-bearing FRD sources are identified in [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md).
2. **Passed:** the external network uses measured components and accessible development construction.
3. **Passed:** the practical model contains the as-built component values and parasitics.
4. **Passed:** individual filtered drivers, normal-polarity sum, physical reverse-polarity null, and the sparse positive-horizontal full-system set.
5. **Open:** measure as-built system impedance/phase and derive the applicable load classification/EPDR.
6. **Open:** controlled full-system distortion/compression and thermal validation at required listening levels.
7. Move the network inside only after the complete measured assembly is stable under the remaining gates; repeat one controlled design change at a time if refinement is justified.

## 6. Open crossover items

- whether the final-production crossover retains Seed A's measured frequency,
  topology, values, and normal acoustic polarity after the remaining gates;
- second-channel component matching and final inductor implementation;
- permanent inductor interlock, outer-layer binding, and PCB restraint;
- final system impedance classification and amplifier headroom;
- final crossover mounting position;
- whether DSP remains development-only or is used in the finished system.
