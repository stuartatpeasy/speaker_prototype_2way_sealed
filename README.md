# DIY Near-Wall Two-Way Loudspeaker

This is the compact project dashboard and documentation router for the sealed
passive two-way prototype. Read it first, then follow only the route relevant to
the task. Detailed procedures, evidence, and history are deliberately kept out
of this file.

## 1. Current Project State

**Lifecycle:** ACTIVE PROTOTYPE DEVELOPMENT

**Current phase:** the woofer-axis and common-position woofer sources are
retained and validated. Protected-tweeter C2 completed cleanly at the common
`20-20000 Hz` timing basis. Its `47,857.68` timing-reference index and
`3.00670 ms` System Delay confirm that C1's gross `79.860 ms` delay was a
bandwidth-dependent reference-index displacement, not physical movement. The
two raw tweeter impulses align within two samples and correlate at `0.99883`.
C2's saved source, native window, and FRD pass verification. No additional
on-axis sweep is justified. The common-position TW1/C2 source pair is complete
and validated for the first crossover model. REW's per-measurement loopback
calibration is normalised to `0 dB` at `1 kHz`, so C2 retains the protection
capacitor's `-11.14 dB` terminal/source ratio at that one reference frequency;
apply a derived `+11.14 dB` C2 magnitude scale during import without changing
its phase or delay. The first VituixCAD projects mistakenly stored the
equivalent linear ratio `3.605786` in the project file. That stored value is in
fact correct because VituixCAD serialises the UI's `+11.14 dB` acoustic scale as
a linear multiplier. The screenshots did expose a separate real error: the
intended `39 ohm` tweeter shunt had been placed in series. The retained
`verified` measured baseline preserves the source configuration, and the
retained `verified` sparse-polar Seed A project combines the correct stored
multiplier with the correct parallel topology. Earlier acoustic plots remain
superseded diagnostics.

The protected-tweeter `+20/+40/+60 degree` raw batch and its matched-window
FRDs have passed signal-free verification. The polar data indicate broad
tweeter coverage through the candidate crossover region and progressive
narrowing above it. The four files are preserved in their `polar/`
subdirectory and the separate `3.5 ms` C2 design FRD is restored exactly at
its original pathname.

The woofer `+20/+40/+60 degree` raw batch has also passed signal-free review.
Its common `3.5 ms` window excludes the first fixed room/jig arrival and is
stable enough for the crossover region. The sparse data show material woofer
narrowing through and above that region; all four polar exports pass native-
response verification. The broad cross-driver match is best around
`2.2-2.3 kHz`, supporting the existing design region over a higher handover.

A Seed A sparse-polar VituixCAD project contains explicit
horizontal `0/+20/+40/+60 degree` assignments for both drivers. Its crossover
network and all established source treatment are unchanged and structurally
verified. It is deliberately horizontal-only; the positive-side sparse data do
not establish full-space sound power or CTA-2034 directivity. The first project
opened and rendered without error, but the screenshots revealed the shunt-
connectivity error and then confirmed the VXP scale-serialisation convention.
The intended-topology impedance plot agrees with the independent approximately
`3.7 ohm` minimum and passes. The final user-supplied screenshots show the
normal-polarity branches crossing near `2.1 kHz` with constructive summation,
and the temporary inverted-tweeter plot shows the expected deep null near that
crossing. The measured positive-angle directivity plot is consistent with the
raw sparse evidence and exposes no broad reason to reject Seed A. The user
confirmed that the tweeter is restored to normal polarity. This passes the
bounded crossing, polarity, directivity, and load gates. A signal-free slope
audit records that the tweeter's measured acoustic
high-pass is reasonably close to the intended transition and has about
`24.4 dB` attenuation at `1 kHz` relative to its `8-10 kHz` output, but the
woofer falls only about `9.1 dB` from `2.1` to `4.2 kHz`, versus about
`18.6 dB` for an ideal LR4 branch over that octave. Generated unmeasured angles
remain excluded from the evidence.

