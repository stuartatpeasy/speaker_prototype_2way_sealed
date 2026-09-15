# UMC22 Seed A Full-System Level And Thermal Validation

| State | Value |
| --- | --- |
| Lifecycle | **COMPLETED PROCEDURE / RETAINED REPEAT ROUTE** |
| Owns | The controlled full-system distortion, compression, and external-crossover thermal method used for Seed A |
| Does not own | Detailed results, raw-driver qualification, absolute-SPL calibration, impedance/EPDR, crossover redesign, or final production limits |
| Read when | Auditing the method, deliberately repeating speaker one after an anomaly, or adapting the route for speaker two |
| Current approved action | No further signal on speaker one. A future run requires a fresh current-state report and the applicable no-signal audit |
| Planned ceiling | If deliberately repeated, no more than `4.000 V RMS` at the loudspeaker input, subject to the user's earlier loudness stop |
| Next gate | Apply the route to speaker two, including a correct immediate hot `0-degree` comparison; repeat speaker one only if speaker-two evidence reveals an anomaly |
| Limitations | One prototype and one listening position; generic ECM8000 response calibration rather than absolute SPL calibration; contact temperatures do not measure voice-coil temperature; no vertical or negative-horizontal coverage |
| Last reviewed | 2026-09-10 |

## 1. Purpose And Proportionate Boundary

This procedure tests the normal-polarity, complete Seed A loudspeaker at a
fixed `1 m` tweeter-axis position. It uses four matched log sweeps at
`0.500`, `1.000`, `2.000`, and no more than `4.000 V RMS`, followed by one
moderate thermal exposure if the sweep series passes. It is a prototype gate,
not a laboratory power-rating programme.

The `4.000 V RMS` value is a ceiling. The user may stop at any lower level if
the volume is excessive. The highest clean completed level then becomes the
reported bounded result; stopping for comfort is not a hardware failure and
does not authorise a different signal to compensate.

Use the already qualified UMC22 and protected amplifier-reference fixture.
Do not repeat their qualification unless a relevant item has changed or a gate
fails. The StarTech USB interface may remain attached to the computer but its
DUT leads must be removed from Seed A and it must not be selected in REW for
this acoustic package.

## 2. Fixed Route And Settings

The physical route is:

```text
REW output L -> UMC22 Output 1 -> TS-to-RCA cable
             -> SU-V570 AUX left -> speaker bank B left -> Seed A input

SU-V570 B-left terminals -> qualified reference fixture -> UMC22 INST 2
ECM8000 -> UMC22 Input 1 XLR
```

At the B-left terminals, Seed A and the fixture input are in parallel. Fixture
red/`In+` and Seed A positive go to red; fixture black/`In-` and Seed A negative
go to black. The fixture does not carry loudspeaker current. Never connect the
amplifier output directly to `INST 2`.

Use these fixed settings for every sweep:

| Item | Setting |
| --- | --- |
| REW | `V5.40 beta 133`; Java `Stereo only` |
| Input and output | `EXCL: Behringer UMC22 (USB Audio CODEC)` |
| Sample rate | `48 kHz` |
| Measurement/timing outputs | `L` / `L` |
| Measurement/reference inputs | microphone `L` / fixture `R` — complete `L/L/L/R` route |
| Timing/calibration | use loopback as calibration and timing reference; make calibration data from loopback response |
| Loopback merge / timing offset | off / `0.0000 ms` |
| Input calibration | `ECM8000_calibration_data.csv` on microphone `L` only; no microphone file on reference `R` |
| Input-volume control | `1.00` |
| Sweep | `10-20000 Hz`, `-20 dBFS`, `1M`, one repetition, clipping abort on |
| Geometry | microphone capsule `1000 mm` from baffle plane on tweeter axis; cabinet and microphone fixed at `0 degrees` |
| Loudspeaker | complete Seed A, both drivers connected, normal tweeter polarity |

