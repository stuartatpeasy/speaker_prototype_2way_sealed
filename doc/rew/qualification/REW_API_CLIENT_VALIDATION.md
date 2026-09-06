# REW API Client Validation

| State | Value |
| --- | --- |
| Lifecycle | **QUALIFICATION EVIDENCE** |
| Owns | Dated live-validation inputs, results, limitations, and exact reconstruction commands |
| Does not own | Routine client operation or output policy |
| Current operating authority | [REW API client](../../REW_API_CLIENT.md) |
| Last live validation | 2026-09-06 |

## 1. Authority and interpretation

This record preserves detailed live checks of [`src/rew_api_extract.py`](../../../src/rew_api_extract.py). The source `.mdat` files remain the raw measurement authorities; generated manifests and CSV files are reconstructible convenience outputs.

## 2. Loopback diagnostic extraction

**VERIFIED OPERATION — PASS (2026-09-05):** the Windows `.venv` client connected to the local API and extracted [`rew/UMC22 loopback-cal-data diagnostic.mdat`](../../../rew/UMC22%20loopback-cal-data%20diagnostic.mdat) through REW `V5.40 beta 133`.

- The source SHA-256 matched the manifest.
- REW returned one measurement without warnings.
- The export contained `54,559` unsmoothed SPL/phase samples from `20.1416 Hz` to `19,999.8796 Hz`.
- CSV row count, finite values, and strictly increasing frequency passed.
- API metadata independently reproduced `48 kHz`, `0.510014 ms` delay/IR peak, `0.4375 ms` IR start, `0.0 ppm` clock adjustment, and `43.47 dB` signal-to-noise.

**LIMITATION:** the API summary did not expose REW's `47975.52` timing-reference index. That value remains verified by the retained REW/UI record rather than this extract.

## 3. Selected repeatability-run extraction

**VERIFIED OPERATION — PASS (2026-09-05):** explicit measurement selection, unsmoothed SPL export, and `--include-ir` passed against [`rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat`](../../../rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat).

- Selected final-setting UUIDs were exported as REW session IDs `22`, `23`, and `24`.
- Each impulse CSV contains `131072` samples at `48 kHz`.
- The manifest has no warning.
- It reproduces source size `19138881` bytes.
- It reproduces SHA-256 `b47e6aca826a4a95d77dfcab731edac95c2c6bf21be56f8bf249fcf23bd5e3c1`.
- The ignored convenience export is reconstructible at `outputs/rew-api/sb17nrx2c35-8_umc22_repeatability-final-ir/`.

The source `.mdat` remains authoritative.

### 3.1 Reconstruction command

From Windows PowerShell at the project root:

```powershell
.venv\Scripts\python.exe src\rew_api_extract.py extract `
  "rew\SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat" `
  --output-dir "outputs\rew-api\sb17nrx2c35-8_umc22_repeatability-final-ir" `
  --measurement 87e15c6b-2405-4b89-bf5a-ff5d4b7d858e `
  --measurement 4f79ceb3-d340-44eb-a42e-c4fd3e7541c8 `
  --measurement f3c25546-ff09-44b3-ba4a-30f2751fde6b `
  --frequency-unit SPL --smoothing None --include-ir
```

Expected verification: a warning-free manifest matching the source size and hash above, three selected measurements, and one `131072`-sample impulse CSV per measurement.

## 4. Post-restart bridge and snapshot validation

**VERIFIED OPERATION — PASS (2026-09-06):** after the user enabled WSL mirrored
networking and restarted WSL and Codex, the host-access path passed every
proportionate bridge check:

- Windows interoperability returned `Microsoft Windows [Version
  10.0.26200.9168]` from `cmd.exe /c ver`.
- A direct GET of `http://127.0.0.1:4735/measurements` returned HTTP `200` from
  REW's Jetty server.
- Linux `python3 src/rew_api_extract.py status` completed successfully against
  that address and reported `25` loaded measurements, all carrying stored REW
  version `V5.40 beta 133`.
- The GET-only `snapshot` command completed with `complete: true` and
  `failedEndpointCount: 0`.

**BOUNDARY:** the same probes remain blocked inside the default Codex sandbox:
Windows launch fails before the target process runs, and sandbox-local
`127.0.0.1` does not reach REW. Host-access permission is therefore required
for live REW or Win32-interoperability calls from a Codex task. This is an
execution-policy boundary, not a client defect. No TCP proxy or filesystem
request worker is currently necessary.

The snapshot was written only to disposable `/tmp` validation output. It
contains current application state rather than unique historical evidence, so
retaining it in the project is not necessary.

## 5. Historical first-candidate extraction through WSL

**VERIFIED OPERATION — PASS (2026-09-06):** a host-permitted WSL invocation
used the retained first installed-woofer production candidate to exercise the
complete status, snapshot, selected-measurement, native-response, stored-window,
and windowed-impulse path.

