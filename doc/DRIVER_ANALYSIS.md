# Driver Analysis and Measurement Record

**Project:** sealed passive two-way loudspeaker prototype
**Woofer:** SB Acoustics **SB17NRX2C35-8**
**Tweeter:** SB Acoustics **SB26STWGC-4**
**Record created:** 2026-08-27
**Last updated:** 2026-09-06

> - **Lifecycle:** ACTIVE DRIVER EVIDENCE AUTHORITY
> - **Owns:** evidence classes, approved driver ZMA/FRD sources, measurement conditions and quality, woofer/tweeter results and derivations, retention and procurement decisions, driver-specific modelling consequences, uncertainties, and next evidence gates
> - **Does not own:** REW/interface qualification chronology, fixture design, detailed acoustic-capture procedure, crossover-component construction, or room-placement evidence
> - **Current decision:** provisionally retain both installed drivers; C6, supported by immediate repeat C5, is approved as the installed-woofer source capture for initial crossover modelling alongside the approved ZMA baselines
> - **Next gate:** make a documented signal-free FRD export from C6 when explicitly requested, then prepare a bounded protected-tweeter measurement package
> - **Limitations:** one sample of each driver; incomplete baseline conditions; known approximately `0.5-0.6 dB` local woofer early-tail variability near `2.03 kHz`; no approved tweeter FRD, directivity, or distortion data
> - **As of:** 2026-09-06

This is the durable engineering record for the driver investigation. It supplements [README.md](../README.md). Detailed dated driver-impact history is retained in [DRIVER_ANALYSIS_CHANGELOG.md](history/DRIVER_ANALYSIS_CHANGELOG.md).

## 1. Authority, evidence, and current sources

### 1.1 Evidence labels

- **VERIFIED MEASUREMENT** — directly present in an archived measurement file or explicitly recorded instrument result.
- **DERIVED** — calculated from stated measured or published inputs and retained equations.
- **PUBLISHED** — manufacturer specification or manufacturer technical guidance.
- **EXTERNAL RESEARCH** — relevant non-manufacturer technical literature.
- **USER-REPORTED** — a configuration, condition, or observation reported by the user but not independently encoded in an archived measurement.
- **USER-CONFIRMED CONFIGURATION** — a user-confirmed setting or connection state used to interpret evidence.
- **INFERRED** — a physically plausible interpretation requiring assumptions that have not been measured.
- **PROVISIONAL DECISION** — a present engineering direction subject to stated test gates.
- **OPEN ITEM** — measurement, decision, or archival work still outstanding.
- **HISTORICAL EVIDENCE** — retained evidence whose conclusion or procedure has been superseded.

### 1.2 Approved impedance sources

The only current driver-impedance baselines approved for crossover modelling are:

- Woofer: [`rew/SB17NRX2C35-8 installed.zma`](../rew/SB17NRX2C35-8%20installed.zma)
- Tweeter: [`rew/SB26STWGC-4 installed.zma`](../rew/SB26STWGC-4%20installed.zma)

Both drivers were correctly mounted in the sealed prototype enclosure in their normal mechanical configuration, without temporary sealing putty. The woofer baseline was taken immediately after installation and before deliberate run-in. The matched-rate post-conditioning trace remains comparison evidence only because its approximately 0.342 ohm broadband series-resistance offset prevents promotion to the cooled modelling baseline.

### 1.3 Approved acoustic sources and current capture state

C6 is the approved installed-woofer source capture for initial crossover design,
with C5 as its immediate repeatability witness. No durable FRD export has yet
been made, and no tweeter acoustic source is approved. This is a prototype-
design release with stated uncertainty, not a frozen production response.

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
[`rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_2026-09-06.mdat`](../rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_2026-09-06.mdat),
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
| C4 | [`rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C4_2026-09-06.mdat`](../rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C4_2026-09-06.mdat) | `2,428,186` | `6e53eaba36039769075544f0cde4d286db155e5429df4cfa4d536a12419b6052` |
| C5 | [`rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C5_2026-09-06.mdat`](../rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C5_2026-09-06.mdat) | `2,428,186` | `7d1c45bcf2d58c5582f53db679bf7b0febd32c15c2bd2086d82a076b4ad10c1b` |
| C6 | [`rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C6_2026-09-06.mdat`](../rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_C6_2026-09-06.mdat) | `2,428,186` | `6c9a4223073ac9bd52ec7b7ff2dd6e0106f36cd40b9511c0df77a80eeb686ca0` |

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
approved current installed-woofer source capture for initial crossover
modelling, with immediate C5 as its repeatability witness and C4 retained as an
uncertainty bound.

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
[`rew/SB17NRX2C35-8_UMC22_C3_no_output_diagnostic_2026-09-06.mdat`](../rew/SB17NRX2C35-8_UMC22_C3_no_output_diagnostic_2026-09-06.mdat)
is `2,428,201` bytes with SHA-256
`e60bd9e0643a37d70f2162a8f8aa24214bceb7b2341a17c79198219374d318e2`.
Its retained measurement is named `DIAG-C3-no-output-260906`; it is excluded
from the C1/C2 production authority.

