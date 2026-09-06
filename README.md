# DIY Near-Wall Two-Way Loudspeaker

This is the compact project dashboard and documentation router for the sealed
passive two-way prototype. Read it first, then follow only the route relevant to
the task. Detailed procedures, evidence, and history are deliberately kept out
of this file.

## 1. Current Project State

**Lifecycle:** ACTIVE PROTOTYPE DEVELOPMENT

**Current phase:** the post-repair C4/C5/C6 set passes the revised proportionate
initial crossover-design gate. The former `0.2 dB` maximum across every
`1-5 kHz` native bin was too strict as the sole veto: whole-band RMS is at most
`0.182 dB`, intended `2.2-2.4 kHz` crossover-band maximum is at most `0.185 dB`,
phase and timing pass, and C5/C6 are excellent immediate repeats. C6 is the
approved installed-woofer source capture for initial modelling; its known local
early-tail uncertainty remains recorded.

**Next action:** keep signal stopped, close the open window before the next
acoustic package, and make a documented signal-free C6 FRD export when
explicitly requested. Then prepare a bounded protected-tweeter package. No
further unchanged woofer repeatability sweep is justified.

**Last reviewed:** 2026-09-06

| Subsystem | Current conclusion | Detailed authority |
| --- | --- | --- |
| Cabinet | One acoustically representative sealed prototype is complete. Body is approximately `280 x 430 x 300 mm`; geometric net volume is approximately `21.7 L` before damping. | [Cabinet design](doc/CABINET_DESIGN.md) |
| Drivers | SB17NRX2C35-8 woofer and SB26STWGC-4 tweeter remain provisionally retained. The original cooled installed ZMA files remain the crossover baselines; the woofer still needs a cooled post-conditioning confirmation. | [Driver analysis](doc/DRIVER_ANALYSIS.md) |
| Crossover | Exploratory only. The present target is approximately `2.2-2.4 kHz` with LR4-like acoustic slopes, subject to installed-baffle magnitude, common timing/phase, directivity, distortion, and complete-load measurement. | [Crossover design](doc/CROSSOVER_DESIGN.md) |
| UMC22 measurement path | Qualified for controlled installed-woofer FRD. C6, supported by immediate repeat C5, is released as the installed-woofer source capture for initial crossover modelling under proportionate RMS, crossover-band, phase, timing, and validity criteria. No further unchanged woofer repeats are needed. | [UMC22 runbook](doc/rew/procedures/UMC22_INSTALLED_WOOFER_FRD.md) |
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

1. Export the approved C6 source capture to a documented phase-bearing FRD when
   explicitly requested, then prepare the minimum protected-tweeter measurement
   package needed for initial crossover design.
2. Complete woofer stabilisation and obtain a cooled reproducible `48 kHz` ZMA.
3. Acquire installed-baffle magnitude and common-timing phase for both drivers,
   followed by horizontal off-axis and controlled distortion measurements.
4. Import current ZMA/FRD sources into VituixCAD and optimise only within
   realisable component and load constraints.
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
