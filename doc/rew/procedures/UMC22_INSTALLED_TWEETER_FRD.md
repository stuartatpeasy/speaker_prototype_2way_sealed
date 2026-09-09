# UMC22 Protected Installed-Tweeter FRD Runbook

Lifecycle: **COMPLETED PROCEDURE / RETAINED EVIDENCE**
Current approved action: none. C2 retention/export and the TW1 export-path
repair are complete; preserve both sources and use this runbook only to audit
or deliberately repeat the protected raw-tweeter route after a material change.
Owns: the installed SB26STWGC-4 protection, wiring, sweep limits, first-capture
gate, and bounded on-axis repeat.
Does not own: woofer evidence, final crossover protection, polar rotation, or
high-level/distortion testing.
Next gate: qualified as-built Seed A system impedance and phase under
[Crossover design](../../CROSSOVER_DESIGN.md); this document releases no signal.
Last reviewed: 2026-09-09

The imperative sections below preserve the bounded route used for the dated
captures. They are not a current instruction to reconnect or repeat hardware.

## 1. Scope And Safety Boundary

This procedure adapts the already qualified UMC22/SU-V570/electrical-reference
chain to one installed-tweeter on-axis measurement package. The changed driver,
series protection, post-capacitor reference plane, and microphone height are
material changes, so the woofer release does not itself authorise excitation.
The reusable fixture remains mandatory; never connect an amplifier or driver
terminal directly to UMC22 `INST 2`.

The manufacturer's `120 W` rating is conditional on an IEC Butterworth
high-pass at `2.6 kHz`, `12 dB/octave`. The network below is deliberately not a
claim to that power rating. It is a low-energy measurement-only safeguard for
each of at most two approximately `1 V RMS` logarithmic sweeps. Listening,
distortion testing, or operation above this package requires the designed full
crossover or an independently validated second-order-or-steeper high-pass.

## 2. Required Protection And Reference Plane

Use a measured nominal `10 uF` non-polar polypropylene film capacitor rated at
least `100 V`; a measured `8.2-10 uF` part or parallel film combination is
acceptable. Record the measured value, marked value, voltage rating, and
construction. Do not use a polar electrolytic. Secure and insulate every joint
so the capacitor cannot be bypassed by a loose lead or clip.

**SELECTED COMPONENT — USER-REPORTED / PUBLISHED CHECK, 2026-09-06:** TDK
`B32774H4106K000`, marked `10 uF`, `450 VDC`, MKP polypropylene film. Five
consecutive readings were consistent at `10.13 uF`, `0.08 ohm` ESR. TDK's
catalogue confirms the ordering code as `10 uF`, `+/-10%`, `450 VDC`, radial
boxed MKP. This component passes. The reported ESR is small compared with the
tweeter load but is not a safety dependency because its value depends on meter
test conditions.

The required signal path is:

```text
REW output L -> UMC22 Output 1 -> SU-V570 AUX left -> B-left positive
  -> series protection capacitor -> NL4 2+ -> tweeter positive

SU-V570 B-left negative -> NL4 2- -> tweeter negative

Tweeter terminals after capacitor -> qualified clamp/attenuator -> UMC22 INST 2
ECM8000 -> UMC22 Input 1 XLR
```

Disconnect the woofer conductors (`1+`/`1-`) from the amplifier for this
package. The fixture input red/`In+` goes to the protected tweeter positive
terminal after the capacitor; black/`In-` goes to tweeter negative. This removes
the capacitor's frequency-dependent magnitude and phase from the measured
transfer. REW nevertheless defines the generated calibration magnitude as
`0 dB` at `1 kHz`, so the capacitor's terminal/source ratio at that frequency
remains as a constant level offset; the retained C2 FRD therefore needs the
derived `+11.14 dB` model-import scale. Referencing the amplifier side of the
capacitor would instead embed the full frequency-dependent protection transfer
and is invalid for the intended raw-driver FRD.

For nominal `10 uF` and published `R_e = 3.2 ohm`:

```text
f_c = 1 / (2 pi R_e C) = 4.97 kHz.
```

The measured installed complex impedance combined with the reported `10.13 uF`
and `0.08 ohm` ESR predicts approximately `-16.91 dB` terminal/source voltage at
`500 Hz`, `-9.23 dB` at the measured `761 Hz` resonance, `-7.21 dB` at
`2.297 kHz`, and `-2.41 dB` at `5.01 kHz`. Across `500 Hz-20 kHz`, the
calculated maximum terminal/source ratio is `1.006`; retaining the established
approximately `1.00 V RMS` amplifier-output limit therefore keeps the tweeter
near `1.01 V RMS` maximum. The capacitor, voltage bound, restricted sweep band,
single repetition, and stop rules form one protection package; none substitutes
for the others.

