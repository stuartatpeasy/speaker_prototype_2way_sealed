# Seed A Full-System Level and Thermal Qualification — 2026-09-10

| State | Value |
| --- | --- |
| Lifecycle | **QUALIFICATION EVIDENCE — BOUNDED PASS WITH DEFERRED HOT-ACOUSTIC CHECK** |
| Owns | Retained file identity, trace identities, user-reported conditions, sampled distortion, compression comparison, component-surface temperatures, exclusions, and the resulting prototype decision |
| Does not own | Routine operation, absolute-SPL calibration, driver voice-coil temperature, long-term power rating, final crossover freeze, or speaker-two results |
| Read when | Auditing Seed A's level/distortion/thermal evidence, planning matched speaker-two checks, or investigating an anomaly |
| Current conclusion | Nominal `0.5/1/2/4 V RMS` level and sampled-distortion gates pass; the external R(Tser)/L(W1) surface-thermal gate passes; the wrong-angle post-thermal trace is excluded |
| Next gate | Build and test speaker two, including a correct immediate hot `0-degree` sweep and confirmation of the narrow high-level feature near `2.18 kHz`; retest speaker one only if an anomaly appears |
| Last reviewed | 2026-09-10 |

## 1. Retained evidence and scope

The REW package is retained as:

| Artefact | Size | SHA-256 |
| --- | ---: | --- |
| [`rew/SPK_Seed_A_full_system_level_thermal_20260910.mdat`](../../../rew/SPK_Seed_A_full_system_level_thermal_20260910.mdat) | `12,134,881 bytes` | `c4830990a616e85f08ce2a45b95408966b0b22736937506e8b9848057ca15c8b` |

**VERIFIED FROM RETAINED MDAT:** REW `V5.40 beta 133`, `48 kHz`,
approximately `9.888 Hz-19.9999 kHz`, and loopback timing were retained.
The four valid complete-system, `0-degree`, `1 m`, tweeter-axis traces are:

| Nominal level | Exact REW name | UUID | Stored SNR | System delay |
| ---: | --- | --- | ---: | ---: |
| `0.5 V RMS` | `SPK_sA_full_000deg_t-axis_1m_U22_0.5V_202610` | `f91c0707-e38b-4b31-815d-7fe78cfcae28` | `43.20 dB` | `3.0389 ms` |
| `1.0 V RMS` | `SPK_sA_full_000deg_t-axis_1m_U22_1.0V_202610` | `36c2a327-0dc2-4384-b6e8-4d2229b33822` | `48.96 dB` | `3.0379 ms` |
| `2.0 V RMS` | `SPK_sA_full_000deg_t-axis_1m_U22_2.0V_202610` | `a92d7ad9-115f-44ac-a182-dbe7b0969f03` | `54.39 dB` | `3.0373 ms` |
| `4.0 V RMS` | `SPK_sA_full_000deg_t-axis_1m_U22_4.0V_202610` | `45d7476a-2210-4e4e-b827-63df0fc65be5` | `59.20 dB` | `3.0374 ms` |

The shorter names are exact; REW rejected the longer proposed names. The
unusual `202610` suffix is therefore preserved rather than silently corrected.

The retained package also contains a measurement named `test`. The user
identified it as unrelated live-session material, so it is excluded from this
qualification and from every Seed A comparison; its presence is not a fifth
level trace or a passed gate.

**USER-REPORTED CONDITIONS:** minimum microphone-channel headroom was
`27.9 dB` at nominal `0.5 V RMS`; reference-channel headroom was `33.4 dB`.
All four sweeps completed, the user did not stop for loudness, and there was no
warning, clipping, distortion, dropout, impure tone, audible change, or other
anomaly during any part of the package. The final user-reported state was
safe: all signals stopped, SU-V570 off at minimum volume, speaker restored to
`0 degrees`, both meters still connected as described, wiring otherwise
unchanged, and no anomaly.

The U1282A indications were approximately `0.51`, `1.02`, `2.1`, and
`3.9 V AC` for the four nominal levels. These are explicitly approximate
averages of unsteady readings, and the meter appeared to respond differently
to pink noise and the steady `1 kHz` setting tone. They verify that each level
was within `10%` of target, but they are not exact amplitude calibration.

## 2. Compression comparison

**DERIVED FROM RETAINED FUNDAMENTALS:** traces were compared on a common
`96-point-per-octave` grid using `1/12`-octave smoothing. Over
`200 Hz-10 kHz`, the mean gains relative to the `0.5 V` trace were:

| Pair | Measured mean gain | Ideal nominal gain | Mean residual |
| --- | ---: | ---: | ---: |
| `1/0.5 V` | `6.090 dB` | `6.021 dB` | `+0.069 dB` |
| `2/0.5 V` | `12.197 dB` | `12.041 dB` | `+0.156 dB` |
| `4/0.5 V` | `17.918 dB` | `18.062 dB` | `-0.144 dB` |
| `4/2 V` | `5.721 dB` | `6.021 dB` | `-0.300 dB` |

Using the approximate meter readings instead gives mean residuals of
`+0.069`, `-0.096`, `+0.248`, and `+0.344 dB`, respectively. Because
those readings were not steady, this alternative does not establish greater
accuracy; it shows that either reasonable normalisation supports the same
bounded conclusion.

**COMPRESSION DECISION — BROAD GATE PASSED:** no comparison demonstrates a
broad loss greater than `0.5 dB` over `200 Hz-10 kHz`. After fitting out each
pair's mean gain, the `4 V` versus `2 V` comparison reaches a narrow
approximately `-1.28 dB` difference at `2.175 kHz`, with values beyond
`1 dB` confined to about `2.129-2.207 kHz`. At `1/6`-octave smoothing the
maximum falls to about `-0.83 dB`. This triggers the procedure's narrow
crossover-region review threshold, but is not a broad compression failure.
Confirm whether it repeats on speaker two before changing Seed A.

