# UMC202HD Installed-Driver FRD — Suspended Route

Lifecycle: **CURRENT PROCEDURE — SUSPENDED**
Current approved action: none involving a UMC202HD sweep on the desktop.
Resumption owner: the diagnostic boundary in
[`../UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md`](../UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md).
Last reviewed: 2026-09-06

## 1. Scope And Suspension Decision

This file preserves the last coherent UMC202HD full-dual configuration and the
minimum conditions for resuming it. It is not authority to reinstall a driver,
power the measurement chain, or repeat the failed desktop permutations.

**VERIFIED OBSERVATION — 2026-09-03:** the UMC202HD powered no-signal check
passed and the chain reached a clean `1.00 V RMS` across the woofer. The source
stream then muted for roughly `100-300 ms` every `1-3 s`. The same class of
dropout occurred with REW ASIO, REW Java/WASAPI, and ordinary Windows music.
Because the output stream is not stable, no UMC202HD sweep from this desktop is
valid for timing or response work.

The passive reference fixture retains its electrical release; the dropout does
not revoke that release. Host/interface stability and passive-fixture safety are
separate conclusions.

## 2. Last Valid Physical Topology

The intended full-dual route was:

```text
ECM8000 -> UMC202HD Input 1 / USB input L -> REW measurement input

REW output L -> UMC202HD Output 1 -> mapped cable -> SU-V570 AUX left
             -> selected speaker output -> installed woofer

same SU-V570 speaker terminals -> qualified reference fixture
                                -> UMC202HD Input 2 central TRS / USB input R
```

UMC202HD Output 2 remained physically empty. The fixture reference plane was
the amplifier output, not the driver terminals. The woofer and fixture were in
parallel on the same selected amplifier channel and speaker bank. The true-RMS
meter, not the fixture, established `1.00 V RMS` at the woofer.

All amplifier, loudspeaker, fixture, and TRS connections were to be made with
the SU-V570 off. Input 2 used its central 1/4-inch TRS `LINE` path; the XLR
contacts remained unused. The ECM8000 was connected to Input 1 before phantom
was enabled. `DIRECT MONITOR` and both pads were off. Output 2 and headphones
were unused.

For current fixture inspection, connection, startup, and stop rules, use
[`../fixtures/REFERENCE_FIXTURE_USE.md`](../fixtures/REFERENCE_FIXTURE_USE.md).
Do not rely on the dated development narrative as an operating procedure.

## 3. Last Coherent REW Configuration

The preserved checkout configuration was:

| Setting | Last coherent value |
| --- | --- |
| REW version | V5.40 beta 133 |
| Driver | Behringer UMC ASIO |
| Converter/sample handling | UMC202HD `24 bit`; treat 32-bit container as 24-bit where presented |
| Sample rate | `88.2 kHz` |
| Measurement output | Output L / `1: Out 1` |
| Timing-reference output | Output L / `1: Out 1` |
| Measurement input | Input L / `1: In 1` |
| Electrical-reference input | Input R / `2: In 2` |
| Timing mode | `Use loopback as cal and timing reference` |
| Loopback treatment | `Merge loopback response into IR` was the historical UMC202HD plan |
| Separate soundcard calibration | None |
| Initial timing offset | `0.0000 ms` |
| Initial sweep range | `5-41000 Hz` |
| Initial sweep level | `-20 dBFS` |
| Sweep length/repetitions | `1M`, one repetition |
| Clipping abort | enabled |

The original no-excitation setup selected timing-reference Output R / Output 2.
That assignment is **superseded**: later full-dual evidence proved that an
electrical reference sensed from physical Output 1 requires both measurement
and timing-reference outputs to be L. Reference input remains R. Do not revive
the old R-output setting.

The UMC22 calibration and gain settings do not transfer to this interface.
Before any resumed UMC202HD capture, select the exact active UMC202HD device and
input, recreate or verify any interface/rate-specific calibration, and confirm
the ECM8000 calibration against Input 1 in both Measure and Measurement Info.

## 4. Conditions Required Before Resumption

All of the following are mandatory:

1. Complete the high-information host discriminator in the dropout authority:
   boot a current live Linux environment on the affected desktop and run a
   bounded playback/control test without altering the installed Windows system.
2. Identify a selected host/driver path that completes a proportionate,
   dropout-free control. Stability on the Windows 11 laptop may establish a
   usable alternative host, but it does not explain or silently clear the
   desktop fault.
3. Record the exact OS, driver, USB path, sample rate, buffer, and observed test
   duration. Do not infer sweep stability from device enumeration alone.
4. Confirm the fixture still has `Approved for amplifier use: YES` under
   [`../qualification/REFERENCE_FIXTURE_QUALIFICATION_2026-09-01_TO_03.md`](../qualification/REFERENCE_FIXTURE_QUALIFICATION_2026-09-01_TO_03.md).
   If any fixture part or cable changed, re-run only the affected qualification
   gates before connection.
5. Use the current fixture operating file for a switched-off physical audit,
   connection, USB/phantom no-signal observation, and minimum-volume amplifier
   power-up.
6. Re-establish the complete L/L/L/R channel matrix without excitation. Confirm
   the exact input/output identities, common `88.2 kHz` rate, calibration
   identities, timing mode, and zero initial offset.
7. Make one bounded level/control check. At `1.00 V RMS` woofer voltage, require
   the protected reference to remain broadly near `0.10 V RMS`, with adequate
   headroom and no clipping, dropout, noise instability, heat, smell, or other
   abnormality.
8. Authorise only one checkout sweep, then stop for headroom, metadata, impulse,
   ETC, timing, and dropout review before any repeat series.

## 5. Tests Not To Repeat Routinely

Do not repeat driver reinstallations, ASIO-versus-Java permutations, sample
rates, buffer changes, already-tested USB ports/cables, nonessential peripheral
removal, legacy-disk removal, or broad power-plan changes merely because the
route is suspended. Those branches did not identify a useful cause. Re-open one
only if new evidence gives it a discriminating hypothesis.

Do not load UMC22 chronology to resume this route. Its interface-specific
contact map, phantom isolation, gains, calibration path, and Java `Stereo only`
behaviour do not qualify the UMC202HD.

## 6. Stop Rules And Deferred Work

Stop for any source mute, warning, hardware clip, unstable reference, abnormal
sound, unexpected continuity, heating, smell, smoke, spark, or perceptible
tingle. A single dropout blocks the capture; do not average through it.

Raw-tweeter and polar work remain separate even after UMC202HD stability is
restored. They require their own protection, sweep limits, and geometry gates.
The detailed 2026-09-03 to 2026-09-05 development record is retained only at
[`../history/FRD_REPEATABILITY_DEVELOPMENT_2026-09-03_TO_05.md`](../history/FRD_REPEATABILITY_DEVELOPMENT_2026-09-03_TO_05.md).