## 3. Current Geometry And Environmental State

**USER-REPORTED — 2026-09-06:** the ECM8000 was raised `150 mm` from the woofer
axis until level with the centre of the tweeter dome and aimed directly at the
tweeter. The loudspeaker cabinet was not moved, the capsule remains `1000 mm`
from the baffle plane, and the window is closed. TW1 has passed from this exact
microphone point under the woofer runbook. Leave microphone and cabinet fixed
throughout the electrical change and tweeter package. This
retains the approximately `32.6 us` geometric woofer/tweeter path difference
that would be lost by independently measuring each driver on its own axis.

The slightly open window previously admitted an intermittent breeze. Close it
before this live package and leave it closed throughout. Closure is now
recorded; do not repeat the statement between unchanged captures.

**CURRENT PHYSICAL STATE — USER-REPORTED, 2026-09-06:** the topology is now
assembled as prescribed, the amplifier remains off, and the clamp/attenuator
input has reportedly moved directly across the tweeter after the series
capacitor. No short was found. Resistance directly across the tweeter was
`3.327 ohm`; with the fixture's `11.162 kohm` input in parallel, the calculated
combined value is `3.326 ohm`, so the loading change is only about
`0.001 ohm`. Resistance measured across the amplifier outputs before the
capacitor was `11.162 kohm` and was interpreted by the user as evidence of DC
blocking.

**CORRECTED PHYSICAL GATE — PASS:** the discriminator found a real wiring
mistake before power-up. The user corrected it and then reported that resistance
across the amplifier outputs rises rapidly to open circuit, consistent with the
series capacitor blocking DC; resistance directly across the tweeter remains
`3.326 ohm`; no short is present; and a second, more thorough wiring inspection
finds the prescribed post-capacitor reference topology. This resolves the
reference-plane gate. It was a caught configuration error, not a failed
measurement, and it does not justify additional testing beyond the existing
new-route audit.

## 4. De-Energised Assembly Gate

1. Stop all REW and other application audio. Set SU-V570 volume fully down and
   switch the amplifier off before changing any driver, capacitor, fixture, or
   NL4 connection.
2. Disconnect the woofer from the amplifier route. Confirm the intended NL4
   allocation: `2+` tweeter positive and `2-` tweeter negative.
3. Insert the recorded series capacitor in the tweeter positive path. Inspect
   for exposed conductor, loose clips, a possible bypass, opposite-terminal
   contact, or inadequate strain relief.
4. Connect the qualified fixture across the tweeter after the capacitor with
   correct polarity, then connect only its protected output to UMC22 `INST 2`.
5. With the amplifier still off, use the DMM only to confirm that the capacitor
   is not shorted and that the completed speaker feed has no near-zero-
   resistance short. A resistance reading through the protected tweeter path
   may move as the capacitor charges; that behaviour is not by itself a fault.
6. Do not energise until the exact completed topology, capacitor details,
   present power state, and absence of visible/mechanical defects have been
   reported.

## 5. No-Excitation REW Gate

After the physical report is accepted, power up from minimum volume with all
application signals stopped. The first audit must confirm:

1. idle system silent and normal; no clip indication, heat, smell, instability,
   or other anomaly;
2. REW V5.40 beta 133, Java `Stereo only`, exact exclusive UMC22 input/output,
   and `48 kHz`;
3. complete `L/L/L/R` routing;
4. `Use loopback as cal and timing reference` and `Make calibration data from
   loopback response` enabled;
5. loopback merge off, timing offset `0.0000 ms`, and no separate soundcard
   calibration file;
6. `ECM8000_calibration_data.csv` assigned to microphone input L and no
   microphone calibration assigned to reference input R;
7. Generator stopped and the prepared Measure dialog only:

   | Field | Required value |
   | --- | --- |
   | Name | `SB26-IW-000deg-tweeter-axis-1m-U22-260906-C1` |
   | Range | `500-20000 Hz` |
   | Level | `-20 dBFS` |
   | Length | `256k` |
   | Repetitions | `1` |
   | Measurement output / reference output | `L / L` |
   | Measurement input / reference input | `L / R` |
   | Clipping abort | enabled |

Preparing the dialog is not authorisation to start the sweep.

**USER-REPORTED POWERED-IDLE GATE — PASS (2026-09-06):** after the corrected
physical gate, the powered system was silent and normal with no audible output,
anomaly, or smell. The Measure dialog was then prepared as specified.

