# Measurement Equipment and Workflow

| State | Value |
| --- | --- |
| Lifecycle | **CURRENT POLICY AND ROUTING** |
| Owns | Project-wide measurement policy, evidence boundary, and routing |
| Does not own | Planning detail, interface settings, fixture operation, individual capture steps, qualification results, or crossover fabrication |
| Detailed driver evidence | [Driver analysis](DRIVER_ANALYSIS.md) |
| Procedure dispatcher | [REW documentation map](rew/README.md) |
| Measurement artefacts | [`rew/`](../rew/) |
| Compact data inspection | [Measurement data tooling](MEASUREMENT_DATA_TOOLING.md) |
| Planning and evidence detail | [Measurement planning and evidence](rew/MEASUREMENT_PLANNING_AND_EVIDENCE.md) |
| Current approved measurement action | Follow the [project dashboard](../README.md) for the active gate and the [REW dispatcher](rew/README.md) for its exact procedure; do not infer a signal release from this policy file |
| Limitations | This policy does not qualify a device, preserve detailed measurement results, or replace the current task-specific safety and routing procedure |
| Last reviewed | 2026-09-15 |

## 1. Current measurement policy

- Separate verified measurements, derivations, inferences, provisional decisions, and open items.
- Compare traces only when their controlled conditions are recorded or explicitly bounded.
- Treat impedance-derived alignment as electrical evidence, not a substitute for acoustic magnitude, phase, distortion, and directivity. Design from installed-baffle, phase-bearing acoustic data and current installed ZMA, not nominal impedances or textbook parts alone.
- Keep exploration provisional until its required measurement gates pass.
- Use the [compact measurement-data tools](MEASUREMENT_DATA_TOOLING.md) before loading raw FRD, ZMA, impulse, `.mdat`, or VituixCAD contents into a review. Ask for the smallest band, point set, or semantic comparison that answers the question; retain raw-file hashes, parameters, and warnings with the result.
- Use the current specialised procedure for exact routing, level, calibration, startup, stop, and capture instructions. Do not reconstruct live work from history. The detailed reusable plan, file conventions, safety/mutation implications, development order, and evidence handover are in [Measurement planning and evidence](rew/MEASUREMENT_PLANNING_AND_EVIDENCE.md).

## 2. Task routing

- Select exact REW operating and evidence authorities through the [REW dispatcher](rew/README.md). Qualification and history records are audit context, not normal operating context.
- Use [Measurement data tooling](MEASUREMENT_DATA_TOOLING.md) for compact FRD, ZMA, response, impulse, and VituixCAD inspection or comparison.
- Use the [REW API client](REW_API_CLIENT.md) for current live API status or a session snapshot; use its linked [`.mdat` extraction procedure](rew/procedures/REW_MDAT_EXTRACTION.md) for any `.mdat` load, summary, or export.
- Read [Measurement planning and evidence](rew/MEASUREMENT_PLANNING_AND_EVIDENCE.md) when planning a new/repeated series or interpreting and recording its results.
