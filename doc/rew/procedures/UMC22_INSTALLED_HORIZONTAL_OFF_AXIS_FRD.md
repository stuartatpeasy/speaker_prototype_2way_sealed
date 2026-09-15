# UMC22 Installed Horizontal Off-Axis FRD Runbook

> - **Lifecycle:** COMPLETED PROCEDURE / RETAINED EVIDENCE
> - **Owns:** the first positive-horizontal raw-driver rotation series, angle convention, batch limits, topology-change gates, naming, retention, and stop rules
> - **Does not own:** on-axis source qualification, full polar/CTA-2034 coverage, vertical directivity, distortion testing, filtered-system validation, or final crossover choice
> - **Current approved action:** none; preserve both verified sparse raw-driver families and use this runbook only for audit or a deliberately repeated route after material change
> - **Next gate:** matched speaker-two build and validation under [Crossover design](../../CROSSOVER_DESIGN.md); this document releases no signal
> - **Limitations:** one positive horizontal side at `20 degree` spacing; horizontal symmetry remains an inference; woofer polar conclusions are provisionally limited to `1.5-5 kHz` and protected-tweeter polar conclusions to `1.5-12 kHz`; no signal is released by this document alone
> - **Last reviewed:** 2026-09-15

This procedure is the bounded directivity discriminator required by
[Crossover design](../../CROSSOVER_DESIGN.md). It reuses the qualified UMC22
woofer and protected-tweeter electrical routes without reopening their
completed on-axis investigations. The interface-neutral timing, window, and
retention rules remain in [FRD measurement method](../FRD_MEASUREMENT_METHOD.md).

The imperative sections below preserve the route used for the dated captures.
They are not a current instruction to reconnect or repeat hardware.

## 1. Purpose And Proportionate Scope

The existing common-position TW1/C2 pair is sufficient for a first on-axis
crossover model, but not for choosing whether approximately `2.1`, `2.3`, or
`2.4 kHz` gives the best horizontal directivity match. The smallest useful next
set is therefore three additional positive-horizontal angles for each raw
driver:

```text
existing retained source: 0 degrees
new measurements:        +20, +40, +60 degrees
```

This adds six sweeps in two electrically homogeneous batches. It is not a full
polar set and must not be presented as complete CTA-2034 evidence. Ten-degree
fill angles, the negative side, vertical angles, distortion, and filtered
system measurements are deferred unless the sparse set exposes a
design-relevant ambiguity.

## 2. Verified Rotation Geometry And Angle Convention

**USER-CONFIRMED CONFIGURATION — 2026-09-06:** at `0 degrees`, the front face
of the baffle lies directly over the jig's vertical centre of rotation and the
baffle is centred horizontally over it. The rotation axis therefore runs up
the front baffle plane halfway between the cabinet's left and right edges. The
woofer and tweeter are vertically aligned on this horizontal centreline. The
jig is marked in `10 degree` increments.

Viewed from above, positive angle means rotating the cabinet
**anti-clockwise** from its `0 degree` position. The microphone remains fixed at
the tweeter-centre height and at the established `1.000 m` distance from the
baffle-plane pivot point. Do not swing the microphone with the cabinet, slide
the jig, or re-aim the microphone at the rotated tweeter.

Because the pivot is in the baffle plane on the driver centreline, the nominal
measurement radius does not require a cabinet-translation correction as angle
changes. Each driver's real acoustic-centre depth and directional phase remain
part of the measured response and must not be independently aligned away.

## 3. Common REW Settings And Evidence Boundary

Both batches retain the completed on-axis settings:

| Field | Required value |
| --- | --- |
| REW / driver mode | V5.40 beta 133 / Java `Stereo only` |
| Endpoints | exact exclusive UMC22 input and output |
| Sample rate | `48 kHz` |
| Measurement/reference routing | `L/L/L/R` |
| Timing and calibration | loopback as calibration and timing reference; make calibration data from loopback response |
| Loopback merge / timing offset | off / `0.0000 ms` |
| Microphone calibration | `ECM8000_calibration_data.csv` on microphone input L only |
| Range / level / length / repetitions | `20-20000 Hz` / `-20 dBFS` / `256k` / `1` |
| Clipping abort | enabled |
| Generator and other application audio | stopped except during each explicitly released Measure action |