**VERIFIED NO-EXCITATION API GATE — PASS (2026-09-06):** a complete GET-only
snapshot returned no failed endpoint and confirmed audio ready, Java `Stereo
only`, exact exclusive UMC22 input/output, `48 kHz`, L/L/L/R routing,
`ECM8000_calibration_data.csv` on microphone input L and no calibration file on
reference input R, no separate output calibration, loopback calibration/timing
with merge off and zero offset, Generator stopped, and exact C1 title,
`500-20000 Hz`, `-20 dBFS`, `256k`, one repetition, and clipping abort. REW was
not blocking. Its stored `18:08:40` “Directory not found” error belongs to an
earlier export-path attempt; the subsequently present and independently
validated TW1 FRD resolves that file operation, so the historical error is not
a live route or measurement blocker.

This gate released and completed exactly one surviving C1 sweep. Its timing
review below now releases the one deliberately changed C2 package; it still
does not release Check Levels, Generator, distortion, rotation, or export.

## 6. First Capture And Conditional Repeat

After explicit release of the audited package, run C1 while watching REW and
both UMC22 clip indicators. Stop for clipping, warning, dropout, rubbing,
buzzing, instability, abnormal heat or smell, smoke, spark, or any other
anomaly.

**USER-REPORTED THREE ATTEMPTS — 2026-09-06:** the first attempt ran with the
amplifier accidentally off and caused REW's expected no-signal complaint; the
second ran with a fan accidentally left on and had higher ambient noise; the
third ran as specified with no clipping or anomaly. The user deleted the first
two measurements from REW before review, so they cannot be upgraded or analysed
as measurement evidence. They remain only user-reported discarded diagnostics.
Only the third capture survives.

**VERIFIED SURVIVING C1 / TIMING EXPLAINED, CONFIRMATION PENDING:** surviving
C1 is session ID `44` at the time of inspection, UUID
`00543c2b-4588-4385-9b81-e0d78bca28a0`, captured at
`18:36:05`. REW reports `48 kHz`, `499.87793-19999.879 Hz`, loopback-cal
reference, zero timing offset/IR shift, zero clock adjustment, and `44.64 dB`
SNR. The user reported minimum measurement headroom `19.9 dB`, reference figure
`36.1 dB`, signal-to-distortion `69.5 dB`, no clipping, and no anomaly.
Cumulative warnings at `18:34:41` and `18:35:09` precede surviving C1 and belong
to the discarded attempts; C1 has no run-specific warning. Its separately saved
source is
`rew/SB26STWGC-4_installed_000deg_tweeter-axis_1m_UMC22_C1_2026-09-06.mdat`,
`2,377,078` bytes, SHA-256
`f47fb2499c27b6bdff4e1ab01595998beb1ce2bd0d96ebe4cb6bcfed5f561c7b`.

REW nevertheless places C1's direct peak/System Delay at `79.8603588 ms`
(`27.392 m`) with IR start `79.7916667 ms`. The raw impulse confirms one
dominant direct-looking peak there; signal before `10 ms` is more than `81 dB`
below it, so this is not merely REW choosing a late room reflection over a
physical arrival near `3.1 ms`. The first separated late peaks are about
`3.31 ms` and `6.06 ms` after the dominant peak. Headroom and SNR pass, but the
timing zero is physically impossible and prevents common-timing phase release.

The reported timing-reference index `44,166.70` is `3,684.02` samples below
C6's `47,850.72`. At `48 kHz`, that is `76.7504167 ms`; subtracting it from
C1's reported `79.8603588 ms` gives a corrected acoustic delay of
`3.1099421 ms`. TW1's common-position woofer delay is `3.1388593 ms`, so C1 is
`28.9172 us` earlier. The expected geometric difference from the woofer being
`150 mm` off axis at `1.000 m` is `32.6164 us`; the residual is only
`3.6992 us` (approximately `1.27 mm`). The index displacement therefore fully
accounts for the physically impossible gross delay. The user confirmed that
`Preferences > Analysis > Impulse response calculation > Loopback delay
reference is IR peak` remained checked, so a changed preference is ruled out.

**PROVISIONAL CAUSE:** the changed sweep start (`500 Hz` for C1 versus `20 Hz`
for the woofer captures) is the most economical cause of the reference-peak
index displacement. C1 is preserved as corroborating magnitude/impulse
evidence but is not yet the phase-bearing design source. One controlled repeat
with a common `20 Hz` start is the smallest useful confirmation and should also
produce the clean source candidate.

The wider logged sweep does not materially weaken the protection. With
`C = 10.13 uF`, at `20 Hz`:

```text
X_C = 1 / (2 pi f C) = 785.6 ohm
V_tweeter / V_source ~= 3.3 / sqrt(3.3^2 + 785.6^2)
                         = 0.00420 = -47.53 dB.
```

That is only about `4.2 mV` at the tweeter for a `1 V RMS` amplifier source;
the added low-frequency stress is negligible for this one low-level sweep.

**USER-REPORTED / VERIFIED C2 — PASS:** the one released C2 sweep completed
without warning, clipping, or anomaly. Reported values were `19.1 dB` minimum
headroom, constant `36.2 dB` reference level, timing-reference index
`47,857.68`, System Delay `3.0067 ms`, and `70.9 dB` signal-to-distortion. A
GET-only API review found the new session ID `45`, stable UUID
`898195c2-fc7d-4eee-a877-7be9d3782f0d`, capture time `18:54:03`,
`20.141602-19999.879 Hz`, `48 kHz`, loopback-cal timing, zero timing offset/IR
shift/clock adjustment, `42.19 dB` SNR, Generator stopped, and no new warning.
The Measure title was accidentally left as C1; identify this capture by UUID
and rename it to `SB26-IW-000deg-tweeter-axis-1m-U22-260906-C2` before saving.

The timing-reference check passes. Combining each reported reference index and
delay places C1's direct peak at sample `47,999.997` and C2's at sample
`48,002.002`. Restoring the `20 Hz` start removed the gross reference-index
displacement; the remaining `2.004`-sample (`41.76 us`) peak-position change is
consistent with the different bandwidth changing the band-limited impulse
shape. C2's `3.00670 ms` common-band delay is the source timing value; do not
substitute the earlier approximate correction to C1.

A signal-free raw-impulse comparison found `0.99883` correlation after integer
peak alignment and common late structure at approximately `+0.625 ms`,
`+3.312 ms`, and `+6.062 ms`. This supports the same production window already
used for the common-position woofer while deriving it from C2's own impulse:

| Window field | C2 value |
| --- | --- |
| Reference time | C2 direct peak (`3.0067008 ms`; displayed rounding is acceptable) |
| Left window | `Hann`, `2.0 ms` |
| Right window | `Tukey 0.25`, `3.5 ms` |
| FDW / MTW | off / off |

This window retains the repeatable early driver/baffle structure and tapers the
first separated later arrival near `+3.31 ms`. Apply it without using an IR
shift, delay adjustment, alignment, smoothing, FDW, or MTW. Then use **Save
measurement**, not Save All, to retain only UUID
`898195c2-fc7d-4eee-a877-7be9d3782f0d` as
`rew/SB26STWGC-4_installed_000deg_tweeter-axis_1m_UMC22_C2_2026-09-06.mdat`.
Do not overwrite C1 or the omnibus archive.

No additional on-axis sweep is authorised or justified. After saving the raw
source first, export its native unsmoothed `500 Hz-12 kHz` magnitude/phase
response as
`rew/frd/SB26STWGC-4/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd`, then validate
the source and export together before releasing the fixed geometry for later
polar work. The export is reconstructible from the saved `.mdat`, so an
intermediate Codex round trip adds no proportionate protection.

That validation is complete. The on-axis package no longer requires the
physical geometry to be held unchanged; any later polar series remains a new
explicitly bounded package.

**VERIFIED RETENTION / EXPORT PASS:** the renamed C2 source is `2,428,204`
bytes with SHA-256
`662d759ba08044bbda6bb04b0d824a0905c6a841b049cd342b1964d041f0d26b`.
A UUID-selected extraction read back C2's correct title, UUID, delay, native
window, FDW/MTW-off state, and no warning. Its FRD is `912,077` bytes with
SHA-256
`a409445a40e645682b188b7a12596c10f727d8a0f78138f052c043d60bb0ea1e`.
All `31,404` finite rows span `499.877960-12000.000966 Hz` and match the native
unsmoothed response within `0.000058 Hz`, `0.0005152 dB`, and `0.001502`
degrees circular phase. C2 is the retained protected-tweeter on-axis source.

**RESOLVED FILING ERROR:** the first export was written to TW1's existing
SB17 path. The validated bytes have since been copied without change to the
correct SB26 path above. TW1's raw `.mdat` and live UUID remained intact, and
the corrective re-export restored its original size, SHA-256, and identity.

## 7. Limitations

The ECM8000 file is generic 0-degree magnitude calibration and does not provide
serial-number-specific or absolute-SPL calibration. C2's selected window is
supported by its own impulse/ETC even though it matches the woofer window; this
is not symmetry by assumption. The current package is on-axis only. Off-axis
rotation remains a separate bounded package; it is not released by this
on-axis result.
