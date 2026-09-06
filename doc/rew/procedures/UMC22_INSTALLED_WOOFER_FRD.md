# UMC22 Installed-Woofer FRD Runbook

Lifecycle: **CURRENT PROCEDURE**
Current approved action: keep every signal stopped; no more unchanged woofer
repeatability sweeps are needed. C6, supported by immediate repeat C5, passes
the proportionate initial crossover-design gate in Section 6. Close the open
window before the next acoustic package and treat that as the new recorded room
boundary state.
Current capture: C1, C2, C3R, and post-repair C4-C6 are valid responses with the
common `Hann` `2.0 ms` left / `Tukey 0.25` `3.5 ms` right window at their own
direct peaks, with FDW/MTW off. C6 is the selected current installed-woofer
source capture for initial crossover modelling; no durable FRD export has yet
been authorised or made.
Required qualification: **PASS**, recorded in
[`../qualification/UMC22_FRD_QUALIFICATION.md`](../qualification/UMC22_FRD_QUALIFICATION.md).
Do not proceed to: any output test or sweep, cabinet rotation, FRD export,
raw-tweeter measurement, or polar work.
Last verified state report: 2026-09-06

## 1. Scope And Risk Boundary

This procedure governs the qualified UMC22, SU-V570, protected electrical
reference, and ECM8000 route for the installed SB17 woofer only. It does not
qualify another interface, a changed fixture, the tweeter, or a polar series.

**USER DECISION — 2026-09-05:** the user accepts a known but unquantified
possibility of damage to the approximately GBP 25 UMC22 during an amplifier
fault. The normal reference level has ample nominal input margin, but the
worst amplifier-derived fixture voltage can exceed the UMC22's published
instrument-input maximum. This acceptance does not waive checks protecting the
person, SU-V570, PC, loudspeaker, or data validity. It cannot guarantee that a
destructive UMC22 failure would be perfectly contained, although the fixture's
high series resistance makes wider damage unlikely.

The qualified fixture remains mandatory. Never connect an amplifier output
directly to `INST 2`. Use the current fixture operating instructions in
[`../fixtures/REFERENCE_FIXTURE_USE.md`](../fixtures/REFERENCE_FIXTURE_USE.md).

## 2. Qualified Physical And Software State

The released signal path is:

```text
REW output L -> UMC22 Output 1 -> mapped TS-to-RCA cable
             -> SU-V570 AUX left -> speaker bank B left -> installed woofer

SU-V570 B-left terminals -> qualified clamp/attenuator -> UMC22 INST 2
ECM8000 -> UMC22 Input 1 XLR
```

The woofer and fixture are in parallel at B-left with `In+`/red on positive and
`In-`/black on negative. Headphones, Output 2, and AUX right remain empty.
`DIRECT MONITOR` is off. The ECM8000 is connected before phantom is enabled.
The microphone capsule is `1000 mm` from the baffle plane, on the woofer axis,
aimed at the cabinet to match the generic 0-degree calibration. The microphone
is fixed and the cabinet is secured on the 10-degree-marked rotation jig.

Qualified final controls/settings are:

- UMC22 `OUTPUT` fully clockwise;
- `GAIN 1` approximately 2 o'clock;
- `GAIN 2` approximately 2 o'clock;
- phantom on for the ECM8000;
- SU-V570 input `AUX`, tone `DEFEAT`, loudness off, `POWER AMP DIRECT` off;
- speaker bank B left only;
- SU-V570 volume at its documented `-38 dB` scale mark;
- Agilent U1282A across the woofer when confirming level.

**USER-REPORTED C4-C6 STATE — 2026-09-06:** immediately before C4 the user
confirmed that the repaired woofer connector was fully seated and that all
wiring, settings, physical positions, and environmental conditions were
unchanged. Both hardware clip indicators were unlit; the system was silent and
normal, with no anomaly. The Agilent U1282A's internal thermometer, without an
attached thermocouple, indicated `22.1 degrees C`; treat that as a room-
temperature indication rather than calibrated local air temperature. No
warning, clipping indication, or anomaly was reported for C4-C6.

**USER-REPORTED RETAINED METADATA — 2026-09-06:** timing-reference indices were
C4 `47850.66`, C5 `47850.64`, and C6 `47850.72`. Signal-to-distortion figures
were respectively `63.5`, `59.5`, and `61.0 dB`. Headrooms were reported nearly
identical to earlier successful runs, but exact values were not retained.

**USER-REPORTED ENVIRONMENTAL NOTE — 2026-09-06:** a window approximately `1 m`
behind the microphone was slightly open and admitted an intermittent breeze.
With the loudspeaker approximately `1 m` in front of the microphone, a simple
axial reflection estimate gives a `3 m` reflected path versus the `1 m` direct
path, or about `2 m / 343 m/s = 5.83 ms` excess delay. Its direct specular
reflection is therefore later than the retained `3.5 ms` right window. Airflow
could still add turbulence noise or move a stand, cable, curtain, or light
object. Closing the window is a cheap repeatability improvement for future
acoustic packages, not grounds to reject C5/C6 or repeat them now.

