# Reference Fixture AC Commissioning

Date prepared: 2026-09-03

Last revised: 2026-09-05

Status: **PROPORTIONATE AC SANITY GATE PASS; APPROVED FOR CONTROLLED
POWERED-AMPLIFIER USE; FIRST FULL-DUAL CHECK CONFIRMS A SEPARATE DESKTOP
UMC202HD/UAC2-HOST PLAYBACK DROPOUT**

This is the completed standalone electrical-release record for the
SU-V570-to-UMC202HD reference fixture. It retains the original low-voltage
procedure and readings, followed by the proportionality decision that moves
remaining performance checks into the actual full-dual setup.

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
fill. Output 2 must therefore drive the clamp/attenuator asymmetrically from tip
and the ring/sleeve common; it is not a two-active-leg balanced source.

The release actions are complete:

1. retain the passed Output 2 source adaptor without alteration;
2. retain the passed breakout cable without alteration;
3. use the observed low-voltage `1 kHz` result only as a gross AC sanity check;
4. retain the detailed readings and the proportionality review below; and
5. evaluate noise, level, and dropout behaviour in the actual full-dual setup;
   no-signal and clean-level checks passed, while the separate UMC202HD desktop
   dropout failed measurement stability.

This record and the main fixture authority approve controlled UMC202HD powered-
amplifier use. Actual UMC202HD measurements remain suspended by the digital
dropout. The UMC22 alternative has its own pending interface gates.

### 1.1 Commissioning Terminology

Use these names throughout the live procedure:

- **straight-through cable:** the approximately `1 m` male-to-male TRS cable
  formerly called the Sony or direct-baseline cable; it has no breakout;
- **breakout cable:** female TRS to the restrained T/R/S terminal block to male
  TRS; it is straight through and provides the measurement nodes;
- **clamp/attenuator:** the complete protected approximately `-20 dB` passive
  network; its amplifier-side inputs are `In+` (red conductor) and `In-` (black
  conductor), and its output is the fixed male TRS plug;
- **source adaptor:** the mapped Output 2 TRS plug and two leads that connect
  Output 2 tip/common to clamp/attenuator `In+`/`In-`; and
- **reference fixture:** the umbrella project term for the protected amplifier-
  reference hardware. In live connection instructions, use the specific item
  names above rather than `fixture` alone.

## 2. Measurement Principle

The originally specified matched comparison used the same interface, Input 2,
breakout cable, REW settings, and gain/control positions for two sequential
paths:

```text
DIRECT BASELINE
UMC202HD Output 2 -> straight-through cable
                   -> breakout cable -> Input 2 central TRS

CLAMP/ATTENUATOR RUN
UMC202HD Output 2 -> source adaptor -> clamp/attenuator In+ and In-
clamp/attenuator male TRS -> same breakout cable -> Input 2 central TRS
```

The straight-through cable is not an extension for the clamp/attenuator. Remove
it for the clamp/attenuator run, but leave the breakout cable connected to Input
2 throughout.

Let $O(f)$ be the UMC202HD output path, $I(f)$ the Input 2 path, $P(f)$ the
straight-through cable, $B(f)$ the breakout cable, $A(f)$ the source adaptor,
and $H_{clamp}(f)$ the complete clamp/attenuator:

$$
D(f)=O(f)P(f)B(f)I(f),
$$

$$
C(f)=O(f)A(f)H_{clamp}(f)B(f)I(f).
$$

Therefore:

$$
\frac{C(f)}{D(f)}=H_{clamp}(f)\frac{A(f)}{P(f)}.
$$

Subtracting the direct trace from the clamp/attenuator trace in decibels, and
subtracting their phases, cancels the common interface and breakout responses. The short
source adaptor and straight-through cable do not cancel, but their mapped residuals are
small; they may be investigated if a practical full-dual result is anomalous.

This optional comparison can measure loaded attenuation, polarity, frequency/phase
flatness, linearity, clamp inactivity, and pickup from the clamp/attenuator's unscreened
output tail. It does not measure the SU-V570, loudspeaker, microphone, acoustic
path, or noise that appears only in the complete powered system.

### 2.1 Proportionality And Release Basis

