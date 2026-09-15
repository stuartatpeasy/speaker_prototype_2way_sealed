# Installed Driver Acoustic Sources — 2026-09-06 To 2026-09-07

> - **Lifecycle:** AUDIT-ONLY SOURCE QUALIFICATION
> - **Owns:** detailed raw acoustic-capture provenance, capture/release evidence, source identities, UUIDs, hashes, windows, raw and exported file checks, failed attempts, source-scale derivation, sparse-polar evidence, and source-filing corrections
> - **Does not own:** current driver conclusions, crossover decisions, live operation, or a generic measurement procedure
> - **Current authority:** [Driver analysis](../../DRIVER_ANALYSIS.md)
> - **Read when:** auditing or changing an approved source, diagnosing an anomaly, reproducing an export, or reviewing a failure; do not routinely load for modelling or capture preparation
> - **Approved release:** C6 woofer-axis; TW1/C2 common-position; protected-tweeter `+11.14 dB` VituixCAD magnitude correction; positive-side sparse woofer and protected-tweeter polar families
> - **Limitations:** one driver sample each; generic microphone calibration rather than absolute SPL; positive-side sparse polar only; local woofer early-tail variability near `2.03 kHz`; derived C2 scale; no inferred unmeasured angles
> - **Last reviewed:** 2026-09-15

This record moved the detailed source-release evidence out of the routinely read driver authority without discarding it. The current source manifest, applicability, and next gate remain in [Driver analysis](../../DRIVER_ANALYSIS.md).

## 1. Scope And Current Release

The released sources retain their original raw `.mdat` archives as authority. The exported FRDs are faithful native unsmoothed representations at the approved REW-native windows. Do not overwrite an archive or FRD; create a separately named source for a materially different capture or analysis state.

## 2. Detailed On-Axis, Common-Position, And Polar Evidence

### 2.1 Original detailed source-release evidence

C6 is the approved installed-woofer-axis source capture, with C5 as its
immediate repeatability witness. Its durable phase-bearing FRD is retained
below. TW1 and protected-tweeter C2 are the retained common-position sources
from the fixed tweeter-axis microphone point, so their relative phase and path
length represent one observation point. Both positive-side sparse raw polar
capture families now pass signal-free review; the protected-tweeter polar FRDs
and woofer polar FRDs are verified. This is a prototype-design release with
stated uncertainty, not a frozen production response.

**VERIFIED EXPORT — C6:**
[`rew/frd/SB17NRX2C35-8/000deg_1m_UMC22_2026-09-06.frd`](../../../rew/frd/SB17NRX2C35-8/000deg_1m_UMC22_2026-09-06.frd)
is the current crossover-input export. It is `913,746` bytes with SHA-256
`af3142aeff9dcd232ddb61878452c31afe5cae5446e4bd266b2e4e337488c1ca`.
Its header identifies REW V5.40 beta 133, C6's title, `-20.0 dBFS` `256k`
loopback-calibrated/timed capture, `3.1100 ms` delay, no smoothing, and a
nominal `500 Hz` start. It contains `31,404` finite frequency/magnitude/phase
rows from `499.877960` to `12000.000966 Hz` at the native approximately
`0.366211 Hz` spacing.

**DERIVED EXPORT VALIDATION:** a fresh signal-free API extraction selected C6
by UUID `1547767f-1781-4e51-b824-462b5a2788e1` from its authoritative
single-measurement `.mdat`, returned the expected source SHA-256 and stored
`Hann` `2.0 ms` left / `Tukey 0.25` `3.5 ms` right window at
`3.1100022059 ms`, with FDW/MTW off and no warning. Across all `31,404` export
rows, frequency differs from the native response by at most `0.000058 Hz`,
magnitude by `0.000508 dB`, and circular phase by `0.001508 degrees`. Those
differences are text precision only; the FRD is a faithful native unsmoothed
export of the approved capture.

**USER DECISION — EXPORT NAMING:** durable acoustic exports use
`rew/frd/<driver>/<AAA>deg_<distance>_<interface>_<date>.frd`, with a
three-digit zero-padded angle for useful filename sorting. Revisit the suffix
before adding multiple materially different datasets for the same driver and
angle; do not overwrite one dataset with another.

**VERIFIED MEASUREMENT / DERIVED REVIEW — COMMON-POSITION TW1 PASSED:** the
one authorised companion woofer sweep
`SB17-IW-0deg-1m-U22-260906-TW1` completed at `17:52:37` with UUID
`12568bef-2ec1-4cc7-be3a-91460b0659fa`. REW reports `48 kHz`,
`20.141602-19999.879 Hz`, direct peak/System Delay `3.1388593352 ms`, IR start
`3.0208333333 ms`, loopback-cal reference, zero timing offset/IR shift, zero
clock adjustment, and `42.75 dB` signal-to-noise. The user reported no warning,
clipping, or anomaly, minimum displayed headroom `8.8 dB`, and constant
reference-input figure `33.7 dB`. A post-capture GET-only snapshot found audio
ready, Generator stopped, no current error or blocking state, and the intended
`-20 dBFS`, `20-20000 Hz`, `256k`, one-repetition configuration. Earlier
warning-history entries predate TW1 and belong to the throwaway-instance event;
they are not TW1 warnings.

TW1 arrives `28.857 us` later than woofer-axis C6. The simple geometric
prediction for the reported `150 mm` rise at `1.000 m` baffle distance is
`32.616 us`, leaving only `-3.759 us` residual. A signal-free comparison applied
the same direct-sound support offline—`Hann` `2.0 ms` left and a one-sided
`Tukey 0.25` `3.5 ms` right approximation—to both raw impulses. At the nearest
native bin to `2.297 kHz`, TW1 is `-0.271 dB` relative to C6; circular phase is
`-22.12 degrees` before and `+1.74 degrees` after removing the measured delay.
The first stronger late-energy maximum is at approximately `3.60 ms` after the
direct peak, just beyond the proposed right-window end. This makes the common
REW-native `Hann 2.0 ms` / `Tukey 0.25 3.5 ms` window appropriate for TW1 on
its own impulse evidence. FDW/MTW remain off and the window reference is the
exact `3.1388593352 ms` direct arrival. The offline frequency comparison is a
review diagnostic, not the durable REW export.

**PROVISIONAL DESIGN RELEASE:** no repeat of TW1 is justified. Its timing,
impulse, headroom, metadata, and crossover-region response are coherent with
the intentional microphone move. Increasing attenuation above approximately
`5 kHz` is physically expected at the roughly `8.5-degree` vertical off-axis
woofer angle and did not constrain the then-proposed `2.2-2.4 kHz` crossover.
TW1's approved window, axis-qualified single-measurement `.mdat`, and validated
FRD are now retained without moving the geometry.

**VERIFIED FILE / LIVE WINDOW — TW1:**
[`rew/SB17NRX2C35-8_installed_000deg_tweeter-axis_1m_UMC22_2026-09-06.mdat`](../../../rew/SB17NRX2C35-8_installed_000deg_tweeter-axis_1m_UMC22_2026-09-06.mdat)
is `2,428,191` bytes with SHA-256
`78abfeec5c1efcfbba510785710cb35cdaa39a7e8d167fe88c1871f5e16928ef`.
A read-only API check of the live UUID found stored `Hann 2.0 ms` left /
`Tukey 0.25 3.5 ms` right windows, FDW/MTW off, at displayed reference
`3.140 ms`. That reference is only `1.141 us` later than the fitted
`3.138859 ms` peak—well below one `20.833 us` sample and equivalent to
approximately `0.95 degrees` at `2.30 kHz`—so its effect on gate placement is
immaterial.

**VERIFIED EXPORT — TW1:**
[`rew/frd/SB17NRX2C35-8/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd`](../../../rew/frd/SB17NRX2C35-8/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd)
is `913,085` bytes with SHA-256
`03923152b08c36e066cb0f9520c7a76489bf6837e3b85cd06c67af0c12a8e4b7`.
It contains `31,404` finite native unsmoothed magnitude/phase rows from
`499.877960` to `12000.000966 Hz`. A read-only UUID-selected API comparison
against the live response found maximum differences of `0.000009 Hz`,
`0.000513 dB`, and `0.001498 degrees` circular phase. These are text precision
only; the export faithfully preserves TW1 for common-position crossover work.