A bounded Seed B search found no alternative that materially improves that
upper stopband without a worse system trade. The best constrained retuned
three-reactance ladder improved the `2.1-4.2 kHz` fall by only about `3.3 dB`
and the `5 kHz` branch separation by about `1.9 dB`, while worsening total-
response span, phase/null, and minimum impedance. Four-reactance searches made
the fourth capacitor negligible; a targeted notch overfit one narrow region.
Seed A is therefore restored as the proportionate first reversible prototype,
with its residual woofer output retained as an explicit measurement question.

**Next action:** the assembled Seed A capacitor banks pass at `17.96`, `12.22`,
and `22.59 uF`, each with reported `0.04 ohm` ESR. Available test coils provide
a credible route to all three inductors: trim the 1.2 mH/1.8 mm donor for
L(W1), wind a new approximately 73-turn 1.8 mm L(W2), and add about three turns
to the 207 uH/1.8 mm donor for L(T1), always stopping on measured inductance.
The DCR method passes and does not expose a model blocker. Measured resistor
selection gives R(Tser) `1.39149 ohm` from 5R6 E/F/I/J in parallel and R(Tpar)
exactly `39.000 ohm` from 13R B/D/E in series. Complete the three windings and
two resistor banks, measure final values, then update the practical model. No
additional raw-driver sweep is presently justified.

**Last reviewed:** 2026-09-08

| Subsystem | Current conclusion | Detailed authority |
| --- | --- | --- |
| Cabinet | One acoustically representative sealed prototype is complete. Body is approximately `280 x 430 x 300 mm`; geometric net volume is approximately `21.7 L` before damping. | [Cabinet design](doc/CABINET_DESIGN.md) |
| Drivers | SB17NRX2C35-8 woofer and SB26STWGC-4 tweeter remain provisionally retained. The original cooled installed ZMA files remain the crossover baselines; the woofer still needs a cooled post-conditioning confirmation. | [Driver analysis](doc/DRIVER_ANALYSIS.md) |
| Crossover | The two retained projects are the `verified` measured baseline and sparse-polar Seed A. Seed A's crossing, polarity, sparse directivity, and approximately `3.7 ohm` load checks pass. Its shallow woofer upper transition is recorded, but a bounded Seed B search found no dominant model alternative; Seed A is released for a reversible external prototype, not final acceptance. | [Crossover design](doc/CROSSOVER_DESIGN.md) |
| UMC22 measurement path | The common-position TW1/C2 sources remain validated. Both `+20/+40/+60 degree` archives and their matched-window polar exports are retained and verified. C2 and every protected-tweeter angle require the common `+11.14 dB` model-import scale. No additional raw-driver sweep is presently needed. | [Horizontal runbook](doc/rew/procedures/UMC22_INSTALLED_HORIZONTAL_OFF_AXIS_FRD.md), [tweeter runbook](doc/rew/procedures/UMC22_INSTALLED_TWEETER_FRD.md) |
| UMC202HD path | The passive fixture is released, but desktop output-stream dropouts suspend UMC202HD sweeps. Live Linux remains the next useful discriminator. | [Dropout diagnosis](doc/rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md) |
| Room | The design is explicitly near-wall/near-corner. Current placement alternatives remain measurement candidates rather than final decisions. | [Room summary](doc/ROOM_DETAILS.md) |

## 2. Project Goal And Locked Architecture

Design and build a pair of accurate, measurement-led passive loudspeakers with
neutral tonal balance, smooth on-axis and off-axis behaviour, low distortion,
and an amplifier-friendly measured load. Installed measurements take precedence
over nominal impedance, textbook crossover values, or unsupported audiophile
claims.

The first version is locked to:

- passive two-way operation;
- SB Acoustics SB17NRX2C35-8 woofer/midwoofer;
- SB Acoustics SB26STWGC-4 waveguide tweeter;
- sealed, near-wall enclosure;
- an external development crossover through a four-pole speakON connection;
- crossover design from phase-bearing measurements of the installed drivers.