**ENGINEERING DECISION - 2026-09-03:** the originally specified `0.2 dB` DMM/
REW agreement, `0.1 dB` broadband flatness, two-level linearity check, and
standalone no-signal captures were disproportionate as prerequisites for
electrical safety. They mixed two different questions:

1. **Can the path safely be connected to the SU-V570 and UMC202HD?** Yes. This
   is established by topology, phantom isolation, resistance matrices, four-
   polarity testing through `64.5 V DC`, the ground-path audit, connector maps,
   and the gross `1 kHz` attenuation check.
2. **Is the complete powered chain quiet, stable, and repeatable enough for
   useful acoustic data?** This belongs in the complete-system checkout.

The passive divider predicts `-20.094 dB`. The corrected low-voltage plateau
readings gave `-20.45 dB`; a deliberately conditional noise subtraction gave
`-20.15 dB`. Both establish attenuation of the intended approximately `-20 dB`
order, with no evidence of gain. Further millivolt-level refinement would not
materially improve the protection decision.

The first powered full-dual check passed the no-signal observation and reached
a clean `1.00 V RMS` at the woofer, but exposed a separate UMC202HD output-
stream dropout. Its extensive host diagnosis is owned by
[UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md](UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md).
That digital-source fault does not change the passive fixture's release.

The safety margin is not a fraction of a decibel. At an ideal waveform bounded
by the SU-V570's `+/-45.5 V` rails, the measured resistor network predicts about
`4.50 V peak` at either interface node. The UMC202HD's published `+20 dBu`
line-input level is `10.96 V peak`, and the independently tested clamp pairs
provide a second bound if a shunt fails. No further open-lead or shorted-lead
millivolt investigation is required for release.

## 3. Interconnect Construction And Preflight

Perform every resistance test with all items loose on the bench, unpowered, and
disconnected from USB. Use nulled meter leads. Insulate permanent joints and
attach or move meter leads only with the signal stopped.

### 3.1 Output 2 Source Adaptor

Connect Output 2 tip to clamp/attenuator `In+` and output common to
clamp/attenuator `In-`. The present conductors are red for `In+` and black for
`In-`. Either of these implementations is valid:

- a TS plug: tip to `In+`, sleeve to `In-`; or
- a TRS plug: tip to `In+`, sleeve to `In-`, with ring open or deliberately
  joined to sleeve.

Ring must never connect to `In+`. Record the implementation actually built. A
low resistance on each intended path and open `In+`-to-`In-`/cross-contact
paths are required before USB connection or signal generation.

**VERIFIED MEASUREMENT - 2026-09-03:** the built adaptor uses a TRS plug with
ring unconnected. With an Agilent U1282A in auto-ranging resistance
mode and the leads nulled before the first reading, tip-to-`In+` measured
`0.400 ohm` and sleeve-to-`In-` measured `0.370 ohm`. Tip-to-`In-`,
ring-to-`In+`, ring-to-`In-`, sleeve-to-`In+`, and `In+`-to-`In-` all
measured open.
The two intended paths are low resistance and every prohibited path is open;
the source adaptor therefore passes. Do not alter it without repeating its
complete map.

### 3.2 Straight-Through Cable

The approximately `1 m` lightweight male-to-male TRS straight-through cable has
already passed with an Agilent U1282A and nulled leads:

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

### 3.3 Breakout Cable

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

The quantitative margin is large. The post-stress clamp/attenuator values give
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

**VERIFIED MEASUREMENT - 2026-09-03:** the passed straight-through cable was
inserted into the breakout's female socket as a safe contact extension. With an Agilent
U1282A in auto-ranging resistance mode and the leads nulled before the first
reading, the complete cable-plus-breakout paths measured T/T `0.345 ohm`, R/R
`0.328 ohm`, and S/S `0.328 ohm`; all six cross-contact combinations measured
open. Subtracting the earlier cable-only readings nominally gives breakout
residuals of `0.000 ohm`, `-0.009 ohm`, and `+0.008 ohm`. The negative result is
not physical resistance: it establishes that contact/null/repeatability effects
of approximately `0.01 ohm` dominate this subtraction. Therefore do not claim
zero or negative breakout resistance. The directly measured complete paths are
low, stable, and correctly mapped, while every prohibited path is open; the
breakout cable passes its connectivity and isolation gate.

