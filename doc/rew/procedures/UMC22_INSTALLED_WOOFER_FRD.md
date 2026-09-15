# UMC22 Installed-Woofer FRD Runbook

Lifecycle: **COMPLETED PROCEDURE / RETAINED EVIDENCE**
Current approved action: none. Preserve the qualified raw-woofer and
common-position captures; use this runbook only to audit or deliberately repeat
that route after a material change.
Completed capture: C1, C2, C3R, post-repair C4-C6, and common-position TW1 are
valid responses. C6 is the selected woofer-axis source and its durable export
is `rew/frd/SB17NRX2C35-8/000deg_1m_UMC22_2026-09-06.frd`.
Required qualification: **PASS**, recorded in
[`../qualification/UMC22_FRD_QUALIFICATION.md`](../qualification/UMC22_FRD_QUALIFICATION.md).
Next gate: matched speaker-two build and validation under [Crossover
design](../../CROSSOVER_DESIGN.md); this document releases no signal.
Last reviewed: 2026-09-15

The imperative sections below preserve the bounded route used for the dated
captures. They are not a current instruction to reconnect or repeat hardware.

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

**CURRENT OPERATIONAL CAVEAT — 2026-09-08:** after several idle hours, REW may
periodically report that the selected device has no supported lines. The user
reports that either restarting REW after saving the open omnibus measurement
file, or temporarily selecting another device and then returning to the UMC22,
clears it. After either recovery, reselect and verify the exact `EXCL:` UMC22
input and output, `Stereo only`, L/L/L/R, input-volume control `1.00`, and the
per-input calibration assignments. A shared UMC22 input is not equivalent: one
such inadvertent selection caused both channels to reach `0.0 dB` and abort a
later Seed A filtered-woofer attempt despite normal acoustic level.

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

C6 is therefore approved as the current woofer-axis source capture, with C5 as
its repeatability witness. C4 remains valid evidence of approximately
`0.5-0.6 dB` local early-tail uncertainty near `2.03 kHz`; it is not discarded.
This is sufficient woofer-axis evidence for an external prototype crossover
that will be measured and iterated. After the microphone's later move to the
tweeter axis, TW1 subsequently supplied the required companion capture from
that fixed point for the common-position summation pair. This is not a claim of
laboratory metrology, a frozen production response, or unit-to-unit tolerance.

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
6. Treat
   `rew/frd/SB17NRX2C35-8/000deg_1m_UMC22_2026-09-06.frd` as the durable C6
   design export: `913,746` bytes, SHA-256
   `af3142aeff9dcd232ddb61878452c31afe5cae5446e4bd266b2e4e337488c1ca`.
   A fresh selected API extraction matches all `31,404` frequency/magnitude/
   phase rows within printed precision. The `.mdat` remains authoritative.

No further unchanged woofer repeat or export is required. The microphone's
reported `150 mm` move creates a new and useful observation point rather than a
repeatability question. At `1000 mm` perpendicular distance, the woofer is
`sqrt(1.000^2 + 0.150^2) = 1.01119 m` from that point, adding approximately
`32.6 us` or `27.0 degrees` at `2.30 kHz` relative to the tweeter. Preserve that
geometric phase by measuring both drivers without another microphone or cabinet
move.

### 6.1 Next Common-Position Woofer Package

Before any signal, confirm that the capsule remains `1000 mm` from the baffle
plane on the tweeter axis, the window is closed, the original qualified woofer
wiring/reference route is still intact, the present power state is known, and
the system is silent and normal. Repeat the Section 4 REW audit because the
geometry changed, but do not repeat fixture qualification or a level tone when
the electrical route and controls are unchanged.

**USER-REPORTED PHYSICAL GATE — PASS (2026-09-06):** capsule remains
`1000 mm` from the baffle plane, window closed, amplifier powered, no wiring
change, and system silent and normal. The only reported physical change since
C6 is the intentional `150 mm` microphone raise onto the tweeter axis.

