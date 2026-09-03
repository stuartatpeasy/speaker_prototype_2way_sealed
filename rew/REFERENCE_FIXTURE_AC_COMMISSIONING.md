# Reference Fixture AC Commissioning

Date prepared: 2026-09-03

Status: **INTERCONNECT PREFLIGHT IN PROGRESS; SOURCE ADAPTOR AND INLINE BREAKOUT
MAPS PENDING; NO AC TRACE CAPTURED; AMPLIFIER USE NOT YET APPROVED**

This is the current procedure and exact resume point for the last electrical
gate on the SU-V570-to-UMC202HD reference fixture. The SU-V570, loudspeaker,
microphone, and normal playback path are absent: UMC202HD Output 2 temporarily
substitutes for the amplifier and drives the fixture at low voltage.

Use the following companion records only when their detail is needed:

- fixture construction, calculations, and release state:
  [SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md);
- completed qualification evidence:
  [SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md); and
- subsequent installed acoustic test:
  [FRD_MEASUREMENT_SETUP_TEST.md](FRD_MEASUREMENT_SETUP_TEST.md).

## 1. Current Gate And Next Actions

All earlier topology, phantom-isolation, construction, resistance, clamp, and
ground-path gates pass. Both UMC202HD rear outputs are mechanically TRS but
electrically TS: their distinct ring and sleeve contacts share a PCB copper
fill. Output 2 must therefore drive the fixture asymmetrically from tip and the
ring/sleeve common; it is not a two-active-leg balanced source.

Complete these actions in order:

1. build and resistance-map the Output 2 source adaptor;
2. build and resistance-map the female-to-male inline TRS breakout;
3. capture matched direct and fixture transfer traces plus no-signal spectra;
4. record the results in Section 5; and
5. approve amplifier use only if every criterion passes.

Do not connect the fixture to a powered amplifier before this record and the
main fixture release gate both say `PASS`/`YES`.

## 2. Measurement Principle

Use the same interface, Input 2, inline breakout, REW settings, and gain/control
positions for two sequential paths:

```text
DIRECT BASELINE
UMC202HD Output 2 -> mapped male-to-male TRS patch cable
                   -> mapped inline TRS breakout -> Input 2 central TRS

FIXTURE RUN
UMC202HD Output 2 -> mapped asymmetric source adaptor -> fixture red/black
fixture male TRS  -> same inline TRS breakout -> Input 2 central TRS
```

The direct patch cable is not an extension for the fixture. Remove it for the
fixture run, but leave the inline breakout connected to Input 2 throughout.

Let $O(f)$ be the UMC202HD output path, $I(f)$ the Input 2 path, $P(f)$ the
direct patch cable, $B(f)$ the inline breakout, $A(f)$ the source adaptor, and
$H_{fixture}(f)$ the complete fixture:

$$
D(f)=O(f)P(f)B(f)I(f),
$$

$$
F(f)=O(f)A(f)H_{fixture}(f)B(f)I(f).
$$

Therefore:

$$
\frac{F(f)}{D(f)}=H_{fixture}(f)\frac{A(f)}{P(f)}.
$$

Subtracting the direct trace from the fixture trace in decibels, and subtracting
their phases, cancels the common interface and breakout responses. The short
source adaptor and direct cable do not cancel, but their mapped residuals are
small; investigate them if the measured result approaches a pass limit.

This comparison measures loaded attenuation, polarity, frequency/phase
flatness, linearity, clamp inactivity, and pickup from the fixture's unscreened
output tail. It does not measure the SU-V570, loudspeaker, microphone, acoustic
path, or noise that appears only in the complete powered system.

## 3. Interconnect Construction And Preflight

Perform every resistance test with all items loose on the bench, unpowered, and
disconnected from USB. Use nulled meter leads. Insulate permanent joints and
attach or move meter leads only with the signal stopped.

### 3.1 Output 2 Source Adaptor

Connect Output 2 tip to fixture red and output common to fixture black. Either
of these implementations is valid:

- a TS plug: tip to red, sleeve to black; or
- a TRS plug: tip to red, sleeve to black, with ring open or deliberately
  joined to sleeve.

Ring must never connect to red. Record the implementation actually built. A
low resistance on each intended path and open red-to-black/cross-contact paths
are required before USB connection or signal generation.

### 3.2 Direct-Baseline Patch Cable

The approximately `1 m` lightweight Sony male-to-male TRS cable has already
passed with an Agilent U1282A and nulled leads:

| Path | Resistance |
| --- | ---: |
| Tip to tip | `0.345 ohm` |
| Ring to ring | `0.337 ohm` |
| Sleeve to sleeve | `0.320 ohm` |
| Every cross-contact path | `OPEN` |

Its differential loop resistance is `0.345 + 0.337 = 0.682 ohm`. Even into a
deliberately conservative hypothetical `1 kohm` load, that adds only
approximately `0.0059 dB` attenuation. The cable is accepted; do not repeat its
map unless it is damaged or altered.