Three-way, open-baffle, transmission-line, horn, and reflex alternatives are
outside this version. DSP may be used experimentally before the passive
crossover is finalised.

## 3. Task-Oriented Reading Routes

Read `AGENTS.md` as the standing collaboration policy. Then use the smallest
route below. Files labelled history or qualification are not routine context.

| Task | Read | Add only when needed |
| --- | --- | --- |
| Driver or enclosure alignment | [Driver analysis](doc/DRIVER_ANALYSIS.md) | [Run-in procedure](doc/DRIVER_RUNIN.md) for conditioning; [cabinet design](doc/CABINET_DESIGN.md) for mechanical consequences |
| Cabinet fabrication | [Cabinet design](doc/CABINET_DESIGN.md) | [3D-model hub](doc/3d_models/README.md) for model selection or reconstruction |
| Crossover modelling | [Driver analysis](doc/DRIVER_ANALYSIS.md), [crossover design](doc/CROSSOVER_DESIGN.md), [measurement workflow](doc/MEASUREMENT_WORKFLOW.md) | [Component development](doc/CROSSOVER_COMPONENT_DEVELOPMENT.md) only for component construction or thermal/mechanical questions |
| UMC22 woofer capture or repeatability investigation | [REW dispatcher](doc/rew/README.md), [UMC22 runbook](doc/rew/procedures/UMC22_INSTALLED_WOOFER_FRD.md) | [FRD method](doc/rew/FRD_MEASUREMENT_METHOD.md) when reviewing geometry, impulse/ETC, the production window, or capture comparisons; [driver analysis](doc/DRIVER_ANALYSIS.md) when assessing or promoting driver-design evidence; qualification only for audit or failure investigation |
| UMC22 protected tweeter capture | [REW dispatcher](doc/rew/README.md), [UMC22 tweeter runbook](doc/rew/procedures/UMC22_INSTALLED_TWEETER_FRD.md) | [FRD method](doc/rew/FRD_MEASUREMENT_METHOD.md) for common timing/window review; [driver analysis](doc/DRIVER_ANALYSIS.md) for the approved impedance and protection derivation |
| UMC22 horizontal off-axis driver series | [REW dispatcher](doc/rew/README.md), [horizontal off-axis runbook](doc/rew/procedures/UMC22_INSTALLED_HORIZONTAL_OFF_AXIS_FRD.md) | [FRD method](doc/rew/FRD_MEASUREMENT_METHOD.md) only when reviewing timing/window validity; completed on-axis runbooks only to audit a disputed electrical-route fact |
| Reconnect or operate the reference fixture | [Fixture use](doc/rew/fixtures/REFERENCE_FIXTURE_USE.md) and the applicable interface procedure | [Fixture specification](doc/rew/fixtures/REFERENCE_FIXTURE_SPECIFICATION.md) if rebuilding or redesigning |
| Audit UMC22 or fixture qualification | [REW dispatcher](doc/rew/README.md), then the named record under `doc/rew/qualification/` | Chronological records under `doc/rew/history/` only for superseded attempts or provenance questions |
| Diagnose or resume UMC202HD | [Dropout diagnosis](doc/rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md) | [Suspended UMC202HD procedure](doc/rew/procedures/UMC202HD_FRD_SUSPENDED.md) when preparing to resume |
| Room placement | [Room summary](doc/ROOM_DETAILS.md), [placement and measurement](doc/room/ROOM_PLACEMENT_AND_MEASUREMENT.md) | [Geometry and screening](doc/room/ROOM_GEOMETRY_AND_SCREENING.md) for CAD, coupled-space, or modal questions |
| REW API use | [REW API client](doc/REW_API_CLIENT.md) | Its qualification record only for maintenance or audit |
| 3D model selection or reconstruction | [3D-model hub](doc/3d_models/README.md), then one component README | [Local tooling](doc/LOCAL_TOOLING.md) if the environment or checkout path changes |
| Documentation review | [Documentation review procedure](doc/DOCUMENTATION_REVIEW.md) | Use its comprehensive mode only for consolidation or handover |
| Repository or generated-artifact maintenance | [AGENTS.md](AGENTS.md), [.gitignore](.gitignore), [local tooling](doc/LOCAL_TOOLING.md) | Relevant reconstruction authority only |

