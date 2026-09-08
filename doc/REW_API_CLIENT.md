# REW API Client

| State | Value |
| --- | --- |
| Lifecycle | **CURRENT TOOL OPERATION** |
| Owns | Purpose, commands, outputs, reconstruction, and current limitations |
| Does not own | Detailed live qualification evidence |
| Validation record | [REW API client validation](rew/qualification/REW_API_CLIENT_VALIDATION.md) |

## 1. Purpose and authority boundary

[`src/rew_api_extract.py`](../src/rew_api_extract.py) uses REW V5.40's local API to
capture current session state and to extract reviewable data from `.mdat`
files. REW remains responsible for interpreting its Java-serialised project
format; the client is deliberately not an independent binary parser.

An `.mdat` remains the raw measurement authority. Client-generated JSON and CSV
files are derived convenience outputs unless one is deliberately retained as a
documented project input or measurement baseline. A session snapshot describes
REW at the time it is captured; it does not reconstruct the historical settings
which produced an older measurement.

## 2. Runtime and preflight

Start REW, enable its API on the normal port `4735`, and leave it open. This
machine is configured to start the API with REW. Windows Python remains the
direct execution route. From Windows PowerShell in the project root, check
connectivity with:

```powershell
.venv\Scripts\python.exe src\rew_api_extract.py status
```

`status` reports API reachability and whitelisted summaries for measurements
currently loaded in REW. It is the proportionate preflight before snapshot or
extraction work.

The host now uses WSL mirrored networking, so the standard-library client can
also reach the Windows-local API directly from an ordinary WSL session:

```text
python3 src/rew_api_extract.py status
```

Within a Codex task, localhost networking and Windows-process interoperability
remain blocked by the default inner sandbox. Run REW API or Win32-interoperability
commands with the task's host-access permission; no TCP proxy or filesystem
request worker is currently required.

## 3. Read-only session snapshots

Capture the current state with:

```powershell
.venv\Scripts\python.exe src\rew_api_extract.py snapshot --output "outputs\rew-api\session-snapshot.json"
```

Without `--output`, the JSON is written to standard output. An existing named
file is protected unless `--overwrite` is supplied.

The command is strictly read-only and collects, where REW makes them available:

- application warnings, errors, and blocking state;
- audio status, driver, sample rate, calibration, device, input/output, channel,
  and reference-channel selections;
- measurement mode, level, sweep, timing-reference, repetition, delay, and
  protection settings;
- generator state, signal configuration, level, frequency, full-scale voltage,
  and protection settings;
- the last available input RMS and peak levels; and
- REW's supported frequency-response units and smoothing choices.

The client selects the Java- or ASIO-specific routing endpoints from REW's
current driver and records individual unavailable endpoints rather than
discarding an otherwise useful snapshot. Absolute Windows, UNC, and common
POSIX host paths are redacted; calibration filenames are retained where
available.

Snapshot interpretation has three important limits:

1. Current state is not historical measurement provenance.
2. The last input levels may be absent or stale because this GET-only command
   does not start level monitoring.
3. REW warning and error histories are cumulative and may include earlier
   activity.

Capture a snapshot immediately before and after a decisive live test when these
facts matter.

## 4. `.mdat` extraction

Load a retained project and export each newly loaded measurement with:

```powershell
.venv\Scripts\python.exe src\rew_api_extract.py extract "rew\example.mdat"
```

The default extract contains:

- whitelisted measurement provenance;
- frequency-response magnitude and phase;
- frequency-axis, unit, smoothing, and sample-count metadata; and
- stored impulse-response window settings.

Add `--include-ir` to write the potentially large impulse-response CSV and
`--windowed-ir` if REW should apply the stored IR windows to it. Use
`--measurement UUID` to select a particular newly loaded measurement from a
multi-measurement file; the option is repeatable. `status` shows the UUIDs and
current session IDs. The client refuses to write into a non-empty output
directory unless `--overwrite` is explicit, and does not delete unrelated
files when overwriting its named outputs.

**CURRENT MANIFEST LIMITATION:** schema version 1 records the frequency-response
request but does not record whether the optional impulse request used
`--windowed-ir`. Inspect `impulse-response-metadata.json`: a full raw response
has the measurement's full sample count, while a windowed response spans only
the stored left/right support. Do not label an existing ignored impulse CSV raw
or windowed from `manifest.json` alone. A later client revision should add the
impulse request mode to the manifest and cover it in the offline tests.

Extraction is signal-free but is not read-only with respect to REW's current
workspace: REW loads the source `.mdat` and leaves the newly loaded measurement
copies in the session. Prefer extraction after the live capture set is complete
or in a disposable REW session. If more production captures must follow, remove
only the known newly loaded copies before saving the production session, or
reload the retained production `.mdat`; do not accidentally save API-loaded
duplicates into the measurement authority.