### 3.4 Preflight Record

| Interconnect | Same-contact resistance | Cross-contact paths | Decision |
| --- | --- | --- | --- |
| Straight-through cable | T/T `0.345 ohm`; R/R `0.337 ohm`; S/S `0.320 ohm` | All open | PASS, 2026-09-03 |
| Output 2 source adaptor | TRS, ring unconnected; T/`In+` `0.400 ohm`; S/`In-` `0.370 ohm` | T/`In-`, R/`In+`, R/`In-`, S/`In+`, and `In+`/`In-` all open | PASS, 2026-09-03 |
| Breakout cable, measured through passed straight-through cable | Combined T/T `0.345 ohm`; R/R `0.328 ohm`; S/S `0.328 ohm`; breakout residual below approximately `0.01 ohm` comparison repeatability | All six open | PASS, 2026-09-03 |

For the source adaptor, record plug type plus tip/`In+`, ring/`In+`,
sleeve/`In+`, tip/`In-`, ring/`In-`, sleeve/`In-`, and `In+`/`In-`. For the
breakout cable, record female-to-male T/T, R/R, and S/S plus all six
cross-contact combinations.
Stop on any unintended low-resistance path.

Source-adaptor detail:

| Output 2 plug contact / clamp input | `In+` (red) | `In-` (black) |
| --- | ---: | ---: |
| Tip | `0.400 ohm`; low | `OPEN`; pass |
| Ring (`N/A` for TS) | `OPEN`; pass | `OPEN`; unconnected; pass |
| Sleeve | `OPEN`; pass | `0.370 ohm`; low |

`In+`-to-`In-` resistance: **OPEN; pass**.

Breakout-cable detail:

| Female contact / male contact | Tip | Ring | Sleeve |
| --- | ---: | ---: | ---: |
| Tip | combined `0.345 ohm`; low | `OPEN`; pass | `OPEN`; pass |
| Ring | `OPEN`; pass | combined `0.328 ohm`; low | `OPEN`; pass |
| Sleeve | `OPEN`; pass | `OPEN`; pass | combined `0.328 ohm`; low |

## 4. Retained AC Transfer And Noise Procedure

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

**HISTORICAL CONFIGURATION NOTE:** the first attempt could not enumerate ASIO
because the Behringer driver had not been installed. Installing it resolved
enumeration and allowed this low-voltage check to complete. The vendor driver
was later removed during the independent dropout diagnosis and should not be
reinstalled merely to repeat a completed fixture gate. See
[UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md](UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md).

### 4.2 Retained Measurements And Superseding Decision

The intended measurement path was:

```text
Output 2 -> source adaptor -> clamp/attenuator In+ and In-
clamp/attenuator TRS -> breakout cable -> UMC202HD Input 2
```

An earlier `34.4 mV AC` / `99.5 mV AC` observation used the straight-through
direct path with no clamp/attenuator in circuit. It cannot describe attenuator
gain; the former apparent positive-gain interpretation is withdrawn.

With the corrected path, the U1282A reported:

| State and point | Reading |
| --- | ---: |
| tone present, clamp/attenuator `In+` to `In-` plateau | `105.3 mV AC` |
| tone present, breakout tip to ring | `10.0 mV AC` |
| tone stopped, `In+` to `In-` | `31 mV AC` |
| tone stopped, breakout tip to ring | `1.5 mV AC` |
| meter leads open in an approximately `10 cm` coil | `25 mV AC` |
| meter leads removed | `3.46 mV AC` |

The raw tone-present ratio is:

```text
k_raw = 10.0 / 105.3 = 0.09497
A_raw = 20 log10(k_raw) = -20.45 dB
```

Only if the connected tone-off readings are stationary and uncorrelated may
they be subtracted in quadrature:

```text
Vin,tone  = sqrt(105.3^2 - 31.0^2) = 100.6 mV
Vout,tone = sqrt(10.0^2 - 1.5^2)   = 9.89 mV
A         = 20 log10(9.89 / 100.6) = -20.15 dB
```

That corrected value is conditional analysis, not a precision measurement.
Open meter leads are pickup antennas and do not establish the noise floor across
a low-impedance source. The U1282A's `440 Hz` low-pass option must not be used
for a `1 kHz` tone.