Starting below `20 Hz` reduces the artificial low-frequency distortion rise
that a band-limited impulse can create. The `1M` sweep improves separation of
the harmonic impulses. There is only one sweep per level because the UMC22
input and output share a clock and the planned signal-to-noise ratio is ample.

UMC22 `OUTPUT` remains fully clockwise and `DIRECT MONITOR` remains off. The
two input gains are fixed for the entire comparison only after the headroom
step in Section 4. The SU-V570 uses `AUX`, tone `DEFEAT`, loudness off,
`POWER AMP DIRECT` off, and speaker bank B left only. Output 2, headphones,
AUX right, and other speaker channels remain unused.

## 3. One De-Energised Setup And Ready Report

Complete all of this before reporting back. It is one setup gate, not a series
of per-connector confirmations.

1. Stop REW Generator, Check Levels, and Measure, and stop other application
   audio. Leave the SU-V570 off with its volume fully down.
2. Remove the StarTech jig's two DUT connections from Seed A. The StarTech USB
   connection may remain in place.
3. With the SU-V570 off, connect the complete normal-polarity Seed A input and
   the qualified reference fixture in parallel to B-left as specified above.
   Connect the fixture output to UMC22 `INST 2`.
4. Connect UMC22 Output 1 to SU-V570 AUX left. Connect the ECM8000 by XLR to
   Input 1 before phantom is enabled. Leave the unused sockets and channels
   empty as listed in Section 2.
5. Put the cabinet and microphone at the fixed `0 degree`, `1 m` tweeter-axis
   geometry. Keep the room and nearby objects fixed; close the nearby window.
6. With no signal and no power, secure the U1272A Type-K contact probe to the
   insulating body of one central R(Tser) `5.6 ohm` resistor. Keep all probe
   metal clear of leads, terminals, adjacent parts, and possible movement.
   Use electrically insulating, heat-tolerant restraint. Do not rely on hand
   pressure during the test.
7. With no signal and no power, clip the U1282A across the Seed A input in
   true-RMS AC-voltage mode. The clips must be insulated, secure,
   correctly polarised, and unable to bridge or fall onto the crossover.
8. Inspect only the newly made connections and probe restraints. Stop for a
   loose strand, exposed conductor, damaged insulation, insecure probe, wrong
   polarity, or changed/damaged fixture.

The one ready report should confirm: generator stopped; SU-V570 off/minimum;
StarTech DUT leads removed; complete normal-polarity Seed A and fixture on
B-left; UMC22/ECM8000 route complete; fixed `1 m` tweeter-axis geometry;
U1272A probe secure on insulated R(Tser); U1282A securely across the Seed A
input; and no anomaly. No unchanged wiring recital will be requested again
within the batch unless something changes or fails.

**COMPLETION NOTE — 2026-09-10:** this setup gate and the bounded powered
package were completed without a reported wiring or equipment anomaly. The
current result belongs in the [qualification
record](../qualification/SEED_A_FULL_SYSTEM_LEVEL_AND_THERMAL_QUALIFICATION_2026-09-10.md).
This paragraph is not a standing signal release: before a deliberate repeat,
obtain the then-current physical state and apply the no-signal gate again.

## 4. Startup, Headroom, And Voltage Setting

For a deliberate repeat or speaker-two adaptation, run this section only after
a fresh current-state report and the Section 3 no-signal gate pass.

1. With the SU-V570 still off, connect UMC22 USB, enable phantom, select the
   exact settings in Section 2, and set both input gains low. Confirm normal
   indicators and silence.
2. Power the SU-V570 at minimum with every generator stopped. Wait about
   `30 s`; stop for hum/buzz, a clip light, instability, unexpected heat,
   smell, or any abnormal sound.
3. Select a `1 kHz`, output-L sine at `-20 dBFS`. Start it at minimum amplifier
   volume, raise the SU-V570 slowly to `0.500 V RMS` at the Seed A input, then
   stop it. The complete crossover strongly attenuates the tweeter at `1 kHz`;
   nevertheless keep each tone only as long as needed to set voltage.