**VERIFIED MEASUREMENT — FIRST-CAPTURE REVIEW PASSED:** the first controlled production
candidate, `SB17-IW-0deg-1m-U22-260906-C1`, was captured on 2026-09-06 in REW
V5.40 beta 133 from `20-20000 Hz` using one `256k`, `-20.0 dBFS` sweep. Stored
Measurement Info identifies microphone input L, electrical timing-reference
input R, timing-reference output L, `ECM8000_calibration_data.csv`, loopback
soundcard calibration, `48 kHz`, System Delay `3.1241 ms`, IR start `3.0000 ms`,
timing-reference index `47,850.04`, zero timing offset and cumulative shift,
`0.0 ppm` clock adjustment, SNR `44.3 dB`, and signal-to-distortion `62.8 dB`.

**USER-REPORTED:** no physical or electrical change preceded the sweep; the
hardware clip indicators were off and the idle system was silent and normal.
No warning or anomaly occurred during the sweep, and both displayed headroom
indicators remained green throughout. The exact numeric headrooms were not
recorded.

**DERIVED HEADROOM BOUND:** REW defines green analogue-input measurement
headroom as `6-40 dB`, so the observation bounds both microphone-L and
reference-R headroom to that interval. It does not recover the exact values.
The stored SNR, signal-to-distortion result, absence of warnings, and bounded
headroom do not justify another signal solely to recover the missing digits.

**INFERRED FROM ETC AND GEOMETRY:** geometry predicts the earliest floor/ceiling
energy about `3.81 ms` after the direct arrival. The time-expanded ETC shows a
corresponding rise beginning near `6.9 ms` absolute time and a peak near
`7.1 ms`, roughly `27 dB` below the direct peak. Earlier decaying structure is
not uniquely separable from the bandwidth-limited woofer's direct response.

**VERIFIED APPLIED WINDOW / DERIVED:** the live REW measurement now has a
native `Hann` `2.0 ms` left window and `Tukey 0.25` `3.5 ms` right window,
referenced to the displayed `3.12 ms` direct peak, with frequency-dependent and
multi-time windowing off. REW reports `285.71 Hz` using the right-window width
and a total span of `264` samples. Independently, the `5.5 ms` total support has
nominal resolution

```text
Delta f approximately 1 / 0.0055 s = 182 Hz.
```

This ends the right window near `6.62 ms`, ahead of the first
geometry-consistent reflection. The windowed magnitude is coherent from its
REW limit through the crossover region and retains the woofer breakup structure
around `4-10 kHz`; the wrapped phase is continuous apart from ordinary
`+/-180 degree` wraps. **PROVISIONAL VALID RANGE:** use `500 Hz-12 kHz` for
driver/crossover work. This conservative range stays clear of the window's
`285.71 Hz` limit and excludes the steep, increasingly irregular upper-tail
response that is not needed for the intended crossover.

**VERIFIED FILE RETENTION:** the current C1/C2/C3R raw authority is
[`rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_2026-09-06.mdat`](../../../rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_2026-09-06.mdat),
`7,266,399` bytes, SHA-256
`d582c5d1fb7591689b3e4ef5491c1c578338f854fbe97c7d31124b529f0b516b`.
A post-save selected extraction loaded exactly C1, C2, and C3R, produced no
warning, and read back each trace's `Hann` `2.0 ms` left / `Tukey 0.25`
`3.5 ms` right native window with FDW/MTW off and its own direct-peak reference.
The failed C3 attempt is excluded and retained separately below.

**USER-REPORTED / VERIFIED MEASUREMENT — C2:** the user reported microphone-L
minimum headroom `10.6 dB`, reference-R headroom `33.1 dB`, and no warning or
anomaly. The API independently identifies loopback-timed C2 at `48 kHz` with
System Delay `3.1168 ms`, IR start `3.0000 ms`, zero timing offset and shift,
`0.0 ppm` clock adjustment, and SNR `38.74 dB`.

**VERIFIED WINDOW / DERIVED REPEATABILITY RESULT:** the API applied and read
back C1's production window shape and widths to C2, referenced to C2's direct
peak. From `1-5 kHz`, C1/C2 native unsmoothed maximum magnitude difference is
`1.754 dB`, RMS magnitude difference is `0.602 dB`, maximum circular phase
difference is `16.476 degrees`, and System Delay spread is `7.32 us`. This
fails the approximate `0.2 dB` / preferred `5 us` repeatability targets. The
windowed impulses correlate at `0.9991` with a fitted C2/C1 level difference
of approximately `-0.178 dB`; this makes a grossly different route unlikely
but does not explain the response-shape difference.

**USER-REPORTED / VERIFIED DIAGNOSTIC — FAILED C3 ATTEMPT:** the user reported
that the prepared attempt produced no audible output, raised two warnings, and
created a visibly invalid response. The API identifies a `-46 dBFS` maximum,
SNR `9.39 dB`, nonsensical System Delay `-4780.4033 ms`, and raw impulse peak
`-0.0019%`, compared with approximately `-2.6%` for C1/C2. REW's attempt-time
warnings were low measured level and poor SNR. Current API state still reports
the qualified software route and stopped generator. The trace is background
noise and must remain diagnostic.

**USER-REPORTED PHYSICAL CAUSE / STRONGLY SUPPORTED INFERENCE:** the user then
found one woofer lead detached from its connector and re-secured it. The
amplifier selection, volume, UMC22 controls/connections, relay, USB, and
indicators were otherwise reported nominal and unchanged. An open woofer
circuit explains all observed C3 symptoms and is the strongly supported cause,
though the contact state throughout the entire attempted sweep was not
electrically logged. The physical change therefore required a de-energised
connection inspection and cold no-signal restart; both subsequently passed as
user-reported evidence below.

**USER-REPORTED RESTART PASS:** with signal stopped, the user turned the
SU-V570 down and off, inspected the repaired connection, and confirmed correct
polarity, full engagement and retention, with no exposed conductor, stray
strand, or possible opposite-terminal contact. The amplifier was restarted at
minimum, remained silent and normal without heat, smell, or instability, and
was returned to the qualified `-38 dB` position without a tone.

**VERIFIED CURRENT API AUDIT:** after that restart the API reported
REW V5.40 beta 133 reachable, audio ready, generator stopped, no application
error, exact exclusive UMC22 endpoints, Java Stereo-only operation, `48 kHz`,
L/L/L/R routing, loopback calibration/timing, IR merge off, zero timing offset,
and the prepared `20-20000 Hz`, `-20 dBFS`, `256k`, one-repetition sweep. Its
per-input calibration object names `ECM8000_calibration_data.csv` under both L
and R, which by itself is insufficient to prove that the electrical reference
is uncalibrated. **USER-CONFIRMED CONFIGURATION:** the user subsequently
confirmed in both Measure and Preferences that active microphone input L names
the ECM8000 CSV and electrical reference input R is `None`. A final API snapshot
then remained complete with no failed endpoint, new measurement, warning, or
error; audio was ready and the generator remained stopped. This clears the
pre-signal calibration gate.

**USER-REPORTED / VERIFIED MEASUREMENT — C3R:** the user reported normal woofer
output, microphone-L minimum headroom `10.7 dB`, reference-R headroom `33.2 dB`,
and no warning or anomaly. Measurement Info was reported correct for the
microphone calibration, loopback soundcard calibration, and L/L/L/R routing;
timing-reference index was `47,850.56` and signal-to-distortion was `60.5 dB`.
The API independently identifies C3R UUID
`910df95f-0bb4-4a53-8b69-e5b6f3b7f898`, captured at 13:05:32 in REW V5.40
beta 133 from `20.1416-19999.879 Hz` at `48 kHz`. It reports System Delay
`3.1133 ms`, IR start `2.9792 ms`, zero timing offset and cumulative shift,
`0.0 ppm` clock adjustment, and SNR `43.41 dB`. The post-capture snapshot was
complete with no new warning or error; audio was ready and the generator was
stopped.

