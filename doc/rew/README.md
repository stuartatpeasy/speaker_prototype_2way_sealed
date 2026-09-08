# REW Documentation Dispatcher

Lifecycle: **CURRENT DISPATCHER**
Last reviewed: 2026-09-06

## 1. Purpose

This file routes a task to one REW authority. It owns navigation and lifecycle
labels only; it does not own measurement status, results, settings, or safety
release. Begin with the smallest route below and load evidence or history only
when the task actually requires it.

The lifecycle labels mean:

- **CURRENT PROCEDURE** — instructions that may govern the next physical or
  software action after their stated prerequisites are satisfied.
- **METHOD** — interface-neutral measurement principles and data-handling
  requirements; not an equipment power-up authority.
- **QUALIFICATION EVIDENCE** — concise retained results supporting a release or
  engineering conclusion; normally read for audit, failure investigation, or
  hardware/configuration change.
- **ACTIVE DIAGNOSTIC** — the authority for an unresolved fault and its next
  useful discriminator.
- **HISTORY** — superseded and failed branches retained for provenance. Do not
  load routinely and never follow an old instruction without checking the
  current procedure.

## 2. Task Routes

| Task | Read first | Add only if needed |
| --- | --- | --- |
| UMC22 installed-woofer capture or repeatability investigation | [`procedures/UMC22_INSTALLED_WOOFER_FRD.md`](procedures/UMC22_INSTALLED_WOOFER_FRD.md) | [`FRD_MEASUREMENT_METHOD.md`](FRD_MEASUREMENT_METHOD.md) when choosing/reviewing the production window or comparing captures; [`../DRIVER_ANALYSIS.md`](../DRIVER_ANALYSIS.md) when assessing or promoting driver-design evidence |
| UMC22 protected installed-tweeter capture | [`procedures/UMC22_INSTALLED_TWEETER_FRD.md`](procedures/UMC22_INSTALLED_TWEETER_FRD.md) | [`FRD_MEASUREMENT_METHOD.md`](FRD_MEASUREMENT_METHOD.md) for common timing/window review; [`../DRIVER_ANALYSIS.md`](../DRIVER_ANALYSIS.md) for the measured load and protection derivation |
| UMC22 installed-driver horizontal off-axis series | [`procedures/UMC22_INSTALLED_HORIZONTAL_OFF_AXIS_FRD.md`](procedures/UMC22_INSTALLED_HORIZONTAL_OFF_AXIS_FRD.md) | The completed woofer/tweeter runbooks only if an existing electrical-route fact is disputed; qualification only for a failed gate or changed hardware |
| General installed-driver measurement design or FRD review | [`FRD_MEASUREMENT_METHOD.md`](FRD_MEASUREMENT_METHOD.md) | The applicable interface procedure |
| Audit the UMC22 release | [`qualification/UMC22_FRD_QUALIFICATION.md`](qualification/UMC22_FRD_QUALIFICATION.md) | The dated UMC22 history only for failed or superseded branches |
| Audit or reproduce REW API extraction validation | [`qualification/REW_API_CLIENT_VALIDATION.md`](qualification/REW_API_CLIENT_VALIDATION.md) | [`../REW_API_CLIENT.md`](../REW_API_CLIENT.md) for the current operating procedure |
| Operate or reconnect the reference fixture | [`fixtures/REFERENCE_FIXTURE_USE.md`](fixtures/REFERENCE_FIXTURE_USE.md) | Qualification only if a gate fails or hardware changed |
| Rebuild, modify, or redesign the fixture | [`fixtures/REFERENCE_FIXTURE_SPECIFICATION.md`](fixtures/REFERENCE_FIXTURE_SPECIFICATION.md) | [`qualification/REFERENCE_FIXTURE_QUALIFICATION_2026-09-01_TO_03.md`](qualification/REFERENCE_FIXTURE_QUALIFICATION_2026-09-01_TO_03.md) |
| Diagnose UMC202HD desktop dropouts | [`UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md`](UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md) | No other REW file unless a specific analogue result is disputed |
| Decide whether UMC202HD FRD may resume | [`procedures/UMC202HD_FRD_SUSPENDED.md`](procedures/UMC202HD_FRD_SUSPENDED.md) | Dropout authority, fixture-use file, then qualification evidence if the physical chain changed |

## 3. Evidence And History

- [`qualification/UMC22_FRD_QUALIFICATION.md`](qualification/UMC22_FRD_QUALIFICATION.md) — **QUALIFICATION EVIDENCE** for UMC22 Gates A-E and the final repeatability release.
- [`qualification/REFERENCE_FIXTURE_QUALIFICATION_2026-09-01_TO_03.md`](qualification/REFERENCE_FIXTURE_QUALIFICATION_2026-09-01_TO_03.md) — **QUALIFICATION EVIDENCE** for amplifier topology, fixture construction, clamps, ground paths, cables, and AC commissioning.
- [`qualification/REW_API_CLIENT_VALIDATION.md`](qualification/REW_API_CLIENT_VALIDATION.md) — **QUALIFICATION EVIDENCE** for offline tests and live selected extraction; the Codex host-access boundary remains separately stated.
- [`history/UMC22_FRD_QUALIFICATION_LOG_2026-09-05.md`](history/UMC22_FRD_QUALIFICATION_LOG_2026-09-05.md) — **HISTORY** containing the detailed UMC22 chronology.
- [`history/FRD_REPEATABILITY_DEVELOPMENT_2026-09-03_TO_05.md`](history/FRD_REPEATABILITY_DEVELOPMENT_2026-09-03_TO_05.md) — **HISTORY** containing the UMC202HD-to-UMC22 method-development narrative.

History files are deliberately excluded from normal orientation. Search or
open the relevant dated subsection only when reconstructing why a setting or
decision changed.