4. Run REW Check Levels at the `0.500 V RMS` position. It may produce the
   steady tone already observed on this REW version. Adjust UMC22 `GAIN 1` and
   `GAIN 2` only as needed so **both** channels have at least `24 dB` headroom,
   no clip indication, and a usable reading. Stop Check Levels.
5. Do not change either UMC22 input gain again during the series. If a gain
   must change later, repeat the `0.500 V RMS` baseline with the final gains.
6. Record initial R(Tser) surface temperature and room indication. Leave the
   U1282A voltage clips and U1272A temperature probe fixed for the sweep series.

At each later level, use the same brief `1 kHz`, `-20 dBFS` tone to set the
actual Seed A input voltage. Stop the tone before opening Measure and before
touching anything. Amplifier-knob position is a convenience only; the U1282A
reading owns the voltage.

## 5. Matched Sweep Series

Run these in order without a report between them:

| Order | Seed A input | Measurement name |
| ---: | ---: | --- |
| 1 | `0.500 V RMS` | `SPK_sA_full_000deg_t-axis_1m_U22_0.5V_<date>` |
| 2 | `1.000 V RMS` | `SPK_sA_full_000deg_t-axis_1m_U22_1.0V_<date>` |
| 3 | `2.000 V RMS` | `SPK_sA_full_000deg_t-axis_1m_U22_2.0V_<date>` |
| 4 | no more than `4.000 V RMS` | `SPK_sA_full_000deg_t-axis_1m_U22_4.0V_<date>` |

For each row: set voltage with the brief tone, stop the tone, run exactly one
matched sweep, confirm no REW or hardware clipping/warning, note the exact
voltage and R(Tser) temperature, and inspect the Distortion graph before moving
up. The user may end the series at any time for excessive volume.

The expected linear offsets from `0.500 V RMS` are:

```text
20 log10(1.000 / 0.500) =  6.0206 dB
20 log10(2.000 / 0.500) = 12.0412 dB
20 log10(4.000 / 0.500) = 18.0618 dB
```

When comparing fundamentals, subtract the applicable offset from each higher-
level trace. After normalisation, a broad loss greater than `0.5 dB` over
`200 Hz-10 kHz`, or a new level-dependent feature greater than `1 dB` through
`1.5-2.5 kHz`, requires review. A narrow point coincident with a room null or
noise floor is not a failure without corroboration.

The provisional distortion gate at the highest clean completed level is:

- no broad THD above `3%` from `100 Hz-10 kHz`;
- no broad third-or-higher harmonic above `1%` from `200 Hz-10 kHz`;
- no abrupt level-dependent harmonic hotspot around the crossover or tweeter
  band; and
- no audible rattle, buzz, harsh breakup, protection event, or clipping.

Below `100 Hz`, retain the result as excursion/room evidence rather than using
the same numerical gate. Narrow percentage spikes where the fundamental falls
into a room null must be checked against the absolute harmonic levels.

## 6. Moderate Thermal Exposure

Run this only if at least the `2.000 V RMS` sweep is clean. Omit it if the user
stopped below that level for loudness or any technical stop rule fired.

1. Stop all signals and turn the SU-V570 to minimum. In REW Generator select
   output `L`, **Pink Periodic Noise**, **CTA-2034**, `64k`, and `-20 dBFS`.
2. With the U1282A still across Seed A, start the noise at minimum volume and
   raise the amplifier slowly to `2.000 V RMS`. Record the knob position and
   stop the noise.
3. Turn the amplifier to minimum and off. Remove the U1282A voltage clips.
   Connect its Type-K contact probe to the insulating outer surface of L(W1),
   secure it as for R(Tser), and keep probe metal clear of winding lead-outs,
   terminals, and adjacent components.
4. Record ambient, R(Tser), and L(W1) baseline temperatures. Power the
   amplifier at minimum with the generator stopped, restore the recorded
   `2.000 V RMS` knob position, then start the noise. Do not leave the system
   unattended.
