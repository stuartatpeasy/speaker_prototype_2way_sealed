# REW MDAT Extraction

| State | Value |
| --- | --- |
| Lifecycle | **CURRENT SUPPORTING PROCEDURE** |
| Owns | `.mdat` extraction and compact summary semantics, output/reconstruction, and REW-workspace mutation safeguards |
| Does not own | REW API connectivity, live-session qualification evidence, or the retained `.mdat` authority |
| Read when | Extracting or summarising a retained `.mdat`, choosing native-grid settings, or auditing an ignored API export |
| Current approved action | Run `status` first through the [REW API client](../../REW_API_CLIENT.md), then use the narrowest command below only when its workspace mutation is acceptable |
| Limitations | The API cannot expose all historical routing/timing facts; REW, retained records, and external observations remain authoritative for those facts |
| Last reviewed | 2026-09-15 |

## 1. Authority and workspace rule

REW V5.40 interprets its Java-serialised `.mdat`; [`src/rew_api_extract.py`](../../../src/rew_api_extract.py) is deliberately not an independent binary parser. The retained `.mdat` is the raw measurement authority. Generated JSON and CSV are derived convenience outputs unless deliberately retained as a documented project input or baseline.

Extraction and `summarize` are signal-free but mutate the current REW workspace: loading the source leaves new measurement copies in the session. Extract after a live capture set, or in a disposable session. If production captures must continue, remove only known API-loaded copies before saving, or reload the retained production `.mdat`; never save those duplicates into the measurement authority.

**Current UMC22 instance rule (user-reported, 2026-09-06):** do not open a second REW instance while the primary instance must retain UMC22 handles. A throwaway export/re-import instance caused the primary instance to lose them permanently; recovery required saving the open omnibus session, exiting, and reloading it in one restarted REW instance. Use one process for subsequent hardware work, defer disposable inspection until the interface is no longer needed, or first close the hardware-owning instance. This is an observed operational limitation, not proof of a bad capture.

## 2. Full extraction

From the project root in Windows PowerShell:

```powershell
.venv\Scripts\python.exe src\rew_api_extract.py extract "rew\example.mdat"
```

The default output contains whitelisted provenance, magnitude/phase, frequency-axis/unit/smoothing/sample-count metadata, and stored impulse-window settings. Add `--include-ir` for the potentially large impulse CSV and `--windowed-ir` to apply stored IR windows. Repeat `--measurement UUID` to select newly loaded measurements from a multi-measurement file; `status` shows UUIDs and current session IDs. Output refuses a non-empty directory without explicit `--overwrite`, and overwrite does not delete unrelated files.

For a native-grid impedance extraction with explicit display-independent settings:

```powershell
.venv\Scripts\python.exe src\rew_api_extract.py extract "rew\example.mdat" --frequency-unit ohm --smoothing None
```

Controls are `--frequency-unit`, `--smoothing`, and optional positive-integer `--ppo`. REW beta 133 calls impedance `ohm`; valid smoothing names include `None`, `1`, `1/2`, `1/3`, `1/6`, `1/12`, `1/24`, `1/48`, `Var`, `Psy`, and `ERB`. The manifest records the request and returned metadata. Unit or PPO mismatch stops extraction; smoothing mismatch is a warning. Omit `--ppo` for the native grid because forced resampling may apply PPO/2 anti-alias smoothing: `96` PPO can report `1/48` smoothing even when `None` was requested.

Schema version 1 records the frequency-response request but not whether an optional impulse used `--windowed-ir`. Inspect `impulse-response-metadata.json`: a raw response has the measurement's full sample count, while a windowed response spans only the stored left/right support. Do not label an existing ignored impulse CSV from `manifest.json` alone. A later client change should record the mode and test it offline.

## 3. Compact `.mdat` summary

For engineering facts rather than reusable exports:

```powershell
.venv\Scripts\python.exe src\rew_api_extract.py summarize "rew\example.mdat" --band 20 20000 --frequency-unit ohm --smoothing None --ppo 96 --at 1000
```

Band and unit are required. Repeat `--measurement` or `--at` as needed; the former accepts IDs/UUIDs and the latter makes nearest-sample queries. `--smoothing` defaults to `None`, `--ppo` to `96`; record both and use full native-grid extraction if PPO's possible anti-alias smoothing could change the decision.

`summarize` requests frequency responses, analyses decoded rows in memory, and prints bounded JSON only. It includes source hash/size, selection and response parameters, scalar metadata, warnings, extrema, and requested points; `ohm` additionally reports real/imaginary impedance extrema and ideal class-B EPDR. It neither writes CSV nor requests impulse samples. It has the same workspace mutation as extraction. For existing FRD, ZMA, response, or impulse exports, prefer the offline [measurement-data tools](../../MEASUREMENT_DATA_TOOLING.md).

## 4. Outputs and reconstruction

Default extracts and session snapshots use `outputs/rew-api/<source>-<sha256-prefix>/` and `outputs/rew-api/`; the directory is ignored because outputs are disposable and reconstructible. Compact summaries normally stay on standard output.

Reconstruct a full export or summary from the retained `.mdat` and recorded hash, the committed client, identified REW build, and recorded command parameters. For full extracts, confirm `manifest.json` has the expected source hash, count, stored measurement REW version, frequency-response request, and returned metadata. Under the schema-1 limitation, confirm raw/windowed impulse content from sample count, time span, and command as well. If a CSV or FRD becomes a VituixCAD input or cited baseline, copy it into `rew/` under a descriptive name, retain provenance, and commit it; never leave unique information only in ignored convenience output.

## 5. Evidence boundary and verification

The client exposes the completed `.mdat` analyses' summary fields, magnitude/phase, IR windows, and optional impulse samples. It does not expose some historical routing/timing facts, including timing-reference sample index and per-measurement device/channel routing; retain REW records, exports, screenshots, observations, and meter readings for those. It does not wrap distortion, group-delay, or RT60 endpoints; add an endpoint only for an actual project analysis.

Run the standard-library tests after changing the client:

```text
python -m unittest discover -s tests -v
```

They cover decoding, frequency axes, response settings, partial GET-only snapshots, Java/ASIO selection, redaction, path translation, selection, overwrite guards, CSV rows, summaries, impedance calculations, and representative API failures without REW. Live Windows/REW validation passed on 2026-09-05 and host-permitted WSL validation on 2026-09-06, including selected native unsmoothed SPL/phase and raw/windowed impulse work; detailed identifiers, hashes, results, and commands are in the [qualification record](../qualification/REW_API_CLIENT_VALIDATION.md). Repeat `status`, `snapshot`, and one controlled explicit-settings extraction after changing REW, WSL networking, or endpoint coverage.