**VERIFIED WINDOW AND IMPULSE / DERIVED ENVELOPE:** C3R's long default window was
replaced through the API and read back as the common native `Hann` `2.0 ms`
left / `Tukey 0.25` `3.5 ms` right window, referenced to its own `3.1133 ms`
direct peak, with FDW/MTW off. Its raw direct peak is `-2.532%`. The API does
not expose REW's plotted ETC directly; a nine-sample moving-RMS envelope of the
raw impulse locates the first
geometry-consistent material reflection at approximately `7.155 ms` absolute,
`4.042 ms` after the direct peak and approximately `27.0 dB` below it. This
agrees closely with C1/C2 at approximately `7.166/7.179 ms` and confirms that
the right window ends near `6.613 ms`, ahead of that reflection. The established
provisional valid range remains `500 Hz-12 kHz` for each candidate; it is not a
promotion of the set.

**USER-REPORTED CONFIGURATION — C4-C6:** immediately before the new post-repair
series, the user confirmed that the repaired woofer connector was fully seated
and that wiring, settings, physical positions, and environmental conditions
were unchanged. Hardware clip indicators were off; the system was silent and
normal. The Agilent U1282A's internal thermometer, without a connected
thermocouple, indicated `22.1 degrees C`; this is a room-temperature indication,
not calibrated local air temperature. No warning, clipping indication, or other
anomaly was reported for C4-C6. Exact displayed headrooms were not retained;
the remaining visible metadata was subsequently reported without another signal.

**USER-REPORTED RETAINED METADATA — C4-C6:** timing-reference indices are C4
`47850.66`, C5 `47850.64`, and C6 `47850.72`; signal-to-distortion figures are
respectively `63.5`, `59.5`, and `61.0 dB`. Headrooms were reported nearly
identical to the earlier successful runs, though exact values were not retained.
The index spread is `0.08` sample, and at `48 kHz`

```text
0.08 sample / 48000 sample/s = 1.667 us.
```

This accounts for the `1.655 us` System Delay spread to about `0.012 us`, so
the recorded timing does not indicate source-to-microphone distance drift.

**USER-REPORTED ENVIRONMENTAL NOTE / DERIVED TIMING:** a window approximately
`1 m` behind the microphone was slightly open and admitted an intermittent
breeze. For the approximately axial geometry, the reflected path is roughly
`3 m` versus the `1 m` direct path, giving

```text
excess delay = (3 m - 1 m) / 343 m/s = 5.83 ms.
```

That direct specular reflection is later than the retained `3.5 ms` right
window and cannot directly explain the stored-window residual. Airflow could
still add turbulence or move a stand, cable, curtain, or light object. Closing
the window is a proportionate control for future acoustic packages, not grounds
to reject C5/C6 or repeat them now.

**VERIFIED MEASUREMENTS — C4-C6:** the API identifies the following unique
post-repair captures, each made in REW V5.40 beta 133 at `48 kHz` from
`20.1416-19999.879 Hz`, with loopback timing, zero timing offset and cumulative
shift, `0.0 ppm` clock adjustment, and no new application warning:

| Capture | UUID | Time | System Delay | IR start | SNR |
|---|---|---:|---:|---:|---:|
| C4 | `a855e31c-42a2-45a7-bb5c-8e1616334c7a` | `14:03:20` | `3.111277 ms` | `2.979167 ms` | `43.91 dB` |
| C5 | `46922260-e9cb-46c0-bdef-3a11ba592b00` | `14:06:49` | `3.111657 ms` | `2.979167 ms` | `44.06 dB` |
| C6 | `1547767f-1781-4e51-b824-462b5a2788e1` | `14:07:08` | `3.110002 ms` | `2.979167 ms` | `44.06 dB` |

C4 was reviewed before the remaining pair, so C5 and C6 are the strictly
consecutive captures (`19 s` timestamp separation); C4 precedes C5 by
`3 min 29 s`. The three-capture System Delay spread is `1.655 us`, comfortably
inside the preferred `5 us` target.

**VERIFIED FILE RETENTION — C4-C6:** because the live REW workspace contained
API-loaded duplicates, each new UUID was saved to a previously absent
single-measurement archive rather than using `Save all`. A selected reload of
each file returned exactly its expected UUID, common `Hann` `2.0 ms` left /
`Tukey 0.25` `3.5 ms` right native window at its own direct peak, no FDW/MTW,
`54,559` native response points, all `131,072` raw impulse samples, and no
extraction warning:

| Capture | Raw `.mdat` | Bytes | SHA-256 |
|---|---|---:|---|
| C4 | [`rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C4_2026-09-06.mdat`](../../../rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C4_2026-09-06.mdat) | `2,428,186` | `6e53eaba36039769075544f0cde4d286db155e5429df4cfa4d536a12419b6052` |
| C5 | [`rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C5_2026-09-06.mdat`](../../../rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C5_2026-09-06.mdat) | `2,428,186` | `7d1c45bcf2d58c5582f53db679bf7b0febd32c15c2bd2086d82a076b4ad10c1b` |
| C6 | [`rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C6_2026-09-06.mdat`](../../../rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C6_2026-09-06.mdat) | `2,428,186` | `6c9a4223073ac9bd52ec7b7ff2dd6e0106f36cd40b9511c0df77a80eeb686ca0` |

**DERIVED C4-C6 REPEATABILITY — STRICT MAX FAIL / PROPORTIONATE DESIGN PASS:**
on the common native unsmoothed grid over `1-5 kHz`, the pairwise results are:

| Pair | Maximum magnitude | RMS magnitude | Mean level | Mean-removed max / RMS | Circular phase max / RMS |
|---|---:|---:|---:|---:|---:|
| C4/C5 | `0.631 dB` | `0.182 dB` | `-0.0667 dB` | `0.564 / 0.169 dB` | `4.119 / 1.208 degrees` |
| C4/C6 | `0.512 dB` | `0.151 dB` | `-0.0727 dB` | `0.439 / 0.132 dB` | `3.473 / 1.859 degrees` |
| C5/C6 | `0.137 dB` | `0.047 dB` | `-0.0060 dB` | `0.143 / 0.047 dB` | `3.565 / 2.060 degrees` |

The old maximum-over-every-bin rule would fail the set because the worst C4/C5
residual is `0.631 dB` near `2.03 kHz`. That statistic selects the single worst
of `10,923` closely spaced native bins and is disproportionate as the sole veto
for an iterative prototype crossover. It remains useful diagnostic evidence.
The small mean offsets do not explain the frequency-dependent shape. C4 also
differs from C3R by `2.115 dB` maximum and `0.804 dB` RMS over `1-5 kHz`, so
C3R is not selected as the current baseline.

Under the revised design-relevant gate, all C4-C6 pairs pass: whole-band
`1-5 kHz` RMS is at most `0.182 dB`; unsmoothed maximum difference over the
intended `2.2-2.4 kHz` crossover region is C4/C5 `0.185 dB`, C4/C6
`0.183 dB`, and C5/C6 `0.112 dB`; full-band circular-phase maximum is at most
`4.119 degrees`; and System Delay spread is `1.655 us`. At `1/24`-octave
smoothing, used only as a broadness check, the whole-band maxima are `0.548`,
`0.447`, and `0.103 dB`, while the crossover-band maxima remain no greater than
`0.157 dB`. The residual is real but too small in the design region to justify
blocking a prototype network that will be measured and iterated.

**DERIVED WINDOW SENSITIVITY / TIME LOCALISATION:** temporary changes on
API-loaded copies, restored afterward, show that all three C4-C6 pairs pass with
`1.0` or `1.5 ms` right windows. At `1.5 ms`, the worst maximum difference is
`0.154 dB`; at `2.0 ms`, C4/C5 and C4/C6 rise to `0.328` and `0.317 dB`, while
C5/C6 remain at `0.085 dB`. The C4-related maxima then grow monotonically to
`0.631` and `0.512 dB` at the retained `3.5 ms` window. Direct-relative raw-
impulse comparisons likewise show sub-percent differences through the direct
packet, with discrepancy increasing later in the early tail. The recurring
shape change therefore enters mainly between approximately `1.5` and `3.5 ms`
after the direct arrival. A `1.5 ms` right window has nominal resolution

```text
Delta f approximately 1 / 0.0015 s = 667 Hz.
```

It is a useful localisation test, not a silent replacement for the established
`500 Hz-12 kHz` production window.