**SUPERSEDED SOURCE STATE:** this result refers to the earlier single-C1 content
of the production filename. That file was subsequently and intentionally saved
with C1, C2, and C3R, so its current size and hash no longer reproduce the
single-candidate values below. Section 6 owns the reconstructible current
archive validation; these values remain dated evidence of the first live pass.

- `status` reached `127.0.0.1:4735`, reported `25` loaded measurements, and
  identified `SB17-IW-0deg-1m-U22-260906-C1` as UUID
  `08cb0c1d-8c98-4e3f-91b0-efd61903c7a8`.
- `snapshot` returned `complete: true` with no failed endpoints. It confirmed
  audio ready, generator not playing, Java `48 kHz`, exclusive UMC22 input and
  output, L/L/L/R routing, microphone calibration on L, no calibration file on
  R, and the prepared single-sweep settings. Its sole warning was cumulative
  history dated 2026-09-05, not a warning from the production capture.
- The selected extraction matched source size `2,428,191` bytes and SHA-256
  `4fcf3c0168a4856be76f0346ab69e352c2d4df97212aa4564f99b014f092fcdd`.
- REW returned `54,559` native unsmoothed SPL/phase samples at approximately
  `0.366211 Hz` spacing and a `265`-sample windowed impulse at `48 kHz` (264
  sample intervals).
- The stored-window endpoint independently reproduced `Hann` `2.0 ms` left,
  reference time `3.12 ms`, `Tukey 0.25` `3.5 ms` right, with FDW and MTW off.
- The historical ignored convenience output was written under
  `outputs/rew-api/sb17nrx2c35-8_installed_0deg_1m_umc22_2026-09-06-4fcf3c01/`;
  it is not the current reconstruction authority because the singleton source
  state was superseded.

### 5.1 Historical invocation

From WSL at the project root, with host access in a Codex task:

```text
python3 src/rew_api_extract.py extract \
  'rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_2026-09-06.mdat' \
  --measurement 08cb0c1d-8c98-4e3f-91b0-efd61903c7a8 \
  --frequency-unit SPL --smoothing None --include-ir --windowed-ir
```

Against the current expanded archive, this command still selects C1 but does not
reproduce the historical single-candidate source size or hash. Use Section 6
for current reconstruction and verification.

## 6. Current C1/C2/C3R production-archive extraction

**VERIFIED OPERATION — PASS (2026-09-06):** after the production session was
saved with its final selected set, a host-permitted extraction loaded exactly
C1, C2, and C3R. The validation output then showed:

- source size `7,266,399` bytes and SHA-256
  `d582c5d1fb7591689b3e4ef5491c1c578338f854fbe97c7d31124b529f0b516b`;
- REW version `V5.40 beta 133` and `48 kHz` for all three measurements;
- native unsmoothed SPL/phase plus `131072` raw impulse samples for each
  selected UUID;
- `Hann` `2.0 ms` left and `Tukey 0.25` `3.5 ms` right windows for every
  trace, with FDW/MTW off and each trace's own stored reference time; and
- the ignored reconstructible output directory
  `outputs/rew-api/sb17nrx2c35-8_installed_0deg_1m_umc22_2026-09-06-d582c5d1/`.

The load left duplicate copies in the live REW workspace. Session IDs are not
stable identifiers; select by UUID and do not save API-loaded duplicates back
into either retained `.mdat`.

### 6.1 Reconstruction command

From WSL at the project root, with host access in a Codex task:

```text
python3 src/rew_api_extract.py extract \
  'rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_2026-09-06.mdat' \
  --output-dir 'outputs/rew-api/sb17nrx2c35-8_installed_0deg_1m_umc22_2026-09-06-d582c5d1' \
  --measurement 08cb0c1d-8c98-4e3f-91b0-efd61903c7a8 \
  --measurement 16dfc7f0-bb73-4d4b-9673-2f0f4da5b071 \
  --measurement 910df95f-0bb4-4a53-8b69-e5b6f3b7f898 \
  --frequency-unit SPL --smoothing None --include-ir --overwrite
```

Expected verification: a warning-free manifest matching the current source
size and hash above, exactly three selected measurements, one `131072`-sample
raw impulse CSV per measurement, and the stored-window settings listed above.
The source `.mdat` remains authoritative.

### 6.2 Current convenience-output audit

**VERIFIED OUTPUT LIMITATION — 2026-09-06:** the ignored directory named above
later contained `265` impulse samples per measurement, spanning the stored
`2.0 + 3.5 ms` window, rather than the `131072` raw samples specified by the
reconstruction command. The frequency responses, UUID selection, source hash,
and stored-window JSON remained internally consistent. An independent temporary
re-extraction from the authoritative `.mdat`, using the same UUIDs and command
without `--windowed-ir`, returned `131072` raw samples for each trace and no
manifest warning.

The schema-1 manifest does not record the impulse request's `windowed` flag, so
it cannot reveal how an ignored output directory came to contain a windowed
extraction. This is a convenience-output provenance limitation, not a change to
either retained `.mdat`; inspect impulse sample count and time span before
calling such output raw. The current operating limitation is documented in
[REW_API_CLIENT.md](../../REW_API_CLIENT.md).