### 3.3 Inline TRS Breakout

The approved topology is:

```text
female inline TRS socket -> short screened cable -> restrained three-node
T/R/S screw-terminal block -> short screened cable -> male TRS plug
```

Use two-insulated-core screened cable: tip and ring use the cores and both cable
screens meet only at the sleeve node. Keep the total cable and every stripped
length short; approximately `0.5 m` total is a construction target, not a
separately verified limit. Restrain the insulating terminal block, provide
strain relief, keep T/R/S junctions independent, and prevent screws, screens,
or strands from bridging nodes.

A machined conductive enclosure is not required for the proposed approximately
`5 cm` compact terminal break. Keep it away from mains leads, power supplies,
and transformers. A removable insulated screen bonded only to sleeve is a
contingency if the matched no-signal test reveals position-, hand-, or
movement-sensitive pickup.

The quantitative margin is large. The post-stress fixture values give
approximately `0.903 kohm` tip and `0.905 kohm` ring source resistance, or
`1.808 kohm` differential. An illustrative `100 pF` directly between tip and
ring produces:

```text
f_c = 1 / (2 pi x 1.808 kohm x 100 pF) = 880 kHz
```

This would cause only about `0.009 dB` loss at `41 kHz`. For an illustrative
`1 cm^2` loop at `50 Hz`, magnetic pickup is `0.031`, `0.314`, or `3.14 uV`
for fields of `1`, `10`, or `100 uT`; a conventional conductive box would not
remove that low-frequency magnetic term. Electric-field pickup is less
predictable, which is why the identical-breakout no-signal comparison is the
acceptance evidence rather than an assumed screening benefit.

Do not reuse the phantom-isolation adaptor containing `100 kohm` loads: this
breakout must be straight through.

### 3.4 Preflight Record

| Interconnect | Same-contact resistance | Cross-contact paths | Decision |
| --- | --- | --- | --- |
| Direct male-to-male TRS cable | T/T `0.345 ohm`; R/R `0.337 ohm`; S/S `0.320 ohm` | All open | PASS, 2026-09-03 |
| Output 2 source adaptor | PENDING | PENDING | PENDING |
| Female-to-male inline TRS breakout | PENDING | PENDING | PENDING |

For the source adaptor, record plug type plus tip/red, ring/red, sleeve/red,
tip/black, ring/black, sleeve/black, and red/black. For the inline breakout,
record female-to-male T/T, R/R, and S/S plus all six cross-contact combinations.
Stop on any unintended low-resistance path.

Source-adaptor detail:

| Output 2 plug contact / fixture lead | Red | Black |
| --- | ---: | ---: |
| Tip | PENDING; low | PENDING; open |
| Ring (`N/A` for TS) | PENDING / N/A; open | PENDING / N/A; open or low only if deliberately commoned |
| Sleeve | PENDING; open | PENDING; low |

Red-to-black resistance: **PENDING; must be open**.

Inline-breakout detail:

| Female contact / male contact | Tip | Ring | Sleeve |
| --- | ---: | ---: | ---: |
| Tip | PENDING; low | PENDING; open | PENDING; open |
| Ring | PENDING; open | PENDING; low | PENDING; open |
| Sleeve | PENDING; open | PENDING; open | PENDING; low |

## 4. AC Transfer And Noise Procedure

### 4.1 Preparation

1. Keep the SU-V570, loudspeaker, microphone, playback cable, and every other
   analogue connection absent. Leave phantom power off.
2. Set Input 2 to `LINE`, `PAD` off, `GAIN 2` fully down, `DIRECT MONITOR` off,
   and `OUTPUT` fully down.
3. Connect the UMC202HD directly to USB and select its ASIO driver at `24 bit`,
   `88.2 kHz`.
4. Use Output 2 and Input 2 only. Begin at low level and verify channel identity
   and absence of clipping before raising either control.
5. Select no timing reference and clear any unrelated soundcard calibration.
   Use REW's `Set t=0 at IR peak` option identically for both traces. A REW
   loopback timing reference requires a physical connection on another output/
   input channel; none is part of this procedure. If a repeat direct trace does
   not reproduce phase after the same t=0 operation, do not approve phase until
   a separately mapped Output 1-to-Input 1 timing loop is added or the cause is
   otherwise resolved.

### 4.2 Matched Measurements

1. With the signal stopped, connect the mapped source adaptor, fixture, and
   inline breakout to Input 2. Attach the meter to the required points before
   starting each `1 kHz` tone.
2. Starting at low output, record red-to-black input and tip-to-ring output at
   one intermediate level and again at the highest clean level no greater than
   approximately `100 mV RMS` fixture output. Calculate `k_loaded` and
   `A_loaded` at both levels:

   ```text
   k_loaded = V(tip-ring) / V(red-black)
   A_loaded = 20 log10(k_loaded)
   ```

   Confirm proportional scaling within meter uncertainty. Stop the tone before
   moving either meter connection. Leave the final digital level and `OUTPUT`
   position unchanged.