The current user-reported physical/no-signal state and API-assisted audit are
recorded in the current [UMC22 installed-woofer FRD
runbook](rew/procedures/UMC22_INSTALLED_WOOFER_FRD.md). That authority keeps
the signal stopped while the next bounded measurement package is prepared; no
further unchanged woofer repeatability sweep is required.
Qualification evidence and its generic microphone/absolute-SPL limitations are
in [UMC22 FRD
qualification](rew/qualification/UMC22_FRD_QUALIFICATION.md).

### 1.4 Current driver state

- Only one woofer and one tweeter are presently available.
- The prototype's geometric net volume is approximately 21.7 L before damping-material effective-volume change.
- The cooled pre-conditioning woofer baseline has one clean sealed-box resonance at approximately 67.0 Hz and no separate resonance near 83 Hz.
- The matched 48 kHz post-conditioning trace moves the resonance to approximately 65.71 Hz, a 1.88% decrease, but still awaits a fully cooled confirmation.
- The woofer's installed total system Q is approximately 0.81–0.82 and remains manageable for development.
- The tweeter's installed impedance agrees closely with published parameters and has no suspicious additional resonance.
- Both drivers remain provisionally retained.
- The intended approximately 2.2–2.4 kHz LR4-like acoustic region remains provisional pending installed magnitude, common timing/phase, directivity, and distortion evidence.
- The UMC22 route is qualified only for controlled installed-woofer FRD at this stage. Raw-tweeter and polar work require their own protection/procedure gates.

### 1.5 Project file-location convention

- `rew/` — REW measurements and exports, including `.mdat`, `.zma`, tab-delimited impedance exports, and FRD exports.
- `vituixcad/` — VituixCAD projects and VituixCAD-generated outputs.

## 2. Current impedance-measurement data

### 2.1 File metadata

**VERIFIED FROM BOTH FILE HEADERS**

| Field | Value |
|---|---|
| REW version | 5.40 beta 133 |
| Measurement date | 2026-08-30 |
| Sweep | 1M logarithmic swept sine, one sweep, -12 dBFS |
| Sample rate | 48 kHz |
| Sense resistor | 100.0 ohm |
| Entered lead resistance | 0.000 ohm |
| Input resistance | 20 kohm |
| Calibration factor | 0.9783 |
| Smoothing / spacing | none / 1/96 octave |
| Point count | 1,276 per file |
| Recorded span | 2.211 Hz to 22.013 kHz |

The woofer was measured at 09:30:58 and the tweeter at 10:00:22. The headers do not record driver-terminal voltage, enclosure fill state, ambient temperature, or screw torque. Those conditions should be recorded with future comparison measurements.

### 2.2 Data quality and usable range

Both files are valid, densely sampled ZMA exports with frequency, impedance magnitude, and phase. Their traces are smooth and physically coherent through the resonances and crossover region.

**VERIFIED MEASUREMENT:** points below approximately **8-10 Hz** are measurement artifacts. They fall below credible voice-coil resistance and must not be used to estimate DCR, Q, or low-frequency load. This does not affect crossover modelling or the sealed-box result around 67 Hz.

### 2.3 Reproducible impedance-peak calculation

The fitted Q values below use a curve-consistent baseline resistance, $R_0$, estimated from the real part of impedance at 10 Hz:

$$
R_0=|Z|\cos\phi.
$$

For a single dominant impedance resonance, define the bandwidth level and crossing frequencies by

$$
Z_{th}=\sqrt{R_0Z_{max}},
$$

with $f_1$ and $f_2$ at the rising and falling crossings of that magnitude. Log-frequency interpolation between adjacent measured points is used. Then

