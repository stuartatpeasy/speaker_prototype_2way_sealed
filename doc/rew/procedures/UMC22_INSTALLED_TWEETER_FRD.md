# UMC22 Installed-Protected-Tweeter FRD Runbook

> - **Lifecycle:** COMPLETED PROCEDURE / SAFE REPEAT ROUTE
> - **Owns:** the safe, bounded UMC22 route for a deliberately repeated protected-tweeter capture
> - **Does not own:** source-release evidence, historic capture results, or crossover decisions
> - **Read when:** deliberately repeating the protected route after a material change or on speaker two
> - **Current approved action:** preserve the released sources; no unchanged speaker-one repeat
> - **Next gate:** matched speaker-two raw-driver capture and validation
> - **Limitations:** protection is a measurement safeguard, not a listening crossover; microphone calibration is not absolute SPL
> - **Last reviewed:** 2026-09-15

The approved C2 source, `+11.14 dB` modelling scale, raw-file identities,
hashes, UUIDs, and source-release checks are in the audit-only
[installed-driver acoustic-source qualification](../qualification/INSTALLED_DRIVER_ACOUSTIC_SOURCES_2026-09-06_TO_07.md).
This runbook releases no signal by itself.

## 1. Scope And Protection

Use only the qualified UMC22, SU-V570, ECM8000, and reference fixture route
with the installed SB26 tweeter. The measured `10.13 uF`, `0.08 ohm` ESR series
capacitor must remain in the tweeter-positive path. Connect the qualified
clamp/attenuator directly across the tweeter after that capacitor through NL4
`2+`/`2-`; never connect the amplifier directly to `INST 2`.

The capacitor protects the tweeter during raw measurement. Its post-capacitor
reference leaves the established `+11.14 dB` magnitude-only VituixCAD scale;
apply no extra phase, delay, polarity, smoothing, or minimum-phase correction.

## 2. Required Geometry And Route

Use the fixed microphone at tweeter-axis height, `1.000 m` from the baffle-plane
pivot, aimed at the cabinet. Secure the cabinet and microphone. Preserve
measured timing; do not add a geometric delay. The electrical and UMC22 controls
are the qualified settings in the [woofer runbook](UMC22_INSTALLED_WOOFER_FRD.md#2-required-unchanged-route).

Before a changed-route startup, stop all audio, set volume down, switch the
amplifier off, disconnect USB and phantom, then inspect the capacitor, wiring,
terminals, strain relief, insulation, and fixture. Before power-up confirm
plausible resistance across the tweeter/reference plane, a capacitor-charging
rise toward open circuit on the amplifier side, and no short, capacitor bypass,
loose connection, or exposed conductor. Connect ECM8000 before phantom, then
start at minimum volume. Stop for abnormal sound, hum, transient, clipping,
instability, heat, smell, or smoke.

## 3. No-Excitation Audit

At the start of a new measurement day or after a power, wiring, endpoint,
geometry, or anomaly change, obtain one current report that the protected route
is connected, the speaker and microphone are secure, and idle operation is
silent and normal. With Generator, Check Levels, Measure, and all other audio
stopped, verify the exact UMC22 endpoints, Java `Stereo only`, `48 kHz`,
L/L/L/R routing, loopback calibration/timing, loopback IR merge off, timing
offset `0.0000 ms`, `ECM8000_calibration_data.csv` on L only, no microphone
calibration on reference R, clips off, and no abnormal condition.

Prepare only an explicitly approved title and one `20-20000 Hz`, `-20 dBFS`,
`256k`, clipping-abort-enabled sweep. Use the read-only REW API snapshot where
available as corroboration, never as proof of physical wiring or geometry.

## 4. Capture, Retention, And Stop Rules

Run only the approved sweep while monitoring both input levels and hardware
clips. Record headrooms, warnings/anomalies, calibration and routing,
timing-reference index, System Delay, IR start, timing offset, clock adjustment,
SNR, and signal-to-distortion. Save raw `.mdat` before signal-free review.

Stop, de-energise safely, and retain a failed capture as diagnostic evidence
for clipping, a REW warning, dropout, unusual sound, rubbing, instability,
heat, smell, smoke, spark, tingle, movement, loose cable, or any anomaly. One
failed capture stops the remaining batch pending review.

Use [FRD measurement method](../FRD_MEASUREMENT_METHOD.md) for source review,
windowing, and export. Keep the `.mdat` authoritative; do not save API-loaded
duplicate measurements into it.