3. Stop the signal and replace the fixture/source-adaptor path with the passed
   direct TRS cable, leaving the breakout connected to Input 2. With `GAIN 2`
   still fully down, confirm the direct signal has at least `6 dB` headroom.
   If it does not, reduce the one common output level and repeat both DMM
   fixture readings; never use different source or input settings for the two
   traces.
4. Capture and save a direct `5 Hz-41 kHz`, `88.2 kHz` trace. Apply the defined
   t=0 operation. Stop the generator and save a direct-path no-signal spectrum
   with fixed RTA/FFT settings.
5. Without changing digital level, `OUTPUT`, `GAIN 2`, REW settings, or the
   breakout-to-Input 2 connection, stop the signal and remove the direct cable.
   Reconnect Output 2 to fixture red/black through the mapped source adaptor and
   insert the fixture TRS plug into the breakout.
6. Capture and save the fixture trace, applying the same t=0 operation. With the
   generator stopped and every setting unchanged, save the fixture-connected
   no-signal spectrum.
7. Subtract direct magnitude and phase from the fixture trace. Record the REW
   relative gain at `1 kHz` and compare it with the final DMM result. Inspect
   polarity, phase, `20 Hz-20 kHz` flatness, and the `5 Hz-41 kHz` endpoints.
   The loaded gain should not exceed the unloaded `-20.094 dB` prediction beyond
   measurement uncertainty. Extra attenuation is possible because the UMC202HD
   line-input impedance is unpublished; investigate more than approximately
   `1 dB` rather than changing the resistor model.
8. Compare the two no-signal spectra at `50 Hz`, `100 Hz`, their harmonics,
   broadband noise, and any movement-sensitive feature. The fixture's
   unscreened tail makes this a release criterion.
9. If the phase comparison is suspicious or close to a limit, restore the
   direct path without moving the breakout or controls and capture a second
   direct trace. The two direct traces must reproduce after the same t=0
   operation before fixture phase is interpreted.
10. Save the direct, fixture, optional repeat-direct, and both no-signal
    captures together, with all settings and filenames recorded below.

## 5. Acceptance And Results

Pass only with:

- correct polarity;
- DMM and REW `1 kHz` attenuation agreeing within `0.2 dB`;
- no gain above the passive unloaded prediction beyond uncertainty;
- adequate Input 2 headroom and no dropout or clipping;
- no unexplained relative magnitude variation greater than `0.1 dB` over
  `20 Hz-20 kHz`;
- reviewed phase and `5 Hz-41 kHz` endpoint behaviour without clamp-capacitance
  resonance or material roll-off;
- linear scaling near the intended `100 mV RMS` output with clamps inactive;
  and
- no material added `50/100 Hz` family, coherent spur, broadband rise, or
  intermittent movement-sensitive pickup.

Review the measured no-signal spectra rather than assigning an unsupported
microvolt limit in advance.

| AC check | Result |
| --- | --- |
| Direct trace filename | PENDING |
| Fixture trace filename | PENDING |
| Direct no-signal filename | PENDING |
| Fixture no-signal filename | PENDING |
| Optional repeat-direct filename | PENDING / NOT REQUIRED |
| Unloaded resistor prediction at `1 kHz` | `-20.094 dB` |
| Intermediate DMM input / output / gain at `1 kHz` | PENDING |
| Final DMM input / output / loaded gain at `1 kHz` | PENDING |
| DMM gain change with level | PENDING |
| REW-relative gain at `1 kHz` | PENDING |
| DMM/REW agreement | PENDING |
| Relative variation, `20 Hz-20 kHz` | PENDING |
| Endpoint/phase review | PENDING |
| Direct phase repeatability, if required | PENDING / NOT REQUIRED |
| Direct-versus-fixture no-signal comparison | PENDING |
| Polarity | PENDING |
| Linear; clamps inactive near `100 mV RMS` | PENDING |
| Overall AC decision | NOT PERFORMED |

## 6. Release Consequence

If any criterion fails, stop and diagnose the fixture, adaptors, breakout, or
interface before amplifier connection. If every criterion passes:

1. mark this record `PASS` with the retained trace filenames and numerical
   results;
2. change the main fixture record to `Approved for amplifier use: YES`;
3. update `README.md`, `DRIVER_ANALYSIS.md`, and the acoustic setup gate; and
4. proceed to the installed full-dual setup under
   [FRD_MEASUREMENT_SETUP_TEST.md](FRD_MEASUREMENT_SETUP_TEST.md).

## 7. REW Method Reference

REW's official measurement documentation defines the no-reference t=0 options
and explains that a loopback timing reference requires the other interface
channel to be physically looped from output to input:
<https://www.roomeqwizard.com/help/help_en-GB/html/makingmeasurements.html>