$$
f_0=\sqrt{f_1f_2},
$$

$$
Q_m=\frac{f_0}{f_2-f_1}\sqrt{\frac{Z_{max}}{R_0}},
\qquad
Q_e=\frac{Q_m}{Z_{max}/R_0-1},
\qquad
Q_t=\frac{Q_m}{Z_{max}/R_0}.
$$

For the installed woofer these are box-system quantities $Q_{mc}$, $Q_{ec}$, and $Q_{tc}$. For the tweeter, whose own rear chamber defines its mechanical system, they are reported conventionally as $Q_{ms}$, $Q_{es}$, and $Q_{ts}$. They are approximate equivalent-circuit fits, not independent direct measurements of every loss mechanism.

## 3. Woofer published reference data

### 3.1 Manufacturer specifications

**PUBLISHED - SB Acoustics SB17NRX2C35-8 datasheet**

| Parameter | Published value |
|---|---:|
| Nominal impedance | 8 ohm |
| DC resistance, $R_e$ | 5.7 ohm |
| Voice-coil inductance, $L_e$ | 0.15 mH |
| Effective diaphragm area, $S_d$ | 118 cm2 |
| Free-air resonance, $F_s$ | 36.5 Hz |
| Sensitivity | 87 dB at 2.83 V/1 m |
| $Q_{ms}$ | 4.55 |
| $Q_{es}$ | 0.47 |
| $Q_{ts}$ | 0.42 |
| Moving mass, $M_{ms}$ | 13.9 g |
| Force factor, $Bl$ | 6.25 T m |
| Equivalent compliance volume, $V_{as}$ | 27 L |
| Suspension compliance, $C_{ms}$ | 1.37 mm/N |
| Mechanical resistance, $R_{ms}$ | 0.7 kg/s |
| Linear excursion, $X_{max}$ | +/-5.5 mm |
| Rated power | 50 W |

### 3.2 Published-parameter enclosure prediction

Using the published $F_s=36.5$ Hz, $Q_{ts}=0.42$, $V_{as}=27$ L, and the approximately 21.7 L geometric net volume gives:

- **DERIVED:** $F_c\approx54.7$ Hz;
- **DERIVED:** $Q_{tc}\approx0.63$;
- **DERIVED:** ideal anechoic small-signal $F_3\approx62.3$ Hz;
- no response peak from the nominal second-order sealed alignment.

These remain a record of the datasheet-based design case, not a description of the completed prototype.

## 4. Woofer installed measurement

### 4.1 Principal measured features

**VERIFIED MEASUREMENT / DERIVED FROM CURRENT ZMA**

| Quantity | Result |
|---|---:|
| Curve-consistent $R_0$ estimate | 5.645 ohm |
| Impedance magnitude maximum | 96.544 ohm at 67.272 Hz |
| Bandwidth threshold, $Z_{th}$ | 23.345 ohm |
| Lower threshold crossing, $f_1$ | 57.811 Hz |
| Upper threshold crossing, $f_2$ | 77.583 Hz |
| Derived sealed-system resonance, $F_c$ | 66.971 Hz |
| $Q_{mc}$ | 14.008 |
| $Q_{ec}$ | 0.870 |
| $Q_{tc}$ | 0.819 |
| Positive phase maximum | +61.79 degrees at 57.81 Hz |
| Negative phase minimum | -63.54 degrees at 77.16 Hz |

The impedance maximum is a magnitude in **ohms**, not an inductance. Its height mainly reflects motional back-EMF and the balance of mechanical and electrical damping. High impedance at resonance is not an amplifier-current hazard.

The close agreement between the curve-derived $R_0\approx5.645$ ohm and the published $R_e=5.7$ ohm is reassuring. A nulled cold-DCR measurement taken with this setup would still be preferable when an exact series-resistance model is required.

### 4.2 The secondary-resonance question

**VERIFIED MEASUREMENT:** the correctly installed woofer trace has one low-frequency resonance only. At **82.94 Hz**, the impedance is **16.46 ohm at -61.06 degrees**, lying smoothly on the falling side of the 67 Hz peak. There is no local maximum or phase reversal there.

This is strong evidence that a distinct feature near 83 Hz is not inherent to the normally installed driver/enclosure system. The ordinary mounting has eliminated the leak-related mode without needing temporary sealing compound.