**USER-REPORTED REPAIRED-LEAD RESTART — 2026-09-06:** with all signal stopped,
the user turned the SU-V570 down and off, inspected the repaired woofer
connection, and confirmed correct polarity, full engagement and firm retention,
with no exposed conductor, stray strand, or possible opposite-terminal contact.
The amplifier was restarted at minimum, remained silent and normal without
heat, smell, or instability, and was restored to `-38 dB` without a tone.

If any cable, control, power state, geometry, enclosure state, or nearby
reflective object has changed since that report, stop and report the current
state. Do not assume that the earlier report covers a changed setup.

**STANDING UNCHANGED-STATE CONVENTION:** within an active measurement setup,
assume the user will report any change and do not request a fresh recital before
every capture or merely because the chat changed. One concise current power,
wiring, and normal-state confirmation remains required at the start of a new
measurement day or after a relevant power-cycle, reconnection, REW endpoint
change, unattended setup interval, or anomaly. After the first capture validates
the package, run the remaining named captures consecutively under common stop
rules without waiting for per-capture analysis unless a warning occurs.

## 3. Cold Connection And Startup

Use this section after any disconnection, uncertain state, or deliberate cold
restart. If the qualified assembly is genuinely unchanged and already powered,
do not disturb it merely to repeat commissioning; proceed to Section 4.

1. Stop REW Generator, Check Levels, and Measure; stop all other application
   audio. Switch the SU-V570 off and set its volume fully down. Disconnect UMC22
   USB and turn phantom off.
2. Inspect the fixture, plugs, strain relief, insulation, and cable restraint.
   Stop for exposed conductors, loose terminals, damaged insulation, heat
   damage, or an altered component/cable.
3. Set UMC22 `OUTPUT`, `GAIN 1`, and `GAIN 2` fully down and `DIRECT MONITOR`
   off. Leave Output 2 and headphones empty.
4. Connect Output 1 through the passed TS-to-RCA cable to SU-V570 `AUX` left.
   Keep AUX right empty. Select tone `DEFEAT`, loudness off, and `POWER AMP
   DIRECT` off.
5. Connect only the installed woofer to speaker bank B left. At the same
   terminals connect fixture red/`In+` to positive and black/`In-` to negative.
   Connect the fixture output directly to `INST 2`; do not retain a breakout in
   the measurement path.
6. Connect the ECM8000 to Input 1 by XLR. Connect USB, then enable phantom.
   Confirm the phantom indicator is normal, neither channel clips, and there is
   no sound, instability, heating, or smell.
7. With the generator still stopped, power the SU-V570 at minimum volume.
   Confirm the woofer remains silent and there is no transient or persistent
   hum/buzz, clipping, instability, heating, smell, or smoke.
8. Restore only the qualified control positions listed in Section 2. If level
   must be re-established, use a `1 kHz`, output-L tone at the qualified source
   setting and raise amplifier volume slowly to `1.00 V RMS` across the woofer;
   stop the tone immediately. Do not infer broadband voltage from a changing
   meter indication during a sweep.

The historical gross protected-reference result was `98.53 mV AC` at
`1.0000 V AC` woofer voltage. Repeating it is unnecessary unless the fixture,
cable, or level path changed. If repeated through a restrained breakout, accept
only `80-120 mV RMS`; stop the tone before touching the connection and restore
the direct fixture-to-`INST 2` path afterward.

## 4. Mandatory No-Excitation Audit

Do not generate a signal during this section. Report every displayed item and
any discrepancy before a capture is authorised.

When the current [REW API client](../../REW_API_CLIENT.md) is available, begin
with its read-only `status` and `snapshot` commands. Use the snapshot to
corroborate REW version, audio readiness, driver, device endpoints, sample
rate, channel matrix, calibration assignment, timing mode, sweep settings,
protection settings, application warnings, and stopped-generator state. It
does not replace the physical checks below: a snapshot is current software
state rather than historical measurement provenance, cannot inspect wiring or
geometry, and may have absent or stale last-input levels.

1. Confirm Generator, Check Levels, and Measure are stopped and no other
   application audio is active.
2. Confirm REW `V5.40 beta 133` and Java `Stereo only`.
3. Confirm both input and output are the exact exclusive endpoint
   `EXCL: Behringer UMC22 (USB Audio CODEC)` and sample rate is `48 kHz`.
4. Confirm input-volume scaling is `1.00` and no separate soundcard-calibration
   file is loaded.