## 3. Sampled distortion result

**VERIFIED VIA REW'S DISTORTION DATA / DERIVED GATE:** the official REW
distortion-data endpoint
`GET /measurements/{uuid}/distortion?unit=percent` was sampled at these 30
approximately third-octave frequencies in hertz: `20, 25, 31.5, 40, 50, 63,
80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600,
2000, 2500, 3150, 4000, 5000, 6300, 8000, 10000, 12500, 16000`. The maxima
relevant to the retained traces were:

| Nominal level | Maximum sampled THD | Maximum sampled H3 or higher |
| ---: | --- | --- |
| `0.5 V RMS` | `1.84%` at `125 Hz` | H3 `0.142%` at `630 Hz` |
| `1.0 V RMS` | `0.968%` at `125 Hz` | H3 `0.066%` at `400 Hz` |
| `2.0 V RMS` | `1.69%` at `4.00 kHz` | H3 `0.842%` at `630 Hz` |
| `4.0 V RMS` | `2.17%` at `125 Hz` | H3 `0.901%` at `3.15 kHz` |

No sampled THD exceeds `3%` from `100 Hz-10 kHz`, and no sampled third-or-
higher harmonic exceeds `1%` from `200 Hz-10 kHz`. Together with the user's
clean audible report and absence of warnings, this passes the bounded
distortion gate. It is sampled evidence rather than a continuous-frequency
proof, and below `100 Hz` remains excursion/room evidence under the procedure.

## 4. Thermal exposure

**USER-REPORTED CONTACT TEMPERATURES:** the nominal `2.000 V RMS` CTA-2034
pink-periodic-noise exposure ran for the full `15 minutes`. Ambient remained
`20.4 degrees C`; no audible change, warning, clipping, dropout, protection
event, or other anomaly occurred.

| Time | Ambient | R(Tser) surface | L(W1) surface |
| ---: | ---: | ---: | ---: |
| `0 min` | `20.4 degrees C` | `20.4 degrees C` | `20.4 degrees C` |
| `2 min` | `20.4 degrees C` | `20.5 degrees C` | `20.5 degrees C` |
| `5 min` | `20.4 degrees C` | `20.6 degrees C` | `20.5 degrees C` |
| `10 min` | `20.4 degrees C` | `20.8 degrees C` | `20.6 degrees C` |
| `15 min` | `20.4 degrees C` | `20.8 degrees C` | `20.6 degrees C` |

Thus R(Tser) rose `0.4 degrees C`, L(W1) rose `0.2 degrees C`, and neither
rose during the final five minutes. Both remain far below the procedure's
`50 degrees C` direct-pass ceiling, `20 degrees C` total-rise ceiling, and
`2 degrees C` final-five-minute rise ceiling.

**THERMAL DECISION — EXTERNAL-SURFACE GATE PASSED:** this is strong direct
evidence for the exposed prototype components under the bounded programme-like
test. It is not an internal winding, resistor hot-spot, driver voice-coil, final
enclosed-mounting, or continuous-power rating.

The user's `2^2/3 = 1.33 W` calculation is a conservative resistive
illustration using an assumed `3 ohm` minimum. With Seed A's measured
`4.366 ohm` minimum magnitude, `2^2/4.366 = 0.916` is a tighter upper bound
in watts on real power for an exact `2 V RMS` signal over the measured band.
The actual broadband real power depends on the signal spectrum and
frequency-dependent complex impedance, and the noise-voltage reading was
approximate; neither illustration is a calibrated input-power measurement.

## 5. Invalid post-thermal trace and decision

The retained MDAT includes
`SPK_sA_full_000deg_t-axis_1m_U22_PT_20260910`, but the user subsequently
reported that the loudspeaker was at `60 degrees` to the microphone during
that sweep. The stored name therefore does not describe the actual geometry.

**EXCLUSION:** do not use this trace as an immediate hot `0-degree`
comparison, do not relabel it as valid, and do not reuse it as intentional
off-axis evidence. It is retained only because it is embedded in the
authoritative MDAT and documents why the planned comparison is absent.

**USER-AUTHORISED PROPORTIONATE DECISION:** do not repeat the post-thermal
sweep on speaker one now. The low observed component-temperature rise, clean
15-minute exposure, clean complete level series, and modest bounded input
justify deferral. When speaker two is built, perform the correct immediate hot
`0-degree` comparison and inspect the narrow high-level crossover-region
feature. Retest speaker one only if speaker two produces an anomaly.

This means the hot-acoustic recovery check is **deferred, not passed**. The
level/distortion and external-component surface-thermal gates pass
proportionately, so no further signal is presently justified on speaker one.

## 6. Limitations

- Only one completed loudspeaker and one room position were tested.
- The ECM8000 has generic response calibration, not serial-specific absolute
  SPL calibration.
- Sweep-voltage readings were approximate averages of an unsteady display.
- Distortion was assessed at 30 selected frequencies rather than as a
  continuous-band maximum.
- Compression depends on smoothing, grid, and amplitude-normalisation choice;
  the narrow `2.18 kHz` feature is therefore carried forward.
- Contact probes measured exposed component surfaces, not internal winding,
  resistor hot-spot, or driver voice-coil temperatures.
- The intended hot `0-degree` response comparison is absent.

## 7. Method references

- [Completed Seed A level and thermal procedure](../procedures/UMC22_SEED_A_LEVEL_AND_THERMAL.md)
- [REW API client](../../REW_API_CLIENT.md)
- [Crossover design consequence](../../CROSSOVER_DESIGN.md)