### 4.3 Idealized low-frequency consequence

For a normalized second-order sealed high-pass response,

$$
|H(x)|^2=\frac{x^4}{(1-x^2)^2+x^2/Q_{tc}^2},
\qquad x=\frac{f}{F_c}.
$$

Using the measured $F_c=66.97$ Hz and derived $Q_{tc}=0.819$:

- **DERIVED:** ideal anechoic small-signal $F_3\approx59.0$ Hz;
- **DERIVED:** a modest maximum of approximately **+0.29 dB near 133 Hz**;
- $F_3$ lies below $F_c$, as expected because $Q_{tc}>0.707$.

The apparently similar or slightly lower $F_3$ than the published-parameter design case does not mean equal deep-bass behaviour. With both responses normalized at high frequency, the idealized installed alignment differs approximately as follows:

| Frequency | Installed minus published-parameter case |
|---:|---:|
| 30 Hz | -2.28 dB |
| 40 Hz | -1.32 dB |
| 50 Hz | -0.33 dB |
| 80 Hz | +1.11 dB |
| 100 Hz | +1.08 dB |
| 150 Hz | +0.64 dB |

Physical interpretation: relative to the nominal design calculation, this state trades some output below roughly 50 Hz for a mild broad lift through the upper bass. The predicted lift is small enough to remain quite plausible for the intended prototype, but room placement and the eventual woofer-series resistance will matter.

These response figures are **DERIVED**, not acoustic measurements. They assume that the installed system is adequately represented by a linear second-order sealed model. Leakage, damping material, baffle step, room gain, crossover resistance, excursion, and thermal effects are not included.

### 4.4 Crossover-region impedance

**VERIFIED FROM CURRENT ZMA**

| Frequency | \|Z\| | Phase |
|---:|---:|---:|
| 2199.83 Hz | 7.9687 ohm | +10.425 degrees |
| 2297.23 Hz | 7.9767 ohm | +10.753 degrees |
| 2398.93 Hz | 8.0119 ohm | +11.068 degrees |
| 2505.14 Hz | 8.0403 ohm | +11.499 degrees |

The woofer is close to 8 ohm in magnitude around the intended crossover, but it is not an 8 ohm resistor. At 2297 Hz its rectangular equivalent is approximately $7.84+j1.49$ ohm. The full ZMA should therefore be used in VituixCAD.

There is no strong electrical anomaly in the 2.2-2.5 kHz region. Small higher-frequency impedance structure cannot establish cone-breakup amplitude or acoustic suitability; the installed FRD and distortion measurements remain decisive.

### 4.5 Woofer judgement

**PROVISIONAL DECISION:** retain the SB17NRX2C35-8 in the present enclosure.

The measured $Q_{tc}\approx0.82$ sits inside the project's broadly manageable **0.75-0.95** development range. The alignment is warmer than the published-parameter design case but is not severely resonant. No additional low-frequency mode survives normal installation, and the impedance near the intended crossover is smooth and convenient to model.

This does not yet establish acoustic smoothness, maximum output, distortion, compression, or suitability for pair matching.

### 4.6 Conditioning calculation and superseded operating note

**USER-REPORTED TEST CONDITION — 2026-08-31:** the installed woofer was driven with a 45 Hz sine wave at 3.44 V RMS measured at its terminals.

**DERIVED FROM THE CURRENT INSTALLED ZMA:** near 45 Hz the load is approximately 10.42 ohm at +50.6 degrees, corresponding to approximately 0.330 A RMS, 1.14 VA apparent power, and 0.72 W real electrical input. The nominal-resistor shorthand $V^2/8=1.48\ \mathrm{W}$ does not describe this reactive, frequency-dependent load.

Using the measured complex impedance with published $R_e=5.7\ \mathrm{ohm}$, $L_e=0.15\ \mathrm{mH}$, and $Bl=6.25\ \mathrm{T\,m}$ gives an **estimated** diaphragm travel of approximately 2.13 mm peak (4.27 mm peak-to-peak). The later 30 Hz, 4.0 V RMS development point predicts approximately 0.565 A RMS, 1.9 W real input, and 2.6 mm peak travel, about 47% of published $X_{max}$. These are linear equivalent-circuit estimates, not displacement measurements.

The former operating steps are superseded by [DRIVER_RUNIN.md](DRIVER_RUNIN.md), which owns the bounded procedure, cold-DCR cooldown gate, fixed 48 kHz calibration, rested confirmation, safety stops, and measurement-based stopping rule.