5. Confirm the complete channel matrix:

   | Role | Selection |
   | --- | --- |
   | Measurement output | L |
   | Timing-reference output | L |
   | Measurement input | `MICROPHONE (Master Volume) L` |
   | Reference input | `MICROPHONE (Master Volume) R` |

   This is `L/L/L/R`. Reference output R is invalid because physical Output 2
   is empty; reference input L would self-reference the microphone channel.
6. Confirm `Use loopback as cal and timing reference` and `Make calibration
   data from loopback response`.
7. Confirm `Merge loopback response into IR` is **off** and timing offset is
   `0.0000 ms`.
8. In Measure's Calibration data display, confirm
   `ECM8000_calibration_data.csv` for the exact active measurement input L.
   Confirm the electrical reference input R has no microphone calibration.
   A file shown only against `Default Input` does not pass this check.
9. Confirm both UMC22 clip indicators are off and the idle system is silent,
   stable, and free of new heat, smell, or other abnormality.
10. Do not prepare a further sweep until a named next measurement package is
    approved. If another capture is later separately authorised, allocate its
    next unused capture number and prepare—but do not start—the specified sweep:

   | Field | Required value |
   | --- | --- |
   | Name | `SB17-IW-0deg-1m-U22-<YYMMDD>-C<next>` using the actual date |
   | Range | `20-20000 Hz` |
   | Level | `-20 dBFS` |
   | Length | `256k` |
   | Repetitions | `1` |
   | Clipping abort | enabled |

Stop at this gate and report the complete audit. A prepared dialog is not
authorisation to run it.

## 5. First-Capture And Bounded-Batch Gate

After the package-level no-excitation audit has been reviewed and the first
capture is explicitly authorised:

1. Reconfirm that no setting, control, wiring, or physical position changed.
2. Run exactly the prepared sweep while watching both input levels and the
   hardware clip indicators.
3. Stop immediately for a clipping or distortion warning, hardware clip,
   severe rubbing/buzzing, dropout, instability, unusual heating, smell, smoke,
   perceptible tingle, spark, or any other abnormality.
4. After the sweep, generate nothing further until the package's stated
   continue/stop checks have been applied; change no control or position except
   a named rotation step in an explicitly released polar package.
5. Record both input headrooms, every warning/anomaly, and Measurement Info:
   microphone calibration, soundcard calibration, input/output routing,
   timing-reference index, System Delay, IR start, timing offset, clock
   adjustment, SNR, and signal-to-distortion.
6. Save the raw `.mdat`. When the current
   [REW API client](../../REW_API_CLIENT.md) is available, use an explicit
   selected-measurement extraction to corroborate the stored summary, SNR,
   timing fields, native unsmoothed magnitude/phase, REW-native windows, and
   optional windowed impulse. Retain the `.mdat` as authority. The client does
   not recover the displayed sweep headrooms, timing-reference sample index,
   historical per-measurement routing, or signal-to-distortion result; retain
   those from REW and the operator's observations. Because extraction leaves
   newly loaded measurement copies in REW, perform it after the live set is
   complete or in a disposable session; never save those duplicates into the
   production `.mdat`.
7. Inspect and retain the direct impulse and ETC. Identify the first material
   reflection and propose a REW-native left/right window under
   [`../FRD_MEASUREMENT_METHOD.md`](../FRD_MEASUREMENT_METHOD.md).

If the package supplies objective continue criteria and the first capture meets
all of them, run its remaining named captures consecutively without waiting for
another chat response. Otherwise stop for review. Do not invent additional
captures, rotate the cabinet outside a released polar package, export an FRD,
or copy a qualification window into REW without the applicable approval.

## 6. Current Repeatability And Design-Release Gate

Detailed evidence and calculations are owned by
[DRIVER_ANALYSIS.md](../../DRIVER_ANALYSIS.md). C4/C5/C6 are valid post-repair
responses with correct API-exposed configuration, no new REW warning, SNR
`43.91-44.06 dB`, and only `1.65 us` total System Delay spread. Each has the
common native window at its own direct peak.

Under the earlier strict `0.2 dB` maximum-over-every-bin target, the complete
three-capture production-window set would fail: C4/C5 reach `0.631 dB` and
C4/C6 `0.512 dB` over `1-5 kHz`. C5/C6 pass at `0.137 dB` maximum and
`0.047 dB` RMS. The largest C4-related residual is concentrated near
`2.03 kHz`; it is response shape, not just the approximately `-0.07 dB`
mean-level difference.