## 4. Documentation Map

| Area | Authority |
| --- | --- |
| Collaboration and retention policy | [AGENTS.md](AGENTS.md), [.gitignore](.gitignore) |
| Documentation review | [doc/DOCUMENTATION_REVIEW.md](doc/DOCUMENTATION_REVIEW.md) |
| Driver evidence and conditioning | [doc/DRIVER_ANALYSIS.md](doc/DRIVER_ANALYSIS.md), [doc/DRIVER_RUNIN.md](doc/DRIVER_RUNIN.md) |
| Cabinet and crossover | [doc/CABINET_DESIGN.md](doc/CABINET_DESIGN.md), [doc/CROSSOVER_DESIGN.md](doc/CROSSOVER_DESIGN.md), [doc/CROSSOVER_COMPONENT_DEVELOPMENT.md](doc/CROSSOVER_COMPONENT_DEVELOPMENT.md) |
| Measurement policy and tooling | [doc/MEASUREMENT_WORKFLOW.md](doc/MEASUREMENT_WORKFLOW.md), [doc/REW_API_CLIENT.md](doc/REW_API_CLIENT.md) |
| REW procedures, qualification, and history | [doc/rew/README.md](doc/rew/README.md) |
| Room geometry and placement | [doc/ROOM_DETAILS.md](doc/ROOM_DETAILS.md) |
| 3D-model documentation | [doc/3d_models/README.md](doc/3d_models/README.md) |
| Local environments and checkout paths | [doc/LOCAL_TOOLING.md](doc/LOCAL_TOOLING.md) |

All tracked project Markdown except this file and `AGENTS.md` lives under
`doc/`. Subtree dispatchers index detailed component, qualification, and history
records without forcing them into normal orientation context.

## 5. Immediate Development Sequence

1. Preserve validated tweeter C2, both woofer sources, both verified sparse-
   polar families, and the two retained VituixCAD authorities: the `verified`
   measured baseline and sparse-polar Seed A project.
2. Complete woofer stabilisation and obtain a cooled reproducible `48 kHz` ZMA.
3. Retain the acquired installed-baffle common-timing and horizontal off-axis
   data; add controlled distortion measurements only when needed to validate a
   viable crossover candidate.
4. Map Seed A onto measured practical components and realistic parasitics;
   retain its residual woofer upper output as an explicit prototype-measurement
   question rather than creating an unsupported Seed B.
5. Build and measure the external development crossover; verify filtered
   responses, normal sum, reverse-polarity null, directivity, distortion,
   impedance/EPDR, and thermal behaviour.
6. Iterate one controlled change at a time and update the owning current record.

## 6. Open Decisions

- final damping quantity and distribution;
- final cooled woofer impedance baseline and whether further conditioning helps;
- exact crossover frequency, topology, acoustic polarity, and component values;
- final inductor implementation, restraint, and crossover mounting position;
- final system impedance classification and amplifier headroom;
- final veneer and finish;
- final room placement among the documented reversible trials;
- whether DSP or a future subwoofer forms part of the finished system;
- production-driver spread and stereo-pair matching after the prototype passes
  its acoustic and load gates.

## 7. One-Line Design Summary

The accepted prototype is a sealed, near-wall, measurement-designed passive
two-way loudspeaker using an SB17NRX2C35-8 woofer and SB26STWGC-4 waveguide
tweeter in an approximately `21.7 L` geometric-net plywood cabinet, with an
externally accessible development crossover and neutral low-distortion
reproduction as the overriding goal.