Do not use Check Levels or a separate level tone. Existing on-axis voltage,
headroom, and route qualification remain sufficient while the applicable
electrical topology and controls are unchanged.

Record the minimum displayed headroom for each batch and any run-specific REW
warning or physical anomaly. Exact timing, SNR, impulse, window, and metadata
will be recovered from the retained `.mdat`; do not create six rounds of manual
transcription merely because the information is visible in REW.

## 4. Woofer Batch

The woofer alone is connected to the amplifier through NL4 `1+`/`1-`, without
the tweeter protection capacitor. The qualified clamp/attenuator samples
directly across the woofer and feeds UMC22 `INST 2`; ECM8000 remains on Input 1.

Use these exact titles:

```text
SB17-IW-020deg-tweeter-axis-1m-U22-260907-P1
SB17-IW-040deg-tweeter-axis-1m-U22-260907-P1
SB17-IW-060deg-tweeter-axis-1m-U22-260907-P1
```

**COMPLETED BATCH BASIS — 2026-09-07:** the user reported the protection
capacitor and tweeter out of circuit, woofer connected, U1282A voltage monitor
and qualified clamp/attenuator both across the measurement plane, `5.73 ohm`
measured there with the separate U1272A before power-up, no wiring or strain
problem, cabinet secured at `0 degrees`, amplifier powered, and silent normal
operation. The GET-only REW audit passed the exact UMC22 route, `48 kHz`,
L/L/L/R loopback timing/calibration, microphone-L calibration, sweep, clipping-
abort, and Generator-stopped requirements. Its only stale field is the prior
tweeter title, which must be replaced before each woofer sweep. Confirm the
fixed U1282A was in a high-impedance voltage mode, not resistance or current
mode, before Measure.

Once the current-state report and GET-only audit pass, the three measurements
may run consecutively. Start at `0 degrees` with Generator stopped, rotate to
`+20 degrees`, secure the jig, run the named sweep, stop, then repeat at `+40`
and `+60 degrees`. Between sweeps check only the angle mark, cabinet security,
unchanged microphone/jig position, silence, and absence of an anomaly. Do not
repeat the settings recital.

After the third sweep, stop all application audio and retain exactly the three
new measurements as:

```text
rew/SB17NRX2C35-8_installed_positive_horizontal_020-060deg_tweeter-axis_1m_UMC22_2026-09-07.mdat
```

Do not add TW1 or API-loaded duplicates to this archive.

**USER-REPORTED CAPTURE RESULT / RETAINED EVIDENCE:** all three sweeps
completed with the displayed headroom remaining in REW's green region. The
exact minimum was not recorded. No repeat is justified: clipping-abort was
enabled, no warning or anomaly was reported, and an exact green headroom value
would not change the acceptance or crossover decision. The retained archive is
`7,266,225` bytes with SHA-256
`47a09014fa84d7ee0aca371ba422f2283c5eb3a089982e77baec44d51163bfab`.
Signal-free byte-string inspection finds each of the three required titles
once. Formal REW load/readback of that archive is deferred while the live
measurements remain available, because loading it would create duplicate
measurements in the working REW session.

## 5. Protected-Tweeter Batch

Changing from woofer to tweeter is a real electrical-topology change. With
Generator stopped, reduce amplifier volume fully, switch the amplifier off,
disconnect the woofer feed, and reinstate the previously verified measured
`10.13 uF`, `0.08 ohm` series protection capacitor in the tweeter-positive
path. Connect the clamp/attenuator directly across the tweeter after the
capacitor through NL4 `2+`/`2-`. Before power-up, repeat only the short checks
that caught the earlier wiring error:

- resistance directly across the tweeter/reference plane remains plausible;
- resistance across the amplifier-side feed rises towards open circuit as the
  series capacitor charges;
- no near-zero-resistance short, capacitor bypass, exposed conductor, loose
  connection, or strain problem is present.

Report the completed topology and readings before energising. A second
GET-only REW audit is required after power-up with all signals stopped; this is
one audit for the whole tweeter batch, not one per angle.

