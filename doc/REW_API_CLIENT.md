# REW API Client

| State | Value |
| --- | --- |
| Lifecycle | **CURRENT STATUS AND SNAPSHOT ROUTER** |
| Owns | Current REW API reachability, status/snapshot operation, and routing |
| Does not own | `.mdat` extraction semantics, workspace safeguards, output reconstruction, or detailed qualification evidence |
| Validation record | [REW API client validation](rew/qualification/REW_API_CLIENT_VALIDATION.md) |
| Compact analysis reference | [Measurement data tooling](MEASUREMENT_DATA_TOOLING.md) |
| Environment and host boundary | [Local tooling](LOCAL_TOOLING.md#2-python-and-application-boundary) |
| `.mdat` extraction | [REW MDAT extraction](rew/procedures/REW_MDAT_EXTRACTION.md) |
| Last reviewed | 2026-09-15 |

## 1. Current purpose and status

[`src/rew_api_extract.py`](../src/rew_api_extract.py) uses REW V5.40's local API for current-session status/snapshots and for `.mdat` work. REW remains the interpreter of its Java-serialised project format. An `.mdat` is the raw measurement authority; JSON/CSV output is derived unless deliberately retained as a documented input or baseline.

Start REW, enable its API on port `4735`, and leave it open. The machine uses WSL mirrored networking; ordinary WSL and host-permitted Codex commands can reach the Windows-local API, while the default Codex sandbox cannot. The [local tooling record](LOCAL_TOOLING.md#2-python-and-application-boundary) owns environment and host-access detail.

Run this proportionate preflight from Windows PowerShell:

```powershell
.venv\Scripts\python.exe src\rew_api_extract.py status
```

`status` reports reachability and whitelisted summaries of measurements loaded in REW. In ordinary WSL, the equivalent is:

```text
python3 src/rew_api_extract.py status
```

## 2. Read-only session snapshot

Capture current REW state with:

```powershell
.venv\Scripts\python.exe src\rew_api_extract.py snapshot --output "outputs\rew-api\session-snapshot.json"
```

The snapshot is GET-only and writes to standard output unless given an output path; named output is protected unless `--overwrite` is explicit. It records available application/audio/measurement/generator state, last input RMS/peak, and supported response units/smoothing, choosing Java/ASIO endpoints from the active driver and recording unavailable endpoints. Absolute host paths are redacted while calibration filenames remain where available.

A snapshot is current state, not historical provenance. Its last input levels can be absent or stale because it does not start monitoring; warning/error histories can include prior activity. Capture one immediately before and after a decisive live test when those facts matter.

## 3. Extraction and validation routing

For a compact `.mdat` summary or full export, including frequency-response settings, workspace-mutation safeguards, UMC22 instance constraint, outputs, and reconstruction, read [REW MDAT extraction](rew/procedures/REW_MDAT_EXTRACTION.md). For existing FRD, ZMA, response, impulse, or VXP data, use the offline [measurement-data tools](MEASUREMENT_DATA_TOOLING.md).

The client passed live Windows/REW extraction on 2026-09-05 and host-permitted WSL `status`, snapshot, and selected extraction on 2026-09-06. The default sandbox remains unable to make live REW calls. Detailed identifiers, source hashes, results, and commands are in the [qualification record](rew/qualification/REW_API_CLIENT_VALIDATION.md). Repeat `status`, `snapshot`, and one controlled explicit-settings extraction after changing REW, WSL networking, or endpoint coverage.