**CURRENT UMC22 INSTANCE RULE (user-reported, 2026-09-06):** do not open a
second REW instance while the primary instance must retain the UMC22. Opening a
throwaway instance for FRD export/re-import inspection caused the original
instance to permanently lose its UMC22 handles. Recovery required saving the
open omnibus session, exiting, and reloading it in one restarted REW instance.
Use one REW process for subsequent hardware work; defer disposable-session
inspection until the interface is no longer needed, or close the hardware-
owning instance first. This is an observed operational limitation, not evidence
of a bad capture.

### 4.1 Explicit frequency-response settings

When physical interpretation must not depend on REW's current display state,
request the response settings explicitly. A native-grid impedance extraction
is:

```powershell
.venv\Scripts\python.exe src\rew_api_extract.py extract "rew\example.mdat" --frequency-unit ohm --smoothing None
```

The controls are `--frequency-unit`, `--smoothing`, and optional positive-
integer `--ppo`. REW beta 133's API name for impedance is `ohm`; smoothing names
include `None`, `1`, `1/2`, `1/3`, `1/6`, `1/12`, `1/24`, `1/48`, `Var`, `Psy`,
and `ERB`.

The manifest records the request and REW's returned metadata. A unit or PPO
mismatch stops extraction; a smoothing mismatch is recorded as a warning for
inspection. Omit `--ppo` when preserving the native frequency grid: forcing PPO
resampling permits REW to apply PPO/2 anti-alias smoothing. For example, 96 PPO
may report 1/48-octave smoothing even when `None` was requested.

## 5. Outputs and reconstruction

Default extracts are written under
`outputs/rew-api/<source>-<sha256-prefix>/`. Session snapshots should also be
placed under `outputs/rew-api/`. That directory is intentionally ignored because
these outputs are disposable and reconstructible.

The complete reconstruction route is:

1. Retain the source `.mdat` for an extraction, or retain access to the live REW
   session for a snapshot.
2. Use the committed [`src/rew_api_extract.py`](../src/rew_api_extract.py) with the
   Windows `.venv` standard-library Python runtime.
3. Run the applicable command from sections 3 or 4 against the identified REW
   build.
4. For extracts, confirm that `manifest.json` records the expected source hash,
   measurement count, stored measurement REW version, frequency-response
   request settings, and returned response metadata. Until the schema-1
   limitation above is fixed, confirm raw versus windowed impulse content from
   its sample count and time span as well as from the reconstruction command.

If an exported CSV or FRD becomes a deliberate VituixCAD input or cited
measurement baseline, copy it to `rew/` with a descriptive filename, retain its
provenance, and commit it. Do not treat the ignored convenience copy as the only
record of unique information.

## 6. Supported and unavailable evidence

The current client retrieves the API-exposed data required for the project's
completed `.mdat` trace analyses: measurement summary fields, magnitude and
phase, IR windows, and optional impulse samples. The API still does not expose
some facts needed to audit earlier tests, including the timing-reference sample
index and historical per-measurement device/channel routing. Existing retained
REW records, exports, screenshots, written observations, and external meter
readings remain authoritative for such evidence.

The client does not currently wrap REW's distortion, group-delay, or RT60
endpoints. None was required for the completed tests reviewed when this client
was introduced. Add them when a real project analysis needs them rather than
expanding the client speculatively.

## 7. Verification

### 7.1 Offline tests

Run the standard-library test suite in Windows or WSL with:

```text
python -m unittest discover -s tests -v
```

The tests cover array decoding, frequency-axis reconstruction, explicit
response settings, GET-only partial snapshots, Java/ASIO selection, path
redaction, Windows-path translation, measurement selection, overwrite guards,
CSV row counts, and representative API failures without requiring REW.

### 7.2 Live validation status

The client passed live Windows/REW extraction checks on 2026-09-05, including
source-hash verification, native-grid SPL/phase export, explicit measurement
selection, and optional impulse export. The complete measurements, identifiers,
hashes, results, and reconstruction command are retained in the
[qualification record](rew/qualification/REW_API_CLIENT_VALIDATION.md).

**PASS (2026-09-06):** after enabling WSL mirrored networking and restarting
WSL and Codex, a host-permitted Linux-side `status` call reached REW at
`127.0.0.1:4735`, and the GET-only `snapshot` command completed with no failed
endpoints. Windows command interoperability also passed outside the inner
sandbox. A host-permitted selected extraction of the retained first
installed-woofer candidate passed, and a later selected extraction of the final
C1/C2/C3R production archive passed source-hash, native unsmoothed SPL/phase,
raw-impulse, and stored-window checks for all three UUIDs. The default sandbox
still blocks both routes, so future Codex tasks must request host access for
live REW calls. A subsequent UUID-selected C6 extraction also validated its
durable FRD against all `31,404` retained rows within printed precision. Full
evidence and the current reconstruction commands are retained in the
[qualification record](rew/qualification/REW_API_CLIENT_VALIDATION.md).

Repeat `status`, `snapshot`, and one controlled explicit-settings extraction
after installing or changing REW, changing WSL networking, or changing this
client's endpoint coverage.