**CURRENT BATCH RELEASE — 2026-09-06:** user report confirms the SU-V570 and
UMC22 powered, protected tweeter connected at the retained `1.000 m` geometry,
series capacitor in circuit, cabinet secured at `0 degrees`, microphone fixed,
all application audio stopped, and the system silent and normal. The GET-only
REW audit passed the route, calibration, timing, sweep, clipping-abort, and
Generator-stopped requirements. The Measure title still names the preceding
on-axis capture and must be replaced with the applicable title below before
each sweep.

Use these exact titles:

```text
SB26-IW-020deg-tweeter-axis-1m-U22-260906-P1
SB26-IW-040deg-tweeter-axis-1m-U22-260906-P1
SB26-IW-060deg-tweeter-axis-1m-U22-260906-P1
```

Run the three angles under the same rotation and between-sweep checks as the
woofer batch. After `+60 degrees`, stop all application audio and retain
exactly the three new measurements as:

```text
rew/SB26STWGC-4_installed_positive_horizontal_020-060deg_tweeter-axis_1m_UMC22_2026-09-06.mdat
```

**VERIFIED CAPTURE AND RETENTION — PASS (2026-09-06):** the user completed the
three-angle batch and reported `19.1 dB` as the minimum headroom across all
three runs. The saved archive is `7,266,429` bytes with SHA-256
`61a9c66b1edef2199f9b267a0172bba5933ecb21f26ee8c22bcf12cdf9a053d7`.
REW loaded exactly the three correctly titled measurements from it, with
distinct UUIDs and no extraction warnings. A post-batch GET-only snapshot
found the Generator stopped, REW non-blocking, and no warning or error newer
than the previously documented discarded on-axis attempts.

The protection capacitor remains a measurement safeguard, not a listening
crossover. Its post-capacitor reference removes frequency-dependent transfer,
while REW's `1 kHz` loopback-calibration normalisation leaves the documented
constant C2-family magnitude offset. Apply the same derived `+11.14 dB` scale
to every protected-tweeter polar response during modelling.

## 6. Review, Windowing, Export, And Stop Rules

Do not export FRDs before the saved batch has passed signal-free review. For
each angle, verify the stable title/identity, native unsmoothed grid, common
timing mode, System Delay, direct arrival, first material reflection, and
stored window. Do not align the driver peaks or apply an IR shift.

**PROTECTED-TWEETER SIGNAL-FREE REVIEW — PASS / POLAR WINDOW ESTABLISHED
(2026-09-06):** the `+20/+40/+60 degree` UUIDs are respectively
`7c673a7d-1e5c-42fa-9c1c-3786a8d0d2eb`,
`3ebfc5ee-445d-492c-a51b-6f68d776e2fa`, and
`8c55d7cb-bc87-4d5b-baed-93fda8e6e251`. All are native unsmoothed `48 kHz`
responses with loopback-cal timing, zero timing offset, no IR shift or clock
adjustment, and System Delays `3.0170751`, `3.0079346`, and `2.9545955 ms`.
The `62.48 us` span is retained rather than aligned away; angular waveform
change can move the dominant impulse peak as the high-frequency direct sound
falls.

The direct-envelope peaks fall approximately `1.15`, `5.39`, and `10.66 dB`
relative to retained on-axis C2. In contrast, the first separated secondary
energy at approximately `+1.56/+1.73/+1.79 ms` remains near `-29 dB` relative
to the on-axis direct peak, and the approximately `+3.33 ms` arrival likewise
remains near `-21 dB`. Its near-constant absolute level while the direct sound
falls identifies fixed room/jig energy rather than tweeter directivity.

Use one common polar-only window for retained C2 and all three new angles:

```text
left:   Hann, 2.0 ms
right:  Tukey 0.25, 1.5 ms
ref:    each measurement's own exact direct-peak time
FDW:    off
MTW:    off
```

An API sensitivity check on disposable loaded copies showed that reducing the
right window from `1.5` to `1.25 ms` changed `1.5-12 kHz` magnitude by only
`0.16-0.23 dB RMS` (`0.47-0.77 dB` maximum) across `0/+20/+40/+60 degrees`.
This is adequate convergence for the crossover-directivity discriminator.
The longer on-axis `3.5 ms` source remains the phase-bearing design baseline;
do not overwrite it. The matched `1.5 ms` family is a separate polar dataset,
provisionally usable over `1.5-12 kHz`.