**VERIFIED NO-EXCITATION API GATE — PASS (2026-09-06):** a complete snapshot
returned no failed endpoint and confirmed audio ready, Generator stopped, Java
`Stereo only`, exact exclusive UMC22 endpoints, `48 kHz`, L/L/L/R routing,
`ECM8000_calibration_data.csv` on input L and no calibration file on R, no
separate output calibration, loopback calibration/timing with merge off and
zero offset, `-20 dBFS`, `20-20000 Hz`, `256k`, one repetition, and clipping
abort enabled. The prepared title was
`SB17-IW-0deg-1m-U22-260906-TW1`; `TW1` is retained as the documented first
tweeter-axis-waypoint woofer capture.

The released one-sweep package was:

| Field | Required value |
| --- | --- |
| Name | `SB17-IW-0deg-1m-U22-260906-TW1` |
| Range | `20-20000 Hz` |
| Level | `-20 dBFS` |
| Length | `256k` |
| Repetitions | `1` |
| Routing | existing `L/L/L/R` |
| Clipping abort | enabled |

**USER-REPORTED CAPTURE RESULT — PASS (2026-09-06):** TW1 completed with no
warning, clipping, or anomaly. Minimum displayed headroom was `8.8 dB` and the
reference-input figure remained `33.7 dB`. The woofer alone remained connected
to the amplifier and unmodified sampling harness; the prepared capacitor and
tweeter were not in circuit.

**VERIFIED API RESULT — PASS:** TW1 is UUID
`12568bef-2ec1-4cc7-be3a-91460b0659fa`, captured `17:52:37` in REW V5.40 beta
133 at `48 kHz`. Its direct peak/System Delay is `3.1388593352 ms`, IR start is
`3.0208333333 ms`, SNR is `42.75 dB`, and timing offset, cumulative IR shift,
and clock adjustment are zero. A post-capture snapshot confirmed audio ready,
Generator stopped, no current error/block, and the intended `-20 dBFS`,
`20-20000 Hz`, `256k`, one-repetition settings. Cumulative warning entries at
`17:27-17:33` predate TW1 and belong to the throwaway-instance event.

**DERIVED REVIEW — PASS:** TW1's direct arrival is `28.857 us` later than C6,
against `32.616 us` predicted for the reported `150 mm` vertical move at
`1.000 m`; residual is `-3.759 us`. A signal-free common-window diagnostic at
the nearest native bin to `2.297 kHz` gives TW1 minus C6 of `-0.271 dB` and
`-22.12 degrees`, becoming `+1.74 degrees` after removing the measured delay.
The first stronger late-energy maximum occurs approximately `3.60 ms` after
TW1's direct peak. This supports a REW-native `Hann 2.0 ms` left /
`Tukey 0.25 3.5 ms` right window at exact reference `3.1388593352 ms`, with
FDW/MTW off. The offline one-sided taper approximation was diagnostic only;
the retained/exported response must be REW's native result.

No repeat is planned: the unchanged route already has repeatability evidence,
while TW1's purpose is the new common observation point and it passes.

**VERIFIED RETENTION / RESOLVED EXPORT DISPLACEMENT:** the axis-qualified single-measurement `.mdat` is
`2,428,191` bytes with SHA-256
`78abfeec5c1efcfbba510785710cb35cdaa39a7e8d167fe88c1871f5e16928ef`.
The live UUID stores `Hann 2.0 ms` left / `Tukey 0.25 3.5 ms` right,
FDW/MTW off, at displayed reference `3.140 ms`. Its `1.141 us` displacement
from the fitted peak is sub-sample and immaterial. The native unsmoothed
magnitude/phase FRD
`rew/frd/SB17NRX2C35-8/000deg_tweeter-axis_1m_UMC22_2026-09-06.frd` is
`913,085` bytes with SHA-256
`03923152b08c36e066cb0f9520c7a76489bf6837e3b85cd06c67af0c12a8e4b7`.
Its `31,404` rows span `499.877960-12000.000966 Hz` and match the live native
UUID-selected response within `0.000009 Hz`, `0.000513 dB`, and
`0.001498 degrees` circular phase. The later tweeter export accidentally
overwrote this path, but its bytes were first preserved at the correct SB26
path and TW1 was then re-exported. The restored file is exactly `913,085` bytes
with the original SHA-256 above and its header again identifies TW1. No unique
evidence was lost and no measurement repeat is required.

After those signal-free retention steps, power the amplifier down with volume
fully down and follow the separate
[protected-tweeter runbook](UMC22_INSTALLED_TWEETER_FRD.md).

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
