# DIY Near-Wall Two-Way Loudspeaker

This is the compact project dashboard and documentation router for the sealed
passive two-way prototype. Read it first, then follow only the route relevant to
the task. Detailed procedures, evidence, and history are deliberately kept out
of this file.

## 1. Current Project State

**Lifecycle:** ACTIVE PROTOTYPE DEVELOPMENT

**Current phase:** measured Seed A is the accepted reversible external
prototype. Its acoustic summation, as-built load, bounded level/distortion, and
exposed-component surface-thermal gates pass. Driver procurement and final
crossover/placement decisions remain provisional. The owning
[driver](doc/DRIVER_ANALYSIS.md), [crossover](doc/CROSSOVER_DESIGN.md), and
[REW](doc/rew/README.md) records provide the conditions and evidence.

**Next action:** inventory/procure and build speaker two to the same design,
then compare the decisive installed, acoustic, load, level, and thermal results
under matched conditions. On speaker two, capture a valid immediate hot
`0-degree` response and check whether the narrow `2.18 kHz` high-level feature
repeats. Speaker one's wrong-angle hot trace remains excluded; retest it only if
speaker two reveals an anomaly.

**Last reviewed:** 2026-09-15

| Subsystem | Current consequence | Detailed authority |
| --- | --- | --- |
| Cabinet | One representative sealed prototype is complete; speaker two should match it. | [Cabinet design](doc/CABINET_DESIGN.md) |
| Drivers | The original cooled installed ZMAs remain model baselines; a cooled post-conditioning woofer check is lower priority. | [Driver analysis](doc/DRIVER_ANALYSIS.md) |
| Crossover | Seed A passes the bounded hardware and acoustic gates; keep it external through pair matching. | [Crossover design](doc/CROSSOVER_DESIGN.md) |
| Measurement | StarTech load and UMC22 raw-driver routes pass; desktop UMC202HD sweeps remain suspended. | [REW dispatcher](doc/rew/README.md) |
| Room | Near-wall placement candidates remain measurement trials. | [Room summary](doc/ROOM_DETAILS.md) |

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
| Cabinet fabrication | [Cabinet design](doc/CABINET_DESIGN.md) | [3D-model hub](doc/3d_models/README.md) for model selection; [regeneration and retention](doc/3d_models/REGENERATION_AND_RETENTION.md) only for rebuilding a model or printer job |
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
| FRD, ZMA, impulse, or VituixCAD file inspection/comparison | [Measurement data tooling](doc/MEASUREMENT_DATA_TOOLING.md) | [Measurement workflow](doc/MEASUREMENT_WORKFLOW.md) only when interpreting evidence or changing measurement policy |
| REW API status or session snapshot | [REW API client](doc/REW_API_CLIENT.md) | Its qualification record only for maintenance or audit |
| Retained `.mdat` extraction or summary | [REW MDAT extraction](doc/rew/procedures/REW_MDAT_EXTRACTION.md) | [REW API client](doc/REW_API_CLIENT.md) for live reachability; API qualification only for maintenance or audit |
| 3D model selection | [3D-model hub](doc/3d_models/README.md), then one component README | [Regeneration and retention](doc/3d_models/REGENERATION_AND_RETENTION.md) only for rebuilding or re-slicing |
| Documentation review | [Documentation review procedure](doc/DOCUMENTATION_REVIEW.md) | [Local tooling](doc/LOCAL_TOOLING.md) for the offline link, route, and changed-file checks; use comprehensive mode only for consolidation or handover |
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
| Dated driver and crossover decisions | [doc/history/README.md](doc/history/README.md) — history dispatcher; load only for provenance |
| Room geometry and placement | [doc/ROOM_DETAILS.md](doc/ROOM_DETAILS.md) |
| 3D-model documentation | [doc/3d_models/README.md](doc/3d_models/README.md) |
| Local environments and checkout paths | [doc/LOCAL_TOOLING.md](doc/LOCAL_TOOLING.md) |

All durable project Markdown except this file and `AGENTS.md` lives under
`doc/`. Subtree dispatchers index detailed component, qualification, and history
records without forcing them into normal orientation context.

## 5. Open Decisions

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