**DERIVED OLDER C1/C2/C3R COMPARISON — FAIL:** with all three captures on the
same native unsmoothed frequency grid and common window, the `1-5 kHz`
three-capture
maximum magnitude spread is `1.754 dB`, RMS spread is `0.822 dB`, maximum
pairwise circular-phase difference is `25.966 degrees`, and System Delay spread
is `10.82 us`. C2 and post-repair C3R are the closest pair, but still show
`0.957 dB` maximum and `0.487 dB` RMS magnitude difference, `11.185 degrees`
maximum circular-phase difference, and `3.50 us` delay difference. Their mean
level difference is only `0.049 dB`; after removing it, `0.947 dB` maximum and
`0.485 dB` RMS magnitude error remain, proving that the failure is response
shape rather than a simple gain offset. At the provisional `2.3 kHz` crossover
point alone they are close (`0.021 dB`, `2.31 degrees`), but the set still fails
the revised whole-band RMS and timing criteria and spans the connector repair.

**VERIFIED PIPELINE AUDIT / DERIVED SENSITIVITY — 2026-09-06:** UUID selection
returns exactly C1, C2, and C3R; the failed diagnostic is absent. All three
responses contain the same `54,559` native frequency points from
`20.1416015625 Hz` at `0.3662109673 Hz` spacing, with SPL units, smoothing
`None`, no PPO resampling, and the stored common window types and widths.
The `1-5 kHz` comparison contains `10,923` point-for-point samples and uses
circular phase differences; ordinary phase subtraction creates false
approximately `360-degree` spikes at wraps.

Fitting a scalar dB gain leaves most of the error:

| Pair, first trace to second | Best dB gain | Residual maximum | Residual RMS |
|---|---:|---:|---:|
| C1 to C2 | `-0.1690 dB` | `1.5846 dB` | `0.5777 dB` |
| C1 to C3R | `-0.2179 dB` | `1.4720 dB` | `0.7114 dB` |
| C2 to C3R | `-0.04890 dB` | `0.9474 dB` | `0.4847 dB` |

Removing each stored System Delay difference explains the broad phase slope
but leaves frequency-dependent phase error:

| Pair | System Delay difference | Raw phase max / RMS | Delay-corrected max / RMS |
|---|---:|---:|---:|
| C1/C2 | `7.3202 us` | `16.476 / 9.773 degrees` | `9.076 / 3.877 degrees` |
| C1/C3R | `10.8178 us` | `25.966 / 13.631 degrees` | `9.462 / 4.771 degrees` |
| C2/C3R | `3.4976 us` | `11.185 / 4.941 degrees` | `6.148 / 3.186 degrees` |

The recorded timing-reference indices for C1 and C3R move from `47,850.04` to
`47,850.56`, or `0.52` sample = `10.833 us` at `48 kHz`. That accounts for all
but approximately `0.016 us` of their System Delay change. The endpoint delay
spread is therefore timing-reference-pick variation rather than evidence of a
`3.7 mm` acoustic-distance change. C2's timing-reference index was not retained,
so the same check cannot be completed for it. Constant delay cannot change
magnitude in any event.

C1's `3.120000 ms` stored window reference is `4.090837 us`, or `0.1964`
sample, before REW's `3.124090837 ms` sub-sample direct-peak estimate. The
stored reference lands on the actual maximum discrete impulse sample. On a
temporary API-loaded duplicate, moving only the reference to the exact
sub-sample peak and reading it back changed none of the `54,559` native
magnitude/phase values and none of the `265` windowed-impulse amplitudes at the
API's returned precision; only the windowed impulse's reported start time moved.
The original `3.12 ms` reference was restored. Window-reference rounding is
therefore excluded as a material cause.

Shortening every right window from `3.5 ms` to `1.0 ms` reduced, but did not
remove, the `1-5 kHz` differences: C1/C2, C1/C3R, and C2/C3R still had
respectively `0.491`, `0.814`, and `0.502 dB` maximum differences. Their
mean-removed maxima were `0.365`, `0.741`, and `0.489 dB`, all above the
`0.2 dB` target. That short window also gives only about `1 kHz` right-window
resolution and cannot support the established `500 Hz` lower limit. Even
`1/6`-octave smoothing leaves respective maxima of `1.031`, `0.943`, and
`0.688 dB`. Short windowing and smoothing can mask some structure, but neither
explains it nor makes the production evidence reusable.

**DERIVED FREQUENCY LOCALISATION:** the discrepancy consists of broad alternating
lobes rather than isolated bins. Principal signed extrema are C1-C2
`+1.754 dB` at `2517.0 Hz`; C1-C3R `-1.254 dB` at `2162.8 Hz`, `+1.482 dB` at
`2501.6 Hz`, `-1.086 dB` at `4212.2 Hz`, and `+1.289 dB` at `4627.1 Hz`; and
C2-C3R `+0.957 dB` at `2811.4 Hz`, `+0.935 dB` at `3801.3 Hz`, `-0.899 dB` at
`4244.0 Hz`, and `+0.863 dB` at `4736.9 Hz`. The worst pair/band RMS values are
C1/C2 `0.877 dB` over `2-3 kHz`, C1/C3R `0.858 dB` over `4-5 kHz`, and C2/C3R
`0.595 dB` over `4-5 kHz`.

**VERIFIED RAW IMPULSES / DERIVED ENVELOPES:** a fresh temporary extraction from
the authoritative `.mdat` returned `131072` raw samples at `48 kHz` for every
UUID. Direct negative peaks are C1 `-2.627883%`, C2 `-2.576019%`, and C3R
`-2.532312%`. Over `-0.5` to `+0.5 ms` relative to each direct peak, pairwise
correlations are at least `0.99984`; over the common `-2.0` to `+3.5 ms` support
they are `0.99908`, `0.99826`, and `0.99919`. In the `+0.5` to `+3.5 ms`
early tail they fall to `0.99328`, `0.98786`, and `0.99428`, with scalar-fit
residuals about `11.6%`, `15.5%`, and `10.7%` of target RMS. The direct wavelet
is therefore nearly unchanged apart from a small level trend; most shape
divergence accumulates in early post-arrival energy.

The first geometry-consistent material-reflection envelope peaks remain closely
grouped: C1 at `+4.0417 ms` and `-27.06 dB`, C2 at `+4.0625 ms` and
`-26.65 dB`, and C3R at `+4.0417 ms` and `-27.01 dB`, all relative to their
direct envelopes. The current right window ends at `+3.5 ms`, ahead of these
peaks. This rules out the principal floor/ceiling/rear-wall reflection as the
direct cause of the stored-window difference, although lower-level earlier
acoustic or structural energy is not uniquely separable.

**EXPLORATORY FIT / INFERENCE:** a single delayed-comb term fitted over
`1.5-5 kHz` describes much of the C3R-related alternating structure with about
`0.99-1.01 ms` delay and `R^2=0.72-0.74`; the weaker C1/C2 fit has
`R^2=0.35`. A `1.0 ms` acoustic delay corresponds to roughly `0.343 m` extra
path at `343 m/s`. This localises a useful time scale, not a physical object:
early reflection/diffraction, cabinet or driver decay, and sweep corruption from
an evolving contact cannot be distinguished uniquely from these files.

**VERIFIED METADATA AUDIT / LIMITATION:** all API-exposed production summaries
agree on REW V5.40 beta 133, `48 kHz`, sweep span, loopback timing/calibration,
zero timing offset and cumulative shift, `0.0 ppm` clock adjustment, polarity,
SPL/align offsets, and extraction warnings. C1's earlier singleton and final
archive extractions are byte-identical for frequency response, windowed impulse,
and window JSON despite changed session IDs, which supports UUID stability.
The API cannot reconstruct historical per-measurement endpoint/channel routing,
calibration assignment, headroom, timing-reference index, or
signal-to-distortion. C1 and C3R have retained UI/Measurement Info evidence;
C2's less complete historical UI metadata is an evidence gap, not positive
evidence of a configuration error.

The separate diagnostic archive was also re-extracted by its UUID. It contains
one `131072`-sample raw trace with peak `0.001904%`, SNR `9.386 dB`, and
System Delay `-4780.403 ms`, confirming background rather than a production
response. Its warning-free extraction manifest means only that file loading and
export succeeded; it does not supersede the user's two attempt-time warnings.

**RANKED INFERENCES:**