### 4.7 2026-08-31 matched 48 kHz post-conditioning comparison

**USER-CLARIFIED MEASUREMENT HISTORY:** [`rew/SB17NRX2C35-8 installed.zma`](../rew/SB17NRX2C35-8%20installed.zma) was measured immediately after installation, before any deliberate run-in. [`rew/SB17NRX2C35-8 runin 30Hz 4Vrms 1h 48kHz.zma`](../rew/SB17NRX2C35-8%20runin%2030Hz%204Vrms%201h%2048kHz.zma) followed some intervening programme-material use and then one hour of 30 Hz conditioning at 4 V RMS. The comparison therefore shows the net change across both activities; it cannot assign the change uniquely to the final sine-wave hour.

**VERIFIED MEASUREMENT / DERIVED:** both traces use a 48 kHz sample rate and otherwise matched REW impedance settings. The bandwidth-derived sealed-system resonance changed from **66.9712 Hz** to **65.7115 Hz**, a change of **-1.2597 Hz (-1.881%)**. Interpreted as a stiffness/compliance change at effectively constant moving mass, this corresponds to approximately **+3.87% total system compliance**.

The raw impedance maximum changed only from approximately **96.54 ohm** to **96.85 ohm**, while the post-run trace contains approximately **+0.342 ohm** of nearly frequency-independent real series resistance from 300 Hz to 10 kHz and essentially unchanged reactance there. If that offset were entirely voice-coil copper resistance, it would correspond to roughly a **15 °C** temperature rise; changed lead or contact resistance could contribute instead. Subtracting the series offset gives a post-run peak of approximately **96.50 ohm**, $Q_{mc}\approx13.8$, $Q_{ec}\approx0.86$, and $Q_{tc}\approx0.81$. There is therefore no persuasive evidence of a durable resonance-peak or damping change in this pair of files.

**INFERRED:** combining the pre-run free-air estimate $F_s\approx54.22\ \mathrm{Hz}$, the fixed-box stiffness contribution derived from the earlier installed measurement, and the new $F_c$ gives an effective post-conditioning free-air resonance of approximately **52.66 Hz**. That is approximately **2.9% below** the pre-run estimate and implies approximately **6.0% greater driver compliance**, but it remains roughly **44% above** the published 36.5 Hz value. This is an indirect estimate, not a current free-air measurement.

**PROVISIONAL DECISION:** treat the downward resonance-frequency movement as encouraging, but retain the original cooled installed ZMA as the crossover baseline. Repeat the post-run measurement only after the cold-DCR and matched-condition gates in [DRIVER_RUNIN.md](DRIVER_RUNIN.md) have been met.

## 5. Tweeter published reference data

### 5.1 Manufacturer specifications

**PUBLISHED - SB Acoustics SB26STWGC-4 datasheet**

| Parameter | Published value |
|---|---:|
| Nominal impedance | 4 ohm |
| DC resistance, $R_e$ | 3.2 ohm |
| Voice-coil inductance, $L_e$ | 0.04 mH |
| Effective diaphragm area, $S_d$ | 6.2 cm2 |
| Resonance, $F_s$ | 780 Hz |
| Sensitivity | 93 dB at 2.83 V/1 m |
| $Q_{ms}$ | 2.8 |
| $Q_{es}$ | 2.1 |
| $Q_{ts}$ | 1.2 |
| Force factor, $Bl$ | 1.6 T m |
| Moving mass, $M_{ms}$ | 0.3 g |
| Linear excursion, $X_{max}$ | +/-0.6 mm |
| Rated power statement | 120 W with the manufacturer's stated 2.6 kHz, 12 dB/octave Butterworth high-pass condition |

The 120 W figure is conditional, not an unconditional broadband power rating.

## 6. Tweeter installed measurement

### 6.1 Principal measured features

**VERIFIED MEASUREMENT / DERIVED FROM CURRENT ZMA**

| Quantity | Installed result | Published |
|---|---:|---:|
| Curve-consistent $R_0$ estimate | 3.274 ohm | $R_e=3.2$ ohm |
| Impedance magnitude maximum | 7.557 ohm at 755.62 Hz | not stated |
| Bandwidth-derived $F_s$ | 760.91 Hz | 780 Hz |
| $Q_{ms}$ | 2.622 | 2.8 |
| $Q_{es}$ | 2.005 | 2.1 |
| $Q_{ts}$ | 1.136 | 1.2 |
| Positive phase maximum | +24.04 degrees at 574.31 Hz | not stated |
| Negative phase minimum | -22.32 degrees at 979.91 Hz | not stated |