**REW ANALYSIS STATE:** the window above was applied through the API and read
back successfully on every live copy of the four stable tweeter UUIDs. This
changed only the open REW workspace; no retained `.mdat` was overwritten. The
polar files are now verified, and both live C2 copies have been restored to
their `3.5 ms` design window. Do not save API-loaded duplicate measurements
into a source archive.

Export native unsmoothed protected-tweeter `1.5-12 kHz` polar files, including
a matched-window copy of retained on-axis C2, under a separate `polar/`
subdirectory so the existing `3.5 ms` design FRD remains untouched:

```text
rew/frd/SB26STWGC-4/polar/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd
rew/frd/SB26STWGC-4/polar/020deg_tweeter-axis_1m_UMC22_2026-09-06.frd
rew/frd/SB26STWGC-4/polar/040deg_tweeter-axis_1m_UMC22_2026-09-06.frd
rew/frd/SB26STWGC-4/polar/060deg_tweeter-axis_1m_UMC22_2026-09-06.frd
```

**WOOFER SIGNAL-FREE REVIEW — PASS / POLAR WINDOW ESTABLISHED
(2026-09-07):** live UUID selection found exactly one copy of TW1 and each new
angle. The new `+20/+40/+60 degree` UUIDs are respectively
`f486fa1c-6c96-415d-a83f-ace36baacfba`,
`b39a77b4-e206-43ef-b595-e544ac62d53c`, and
`c173e83a-b591-4cbc-97c9-9052423c392b`. All are native unsmoothed `48 kHz`
responses with loopback-cal timing, zero timing offset, no IR shift, inversion,
or clock adjustment, and System Delays `3.1617166`, `3.0571430`, and
`3.0053459 ms`. Their API SNR fields are `38.96`, `33.07`, and `31.21 dB`;
the decline with angle accompanies the woofer's falling high-frequency direct
sound and is not an application warning.

Relative to retained on-axis TW1, the direct-envelope peaks fall approximately
`4.69`, `13.30`, and `17.71 dB`. Secondary energy near `+3.56` to `+3.71 ms`
instead remains at approximately `-23.5`, `-24.0`, and `-24.0 dB` on the same
absolute scale, compared with about `-23.0 dB` on axis. Its nearly fixed
absolute level while the direct peak falls identifies room/jig energy rather
than woofer radiation. The established `3.5 ms` right window excludes that
arrival and begins tapering before it.

Use one common woofer polar window for retained TW1 and the three new angles:

```text
left:   Hann, 2.0 ms
right:  Tukey 0.25, 3.5 ms
ref:    each measurement's own exact direct-peak time
FDW:    off
MTW:    off
```

A REW-native sensitivity check compared this choice with `3.0`, `2.5`, `2.0`,
and `1.5 ms` right windows. Changing only from `3.5` to `3.0 ms` changed the
derived angle-to-on-axis response over `1.8-2.6 kHz` by `0.13 dB RMS` at
`+20 degrees`, `0.53 dB` at `+40 degrees`, and `0.50 dB` at `+60 degrees`
(`0.25`, `0.82`, and `0.90 dB` maxima). Shorter windows produced progressively
larger changes without clearer convergence. The `+40 degree` local feature
near `2.2 kHz` consequently carries approximately `0.8 dB` analysis-window
uncertainty and must not be over-interpreted.

At the selected window, approximate angle-to-TW1 magnitude changes at
`1.5/2.0/2.2/2.4/3.0/4.0/5.0 kHz` are respectively
`+0.20/-1.14/-0.38/-0.94/-1.63/-2.27/-3.28 dB` at `+20 degrees`,
`+0.08/-3.49/+1.45/-1.80/-4.20/-8.11/-12.09 dB` at `+40 degrees`, and
`-3.26/-5.96/-0.63/-4.39/-9.75/-17.76/-15.98 dB` at `+60 degrees`.
These are **DERIVED** native-grid comparisons, not independently measured
absolute levels. Deep upper-band nulls at large angles become increasingly
room/noise sensitive. Use `1.5-5 kHz` for the present woofer directivity and
crossover decision; retaining export rows outside that interpretive range is
harmless.

**REW ANALYSIS STATE:** the woofer window above was applied through the API
and read back successfully on the one live copy of each stable UUID, including
TW1 UUID `12568bef-2ec1-4cc7-be3a-91460b0659fa`. This changed only the open
REW workspace; no retained `.mdat` or FRD was overwritten. A post-batch
GET-only snapshot found Generator playback off, REW non-blocking, and no
warning or error newer than the previously documented discarded attempts.

