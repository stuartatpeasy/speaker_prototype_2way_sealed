# REW API Client

This is the authority for the project's small REW API client: its purpose,
commands, outputs, limitations, and validation status.

## 1. Purpose and authority boundary

[`src/rew_api_extract.py`](src/rew_api_extract.py) uses REW V5.40's local API to
capture current session state and to extract reviewable data from `.mdat`
files. REW remains responsible for interpreting its Java-serialised project
format; the client is deliberately not an independent binary parser.

An `.mdat` remains the raw measurement authority. Client-generated JSON and CSV
files are derived convenience outputs unless one is deliberately retained as a
documented project input or measurement baseline. A session snapshot describes
REW at the time it is captured; it does not reconstruct the historical settings
which produced an older measurement.

## 2. Runtime and preflight

Run the client with Windows Python because REW's default API listener is on the
Windows localhost interface. Start REW, enable its API on the normal port
`4735`, and leave it open. This machine is configured to start the API with
REW. From Windows PowerShell in the project root, check connectivity with:

```powershell
.venv\Scripts\python.exe src\rew_api_extract.py status
```

`status` reports API reachability and whitelisted summaries for measurements
currently loaded in REW. It is the proportionate preflight before snapshot or
extraction work.

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
2. Use the committed [`src/rew_api_extract.py`](src/rew_api_extract.py) with the
   Windows `.venv` standard-library Python runtime.
3. Run the applicable command from sections 3 or 4 against the identified REW
   build.
4. For extracts, confirm that `manifest.json` records the expected source hash,
   measurement count, stored measurement REW version, request settings, and
   returned response metadata.

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

### 7.2 Live validation record

**PASS (2026-09-05):** the Windows `.venv` client connected to the local API and
extracted `rew/UMC22 loopback-cal-data diagnostic.mdat` through REW
`V5.40 beta 133`. The source SHA-256 matched the manifest. REW returned one
measurement without warnings and `54,559` unsmoothed SPL/phase samples from
`20.1416 Hz` to `19,999.8796 Hz`; the CSV row count, finite values, and strictly
increasing frequency axis passed. API metadata independently reproduced
`48 kHz`, `0.510014 ms` delay/IR peak, `0.4375 ms` IR start, `0.0 ppm` clock
adjustment, and `43.47 dB` signal-to-noise. The API summary did not expose REW's
`47975.52` timing-reference index, so that value remains verified by the
retained REW/UI record rather than this extract.

**PASS (2026-09-05):** explicit measurement selection, unsmoothed SPL export,
and `--include-ir` also passed against
`rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat`. The selected final-
setting UUIDs were exported as REW session IDs `22`, `23`, and `24`; each
impulse CSV contains `131072` samples at `48 kHz`. The manifest has no warning
and reproduces the source size `19138881` bytes and SHA-256
`b47e6aca826a4a95d77dfcab731edac95c2c6bf21be56f8bf249fcf23bd5e3c1`.
The ignored convenience export is reconstructible at
`outputs/rew-api/sb17nrx2c35-8_umc22_repeatability-final-ir/`; the source
`.mdat` remains authoritative.

Recreate that selected raw-IR export from Windows PowerShell with:

```powershell
.venv\Scripts\python.exe src\rew_api_extract.py extract `
  "rew\SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat" `
  --output-dir "outputs\rew-api\sb17nrx2c35-8_umc22_repeatability-final-ir" `
  --measurement 87e15c6b-2405-4b89-bf5a-ff5d4b7d858e `
  --measurement 4f79ceb3-d340-44eb-a42e-c4fd3e7541c8 `
  --measurement f3c25546-ff09-44b3-ba4a-30f2751fde6b `
  --frequency-unit SPL --smoothing None --include-ir
```

The session-snapshot additions pass the offline suite but still require a
Windows-side live check. WSL-to-Windows process invocation is unavailable in
the present Codex environment, so repeat `status`, `snapshot`, and one
controlled explicit-settings extraction after installing or changing REW, or
after changing this client's endpoint coverage.