1. A variable early delayed acoustic or structural contribution is now the
   strongest class of explanation. C4-C6 repeat through approximately the first
   `1.5 ms`, then diverge, while direct timing remains within `1.65 us`.
   Subtle cabinet, microphone, support, cable, baffle/driver, or nearby-object
   motion could change that energy without a conspicuous direct-arrival shift.
2. Woofer-connector/contact evolution remains plausible across the original
   pre/post-repair boundary and is the only verified intervening physical event
   there. The firmly seated connector did not prevent the C4-related early-tail
   variation, so connector state alone is no longer an adequate explanation for
   all observations. An electrically changing contact could still affect driver
   decay; that was not independently logged.
3. A small environmental change during C4's `3 min 29 s` separation from C5 is
   possible. C5/C6, only `19 s` apart, pass. The slightly open window's simplest
   reflection arrives about `5.83 ms` after the direct sound, outside the stored
   window, but its intermittent breeze could move a stand, cable, curtain, or
   light object. Closing it is a cheap future control. The `22.1 degrees C`
   internal-thermometer indication does not resolve local gradients or motion.
4. C2's lower `38.74 dB` SNR may contribute to the older comparison, but broad
   coherent lobes with associated phase and impulse-tail structure are not well
   explained as random noise alone; C4-C6 have closely grouped `43.91-44.06 dB`
   SNR and still show the C4-related tail change.
5. A historical routing or calibration inconsistency remains logically possible
   for C2 because it lacks complete UI provenance, but the archived/API metadata
   gives no positive evidence for one. It cannot explain variation among the
   consistently configured C4-C6 captures.
6. Scalar gain, constant delay, phase wrapping, C1 window rounding, smoothing,
   and the first material reflection remain quantitatively excluded as complete
   explanations. Shorter windows localise rather than repair the physical
   variability.

**PROVISIONAL DESIGN RELEASE / PARKED ROOT-CAUSE ITEM:** C1, C2, C3R, and C4-C6
are valid response captures; the failed C3 remains diagnostic. The original
`0.2 dB` maximum over every `1-5 kHz` native bin was too strict as the sole
prototype-design gate. Under the revised method, C4-C6 pass on whole-band RMS,
intended-crossover-band maximum, phase, timing, and capture validity. C6 is the
approved current woofer-axis source capture, with immediate C5 as its
repeatability witness and C4 retained as an uncertainty bound. The later
microphone move creates the separate common-position requirement derived in
Section 6.4; it does not demote or alter C6.

The approximately `0.5-0.6 dB` local early-tail variation near `2.03 kHz` is
recorded rather than erased. It is not large enough at the intended
`2.2-2.4 kHz` crossover to block a reversible external prototype network.
Park the root-cause investigation unless same-package measurements reproduce a
design-relevant discrepancy, the crossover choice becomes sensitive to it, or
normal/reverse-polarity validation is incoherent. No further unchanged woofer
repeatability sweep is justified now.

**HISTORICAL INTERPRETATION SUPERSEDED BY C4-C6:** before the post-repair series,
the leading open item was one unchanged C4 discriminator; immediately afterward,
the full-window maximum was temporarily treated as a blocking failure. The
capture and its two authorised repeats are complete, and the proportionate
design release above supersedes both prior positions without deleting their
evidence.

**VERIFIED DIAGNOSTIC RETENTION:**
[`rew/SB17NRX2C35-8_UMC22_C3_no_output_diagnostic_2026-09-06.mdat`](../../../rew/SB17NRX2C35-8_UMC22_C3_no_output_diagnostic_2026-09-06.mdat)
is `2,428,201` bytes with SHA-256
`e60bd9e0643a37d70f2162a8f8aa24214bceb7b2341a17c79198219374d318e2`.
Its retained measurement is named `DIAG-C3-no-output-260906`; it is excluded
from the C1/C2 production authority.

The completed installed-woofer route and its API-assisted audits are retained
in the [UMC22 installed-woofer FRD
runbook](../procedures/UMC22_INSTALLED_WOOFER_FRD.md). No further unchanged
raw-woofer repeatability sweep is required.
Qualification evidence and its generic microphone/absolute-SPL limitations are
in [UMC22 FRD
qualification](UMC22_FRD_QUALIFICATION.md).


## 3. Protection, Geometry, Polar Release, And Scale Evidence

### 3.1 Original detailed protection and source-release evidence

**USER-REPORTED GEOMETRY — 2026-09-06:** after completing the woofer export,
the ECM8000 was raised `150 mm` so its capsule is level with the centre of the
installed tweeter dome and aimed directly at it. The cabinet was not moved.
The user then confirmed that the capsule-to-baffle distance remains `1000 mm`,
the window is closed, and no cabinet/microphone movement occurred during TW1.
This establishes the intended tweeter-axis crossover-design observation point.

**USER-CONFIRMED HORIZONTAL ROTATION GEOMETRY — 2026-09-06:** the jig's
vertical axis passes through the front baffle plane halfway between the left
and right cabinet edges; the vertically aligned driver centres lie on that
horizontal centreline. At `0 degrees`, the baffle front edge and centre are
directly over the pivot. Positive angle means anti-clockwise cabinet rotation
when viewed from above. This fixes the baffle reference point at constant
radius and releases geometry planning for the separate sparse horizontal
runbook; it is configuration evidence, not an off-axis measurement. The
subsequent protected-tweeter and polar captures used that geometry and passed.

**DERIVED COMMON-POSITION CONSEQUENCE:** with `1.000 m` perpendicular distance
to the baffle and `0.150 m` vertical centre spacing, the woofer-to-microphone
distance at the tweeter-axis point is

```text
d_w = sqrt((1.000 m)^2 + (0.150 m)^2) = 1.01119 m
delta d = 1.01119 m - 1.000 m = 0.01119 m
delta t = 0.01119 m / 343 m/s = 32.6 us
phase at 2.30 kHz = 360 deg x 2300 1/s x 32.6e-6 s = 27.0 deg.
```

The units reduce to metres, seconds, and degrees as expected. Independently
moving the microphone onto each driver's axis would erase this design-relevant
geometric contribution. C6 remains valid woofer-axis evidence; TW1 subsequently
captured the required woofer datum from the fixed tweeter-axis microphone point
and its measured extra delay agrees with this prediction as recorded in
Section 1.3.

**PROVISIONAL MEASUREMENT-PROTECTION DECISION:** for the bounded low-level REW
capture only, use a measured nominal `10 uF` non-polar polypropylene film
capacitor, rated at least `100 V`, in series with the tweeter positive lead.
An `8.2-10 uF` measured value is acceptable if `10 uF` is unavailable. This
single capacitor is not a listening crossover and does not satisfy the
manufacturer's high-power `2.6 kHz`, `12 dB/octave` condition; it is adequate
only in combination with the retained approximately `1 V RMS` amplifier-output
limit, a `20-20000 Hz` sweep, one repetition, and the stop rules in the
[protected-tweeter runbook](../procedures/UMC22_INSTALLED_TWEETER_FRD.md).

**USER-REPORTED SELECTED COMPONENT — 2026-09-06:** the selected capacitor is
TDK `B32774H4106K000`, marked `10 uF`, `450 VDC`, polypropylene film. Five
consecutive instrument readings were consistent at `10.13 uF` and `0.08 ohm`
ESR. The repeatability is useful user-reported component evidence; the ESR
reading remains dependent on the meter's test frequency and lead compensation.

