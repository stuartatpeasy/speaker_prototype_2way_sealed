# DIY Near-Wall Two-Way Loudspeaker

This is the compact project dashboard and documentation router for the sealed
passive two-way prototype. Read it first, then follow only the route relevant to
the task. Detailed procedures, evidence, and history are deliberately kept out
of this file.

## 1. Current Project State

**Lifecycle:** ACTIVE PROTOTYPE DEVELOPMENT

**Current phase:** Seed A is the accepted reversible external prototype. Its
installed raw-driver sources, measured component set, filtered branches,
normal sum, reverse-polarity null, sparse horizontal responses, as-built load,
and bounded level/distortion and exposed-component thermal gates pass. The
[driver](doc/DRIVER_ANALYSIS.md), [crossover](doc/CROSSOVER_DESIGN.md), and
[REW](doc/rew/README.md) authorities own the numerical evidence and provenance.

The moderate crossover-region beamwidth change remains a possible later
refinement, not grounds for a component change. The narrow high-level feature
near `2.18 kHz` needs matched-unit confirmation. The attempted immediate hot
comparison is excluded because the speaker was at `60 degrees`, and its
replacement is deferred rather than passed.

**Next action:** inventory/procure the second crossover's parts, build speaker
two to the same physical and electrical design, and repeat the decisive
installed, crossover, load, level/distortion, and bounded thermal checks under
matched conditions. Include a correct immediate hot `0-degree` comparison and
check whether the `2.18 kHz` feature repeats. Retest speaker one only if that
work reveals an anomaly; no unchanged measurement on it is justified now.

**Last reviewed:** 2026-09-15

| Subsystem | Current conclusion | Detailed authority |
| --- | --- | --- |
| Cabinet | One acoustically representative sealed prototype is complete. Body is approximately `280 x 430 x 300 mm`; geometric net volume is approximately `21.7 L` before damping. | [Cabinet design](doc/CABINET_DESIGN.md) |
| Drivers | SB17NRX2C35-8 woofer and SB26STWGC-4 tweeter remain provisionally retained. The original cooled installed ZMA files remain the crossover baselines; the woofer still needs a cooled post-conditioning confirmation. | [Driver analysis](doc/DRIVER_ANALYSIS.md) |
| Crossover | Measured Seed A component, acoustic, load, level/distortion, and exposed-component thermal gates pass. The moderate directivity flare and narrow `2.18 kHz` high-level feature remain second-speaker checks. | [Crossover design](doc/CROSSOVER_DESIGN.md) |
| StarTech impedance path | The `5 V` USB-powered route and completed Seed A capture pass; no unchanged repeat is justified. | [Completed StarTech procedure](doc/rew/procedures/STARTECH_SEED_A_SYSTEM_IMPEDANCE.md) |
| UMC22 measurement path | Common-position on-axis and `+20/+40/+60 degree` raw-driver sources are validated. Protected-tweeter imports require the documented `+11.14 dB` scale. | [Horizontal runbook](doc/rew/procedures/UMC22_INSTALLED_HORIZONTAL_OFF_AXIS_FRD.md), [tweeter runbook](doc/rew/procedures/UMC22_INSTALLED_TWEETER_FRD.md) |
| Seed A level/thermal path | The bounded package passes; its wrong-angle post-thermal trace is excluded and the correct hot comparison is deferred to speaker two. | [Qualification record](doc/rew/qualification/SEED_A_FULL_SYSTEM_LEVEL_AND_THERMAL_QUALIFICATION_2026-09-10.md) |
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
| Seed A as-built impedance/phase planning or operation | [StarTech Seed A impedance procedure](doc/rew/procedures/STARTECH_SEED_A_SYSTEM_IMPEDANCE.md), [crossover design](doc/CROSSOVER_DESIGN.md) | [Driver analysis](doc/DRIVER_ANALYSIS.md) for baseline comparison; Seed A commissioning history only to audit completed acoustic evidence |
| Review or deliberately repeat Seed A full-system level/thermal validation | [Seed A level/thermal qualification](doc/rew/qualification/SEED_A_FULL_SYSTEM_LEVEL_AND_THERMAL_QUALIFICATION_2026-09-10.md), [crossover design](doc/CROSSOVER_DESIGN.md) | [Completed procedure](doc/rew/procedures/UMC22_SEED_A_LEVEL_AND_THERMAL.md) only for a deliberate repeat; [fixture use](doc/rew/fixtures/REFERENCE_FIXTURE_USE.md) only after reconnection or a changed route |
| Reconnect or operate the reference fixture | [Fixture use](doc/rew/fixtures/REFERENCE_FIXTURE_USE.md) and the applicable interface procedure | [Fixture specification](doc/rew/fixtures/REFERENCE_FIXTURE_SPECIFICATION.md) if rebuilding or redesigning |
| Audit UMC22 or fixture qualification | [REW dispatcher](doc/rew/README.md), then the named record under `doc/rew/qualification/` | Chronological records under `doc/rew/history/` only for superseded attempts or provenance questions |
| Diagnose or resume UMC202HD | [Dropout diagnosis](doc/rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md) | [Suspended UMC202HD procedure](doc/rew/procedures/UMC202HD_FRD_SUSPENDED.md) when preparing to resume |
| Room placement | [Room summary](doc/ROOM_DETAILS.md), [placement and measurement](doc/room/ROOM_PLACEMENT_AND_MEASUREMENT.md) | [Geometry and screening](doc/room/ROOM_GEOMETRY_AND_SCREENING.md) for CAD, coupled-space, or modal questions |
| FRD, ZMA, impulse, or VituixCAD file inspection/comparison | [Measurement data tooling](doc/MEASUREMENT_DATA_TOOLING.md) | [Measurement workflow](doc/MEASUREMENT_WORKFLOW.md) only when interpreting evidence or changing measurement policy; [REW API client](doc/REW_API_CLIENT.md) for `.mdat` or live-session access |
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
| Measurement policy and tooling | [doc/MEASUREMENT_WORKFLOW.md](doc/MEASUREMENT_WORKFLOW.md), [doc/MEASUREMENT_DATA_TOOLING.md](doc/MEASUREMENT_DATA_TOOLING.md), [doc/REW_API_CLIENT.md](doc/REW_API_CLIENT.md) |
| REW procedures, qualification, and history | [doc/rew/README.md](doc/rew/README.md) |
| Room geometry and placement | [doc/ROOM_DETAILS.md](doc/ROOM_DETAILS.md) |
| 3D-model documentation | [doc/3d_models/README.md](doc/3d_models/README.md) |
| Local environments and checkout paths | [doc/LOCAL_TOOLING.md](doc/LOCAL_TOOLING.md) |

