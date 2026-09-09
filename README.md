# DIY Near-Wall Two-Way Loudspeaker

This is the compact project dashboard and documentation router for the sealed
passive two-way prototype. Read it first, then follow only the route relevant to
the task. Detailed procedures, evidence, and history are deliberately kept out
of this file.

## 1. Current Project State

**Lifecycle:** ACTIVE PROTOTYPE DEVELOPMENT

**Current phase:** the installed woofer/tweeter axis sources and both positive-
horizontal raw-driver families are retained and validated. Their common timing,
windowing, `+11.14 dB` protected-tweeter import correction, source assignments,
and provenance are owned by [Driver analysis](doc/DRIVER_ANALYSIS.md). The
bounded Seed B audit found no dominant alternative, so Seed A was built as the
first reversible external prototype. Detailed superseded corrections and
capture chronology remain outside this dashboard.

**Current crossover result — 2026-09-09:** the measured Seed A component set
and completed external network pass. The practical measured-component project
retains the verified sparse-polar sources and predicts branch equality near
`2.116 kHz`, approximately `13.2 degrees` relative phase, `18.6 dB`
normal-to-reverse difference, and minimum impedance about `3.805 ohm`. The
user's later R(Tpar) movement is accepted as cosmetic; neither retained VXP
requires inspection or rewriting.

The retained Seed A acoustic series is preserved in
[`rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat`](rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat);
detailed conditions and chronology are indexed through the
[REW dispatcher](doc/rew/README.md). WF1 and TF1 place broad measured branch
equality near `1.83 kHz` with essentially coincident phase. SUM1 correlates
`0.99566` with their measured vector sum. REV1 passes the physical polarity
gate: at `1/12` octave, normal-to-reverse difference peaks at `25.31 dB` and
is `15.82 dB` near `1.83 kHz`. Normal tweeter polarity was restored.

The measured `0/+20/+40/+60 degree` full-system set has no broad crossover
hole and only about `+1.36 dB` maximum off-axis excess. A real but moderate
roughly `2.5-3.1 dB` beamwidth change across `1.5-2.5 kHz` remains a possible
later refinement, not grounds for an immediate component change. The narrow
approximately `5.3 dB` on-axis feature near `11 kHz` predates Seed A and
partly fills off axis; it does not justify equalisation. The intermittent
distortion seen only with the undamped tweeter-only load is closed/parked after
clean dummy-load, damped-load, and complete-system tests. Its exact mechanism
and possible ultrasonic content remain unproved; controlled full-system
distortion/compression validation is still a separate future gate.

**Next action:** establish the qualified route and perform an as-built
full-system impedance-and-phase measurement before higher-level distortion or
thermal testing. No further unchanged on-axis, reverse-polarity, or positive-
horizontal acoustic sweep is presently required. Preserve current user work and
do not repeat unchanged hardware-state checks merely because the conversation
advances.

**Last reviewed:** 2026-09-09

| Subsystem | Current conclusion | Detailed authority |
| --- | --- | --- |
| Cabinet | One acoustically representative sealed prototype is complete. Body is approximately `280 x 430 x 300 mm`; geometric net volume is approximately `21.7 L` before damping. | [Cabinet design](doc/CABINET_DESIGN.md) |
| Drivers | SB17NRX2C35-8 woofer and SB26STWGC-4 tweeter remain provisionally retained. The original cooled installed ZMA files remain the crossover baselines; the woofer still needs a cooled post-conditioning confirmation. | [Driver analysis](doc/DRIVER_ANALYSIS.md) |
| Crossover | The retained projects are the verified measured baseline, the committed verified nominal sparse-polar Seed A reference, and its practical measured-component successor. WF1 and TF1 cross broadly near `1.83 kHz` with essentially coincident phase; SUM1 confirms normal-polarity summation with `0.99566` raw-impulse correlation to their vector sum. Matched-window REV1 passes the physical-null gate. The complete `0/+20/+40/+60 degree` physical set has no broad crossover hole and only about `+1.36 dB` maximum off-axis excess, but retains a moderate beamwidth flare across `1.5-2.5 kHz`. Seed A remains the reversible prototype; as-built impedance/phase is the next gate. | [Crossover design](doc/CROSSOVER_DESIGN.md) |
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
| Seed A as-built impedance/phase planning | [Driver analysis](doc/DRIVER_ANALYSIS.md), [crossover design](doc/CROSSOVER_DESIGN.md), [measurement workflow](doc/MEASUREMENT_WORKFLOW.md) | [Fixture use](doc/rew/fixtures/REFERENCE_FIXTURE_USE.md) only after a specific qualified route and parameters are defined; Seed A commissioning history only to audit completed acoustic evidence |
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

1. Preserve the completed raw-driver, Seed A acoustic, and three VituixCAD
   authorities; do not repeat passed acoustic measurements without a
   design-relevant reason.
2. Define and qualify the as-built complete-system impedance/phase route without
   deriving a live procedure from old qualification history.
3. Measure Seed A impedance and phase, then calculate the applicable minimum-
   load and EPDR consequence.
4. If the load passes, perform proportionate full-system
   distortion/compression and thermal validation at the required listening
   level.
5. Keep a cooled reproducible `48 kHz` woofer ZMA, final damping, and the
   moderate crossover-region directivity flare as lower-priority refinement
   questions unless the remaining gates make one decisive.
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