The fitted resonance is approximately **2.4% below** the published value; the fitted Q values are within approximately **5-6%**. This is close agreement for a real installed sample and shows no electrical reason to doubt the tweeter.

The magnitude maximum occurs a few hertz below the bandwidth-derived resonance because the rising voice-coil impedance and the discrete frequency samples make the magnitude-peak and ideal phase-centre definitions slightly different. Reporting the result as approximately **761 Hz** is appropriately precise.

### 6.2 Crossover-region impedance

**VERIFIED FROM CURRENT ZMA**

| Frequency | \|Z\| | Phase |
|---:|---:|---:|
| 2199.83 Hz | 3.4884 ohm | -5.699 degrees |
| 2297.23 Hz | 3.4768 ohm | -5.032 degrees |
| 2398.93 Hz | 3.4786 ohm | -4.445 degrees |
| 2505.14 Hz | 3.4787 ohm | -3.725 degrees |

Around the intended crossover the tweeter is approximately **3.48 ohm**, nearly resistive but mildly capacitive. At 2297 Hz its rectangular equivalent is approximately $3.46-j0.30$ ohm. It must not be modelled as a frequency-independent 4 ohm resistor.

There are no suspicious secondary impedance peaks. The normal installed mounting has not introduced an evident rear-cavity or front-cavity electrical resonance.

### 6.3 Tweeter judgement

**PROVISIONAL DECISION:** retain the SB26STWGC-4.

The intended 2.2-2.4 kHz crossover is approximately three times the measured resonance frequency. That is a plausible region for a steep **acoustic** fourth-order high-pass, but the ratio alone does not prove protection or correct summation. Installed-baffle acoustic response, phase, distortion, level testing, and the complete filtered transfer function remain required.

No dedicated tweeter run-in is presently justified. Use the baseline and protected-use procedure in [DRIVER_RUNIN.md](DRIVER_RUNIN.md); never apply an unfiltered conditioning signal directly to the bare tweeter.

## 7. Driver-specific modelling consequences

### 7.1 Current VituixCAD impedance inputs

Use only:

- `rew/SB17NRX2C35-8 installed.zma` for the woofer;
- `rew/SB26STWGC-4 installed.zma` for the tweeter.

The useful loads near 2.30 kHz are approximately 7.98 ohm at +10.8 degrees for the woofer and 3.48 ohm at -5.0 degrees for the tweeter. The full complex ZMA, not those spot values or nominal impedances, belongs in VituixCAD.

The post-conditioning woofer file remains comparison evidence until a cooled repeat confirms resonance position and broadband resistance. No two-driver acoustic optimisation is defensible until the approved C6 woofer source is exported and a protected common-timing tweeter FRD exists.

### 7.2 Consequences for crossover decisions

- Treat approximately 2.2–2.4 kHz LR4-like acoustic slopes as a hypothesis, not a locked electrical network.
- Include each driver's natural acoustic response, complex impedance, physical offset, baffle effects, component DCR, and tolerances.
- Do not infer cone-breakup control, tweeter protection, directivity, or summation from impedance alone.
- Use [CROSSOVER_DESIGN.md](CROSSOVER_DESIGN.md) for the active topology, polarity, validation loop, and system-load gates.
- Use [CROSSOVER_COMPONENT_DEVELOPMENT.md](CROSSOVER_COMPONENT_DEVELOPMENT.md) only when component procurement, winding, PCB, or construction detail is relevant.

## 8. Procurement and pair-matching decision

**PROVISIONAL DECISION:** continue with the present driver pair and enclosure. Delay purchase of the second-channel drivers until the prototype has passed the acoustic-response, distortion, crossover-feasibility, and final-load gates.

If the prototype passes:

- buy another SB17NRX2C35-8 and SB26STWGC-4;
- condition and measure them under the same documented conditions;
- compare installed resonance/Q, crossover-region impedance, acoustic response, and distortion;
- establish acceptable pair tolerances before freezing the stereo build.

Matching complete installed behaviour matters more than reproducing every datasheet value exactly.