Both the raw `-20.45 dB` result and conditional `-20.15 dB` result are consistent
with the resistance-derived `-20.094 dB` prediction for the only required
decision: the passive network attenuates by about `20 dB` and does not provide
gain. Precision DMM repeats, standalone REW transfer sweeps, and separate bench
noise captures were therefore waived as disproportionate release prerequisites.

## 5. Acceptance And Results

The proportionate release criteria are:

- every topology, construction, resistance, DC-clamp, ground-path, and
  interconnect gate passes;
- contact mapping establishes the intended polarity;
- the low-voltage AC observation is of the expected approximately `-20 dB`
  order and shows no evidence of gain; and
- the calculated and tested voltage/current margins remain valid.

These criteria pass. Noise, exact transfer, and repeatability remain legitimate
measurement-quality checks, but are now evaluated in the first powered full-
dual setup rather than used to withhold electrical release.

| AC check | Result |
| --- | --- |
| Standalone direct/clamp trace files | NOT REQUIRED FOR RELEASE; superseded by full-dual checkout |
| Standalone no-signal files | NOT REQUIRED FOR RELEASE; powered-system observation moved to full-dual checkout |
| Unloaded resistor prediction at `1 kHz` | `-20.094 dB` |
| Intermediate DMM input / output / gain at `1 kHz` | AC SANITY PASS - input plateau `105.3 mV AC`, output `10.0 mV AC`; raw `-20.45 dB`, consistent with the passive `-20.094 dB` prediction for release purposes; periodic DMM dips now strongly explained by the later audible source-stream dropout and remain non-safety-critical |
| Additional precision DMM levels | NOT REQUIRED FOR RELEASE |
| Detailed REW transfer/noise/phase | NOT REQUIRED FOR FIXTURE RELEASE; UMC202HD path blocked by the separately documented desktop dropout |
| Polarity | PASS - established by complete resistance/contact maps |
| Clamp inactivity at normal signal | PASS BY MARGIN - normal divided peaks remain below the independently tested clamp knee |
| Safety/connectivity release decision | **PASS, 2026-09-03** |
| Measurement-quality decision | NO-SIGNAL AND CLEAN `1.00 V RMS` LEVEL PASS; UMC202HD DESKTOP STABILITY FAILS, WITH UMC22 FALLBACK SEPARATELY GATED |

## 6. Release Consequence

The safety/connectivity criteria pass. The main fixture record is released for
controlled powered-amplifier use with the qualified UMC202HD Input 2. This
release does not by itself qualify a different interface. The conditional
UMC22 route and its remaining interface-specific gates are in
[UMC22_RISK_ACCEPTED_FRD_FALLBACK.md](UMC22_RISK_ACCEPTED_FRD_FALLBACK.md).
Proceed to the switched-off connection and
minimum-volume startup under
[FRD_MEASUREMENT_SETUP_TEST.md](FRD_MEASUREMENT_SETUP_TEST.md). A gross level,
noise, clipping, or dropout failure there is a stop condition for measurement
quality and triggers diagnosis; it does not retrospectively turn an unexplained
open-lead millivolt reading into evidence of an unsafe passive attenuator.

## 7. REW Method Reference

REW's official measurement documentation defines the no-reference t=0 options
and explains that a loopback timing reference requires the other interface
channel to be physically looped from output to input:
<https://www.roomeqwizard.com/help/help_en-GB/html/makingmeasurements.html>

REW's official soundcard setup documentation distinguishes native ASIO from
`EXCL:` WASAPI access and states that installed ASIO devices should appear even
when their interface is disconnected:
<https://www.roomeqwizard.com/help/help_en-GB/html/calsoundcard.html>

Behringer's UMC202HD product/download page and quick-start guide are the
authoritative sources for the Windows driver package:

- <https://www.behringer.com/en/products/0805-AAR>
- <https://mediadl.musictribe.com/media/PLM/data/docs/UMC/QSG_BE_0805-AAR_U-PHORIA-Series_WW.pdf>

The Keysight U1281A/U1282A user guide documents the U1282A AC low-pass filter
and its `440 Hz` cutoff:
<https://www.keysight.com/us/en/assets/9018-04069/user-manuals/9018-04069.pdf>