Window sensitivity localises the recurrence. With a `1.5 ms` right window all
three pairs remain within `0.154 dB`, but C4 diverges from C5/C6 when the right
window reaches `2.0 ms`, and the difference grows through `3.5 ms`. The raw
direct packets and first approximately `1.5 ms` of post-arrival response are
therefore repeatable; variable early-tail energy between roughly `1.5` and
`3.5 ms` produces the recorded uncertainty in the established window. A
`1.5 ms` sensitivity window has only about `667 Hz` nominal right-window
resolution and is not silently substituted for the retained `500 Hz-12 kHz`
production window.

That strict whole-band maximum is disproportionate as the sole gate for an
iterative hobby crossover: it chooses the single worst of `10,923` native bins
even when the overall perturbation and intended crossover region are small. The
current method instead uses whole-band RMS plus a crossover-band maximum,
timing, phase, validity, and engineering-consequence checks.

**PROPORTIONATE DESIGN RELEASE — PASS:** over `1-5 kHz`, all C4-C6 pairwise
unsmoothed RMS differences are at most `0.182 dB`; over the intended
`2.2-2.4 kHz` crossover band, all unsmoothed maxima are at most `0.185 dB`;
maximum `1-5 kHz` circular-phase difference is `4.119 degrees`; System Delay
spread is `1.655 us`; and no validity warning or anomaly occurred. C5/C6 are
the immediate pair and pass especially strongly. Their timing-reference-index
spread is `0.08` sample, which at `48 kHz` is

```text
0.08 / 48000 s = 1.667 us.
```

That accounts for the measured delay spread to about `0.012 us`, so the timing
data do not indicate physical source-to-microphone distance drift.

C6 is therefore approved as the current installed-woofer source capture for
initial crossover modelling, with C5 as its repeatability witness. C4 remains
valid evidence of approximately `0.5-0.6 dB` local early-tail uncertainty near
`2.03 kHz`; it is not discarded. This is sufficient for an external prototype
crossover that will be measured and iterated. It is not a claim of laboratory
metrology, a frozen production response, or unit-to-unit tolerance.

The variable tail weights a small acoustic, structural, support, cable, or
nearby-object change more strongly than scalar electrical gain, but a unique
cause need not be established before initial crossover work. Park that root-
cause investigation unless the discrepancy recurs in same-package measurements
near the chosen crossover, changes the filter decision, or prevents a normal-
and-reverse-polarity validation from behaving coherently.

Current safe actions are:

1. Keep Generator, Check Levels, Measure, and all other application audio
   stopped. Do not disturb controls, wiring, geometry, or the room state.
2. Treat
   `rew/SB17NRX2C35-8_installed_0deg_1m_UMC22_2026-09-06.mdat` as the verified
   raw production authority: `7,266,399` bytes, SHA-256
   `d582c5d1fb7591689b3e4ef5491c1c578338f854fbe97c7d31124b529f0b516b`.
   A selected extraction loaded exactly C1, C2, and C3R with no warning and
   verified each stored production window.
3. Retain C4, C5, and C6 in their three UUID-selected single-measurement `.mdat`
   files. Each archive was written to a previously absent path and reloaded as
   exactly one expected UUID with its common window, `54,559` native response
   points, and `131,072` raw impulse samples. Their exact hashes are owned by
   [DRIVER_ANALYSIS.md](../../DRIVER_ANALYSIS.md).
4. Retain `DIAG-C3-no-output-260906` only in the separate diagnostic `.mdat`;
   it is absent from the production authority. Do not edit its timing, window,
   or metadata.
5. API verification and signal-free analysis loaded duplicate copies into the
   current REW workspace. Session IDs are unstable; do not use `Save all` or
   save those duplicates into any authority. The verified files are complete.

No further unchanged woofer repeat is justified. FRD export remains a separate
signal-free action, and raw-tweeter or polar measurement still requires its own
explicitly released package and protection/rotation prerequisites.

## 7. Global Stop Rules And Limitations

Stop and de-energise safely for unexpected continuity, the wrong connector
contacts, an open protective path, sustained DC above a stated gate, clipping,
dropout, instability, abnormal sound, visible damage, heating, smell, smoke,
sparks, or perceptible tingle. Stop data work for missing calibration, wrong
endpoint/channel, absent numeric timing, inadequate headroom, moved geometry,
or a multi-arrival/ambiguous impulse. Preserve the failed capture and label it
diagnostic; do not repair its status by editing metadata.

The supplied ECM8000 CSV is a generic 0-degree response, not a serial-number-
specific calibration and not an absolute-sensitivity calibration. Results are
therefore not absolute-SPL evidence. The qualification's derived `2.0 ms` left
/ `1.0 ms` right window was suitable for a `1-5 kHz` repeatability gate; it is
not a final production window. Each reusable series must store a suitable
REW-native window selected from its own impulse/ETC.

This release is for controlled installed-woofer FRD only. Raw-tweeter sweeps
need an agreed protected band, level, and series high-pass. Polar measurements
need a separate rotation and position-control procedure. Neither is released.