All tracked project Markdown except this file and `AGENTS.md` lives under
`doc/`. Subtree dispatchers index detailed component, qualification, and history
records without forcing them into normal orientation context.

## 5. Immediate Development Sequence

1. Preserve the completed raw-driver, Seed A acoustic/load/level/thermal, and
   three VituixCAD authorities; do not repeat passed measurements without a
   design-relevant reason.
2. Procure/build the second speaker and repeat the decisive installed,
   crossover, load, level/distortion, and bounded thermal checks under matched
   conditions. Include a correct immediate hot `0-degree` sweep and examine
   whether the first speaker's narrow high-level feature near `2.18 kHz`
   repeats.
3. Retest the first speaker only if the second-speaker work reveals an anomaly.
   Keep the cooled `48 kHz` woofer ZMA, final damping, and moderate directivity
   flare as lower-priority questions.
4. Iterate one controlled change at a time and update the owning current record.

## 6. Open Decisions

- final damping quantity and distribution;
- final cooled woofer impedance baseline and whether further conditioning helps;
- exact crossover frequency, topology, acoustic polarity, and component values;
- final inductor implementation, restraint, and crossover mounting position;
- amplifier headroom at the required listening level;
- final veneer and finish;
- final room placement among the documented reversible trials;
- whether DSP or a future subwoofer forms part of the finished system;
- production-driver spread and stereo-pair matching during the second-speaker
  build, including the deferred hot `0-degree` comparison.

## 7. One-Line Design Summary

The accepted prototype is a sealed, near-wall, measurement-designed passive
two-way loudspeaker using an SB17NRX2C35-8 woofer and SB26STWGC-4 waveguide
tweeter in an approximately `21.7 L` geometric-net plywood cabinet, with an
externally accessible development crossover and neutral low-distortion
reproduction as the overriding goal.
