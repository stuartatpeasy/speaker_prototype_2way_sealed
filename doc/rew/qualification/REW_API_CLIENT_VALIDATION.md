# REW API Client Validation

| State | Value |
| --- | --- |
| Lifecycle | **QUALIFICATION EVIDENCE** |
| Owns | Dated live-validation inputs, results, limitations, and exact reconstruction commands |
| Does not own | Routine client operation or output policy |
| Current operating authority | [REW API client](../../REW_API_CLIENT.md) |
| Last live validation | 2026-09-05 |

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

## 4. Outstanding live check

**OPEN VALIDATION:** session-snapshot additions pass the offline suite but still require a Windows-side live check. Repeat `status`, `snapshot`, and one controlled explicit-settings extraction after installing or changing REW, or after changing the client's endpoint coverage. The present managed WSL environment cannot invoke the Windows process directly; this is an environment boundary, not evidence of a client defect.
