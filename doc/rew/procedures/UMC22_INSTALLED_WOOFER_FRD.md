# UMC22 Installed-Woofer FRD Runbook

> - **Lifecycle:** COMPLETED PROCEDURE / SAFE REPEAT ROUTE
> - **Owns:** the safe, bounded UMC22 route for a deliberate installed-woofer repeat
> - **Does not own:** source-release evidence, historical capture results, or crossover decisions
> - **Read when:** deliberately repeating the route after a material change or on speaker two
> - **Current approved action:** preserve the released sources; no unchanged speaker-one repeat
> - **Next gate:** matched speaker-two raw-driver capture and validation
> - **Limitations:** the UMC22/fixture route is interface-specific; generic microphone calibration is not absolute SPL
> - **Last reviewed:** 2026-09-15

The approved C6, C5, and TW1 sources, their hashes and UUIDs, and every dated
capture result are in the audit-only [installed-driver acoustic-source
qualification](../qualification/INSTALLED_DRIVER_ACOUSTIC_SOURCES_2026-09-06_TO_07.md).
This runbook releases no signal by itself.

## 1. Scope And Safety Boundary

Use only the qualified UMC22, SU-V570, ECM8000, and protected-reference route
for an installed SB17 woofer. Do not connect an amplifier output directly to
`INST 2`; use the qualified fixture under [fixture use](../fixtures/REFERENCE_FIXTURE_USE.md).
The accepted UMC22 fault risk does not waive checks that protect the person,
amplifier, speaker, PC, or source validity.

## 2. Required Unchanged Route

The released path is REW output L → UMC22 Output 1 → TS-to-RCA → SU-V570 AUX
left → speaker bank B left → woofer; the qualified clamp/attenuator is in
parallel at the woofer terminals and feeds `INST 2`; ECM8000 feeds Input 1 XLR.
Use only B-left, leave Output 2, headphones, and AUX right empty, and keep
`DIRECT MONITOR` off.

Use the established `1.000 m` geometry. For woofer-axis work, place the
microphone on the woofer axis; for a common-position source, place it on the
fixed tweeter axis and do not add a geometric delay. Secure the cabinet and
microphone. Close the window behind the microphone where practical.

Use the qualified controls: UMC22 `OUTPUT` fully clockwise, `GAIN 1` and
`GAIN 2` about 2 o'clock, phantom on only after the ECM8000 is connected,
SU-V570 AUX / tone defeat / loudness off / POWER AMP DIRECT off / B-left only /
`-38 dB` mark. Use the documented `1 kHz` tone only if a changed path requires
level restoration to `1.00 V RMS` across the woofer; stop the tone immediately.

## 3. Cold Start Or Changed-Route Check

For a disconnection, uncertain state, or material route change: stop all audio,
set volume down, switch the amplifier off, disconnect USB, turn phantom off,
and inspect fixture, terminals, insulation, restraint, woofer polarity, and
connector retention. Reconnect the released path, connect the ECM8000 before
phantom, then power the amplifier at minimum. Stop for exposed conductor,
loose/damaged connection, hum, transient, clipping, instability, heat, smell,
or smoke.

At the start of a new measurement day, after a relevant power-cycle,
reconnection, endpoint change, unattended setup interval, or anomaly, obtain
one current confirmation that power, wiring, geometry, and idle behaviour are
normal. If unchanged in an active package, keep the setup undisturbed.

## 4. No-Excitation Audit

With Generator, Check Levels, Measure, and all other application audio stopped,
confirm the following before preparing a named capture:

| Item | Required state |
| --- | --- |
| REW route | V5.40 beta 133, Java `Stereo only`, exact exclusive UMC22 input and output, `48 kHz` |
| Channel matrix | output L / timing output L / measurement input `MICROPHONE (Master Volume) L` / reference input `MICROPHONE (Master Volume) R` |
| Timing/calibration | loopback as calibration and timing reference; make calibration from loopback; IR merge off; timing offset `0.0000 ms` |
| Microphone calibration | `ECM8000_calibration_data.csv` on active L only; reference R has none |
| Physical state | clip indicators off; silent, stable system with no new heat, smell, or anomaly |
| Capture | actual-date `SB17-IW-<angle>-<position>-1m-U22-<YYMMDD>-C<next>`; `20-20000 Hz`, `-20 dBFS`, `256k`, one repetition, clipping abort enabled |

Use the read-only REW API status/snapshot when available as corroboration; it
cannot prove wiring or geometry. If REW recovery was required, reselect and
verify the exact endpoints, Stereo-only mode, L/L/L/R, input-volume `1.00`, and
per-input calibration. A shared UMC22 input is invalid.

## 5. Capture, Retention, And Stop Rules

After a specifically approved capture package, run only the named sweep while
watching both input levels and hardware clips. Record displayed headrooms,
warnings/anomalies, microphone and soundcard calibration, routing,
timing-reference index, System Delay, IR start, timing offset, clock adjustment,
SNR, and signal-to-distortion. Save raw `.mdat` before signal-free review.

Stop, de-energise safely, and preserve any failed capture as diagnostic evidence
for a REW warning, dropout, clipping, rubbing/buzzing, instability, unusual
heat, smell, smoke, spark, tingle, disturbed microphone/cabinet, loose cable,
or any other anomaly. Do not continue a package or modify a failed capture into
apparent validity.

Use [FRD measurement method](../FRD_MEASUREMENT_METHOD.md) for signal-free
impulse/ETC review, REW-native window selection, export, and naming. Retain the
`.mdat` as authority; selected API extraction may corroborate it, but API-loaded
duplicates must never be saved into a production archive.