5. Record both component temperatures at `2`, `5`, `10`, and `15 min`, together
   with any audible change. Stop after `15 min`.

CTA-2034 noise has a `12 dB` crest factor. At `2.000 V RMS`, its nominal peak
is therefore

```text
Vpeak = 2.000 V * 10^(12/20) = 7.96 V,
```

which is about `3 dB` above the `5.66 V` peak of a `4.000 V RMS` sine while
holding average heating to the `2.000 V RMS` level. This is a useful but
proportionate programme-like thermal exposure, not a continuous `4 V RMS`
power test.

The thermal result passes directly if both measured surfaces remain at or
below `50 degrees C`, rise no more than `20 degrees C`, and rise no more than
`2 degrees C` during the final five minutes, with no other anomaly. A result
between that pass boundary and the stop boundary below is retained for review,
not silently called a pass or failure.

## 7. Immediate Post-Thermal Check And Retention

With the noise stopped, note both peak temperatures. Return the amplifier to
the recorded `0.500 V RMS` position and, within about one minute, run one sweep
named:

`SPK_sA_full_000deg_t-axis_1m_U22_PT_<date>`

Keep the same gains, route, geometry, and sweep settings. A sweep made at the
wrong angle or distance is invalid for this comparison: mark it excluded and
do not relabel or reuse it as intentional directional evidence. After
normalisation,
a broad post-thermal loss above `0.5 dB` over `200 Hz-10 kHz`, or a new
`1.5-2.5 kHz` shape change above `1 dB`, requires review. If that occurs, let
the system cool to within `2 degrees C` of both recorded baselines and make
one recovery sweep; otherwise no cooled repeat is required.

Save the complete package as
`rew/SPK_Seed_A_full_system_level_thermal_<date>.mdat`. Record exact completed
voltages, the highest attempted/completed level, any user loudness stop,
headroom and warnings, both temperature series, measurement names, room state,
and departures from this procedure. Do not export many derivative files until
the retained MDAT has been reviewed.

## 8. Common Stop Rules

Stop the signal immediately and reduce amplifier volume for any of these:

- the user judges the volume excessive;
- REW or either UMC22 channel reports clipping, a hardware clip LED lights, or
  the electrical reference drops out;
- new rattle, buzz, scraping, harsh breakup, intermittent distortion, amplifier
  protection, instability, or unexpected silence;
- smoke, smell, softening, discoloration, insecure probe/tape, exposed metal,
  or a component/cable that is becoming unexpectedly hot;
- either measured surface reaches `60 degrees C`, rises `30 degrees C` above
  baseline, or continues rising rapidly without beginning to level; or
- any connection, meter lead, thermocouple, cabinet, microphone, or control
  moves.

Do not touch the crossover, meter leads, probes, or loudspeaker connections
with a signal present. A loudness stop is an acceptable bounded endpoint. For
a technical stop, retain the result and investigate the specific cause before
another signal; do not automatically restart at a lower level.

## 9. Result Authority

This file is the completed operating route, not a work log. The first
speaker's results and calculations are owned by the [dated qualification
record](../qualification/SEED_A_FULL_SYSTEM_LEVEL_AND_THERMAL_QUALIFICATION_2026-09-10.md).
Its immediate post-thermal trace is excluded for wrong geometry, and the user
has deferred a correct replacement to the speaker-two test. Keep future
results in their own dated evidence record rather than appending chronology
here.

## 10. Primary Method Sources

- [REW Distortion Graph](https://www.roomeqwizard.com/betahelp/help/html/graph_distortion.html)
- [REW Signal Generator](https://www.roomeqwizard.com/betahelp/help/html/siggen.html)
- [REW Making Measurements](https://www.roomeqwizard.com/betahelp/help/html/makingmeasurements.html)
- [Qualified reference-fixture use](../fixtures/REFERENCE_FIXTURE_USE.md)