Export native unsmoothed `500 Hz-12 kHz` woofer files under the separate
`polar/` subdirectory. The wider retained row range preserves data; apply the
`1.5-5 kHz` interpretation limit during modelling:

```text
rew/frd/SB17NRX2C35-8/polar/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd
rew/frd/SB17NRX2C35-8/polar/020deg_tweeter-axis_1m_UMC22_2026-09-07.frd
rew/frd/SB17NRX2C35-8/polar/040deg_tweeter-axis_1m_UMC22_2026-09-07.frd
rew/frd/SB17NRX2C35-8/polar/060deg_tweeter-axis_1m_UMC22_2026-09-07.frd
```

Do not overwrite TW1's root `3.5 ms` design FRD. The polar on-axis file uses
the same window but remains a separately named family member so that all
directivity inputs can be selected without ambiguity.

**VERIFIED WOOFER POLAR EXPORTS — PASS (2026-09-07):** all four files identify
the correct SB17 measurement, contain `31,404` finite native unsmoothed rows
over `499.877960-12000.000966 Hz`, and match the corresponding UUID-selected
live REW response within `0.000009 Hz`, `0.000530 dB`, and `0.001724 degree`
circular phase. Their retained sizes and SHA-256 hashes are:

| Angle | Bytes | SHA-256 |
| ---: | ---: | --- |
| `0 degrees` | `913,085` | `03923152b08c36e066cb0f9520c7a76489bf6837e3b85cd06c67af0c12a8e4b7` |
| `+20 degrees` | `911,885` | `f418f7a50449bead7b97c4c89a52ffc938fb199bf4f0d0efc09171e638b03453` |
| `+40 degrees` | `911,941` | `c7c902610f35623e32355b4c4b1a78390f9a6f3266dd61d0fe84336e84e1ea6a` |
| `+60 degrees` | `912,085` | `c34213923124963ba5dad703729ab84c61f4e84d23e0d33c0c3778d0663b63a1` |

The first attempt selected the already verified SB26 off-axis traces for the
three new filenames; those non-unique copies were replaced by the correct SB17
exports. No source, design FRD, measurement, or unique evidence was lost.

**VERIFIED EXPORT CONTENT / OPEN FILING CORRECTION (2026-09-06):** the user
exported the four measurements carrying the `1.5 ms` right window. Each file
has `31,404` finite native unsmoothed rows over
`499.877960-12000.000966 Hz`; comparison with the corresponding live REW
response differs by at most `0.000009 Hz`, `0.000514 dB`, and `0.00194 degree`
circular phase. Retaining rows below the provisional `1.5 kHz` polar limit is
harmless and does not justify another export; model interpretation must still
exclude that lower-confidence range.

The files were written to `rew/frd/SB26STWGC-4/` rather than its `polar/`
subdirectory. The new matched-window `000deg` file consequently displaced the
pathname of C2's previously verified `3.5 ms` design FRD. No unique evidence
was lost: the new `1.5 ms` file is verified and C2's retained `.mdat` remains
the reconstruction authority for the original design FRD. Preserve both
variants, file all four polar responses under `polar/`, and restore the
`3.5 ms` design export at its existing root pathname before reopening or
saving a model which consumes that pathname. Do not move, overwrite, or
re-export either variant until that corrective action is explicitly approved.

**RESOLVED FILING STATE:** the four verified `1.5 ms` polar files are correctly
preserved under `rew/frd/SB26STWGC-4/polar/`. The root C2 design FRD has been
restored exactly: it identifies C2, is `912,077` bytes, and its SHA-256
`a409445a40e645682b188b7a12596c10f727d8a0f78138f052c043d60bb0ea1e`
matches the previously verified `3.5 ms` export. No further tweeter export or
measurement is required.

Stop the active sweep and de-energise safely for clipping, REW warning,
dropout, abnormal sound, rubbing, instability, heat, smell, smoke, spark,
cabinet/jig movement, a disturbed microphone, loose cable, or any other
anomaly. Preserve a failed capture as diagnostic evidence rather than deleting
or editing it into apparent validity. One failed angle stops the remaining
batch pending review; it does not invalidate already completed angles.