## 9. Open items and priorities

### 9.1 Next driver evidence gates

1. Preserve the verified C1/C2/C3R production archive, the separate C4/C5/C6 UUID-selected archives, and the separate failed-C3 diagnostic under the [current UMC22 runbook](rew/procedures/UMC22_INSTALLED_WOOFER_FRD.md).
2. When explicitly requested, make a documented signal-free FRD export from C6, retaining its native common-timing phase, `Hann` `2.0 ms` left / `Tukey 0.25` `3.5 ms` right window, no smoothing, and `500 Hz-12 kHz` validity limit.
3. Close the open window before the next acoustic package and record that room-boundary state once. Do not repeat settings confirmations within an unchanged bounded package.
4. Complete the bounded conditioning/cooldown loop in [DRIVER_RUNIN.md](DRIVER_RUNIN.md), then promote a reproducible cooled 48 kHz woofer ZMA only if its resistance and conditions pass.
5. Record enclosure fill/lining, ambient temperature, driver-terminal voltage, mounting, and calibration conditions with replacement evidence.
6. Prepare a bounded protected-tweeter common-timing measurement package, then acquire the minimum on-axis and horizontal off-axis data needed for crossover/directivity design.
7. Validate the filtered drivers, acoustic sum, reverse-polarity null, and final impedance/EPDR after crossover construction.

### 9.2 Remaining driver uncertainties

- Durable phase-bearing C6 woofer FRD export; installed tweeter magnitude/phase;
  and useful directivity data for both drivers.
- Woofer and tweeter distortion/compression at required listening levels.
- Final damping's effect on the sealed alignment and the woofer-series inductor DCR's effect on $Q_{tc}$.
- Reproducibility of the cooled woofer impedance after conditioning.
- Generic rather than unit-specific ECM8000 magnitude calibration and lack of absolute-SPL calibration.
- Raw-tweeter protection and polar-measurement release.
- Production spread and stereo-pair matching.
- Individual free-air T/S parameters, if later needed to explain rather than directly model the installed alignment.

## 10. Sources and related authorities

### 10.1 Current project measurements

- [`rew/SB17NRX2C35-8 installed.zma`](../rew/SB17NRX2C35-8%20installed.zma)
- [`rew/SB17NRX2C35-8 runin 30Hz 4Vrms 1h 48kHz.zma`](../rew/SB17NRX2C35-8%20runin%2030Hz%204Vrms%201h%2048kHz.zma) — comparison evidence; not the crossover baseline
- [`rew/SB26STWGC-4 installed.zma`](../rew/SB26STWGC-4%20installed.zma)

### 10.2 Primary sources

- [SB17NRX2C35-8 datasheet](https://sbacoustics.com/wp-content/uploads/2020/02/6in-SB17NRX2C35-8.pdf)
- [SB26STWGC-4 product page](https://sbacoustics.com/product/sb26stwgc-4-fabric/)
- [SB26STWGC-4 datasheet](https://sbacoustics.com/wp-content/uploads/2020/05/SB26STWGC-4.pdf)
- [Klippel, *Mechanical Fatigue and Load-Induced Aging of Loudspeaker Suspension*](https://www.klippel.de/fileadmin/klippel/Bilder/Know-How/Literature/Papers/Aging%20of%20loudspeaker%20suspension_Klippel.pdf)
- [REW impedance-measurement documentation](https://www.roomeqwizard.com/help/help_en-GB/html/impedancemeasurement.html)

### 10.3 Procedures and qualification evidence

- [Woofer conditioning and impedance procedure](DRIVER_RUNIN.md)
- [Installed acoustic-response method](rew/FRD_MEASUREMENT_METHOD.md)
- [Current UMC22 installed-woofer runbook](rew/procedures/UMC22_INSTALLED_WOOFER_FRD.md)
- [UMC22 qualification evidence](rew/qualification/UMC22_FRD_QUALIFICATION.md)
- [UMC202HD desktop-dropout diagnosis](rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md)
- [Driver-impact change history](history/DRIVER_ANALYSIS_CHANGELOG.md)

## 11. Change history

The active file intentionally excludes interface/UI/fixture chronology. Read [DRIVER_ANALYSIS_CHANGELOG.md](history/DRIVER_ANALYSIS_CHANGELOG.md) for driver-impact changes and supersession rationale; use the linked REW qualification/history records only when auditing the measurement route.
