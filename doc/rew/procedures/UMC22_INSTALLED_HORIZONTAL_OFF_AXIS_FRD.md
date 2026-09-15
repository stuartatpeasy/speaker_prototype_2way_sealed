# UMC22 Installed Horizontal Off-Axis FRD Runbook

> - **Lifecycle:** COMPLETED PROCEDURE / SAFE REPEAT ROUTE
> - **Owns:** a bounded positive-horizontal raw-driver repeat series
> - **Does not own:** source-release evidence, a full polar specification, or crossover decisions
> - **Read when:** deliberately repeating the sparse polar route after a material change or on speaker two
> - **Current approved action:** preserve the verified source families; no unchanged speaker-one repeat
> - **Next gate:** matched speaker-two raw-driver and Seed A validation
> - **Limitations:** positive side only at `20 degree` spacing; inferred symmetry; woofer use `1.5-5 kHz`, protected-tweeter use `1.5-12 kHz`
> - **Last reviewed:** 2026-09-15

The completed raw sources, UUIDs, hashes, windows, releases, and known filing
corrections are in the audit-only [installed-driver acoustic-source
qualification](../qualification/INSTALLED_DRIVER_ACOUSTIC_SOURCES_2026-09-06_TO_07.md).
This runbook releases no signal by itself.

## 1. Geometry And Scope

The smallest directivity discriminator is the existing `0 degree` source plus
`+20`, `+40`, and `+60 degree` captures for each raw driver. It is not a full
polar set. Do not infer negative-side, vertical, 10-degree, or laboratory-grade
behaviour from it.

At `0 degree`, centre the baffle over the jig's vertical rotation axis in the
baffle plane. Positive means anti-clockwise viewed from above. Keep the
microphone fixed at tweeter-centre height and `1.000 m` from the baffle-plane
pivot; do not move, swing, or re-aim it as the cabinet rotates. Secure the
cabinet at every mark.

## 2. Common No-Excitation Audit

Use the qualified UMC22 settings: V5.40 beta 133, Java `Stereo only`, exact
exclusive UMC22 input/output, `48 kHz`, L/L/L/R, loopback as calibration and
timing reference, loopback IR merge off, timing offset `0.0000 ms`, and
`ECM8000_calibration_data.csv` on microphone L only. Prepare each named sweep
at `20-20000 Hz`, `-20 dBFS`, `256k`, one repetition, with clipping abort
enabled. Keep Generator and other application audio stopped except for an
explicitly approved Measure action.

At the start of a day or after a material electrical, power, endpoint, geometry,
or anomaly change, obtain one current confirmation of normal silent operation,
secure microphone/jig, and relevant driver topology. Use a read-only REW API
snapshot when available only to corroborate software state.

## 3. Woofer Batch

Connect the woofer alone through NL4 `1+`/`1-`, with the qualified
clamp/attenuator directly across it to `INST 2`; keep the tweeter and protection
capacitor out of circuit. Before power-up confirm plausible resistance at the
measurement plane, no strain/short, and the U1282A in high-impedance voltage
mode if used. Use the safe startup and stop rules in the
[woofer runbook](UMC22_INSTALLED_WOOFER_FRD.md).

With Generator stopped, rotate and secure at `+20`, `+40`, then `+60 degrees`.
Run only the explicitly approved named sweep at each angle. Between sweeps check
the angle mark, security, fixed microphone/jig, silence, and any anomaly. Save
only the three new measurements to a fresh raw archive; never include retained
on-axis sources or API-loaded duplicates.

## 4. Protected-Tweeter Batch

A woofer-to-tweeter change is a topology change. With signals stopped, lower
volume, switch the amplifier off, disconnect woofer feed, restore the measured
`10.13 uF`, `0.08 ohm` ESR protection capacitor, and connect the fixture across
the tweeter after it through NL4 `2+`/`2-`. Recheck the protection topology and
perform a new no-excitation audit after power-up. Use the safe startup and stop
rules in the [tweeter runbook](UMC22_INSTALLED_TWEETER_FRD.md).

Run only the approved `+20/+40/+60 degree` titles, retaining exactly the three
new measurements in a fresh raw archive. The protected-tweeter model scale
remains `+11.14 dB` magnitude only.

## 5. Review, Export, And Stop Rules

Do not export before signal-free review under [FRD measurement method](../FRD_MEASUREMENT_METHOD.md).
Verify each title/identity, native unsmoothed grid, loopback timing, direct
arrival, first material reflection, and REW-native window. Do not align peaks,
apply an IR shift, or overwrite the phase-bearing on-axis design FRD.

Use the established polar windows: woofer `Hann 2.0 ms` left / `Tukey 0.25
3.5 ms` right; protected tweeter `Hann 2.0 ms` left / `Tukey 0.25 1.5 ms`
right; each at its own exact direct peak, FDW/MTW off. Export under the separate
per-driver `polar/` subdirectory and interpret only the stated bands.

Stop, de-energise safely, and retain the failed measurement for any clipping,
REW warning, dropout, abnormal sound, instability, heat, smell, smoke, spark,
tingle, cabinet/jig/microphone movement, loose cable, or other anomaly. A
failed angle stops the rest of that batch pending review.
