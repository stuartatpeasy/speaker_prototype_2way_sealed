# StarTech Seed A Complete-System Impedance and Phase

| State | Value |
| --- | --- |
| Lifecycle | **COMPLETED PROCEDURE — CAPTURE PASSED** |
| Owns | Proportionate connection, capture, stop rules, retention, and handoff to load/EPDR analysis |
| Does not own | Driver baselines, crossover topology, acoustic validation, or qualification chronology |
| Current approved action | None for the unchanged impedance setup; do not repeat the passed sweep without a design-relevant reason |
| Result | [Seed A as-built impedance and EPDR](../qualification/SEED_A_AS_BUILT_IMPEDANCE_AND_EPDR_2026-09-09.md) — load gate passed |
| Next gate | Controlled full-system distortion/compression and thermal validation at the required listening level |
| Audit only if needed | [StarTech impedance-route qualification](../qualification/STARTECH_IMPEDANCE_ROUTE_QUALIFICATION_2026-09-09.md) |
| Last reviewed | 2026-09-09 |

## 1. Qualified route

All retained project impedance measurements used the StarTech ICUSBAUDIO2D
generic external USB sound card. Continue with it for consistency.

| Setting | Qualified value |
| --- | --- |
| REW input device | `EXCL: StarTech USB audio interface (USB Audio Device)` |
| REW output device | `EXCL: StarTech USB audio interface (USB Audio Device)` |
| Output channel | `R` |
| Reference input | `R` |
| Measurement input | `L` |
| Sample rate | `48 kHz` |
| Sense resistor | `100.00 ohm` |
| Sweep | One `1M` logarithmic sweep at `-12 dBFS` |
| Analysis span | `10 Hz-20 kHz`, no smoothing; the completed capture retains the native dense export |
| Established Seed A level | `14.7 mV RMS` at the input during Check Levels, with no clipping |

The jig is a `5 V` USB-powered measurement system. It is not necessary to
unplug or reconnect the StarTech interface for ordinary load changes. Stop the
REW Generator before changing the DUT connection; this is sufficient for the
normal qualified workflow.

The current open/short/reference calibration passed a `6.755 ohm` nulled-DMM
control check at `6.72 ohm` (`-0.52%`) with a flat `0 degree` phase trace. Carry
that calibration and the settings above forward while the interface path,
channels, gains, leads, sample rate, and sense resistor remain unchanged.

Recalibrate only after a relevant route change or if a known-load result,
warning, or implausible trace gives a specific reason. A new chat, application
restart, elapsed time, or unchanged DUT swap is not such a reason.

## 2. Passed one-batch Seed A capture

The recent state is carried forward: Seed A remains complete with normal
tweeter polarity, and the powered-off SU-V570 was disconnected for the jig
work. Do not request a fresh recital unless the user reports a change.

1. Stop REW Generator. Leave the StarTech USB interface connected.
2. Replace the calibration resistor with the Seed A input: jig DUT positive to
   Seed A positive and jig DUT negative to Seed A negative.
3. At this actual connection transition, make one local sanity check: correct
   polarity, secure contacts without stray strands, and no amplifier lead in
   parallel. This need not be reported separately before proceeding.
4. If the qualified settings in Section 1 have not changed, do not repeat the
   device, wiring, calibration, resistance, or level qualification. The prior
   `14.7 mV RMS` Check Levels result remains applicable.
5. Run one complete-system impedance sweep using the Section 1 settings.
6. Stop and inspect the whole trace before any repeat. Save the raw REW
   measurement and export the unsmoothed ZMA if there was no stop condition.

The `1M/48 kHz` sweep lasts approximately

```text
1,048,576 samples / 48,000 samples/s = 21.845 s.
```

This is a small-signal characterisation measurement, not a compression or
thermal test.

## 3. Proportionate stop rules

Stop the sweep for:

- an REW clipping, lost-channel, or calibration warning;
- an obviously impossible, discontinuous, or unstable trace;
- a loose/shorting connection or discovery that the amplifier is still in
  parallel; or
- unexpected distress noise, smell, or heating.

At the established `14.7 mV RMS` DUT level from a `5 V` USB interface, repeated
power isolation, cold-resistance checks, staged micro-confirmations, and a new
Check Levels run do not add proportionate value when the route is unchanged.
Do not repeat a sweep merely to make an already coherent result look tidier.

## 4. Retention and completed analysis

The passed capture is retained as
[`rew/SPK_impedance_WT_1_20260909.mdat`](../../../rew/SPK_impedance_WT_1_20260909.mdat)
and
[`rew/SPK_impedance_both_drivers_run1_2026-09-09.zma`](../../../rew/SPK_impedance_both_drivers_run1_2026-09-09.zma).
The [owning evidence record](../qualification/SEED_A_AS_BUILT_IMPEDANCE_AND_EPDR_2026-09-09.md)
contains the verified metadata, file hashes, derived load metrics, EPDR method,
model comparison, and pass decision.

The completed derivation covers:

- minimum impedance magnitude and frequency;
- phase at that minimum and the largest relevant phase excursions;
- minimum real part of impedance;
- minimum equivalent peak dissipation resistance (EPDR), with its frequency,
  impedance magnitude, and phase; and
- comparison with the practical model's approximately `3.805 ohm` minimum and
  the existing `3.5 ohm` prototype model gate.

EPDR is an idealised class-B output-device dissipation metric, mainly relevant
to conventional class-AB amplifiers. It does not replace impedance magnitude
for output-current assessment and is not automatically transferable to
class-A or class-D amplifiers.

## 5. Primary method source

- [REW impedance measurement documentation](https://www.roomeqwizard.com/help/help_en-GB/html/impedancemeasurement.html)