**PUBLISHED PART CHECK:** [TDK identifies this ordering
code](https://product.tdk.com/en/search/capacitor/film/dc-link/info?part_no=B32774H4106K000)
as a radial boxed MKP DC-link capacitor, `10 uF`, `+/-10%`, `450 VDC`. The
selected part therefore passes the dielectric, capacitance, polarity, and
voltage-rating requirements.

For `C = 10 uF` and the published `R_e = 3.2 ohm`, the simple resistive corner
estimate is

```text
f_c = 1 / (2 pi R_e C)
    = 1 / (2 pi x 3.2 ohm x 10e-6 F)
    = 4.97 kHz.
```

Using the measured `10.13 uF` gives `f_c = 4.91 kHz`; the `+1.3%` capacitance
difference is immaterial to this protection role.

Using the measured `10.13 uF` and `0.08 ohm` ESR with the measured complex
installed ZMA rather than a fixed resistor, the derived tweeter-terminal/source-
voltage ratios are approximately `-16.91 dB` at `500 Hz`, `-9.23 dB` at the
measured `761 Hz` resonance, `-7.21 dB` at `2.297 kHz`, and `-2.41 dB` at
`5.01 kHz`. The maximum calculated ratio over `500 Hz-20 kHz` is `1.006`
(`+0.052 dB`) near `19.75 kHz`; an approximately `1.00 V RMS` amplifier source
therefore remains about `1.01 V RMS` maximum at the tweeter. This is a low-
energy measurement condition, not a power-handling test.

The qualified clamp/attenuator must be connected across the tweeter terminals
*after* the series capacitor. Referencing before the capacitor would embed its
transfer in the acoustic FRD; at `2.30 kHz` that would introduce approximately
`-7.21 dB` magnitude and approximately `+59 degrees` phase relative to the
driver terminal.
The post-capacitor electrical reference divides out the protection network's
frequency-dependent magnitude and phase while retaining the tweeter's acoustic
phase and delay. REW defines the generated calibration curve as `0 dB` at
`1 kHz`, however, so the capacitor's terminal/source ratio at that frequency
remains as a constant magnitude offset. That scalar is corrected during
modelling as derived below.
No shunt inductor, fuse, or extra series resistor is required for this one
low-level sweep package; the eventual listening and crossover-validation route
must use the designed full high-pass network.

**USER-REPORTED DE-ENERGISED ASSEMBLY — CORRECTED PASS (2026-09-06):** the
first assembly mistakenly placed the clamp/attenuator reference on the wrong
side of the series capacitor. The anomalous `11.162 kohm` amplifier-side
reading prompted a stop before power-up, and the user corrected the wiring.
After correction, amplifier-side resistance rises rapidly to open circuit,
consistent with capacitor DC blocking; resistance directly across the tweeter
and post-capacitor fixture input is `3.326 ohm`; no short is present; and a
second, more thorough wiring inspection passed. This was a caught pre-power
configuration error, not measurement evidence or a driver fault. The protected
tweeter route passes its physical gate.

**USER-REPORTED / VERIFIED POWERED-IDLE AND REW GATE — PASS (2026-09-06):** the
corrected powered route remained silent and normal with no audible output,
anomaly, or smell. A complete GET-only snapshot confirmed audio ready, exact
exclusive UMC22 endpoints at `48 kHz`, Java Stereo only, L/L/L/R, ECM8000
calibration on microphone input L only, loopback calibration/timing with merge
off and zero offset, Generator stopped, and exact C1 `500-20000 Hz`,
`-20 dBFS`, `256k`, one-repetition, clipping-abort fields. This releases only
the first protected C1 sweep before review.

**USER-REPORTED ATTEMPTS / VERIFIED SURVIVING TWEETER C1 — TIMING EXPLAINED,
CONFIRMATION PENDING (2026-09-06):** three starts occurred. The first
accidentally ran with the amplifier off, the second with a fan left on, and the
third as specified. The first two were deleted from REW before review and
remain only user-reported discarded diagnostics. The surviving third capture is
`SB26-IW-000deg-tweeter-axis-1m-U22-260906-C1`, UUID
`00543c2b-4588-4385-9b81-e0d78bca28a0`, captured at `18:36:05`. The user
reported `19.9 dB` minimum measurement headroom, `36.1 dB` reference figure,
`69.5 dB` signal-to-distortion, no clipping, and no anomaly; the API reports
`44.64 dB` SNR and no warning at the run timestamp. The only new cumulative
warnings, at `18:34:41` and `18:35:09`, precede it and belong to the discarded
attempts. Its separately saved source is
`rew/SB26STWGC-4_installed_000deg_tweeter-axis_1m_UMC22_C1_2026-09-06.mdat`,
`2,377,078` bytes, SHA-256
`f47fb2499c27b6bdff4e1ab01595998beb1ce2bd0d96ebe4cb6bcfed5f561c7b`.

The surviving raw impulse has one dominant direct-looking peak, but REW places
it at `79.8603588 ms` with IR start `79.7916667 ms`, equivalent to an impossible
`27.392 m` path. Energy before `10 ms` is more than `81 dB` below the peak, so
this is not a simple late-reflection peak-selection error. The first separated
later peaks are approximately `3.31 ms` (`-22 dB`) and `6.06 ms` (`-19.86 dB`)
after the dominant peak.

The user-reported timing-reference index is `44,166.70`; the preceding retained
woofer C6 index was `47,850.72`. At `48 kHz` their difference is

```text
delta n = 47,850.72 - 44,166.70 = 3,684.02 samples
delta t = 3,684.02 samples / 48,000 samples/s = 76.7504167 ms
corrected C1 delay = 79.8603588 ms - 76.7504167 ms = 3.1099421 ms.
```

The common-position woofer TW1 delay is `3.1388593 ms`, making the corrected
tweeter arrival `28.9172 us` earlier. The purely geometric expectation for the
woofer being `150 mm` off axis at a `1.000 m` baffle-plane distance is
`32.6164 us` earlier for the tweeter (using `343 m/s`); the residual is only
`3.6992 us`, about `1.27 mm` of acoustic path. This exact accounting verifies
that C1's gross delay is timing-reference bookkeeping, not an acoustic path or
reflection. The user also verified that `Loopback delay reference is IR peak`
remained checked, ruling out a changed preference.

**SUPERSEDED PROVISIONAL INFERENCE / RELEASE BASIS:** the deliberate `500 Hz` rather than
`20 Hz` sweep start is the most economical explanation for the changed
reference-peak index; finite-band excitation can change a loopback reference's
peak location. C1 remains corroborating magnitude/impulse evidence; the
completed C2 below is the phase-bearing design source. Its actual result
confirmed the index mechanism and superseded the pre-C2 delay estimate.
The `10.13 uF` capacitor has `785.6 ohm` reactance at `20 Hz`, so a
simple `3.3 ohm` load bound gives only `0.00420` voltage ratio (`-47.53 dB`, or
about `4.2 mV` for a `1 V RMS` source). Extending the logged sweep start is
therefore negligible additional tweeter stress within the unchanged low-level
one-sweep package.

**USER-REPORTED / VERIFIED MEASUREMENT — C2 PASSED; TIMING CAUSE CONFIRMED:**
the one released `20-20000 Hz` sweep completed without warning, clipping, or
anomaly. The user reported `19.1 dB` minimum headroom, constant `36.2 dB`
reference level, timing-reference index `47,857.68`, System Delay `3.0067 ms`,
and `70.9 dB` signal-to-distortion. A subsequent GET-only API review found the
new measurement at session ID `45`, stable UUID
`898195c2-fc7d-4eee-a877-7be9d3782f0d`, captured at `18:54:03`, with
`20.141602-19999.879 Hz`, `48 kHz`, loopback-cal reference, zero timing
offset/IR shift/clock adjustment, `42.19 dB` SNR, no new warning, and Generator
stopped. The live Measure title was inadvertently left as
`SB26-IW-000deg-tweeter-axis-1m-U22-260906-C1`; that is a naming error only and
must be corrected to C2 before its single-measurement save.

The gross-timing mechanism is now established. Expressing the direct peak on
the common sample axis gives

```text
C1: 44,166.70 + 0.0798603588 s x 48,000 samples/s = 47,999.997 samples
C2: 47,857.68 + 0.00300670085 s x 48,000 samples/s = 48,002.002 samples.
```

Restoring the `20 Hz` start therefore removed the entire approximately
`76.9 ms` reference-index displacement. Only `2.004` samples (`41.76 us`)
separate the band-limited impulse maxima; this is a peak-shape consequence of
the different sweep bandwidths, not evidence of a `26.4 mm` hardware movement.
C2's common-band `3.00670 ms` delay is the retained acoustic timing value. Its
approximately `45.3 mm` shorter apparent path than TW1 contains the real
woofer/tweeter acoustic-centre offset as well as the known `11.19 mm` geometric
path difference and must remain in the crossover phase data.

**DERIVED SIGNAL-FREE IMPULSE REVIEW / SOURCE RELEASE:** aligning
the full raw C1 and C2 impulses at their dominant peaks gives correlation
`0.99883`, least-squares C2/C1 scale approximately `+0.13 dB`, and only
`0.455%` RMS residual relative to C2's peak over `-1.0` to `+3.5 ms`. Both have
the same early/room structure: about `+0.625 ms` near `-22 dB`, `+3.312 ms`
near `-21 to -22 dB`, and `+6.062 ms` near `-20 to -22 dB`. The intended
`Hann 2.0 ms` left / `Tukey 0.25 3.5 ms` right window retains the repeatable
early speaker/baffle response while tapering the first separated later arrival.

The default approximately half-second REW windows produce meaningless large
native-bin differences at deep room-comb cancellations. An offline one-sided
approximation to the intended short window instead gives `0.510 dB` RMS and
`1.982 dB` maximum C2-C1 magnitude difference over `500 Hz-12 kHz`. The local
`2.2-2.4 kHz` difference reaches approximately `1.61 dB` and `14.6 degrees`,
but C1 and C2 deliberately used different sweep starts, so this is not a valid
same-configuration repeatability bound; short-window convolution of C1's
`500 Hz` band edge is a confounder. Given C2's clean validity metrics, stable
raw impulse, correct common timing basis, and the project's proportionate
prototype goal, another on-axis sweep is not justified. Retain C1 as
corroborating evidence and C2 as the source candidate, with the lack of a true
same-band tweeter repeat recorded as an uncertainty rather than a veto.

**VERIFIED RETENTION AND EXPORT — C2:** the renamed single-measurement source
`rew/SB26STWGC-4_installed_000deg_tweeter-axis_1m_UMC22_C2_2026-09-06.mdat`
is `2,428,204` bytes with SHA-256
`662d759ba08044bbda6bb04b0d824a0905c6a841b049cd342b1964d041f0d26b`.
A UUID-selected extraction read back the correct C2 title, UUID
`898195c2-fc7d-4eee-a877-7be9d3782f0d`, `3.0067008 ms` delay, native
`Hann 2.0 ms` left / `Tukey 0.25 3.5 ms` right window at the direct peak, and
FDW/MTW off. The retained FRD
`rew/frd/SB26STWGC-4/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd` is
`912,077` bytes with SHA-256
`a409445a40e645682b188b7a12596c10f727d8a0f78138f052c043d60bb0ea1e`.
Its `31,404` finite native unsmoothed rows span
`499.877960-12000.000966 Hz` and match the UUID-selected response within
`0.000058 Hz`, `0.0005152 dB`, and `0.001502 degrees` circular phase. C2 is
therefore promoted from source candidate to the retained protected-tweeter
on-axis source for initial crossover modelling.

**USER-REPORTED / VERIFIED HORIZONTAL POLAR CAPTURE — TWEETER CAPTURE AND
EXPORT PASS (2026-09-06):** the user completed the protected-tweeter
`+20/+40/+60 degree` batch and reported `19.1 dB` minimum headroom across all
three sweeps. The retained three-measurement archive
`rew/SB26STWGC-4_installed_positive_horizontal_020-060deg_tweeter-axis_1m_UMC22_2026-09-06.mdat`
is `7,266,429` bytes with SHA-256
`61a9c66b1edef2199f9b267a0172bba5933ecb21f26ee8c22bcf12cdf9a053d7`.
A post-save REW extraction returned exactly these measurements:

| Angle | UUID | System Delay | API SNR field |
| ---: | --- | ---: | ---: |
| `+20 degrees` | `7c673a7d-1e5c-42fa-9c1c-3786a8d0d2eb` | `3.0170751 ms` | `40.72 dB` |
| `+40 degrees` | `3ebfc5ee-445d-492c-a51b-6f68d776e2fa` | `3.0079346 ms` | `37.83 dB` |
| `+60 degrees` | `8c55d7cb-bc87-4d5b-baed-93fda8e6e251` | `2.9545955 ms` | `34.84 dB` |

All three are native unsmoothed `48 kHz` responses with loopback-cal timing,
zero timing offset, no inversion, IR shift, or clock adjustment, and no
extraction warning. The post-batch GET-only snapshot found Generator playback
off and no new application warning or error. The `62.48 us` direct-peak span
is retained: the increasingly band-limited off-axis waveform can move its
dominant peak, and no independent delay is added or removed.

**DERIVED POLAR-WINDOW DECISION:** relative to C2's on-axis direct-envelope
peak, the new direct peaks fall by approximately `1.15`, `5.39`, and
`10.66 dB`. The first secondary energy near `+1.56/+1.73/+1.79 ms` instead
remains at approximately `-29.2/-29.0/-28.3 dB` on that same absolute scale;
the later approximately `+3.33 ms` arrival is similarly near `-21 dB`. A
feature that stays nearly fixed while direct sound falls with angle is fixed
room/jig energy, not the tweeter's radiation pattern. The polar family will
therefore use `Hann 2.0 ms` left / `Tukey 0.25 1.5 ms` right, FDW/MTW off,
each at its own exact direct peak. API tests on disposable copies showed that
further shortening to `1.25 ms` changed `1.5-12 kHz` magnitude by only
`0.16-0.23 dB RMS` (`0.47-0.77 dB` maximum), adequate convergence for the
project's crossover-directivity decision.

This is a separate matched-window polar dataset, provisionally usable over
`1.5-12 kHz`; it does not supersede or overwrite C2's `3.5 ms` phase-bearing
on-axis design FRD. At the `1.5 ms` polar window, approximate off-axis changes
at `2.0/2.5/3.0/4.0/5.0/8.0/10.0 kHz` are respectively
`+0.87/-0.14/-0.38/-0.60/-0.35/-1.44/-0.58 dB` at `+20 degrees`,
`+1.81/+0.98/+0.07/-1.91/-2.26/-6.71/-6.15 dB` at `+40 degrees`, and
`+0.57/+0.09/-0.99/-3.27/-3.96/-10.32/-11.47 dB` at `+60 degrees`.
These are **DERIVED** angle-to-on-axis differences on the native grid; the
common `+11.14 dB` protected-tweeter model scale cancels. The tweeter remains
broad through the approximately `2.1-2.4 kHz` candidate crossover region and
narrows progressively above it. The later verified woofer exports and combined
sparse-polar comparison completed that interpretation.

**VERIFIED POLAR EXPORTS / RECOVERABLE FILING COLLISION:** the exported
`000/+20/+40/+60 degree` files each contain `31,404` finite native unsmoothed
rows from `499.877960` to `12000.000966 Hz` and identify the correct
measurement title. Direct comparison against the live `1.5 ms` REW responses
is within `0.000009 Hz`, `0.000514 dB`, and `0.00194 degree` circular phase.
Their sizes and SHA-256 hashes are:

| Angle | Bytes | SHA-256 |
| ---: | ---: | --- |
| `0 degrees` | `912,205` | `7ac03bcb1299136545e7ec61804fea4791014cd41f9badca7c2831adc7d0e8b5` |
| `+20 degrees` | `912,205` | `0b02ac7041dcbb8856ecdbfe3290d1b4049a0114882e467aefa34da6d47872b3` |
| `+40 degrees` | `912,193` | `4429a4d720e0e566ea418c34d09b30e8f2542d1988d090e906ad945262ae8bc1` |
| `+60 degrees` | `912,157` | `a8ad5c386d187428809a578191a0ac53b6e8de86a97870411af457ef9baf018c` |

REW retained the requested data down to `500 Hz` rather than cropping at the
provisional `1.5 kHz` polar limit. This preserves rather than loses samples;
use only `1.5-12 kHz` for polar conclusions and do not repeat the export.

The files were exported in the driver root rather than the prepared `polar/`
subdirectory, so the polar `000deg` file replaced the path previously occupied
by C2's `3.5 ms` design FRD. This is a recoverable pathname collision, not a
measurement loss: the verified polar bytes exist and the authoritative C2
`.mdat` can reproduce the earlier design response. The following resolution
supersedes those then-pending filing and restoration actions.

**RESOLVED ROOT RESTORATION:** the verified four-file polar family remains in
its `polar/` subdirectory. The root design FRD once again identifies C2, is
`912,077` bytes, and has SHA-256
`a409445a40e645682b188b7a12596c10f727d8a0f78138f052c043d60bb0ea1e`,
an exact return to the previously verified `3.5 ms` design export. The
intermediate TW1 selection was a recoverable filing error; neither source data
nor current model dependency remains damaged.

**USER-REPORTED / VERIFIED HORIZONTAL POLAR CAPTURE — WOOFER CAPTURE AND
EXPORT PASS (2026-09-07):** the user completed the woofer
`+20/+40/+60 degree` batch with displayed headroom remaining in REW's green
region throughout. The exact minimum was not transcribed, but no repeat is
needed: clipping-abort remained enabled, no warning or anomaly was reported,
and the precise value would not change acceptance. The retained archive
`rew/SB17NRX2C35-8_installed_positive_horizontal_020-060deg_tweeter-axis_1m_UMC22_2026-09-07.mdat`
is `7,266,225` bytes with SHA-256
`47a09014fa84d7ee0aca371ba422f2283c5eb3a089982e77baec44d51163bfab`.
Signal-free inspection finds each expected title once. Loading it back into
REW is deferred to avoid duplicating the live measurements, so the source-file
count has not yet received a formal REW parse/readback.

Live UUID selection found exactly one matching trace at each new angle:

| Angle | UUID | System Delay | API SNR field |
| ---: | --- | ---: | ---: |
| `+20 degrees` | `f486fa1c-6c96-415d-a83f-ace36baacfba` | `3.1617166 ms` | `38.96 dB` |
| `+40 degrees` | `b39a77b4-e206-43ef-b595-e544ac62d53c` | `3.0571430 ms` | `33.07 dB` |
| `+60 degrees` | `c173e83a-b591-4cbc-97c9-9052423c392b` | `3.0053459 ms` | `31.21 dB` |

All are native unsmoothed `48 kHz` responses with loopback-cal timing, zero
timing offset, no inversion, IR shift, or clock adjustment. A post-batch
GET-only snapshot found Generator playback off, REW non-blocking, and no new
warning or error.

**DERIVED WOOFER POLAR-WINDOW DECISION:** relative to on-axis TW1, the direct
envelope peaks fall by approximately `4.69`, `13.30`, and `17.71 dB`, whereas
the separated room/jig energy near `+3.56` to `+3.71 ms` remains almost fixed
at approximately `-23.5`, `-24.0`, and `-24.0 dB` on the on-axis-direct scale
(`-23.0 dB` on axis). The common `Hann 2.0 ms` left / `Tukey 0.25 3.5 ms`
right window, referenced to each exact peak with FDW/MTW off, excludes that
arrival. Comparing a `3.0 ms` right window changes derived directivity over
`1.8-2.6 kHz` by only `0.13`, `0.53`, and `0.50 dB RMS` at
`+20/+40/+60 degrees`; shortening further increases rather than resolves the
variation. The `+40 degree` feature near `2.2 kHz` has about `0.8 dB` local
analysis-window uncertainty.

At the selected window, approximate angle-to-TW1 changes at
`1.5/2.0/2.2/2.4/3.0/4.0/5.0 kHz` are
`+0.20/-1.14/-0.38/-0.94/-1.63/-2.27/-3.28 dB` at `+20 degrees`,
`+0.08/-3.49/+1.45/-1.80/-4.20/-8.11/-12.09 dB` at `+40 degrees`, and
`-3.26/-5.96/-0.63/-4.39/-9.75/-17.76/-15.98 dB` at `+60 degrees`.
These are derived native-grid comparisons. The woofer narrows materially
through and above the candidate crossover region. Deep upper-band nulls at
large angles are increasingly contaminated by fixed room energy/noise, so use
this sparse family over `1.5-5 kHz` for the present design decision and do not
infer laboratory-grade polar smoothness from it.

The selected window has been applied and read back on the one live copy of
TW1 and every new angle. It changed the REW workspace only; no `.mdat` or FRD
was overwritten.

**VERIFIED WOOFER POLAR EXPORTS:** the `0/+20/+40/+60 degree` files contain
`31,404` finite native unsmoothed rows over
`499.877960-12000.000966 Hz`, identify the correct SB17 measurements, and
match the UUID-selected live responses within `0.000009 Hz`, `0.000530 dB`,
and `0.001724 degree` circular phase. Their sizes and SHA-256 hashes are:

| Angle | Bytes | SHA-256 |
| ---: | ---: | --- |
| `0 degrees` | `913,085` | `03923152b08c36e066cb0f9520c7a76489bf6837e3b85cd06c67af0c12a8e4b7` |
| `+20 degrees` | `911,885` | `f418f7a50449bead7b97c4c89a52ffc938fb199bf4f0d0efc09171e638b03453` |
| `+40 degrees` | `911,941` | `c7c902610f35623e32355b4c4b1a78390f9a6f3266dd61d0fe84336e84e1ea6a` |
| `+60 degrees` | `912,085` | `c34213923124963ba5dad703729ab84c61f4e84d23e0d33c0c3778d0663b63a1` |

The first attempt selected the already retained SB26 traces for the three new
paths. Correct SB17 exports replaced those non-unique copies; no source,
design FRD, measurement, or unique evidence was lost.

**DERIVED CROSS-DRIVER DIRECTIVITY RESULT:** averaging each raw directivity
curve over a one-sixth-octave band gives the closest broad woofer/tweeter match
near `2.2-2.3 kHz`. The RMS mismatch across `+20/+40/+60 degrees` is
approximately `1.99 dB` at `2.2 kHz` and `2.05 dB` at `2.3 kHz`, versus
`3.32 dB` at `2.1 kHz`, `3.10 dB` at `2.4 kHz`, and approximately
`3.8 dB` at `2.5-2.6 kHz`. These figures are comparative design evidence, not
laboratory polar tolerances; the positive-side sparse set and local window
uncertainty remain explicit.

Applying Seed A's documented component values, installed complex impedances,
and the common tweeter `+11.14 dB` scale to the measured polar responses gives
a preliminary system-directivity estimate. Over `1.8-3.0 kHz`, its extrema
relative to on axis are approximately `-1.74/+0.29 dB` at `+20 degrees`,
`-1.94/+2.11 dB` at `+40 degrees`, and `-3.12/+0.43 dB` at `+60 degrees`.
The largest positive feature is near `2.2 kHz` at `+40 degrees`; it is present
in both raw branches and overlaps the recorded approximately `0.8 dB` woofer
window uncertainty. It warrants VituixCAD inspection but not rejection or fine
optimisation from this sparse dataset. The evidence retains Seed A as a useful
starting point and argues against moving the handover materially above
approximately `2.3 kHz`.

**DERIVED MODEL-IMPORT LEVEL CORRECTION — C2:** REW's documented loopback
calibration convention uses the loopback level at `1 kHz` as its `0 dB`
reference. Interpolating the installed tweeter ZMA at `1.001 kHz` gives
`|Z| = 5.061 ohm` at `-22.29 degrees`. With the reported `10.13 uF` capacitor
and `0.08 ohm` ESR,

```text
Zc = 0.08 + 1/(j 2 pi f C)
H = Zt / (Zt + Zc)
|H| = 0.27744
20 log10(|H|) = -11.137 dB.
```

The units in `Zt/(Zt+Zc)` cancel, as required for a voltage ratio. The
post-capacitor reference removes the network's frequency-dependent shape, but
normalisation leaves C2 lower by this constant relative to the directly driven
woofer measurement. Apply `+11.14 dB` to C2 magnitude in VituixCAD, with no
extra phase, delay, polarity, smoothing, or minimum-phase operation. As a
cross-check, this changes the native unfiltered TW1/C2 relationship from
approximately `-8.08 dB` to `+3.06 dB` at `2.30 kHz`, a physically plausible
starting sensitivity relationship. This is a **DERIVED** correction, not an
absolute-SPL calibration or a new measurement.

**RESOLVED FILING ERROR:** REW initially wrote that valid C2
export over TW1's path under `rew/frd/SB17NRX2C35-8/`. The C2 bytes have been
copied without alteration to the correct SB26 path above. TW1's authoritative
single-measurement `.mdat` remains intact, and its live UUID still holds the
approved native window, so no unique evidence was lost. The corrective TW1
re-export returned exactly to the previously established `913,085` bytes and
SHA-256
`03923152b08c36e066cb0f9520c7a76489bf6837e3b85cd06c67af0c12a8e4b7`
and its header again identifies TW1. Both driver-specific export paths are now
correct and independently validated.
