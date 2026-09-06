# UMC22 FRD Qualification Log - 2026-09-05

Lifecycle: **HISTORY — AUDIT ONLY; DO NOT USE AS A CURRENT PROCEDURE**

This is the preserved chronological development record from the UMC22
qualification. It intentionally retains interim instructions, failed routes,
partial gates, superseded conclusions, and the final release decision so the
engineering path remains auditable. Those instructions describe the state at
their dated checkpoint and may conflict with later evidence in this file.

For current work use
[`../procedures/UMC22_INSTALLED_WOOFER_FRD.md`](../procedures/UMC22_INSTALLED_WOOFER_FRD.md).
For the concise final evidence use
[`../qualification/UMC22_FRD_QUALIFICATION.md`](../qualification/UMC22_FRD_QUALIFICATION.md).

Date prepared: 2026-09-05

Archived as lifecycle-separated history: 2026-09-06

Status: **QUALIFIED FOR CONTROLLED INSTALLED-WOOFER FRD. GATES A-E PASS WITH
THE RISK ACCEPTANCE AND LIMITATIONS BELOW. ALL THREE FINAL-SETTING SWEEPS STAYED
GREEN AND COMPLETED WITHOUT WARNING OR ABNORMALITY; SYSTEM-DELAY SPREAD IS
`1.0 us`. A COMMON DERIVED DIRECT-SOUND WINDOW PASSES `1-5 kHz` REPEATABILITY:
MAXIMUM MAGNITUDE SPREAD `0.0743 dB` AND MAXIMUM CIRCULAR PHASE SPREAD
`1.931 degrees`. THE WINDOW IS A CONSERVATIVE `2.0 ms` LEFT / `1.0 ms` RIGHT
ANALYSIS WINDOW, NOT A STORED REW WINDOW OR A FINAL PRODUCTION FRD CHOICE.
RAW-TWEETER AND POLAR WORK REMAIN OUTSIDE THIS RELEASE.**

## 1. Purpose And Scope

This is a bounded fallback route for moving the installed-driver FRD work
forward while the desktop-specific UMC202HD dropout is investigated
separately. It reuses the qualified SU-V570 clamp/attenuator, but it does not
silently transfer the UMC202HD-specific connector, phantom-isolation, or input-
headroom findings to the UMC22.

The user is willing to accept a known but unquantified possibility of damage to
the approximately GBP 25 UMC22 in an amplifier fault. That acceptance does not
waive checks which protect the person, SU-V570, PC, loudspeaker, or validity of
the measurements. It also cannot guarantee that a destructive UMC22 input
failure would be perfectly contained within the interface, although the
fixture's high series resistance makes wider damage unlikely.

## 2. Engineering Basis

The UMC22 manufacturer specifications identify:

- Input 1 as an XLR/TRS microphone/line input;
- Input 2 as a 1/4-inch TRS instrument input;
- Input 2 impedance as `1 Mohm`;
- maximum instrument input level as `+2 dBu`; and
- supported sampling rates up to `48 kHz`.

**VERIFIED INTERNAL INSPECTION - 2026-09-05 (USER-OBSERVED):** the UMC22 was
dismantled and both rear output sockets were traced visually on the PCB. Each
socket has separate mechanical tip, ring, and sleeve/shield contacts, but its
ring and sleeve pads join the same copper fill. In the user's terminology the
sockets are physically `TRS` but electrically `TS`: tip is signal, while ring
and sleeve are the same return node. They are not balanced two-active-leg TRS
outputs. This establishes the internal output-contact topology but not USB
channel routing, external cable continuity, output level, or full-duplex
stability.

The fixture's resistance-derived, unloaded floating differential transfer is
`0.09892` (`-20.094 dB`; pre-stress values). The post-stress prediction differs
immaterially at approximately `0.09894` (`-20.092 dB`). At the established
`1.00 V RMS` woofer test level:

```text
Vreference = 1.00 V RMS x 0.09892 = 0.09892 V RMS

+2 dBu = 0.775 V RMS x 10^(2/20) = 0.976 V RMS

normal headroom = 20 log10(0.976 / 0.09892) = 19.9 dB
```

Normal operation therefore has ample nominal level margin. Gate A establishes
that the mechanically TRS `INST 2` socket is single-ended: tip is isolated in
the unpowered resistance map, while ring and sleeve are a low-resistance common
bonded to the USB shell. In the intended system this common will bypass the
fixture's ring-to-sleeve shunt while leaving the tip-leg prediction at
approximately `0.09894 V RMS` for `1.00 V RMS` amplifier output. The final
unpowered ground-path audit must still confirm the complete assembled paths.

The fault case is different. With an amplifier-derived waveform bounded by the
SU-V570's approximately `+/-45.5 V` rails, the qualified resistor network can
place approximately `4.50 V peak` (`3.18 V RMS`, `+12.3 dBu`) on one fixture
node. This is about `10.3 dB` above the UMC22's published maximum instrument
input level. The fixture's `5.5-6.2 V peak` clamp range is higher still. The
published maximum input level is not identified as a destruction threshold, so
neither survival nor damage can be inferred from it.

The primary `9.1 kohm` series resistors still bound amplifier-derived current
to approximately `5 mA` per leg even if an interface node is held near zero:

```text
Imaximum,approx = 45.5 V / 9.1 kohm = 5.0 mA
```

This preserves the fixture's important current-limiting and amplifier-loading
functions. It does not make the UMC22 input compliant with its published level
limit under every fault. A UMC22-specific secondary attenuator/protector remains
an optional risk-reduction improvement, not a prerequisite under the explicit
interface-risk acceptance, unless the connection mapping exposes a new hard
path or unsafe topology.

Manufacturer source: [Behringer U-PHORIA series Quick Start Guide](https://mediadl.musictribe.com/media/PLM/data/docs/UMC/QSG_BE_0805-AAR_U-PHORIA-Series_WW.pdf).

## 3. Minimum Release Gates

These are deliberately limited to uncertainties that materially affect safety
or usable FRD data. Do not repeat the completed component-level fixture
qualification.

### 3.1 Gate A - Unpowered Input 2 Contact Map

Initial state:

1. SU-V570 off and not connected to the UMC22 or fixture.
2. UMC22 USB disconnected, phantom off, and every other UMC22 socket empty.
3. Insert the passed breakout cable's male TRS plug into UMC22 `INST 2`; leave
   its female socket empty.
4. Set the Agilent U1282A to auto-ranging resistance and null the leads.

Measure at the breakout terminal block:

| Measurement | Result |
| --- | --- |
| Tip to ring | open |
| Tip to sleeve | open |
| Ring to sleeve | `0.314 ohm` |
| Tip to USB Type-B shell | open |
| Ring to USB Type-B shell | `0.050 ohm` |
| Sleeve to USB Type-B shell | `0.030 ohm` |

Record a stable resistance, `open`, or a description of any settling or
polarity-sensitive reading. Gate A requires that tip is not hard-shorted to
ring, sleeve, or USB shell. Ring-to-sleeve and sleeve-to-shell results determine
the final adaptor/ground arrangement rather than passing or failing in
isolation. Do not connect USB or generate a signal before this map is reviewed.

**VERIFIED MEASUREMENT - 2026-09-05:** the SU-V570 was off; the UMC22 was
unpowered and otherwise disconnected; phantom was disabled; the passed
breakout cable was inserted into `INST 2`; and its female socket was empty. The
Agilent U1282A was in auto-ranging resistance mode with its leads nulled before
the first reading. All six results above were stable and showed no polarity
sensitivity.

The three sub-ohm common-node readings do not form a precision resistance
triangle: `0.314 ohm` ring-to-sleeve is greater than the sum of the two readings
to the USB shell (`0.080 ohm`). At this scale, changing probe/contact resistance
and residual-zero uncertainty dominate the comparison. This does not obscure
the needed topology: tip is open to every tested return, while ring, sleeve,
and USB shell are mutually connected at sub-ohm resistance. Repeating these as
precision milliohm measurements would not materially improve this gate.

**GATE A DECISION - PASS:** tip is not hard-shorted to ring, sleeve, or USB
shell. `INST 2` is mechanically TRS but behaves as a single-ended input with a
ring/sleeve/USB-shell common. USB connection is now permitted only for the
otherwise-unloaded Gate B phantom-isolation measurements. Signal generation
and any SU-V570 connection or power remain prohibited.

### 3.2 Gate B - Input 2 Phantom Isolation

After Gate A defines the contacts, power the otherwise unloaded UMC22 by USB
and measure DC voltage at tip-sleeve, ring-sleeve, and tip-ring with phantom off
and then on. The microphone, amplifier, fixture, and every other analogue cable
remain disconnected. Stop if any pair exceeds `0.1 V DC`, is unstable, or
behaves materially differently when phantom is enabled. This is one direct
isolation check, not a repeat of the UMC202HD's exhaustive qualification.

| Red probe to black probe | Phantom off | Phantom on |
| --- | ---: | ---: |
| Tip to sleeve | `0.0005 V DC` | `0.0000 V DC` |
| Ring to sleeve | `0.0000 V DC` | `0.0000 V DC` |
| Tip to ring | `0.0004 V DC` | `0.0000 V DC` |

**VERIFIED PARTIAL MEASUREMENT - 2026-09-05:** the SU-V570 was off; the UMC22
was connected only to USB and the passed breakout cable in `INST 2`; phantom
was disabled; and the Agilent U1282A was in auto-ranging DC-voltage mode. No
instability was reported. The largest magnitude, `0.0005 V DC`, is `200` times
below the `0.1 V DC` stop threshold. The close tip-to-sleeve and tip-to-ring
values are consistent with Gate A's ring/sleeve common.

**GATE B PARTIAL DECISION - PHANTOM-OFF HALF PASS:** retain the isolated setup
and complete the three phantom-on readings. Gate B and every downstream gate
remain pending until the on/off comparison is reviewed.

**VERIFIED PHANTOM-ON MEASUREMENT - 2026-09-05:** with the meter already
connected tip-to-sleeve, enabling phantom produced no movement beyond
`0.001 V DC`. Each subsequent pair initially displayed approximately
`0.0020 V DC` and settled to `0.0000 V DC` in approximately `10 s`. This brief
settling was common to all three probe placements rather than a sustained
phantom-derived bias. The largest observed magnitude was `50` times below the
`0.1 V DC` stop threshold.

**GATE B DECISION - PASS:** no tested `INST 2` pair exceeded the threshold,
remained unstable, or changed materially when phantom was enabled. Disable
phantom and disconnect USB before Gate C. Signal generation and SU-V570 power
remain prohibited.

### 3.3 Gate C - Final Unpowered Ground-Path Audit

With the UMC22 contact behaviour known, assemble the intended final cables with
the SU-V570 switched off. Confirm that amplifier positive cannot reach the
UMC22 active input contact without the intended `9.1 kohm` series resistance.
Map amplifier negative, ring, sleeve, USB shell, and the playback-cable ground;
record any deliberate ring-to-sleeve or system-ground commoning and confirm it
does not create an unexpected active-signal path. Stop for an unexplained low-
resistance amplifier-positive to interface-ground path.

The inspected rear-output ring/sleeve common predicts that the playback-cable
return will use that single PCB return node. Gate C must still verify this
end-to-end through the actual selected output and cable; internal inspection
does not replace the final assembled ground-path audit.

**SELECTED PLAYBACK PATH - 2026-09-05:** UMC22 Output 1 will feed SU-V570
`AUX` left through the same already-mapped TS-to-RCA playback cable used for
the UMC202HD checkout. Its retained cable-only results are TS tip to RCA centre
`0.244 ohm`, TS sleeve to RCA shell `0.078 ohm`, and both cross-paths open. The
UMC22 output inspection establishes the same tip-plus-ring/sleeve-common source
topology as the UMC202HD, so repeating the isolated cable map would add no
useful evidence. Gate C will instead measure the complete UMC22 assembled
paths.

For the first Gate C stage, keep the UMC22 unpowered and USB disconnected;
keep the SU-V570 switched off with no loudspeaker connected; connect UMC22
Output 1 through that cable to `AUX` left; connect fixture red/`In+` and
black/`In-` to speaker-bank `B` left positive and negative respectively; and
connect the fixture output to `INST 2` through the passed breakout. With
auto-ranging resistance and nulled leads, measure from speaker `B` left positive
to the following nodes:

| Speaker `B` left positive to | Expected path | Result |
| --- | ---: | ---: |
| Breakout tip | approximately `9.13 kohm` through R1 | `9125 ohm` |
| Breakout ring | approximately `10.13 kohm` through R1 + R3 to common | `10127 ohm` |
| Breakout sleeve | approximately `10.13 kohm` through R1 + R3 to common | `10127 ohm` |
| UMC22 USB Type-B shell | approximately `10.13 kohm` through R1 + R3 to common | `10127 ohm` |

Stop for a hard or unexpectedly low path, instability, or unexplained polarity
sensitivity. Review this amplifier-positive isolation stage before completing
the low-resistance return map.

**VERIFIED GATE C POSITIVE-PATH MEASUREMENT - 2026-09-05:** the SU-V570 was
off with no loudspeaker connected. The fixture ran from speaker-bank `B` left
through the breakout to UMC22 `INST 2`; UMC22 Output 1 used the selected
TS-to-RCA cable into `AUX` left; and the UMC22 was USB-disconnected with
phantom off. The U1282A was in auto-ranging resistance mode with its leads
nulled before the first measurement. The four readings are recorded above.

The active-input path is the intended `9125 ohm` R1 resistance. Each return
reading adds exactly:

```text
10127 ohm - 9125 ohm = 1002 ohm
```

That is the fixture's measured R3 shunt. Ring, sleeve, and USB shell therefore
reach amplifier positive only through R1 plus R3; no low-resistance bypass is
present.

**GATE C PARTIAL DECISION - AMPLIFIER-POSITIVE ISOLATION PASS:** retain the
same unpowered assembly and map the deliberate common return from speaker-bank
`B` left negative to these nodes:

| Speaker `B` left negative to | Expected result | Result |
| --- | ---: | ---: |
| SU-V570 `AUX` left RCA shell | low resistance; previous amplifier result approximately `0.12-0.15 ohm` | `0.137 ohm` |
| Breakout ring | low resistance through the assembled playback return; broadly below `1 ohm` | `0.311 ohm` |
| Breakout sleeve | low resistance through the assembled playback return; broadly below `1 ohm` | `0.290 ohm` |
| UMC22 USB Type-B shell | low resistance through the assembled playback return; broadly below `1 ohm` | `0.299 ohm` |

These are topology checks, not precision milliohm measurements. Stop for an
open, unstable, or otherwise unexplained result. Gate C remains incomplete
until this return map is reviewed.

**VERIFIED GATE C RETURN-PATH MEASUREMENT - 2026-09-05:** in the unchanged
unpowered assembly, speaker-bank `B` left negative measured `0.137 ohm` to the
`AUX` left RCA shell, `0.311 ohm` to breakout ring, `0.290 ohm` to breakout
sleeve, and `0.299 ohm` to the UMC22 USB Type-B shell. No instability was
observed.

The `0.137 ohm` amplifier-local result lies within the previous
`0.12-0.15 ohm` range. The complete return paths are all below `0.32 ohm`; their
additional approximately `0.15-0.17 ohm` is consistent with the mapped
`0.078 ohm` playback-cable return plus interface, plug, breakout, and probe-
contact resistance. These are coherent topology results rather than precision
subtraction of remade milliohm contacts.

**GATE C DECISION - PASS:** the selected playback cable creates the intended
single low-resistance bond between UMC22 common and SU-V570 signal/speaker
ground. The fixture independently retains R1 in every amplifier-positive path,
and no unexplained hard active-signal path is present. Disconnect the complete
SU-V570 path before Gate D; amplifier power remains prohibited.

### 3.4 Gate D - Low-Voltage UMC22 Full-Duplex Checkout

At `48 kHz`, prove the actual UMC22 output channel, Input 1 microphone channel,
Input 2 reference channel, REW timing-reference mode, gain range, and dropout-
free operation without the powered amplifier. A direct or fixture-mediated
low-voltage loopback must remain below the UMC22 input maximum. Recreate any
soundcard calibration for this interface and rate; do not reuse UMC202HD
calibration or level settings. The historical UMC22 evidence is dropout-free
ordinary playback. In addition, a current matched five-minute media control on
this desktop produced zero audible dropouts with Microsoft `USBAUDIO.sys`
(`10.0.26100.8972`). Gate D later passed with an exact-routing, dropout-free
`256k` sweep using ordinary loopback timing. A valid UMC22 soundcard/electrical-
reference calibration route remains required before reusable acoustic-response
capture; that measurement-validity item is separate from Gate D's hardware,
stream, and timing qualification.

The rear-output contact topology is already established by direct PCB
inspection: tip is the signal contact and ring/sleeve are one common return.
The selected playback cable's existing map is also reusable. Gate D therefore
need not repeat either isolated investigation, but it must prove the actual REW
output channel, level, input paths, timing mode, and dropout-free sweep
operation.

#### 3.4.1 Amplifier-Disconnected No-Signal Check

In this section, *source adaptor* means the already-built and mapped TRS-to-
fixture-input adaptor originally called the `Output 2 source adaptor` during
UMC202HD fixture commissioning. It is not the breakout cable and it does not
bypass the clamp/attenuator. Its TRS tip connects to fixture red/`In+`, its
sleeve connects to fixture black/`In-`, and its ring is unconnected. Its passed
map is tip-to-`In+` `0.400 ohm`, sleeve-to-`In-` `0.370 ohm`, and every
prohibited path open.

The complete Gate D loopback is:

```text
UMC22 Output 1
  -> passed source adaptor
  -> fixture red/In+ and black/In-
  -> complete 9.1 kohm / 1 kohm clamp-attenuator
  -> fixture TRS output
  -> passed breakout (meter access only)
  -> UMC22 INST 2
```

This is therefore an approximately `-20 dB` protected loopback. Do not connect
Output 1 directly to `INST 2` for this stage.

1. Disconnect both the fixture and playback cable completely from the
   SU-V570. Leave the amplifier off and connect no loudspeaker.
2. With UMC22 USB disconnected and phantom off, set `OUTPUT`, `GAIN 1`, and
   `GAIN 2` fully down and set `DIRECT MONITOR` off.
3. Leave Input 1, Output 2, and the headphone socket empty.
4. Insert the passed source adaptor into UMC22 Output 1. Its tip feeds fixture
   `In+`, sleeve feeds `In-`, and ring remains unconnected. Connect the fixture
   output to `INST 2` through the passed breakout.
5. Connect the same known-good USB cable and desktop USB path used for the
   zero-dropout media control. Keep all software audio stopped.
6. Observe for an unexpected clip indication or other instability. In DC-
   voltage mode, measure breakout tip-to-sleeve for approximately `10 s`.

| No-signal observation | Result |
| --- | ---: |
| Breakout tip-to-sleeve DC | initial `0.0015 V`, settled to `0.0000 V` after approximately `15 s` |
| UMC22 clip indication or instability | none observed |

Stop and disconnect USB for sustained or unstable DC above `0.1 V`, a clip
indication, unexpected sound, heat, smell, or other abnormal behaviour. Do not
open REW or generate a signal until this no-signal state is reviewed.

**VERIFIED GATE D NO-SIGNAL MEASUREMENT - 2026-09-05:** in the documented
amplifier-disconnected, fixture-attenuated loopback, breakout tip-to-sleeve
started at `0.0015 V DC` and settled to `0.0000 V DC` after approximately
`15 s`. No clipping indication or abnormal behaviour was observed. The initial
magnitude is approximately `0.1 / 0.0015 = 66.7` times below the stop threshold,
and there is no sustained DC.

**GATE D NO-SIGNAL DECISION - PASS:** retain the unchanged hardware and USB
connection. REW may now be opened for no-excitation `48 kHz` routing setup, but
do not use Generator, Check Levels, or Measure until that routing is reviewed.

#### 3.4.2 REW Routing Setup Without Excitation

Use the Microsoft USB-audio path already selected for the UMC22. In REW
`Preferences -> Soundcard`, select the UMC22/USB Audio CODEC as both input and
output and select `48 kHz`. Do not inherit a UMC202HD or different-rate
soundcard-calibration file. Before excitation, record the exact REW driver,
input/output device names, and available channel names; then establish Input 1
as measurement left, Input 2 as reference right, and Output 1 as measurement
left. Keep every signal command stopped while inspecting these controls.

**VERIFIED REW DEVICE STATE - 2026-09-05:** REW uses driver type `Java` with
`EXCL: Behringer UMC22 (USB Audio CODEC)` selected for both input and output.
Available output channels are `L`, `R`, and `L+R`; available input channels are
`L` and `R`; the selected rate is `48 kHz`; and soundcard calibration is
`None`. This is the intended native Microsoft USB-audio, exclusive-mode,
two-input/two-output basis for the checkout.

**DEVICE-ENUMERATION DECISION - PASS:** output `L` is the measurement output to
physical Output 1, input `L` is the measurement input from physical Input 1,
and input `R` is the loopback/reference input from `INST 2`. `Use loopback as
cal and timing reference`, `Merge loopback response into IR`, and timing offset
`0.0000 ms` were selected without excitation. The screenshot also retained
reference output `R` while physical Output 2 was empty. That last assignment
was not electrically proved at this stage and is superseded by the live timing
correction below.

**VERIFIED NO-EXCITATION CHANNEL/TIMING UI ASSIGNMENT - 2026-09-05:** screenshots of Soundcard
Preferences and the Measure panel confirm output `L`, measurement input `L`,
timing-reference output `R`, loopback/reference input `R`, `Use loopback as cal
and timing reference`, `Merge loopback response into IR`, timing offset
`0.0000 ms`, `48 kHz`, and calibration `None`. Output 2 remains physically
empty. This records the UI state that passed without excitation; the reference-
output choice was later shown to be invalid for the actual wiring and is
superseded below.

The screenshots also showed two inherited setup details to correct before the
first signal. `Control input volume` was enabled at `0.25`; unity (`1.00`)
avoids digital attenuation of both captured channels before the physical UMC22
gain controls are set. The dormant measurement also retained the stale name
`SB17 UMC202HD checkout 1` and an exact-Nyquist `24 kHz` endpoint.
REW documents that Windows Java uses 16-bit data, so the inherited `Treat
32-bit data as 24-bit` check box is immaterial on this path and need not become
a separate test. See [REW Soundcard Preferences](https://www.roomeqwizard.com/help/help_en-GB/html/soundcard.html).

**VERIFIED PRE-EXCITATION SETTINGS - 2026-09-05:** the user confirms that
`Control input volume` is now `1.00`, the measurement is named `UMC22
low-voltage loopback 1`, and the sweep range is `20-20000 Hz`. The first-checkout
settings remain `-20 dBFS`, `1M`, one repetition, and timing offset `0.0000 ms`.
This establishes configuration only; no excitation or sweep result is inferred.

**PRE-EXCITATION SETTINGS DECISION - PASS:** with the amplifier still fully
disconnected, Gate D may advance to one bounded `1 kHz` level-setting tone
through the protected fixture loopback:

1. Keep phantom off, `GAIN 1`, `GAIN 2`, and the physical `OUTPUT` control fully
   down. Keep Input 1, Output 2, and the headphone socket empty.
2. Without moving the loopback wiring, place the true-RMS meter across breakout
   tip-to-sleeve in AC-voltage mode.
3. In REW Generator select sine, `1 kHz`, output `L`, and `-20 dBFS`. Start the
   tone with the physical `OUTPUT` control still fully down.
4. Raise only `OUTPUT` slowly to a target of approximately `0.020 V RMS` at the
   breakout; `0.018-0.022 V RMS` is close enough and avoids needless knob
   chasing. Stop immediately at `0.050 V RMS`, any clip indication,
   dropout/instability, or other abnormal behaviour. If the target cannot be
   reached at maximum `OUTPUT`, do not increase the digital level; record the
   maximum instead.
5. Hold the achieved level for approximately `30 s`, stop Generator, then
   record the stable voltage, approximate `OUTPUT`-control position, and any
   clip indication, dropout, or abnormality.

The `0.020 V RMS` target is approximately `33.8 dB` below the published
`0.976 V RMS` input maximum:

```text
20 log10(0.976 / 0.020) = 33.8 dB
```

It corresponds to only approximately `0.202 V RMS` at the fixture input under
the resistance-derived `0.09892` transfer ratio. This is a proportionate first
AC check, not the Gate D sweep and not authorization to power the amplifier.

**VERIFIED CONTROLLED AC LEVEL - 2026-09-05:** with the amplifier absent and
the protected loopback unchanged, the breakout tip-to-sleeve voltage reached
`0.0207 V RMS` with the UMC22 `OUTPUT` control at approximately 3 o'clock
(estimated by the user as about 80% of its travel). During the observation it
wandered slowly between `0.0205 V RMS` and `0.0210 V RMS`. No clip indication,
dropout, or other abnormality was observed.

The full observed voltage span is only:

```text
20 log10(0.0210 / 0.0205) = 0.21 dB
```

That slow approximately `0.21 dB` end-to-end movement is immaterial for this
bounded level check and is distinct from an abrupt stream dropout. Even the
highest observed level remains approximately `33.3 dB` below the UMC22's
published `0.976 V RMS` instrument-input maximum.

**CONTROLLED AC-LEVEL DECISION - PASS:** leave the `OUTPUT` position unchanged
and keep the amplifier disconnected. Set the reference-channel ADC level before
attempting the Gate D sweep:

1. Keep phantom off, `GAIN 1` fully down, Input 1 empty, and all hardware and
   routing otherwise unchanged. Leave the true-RMS meter across breakout
   tip-to-sleeve in AC-voltage mode.
2. Open REW's Level Meters so both `In` and `Ref In` are visible. Restart the
   same output-L, `1 kHz`, `-20 dBFS` sine; the external meter must remain below
   the existing `0.050 V RMS` stop limit.
3. Raise only UMC22 `GAIN 2` slowly until the `Ref In` RMS level is in the
   approximate `-24` to `-18 dBFS` range. A sine-wave peak should then be about
   `3 dB` higher. Do not chase an exact value.
4. Stop immediately if `Ref In` peak reaches `-6 dBFS`, the front-panel clip
   indicator illuminates, the external voltage changes unexpectedly, or any
   dropout/instability or other abnormality occurs. If maximum `GAIN 2` cannot
   bring `Ref In` above `-30 dBFS`, stop and record that result rather than
   raising output level.
5. After approximately `10 s` of stable indication, stop Generator and record
   `Ref In` RMS and peak levels, approximate `GAIN 2` position, the external
   AC voltage, and any abnormality. Do not use Check Levels or Measure yet.

REW's Level Meters show RMS as the lower numeric value and peak as the upper
numeric value; see [REW Level Meters](https://www.roomeqwizard.com/help/help_en-GB/html/vumeters.html).

**LIVE REFERENCE-CAPTURE HOLD - 2026-09-05:** with the externally verified
approximately `0.0207 V RMS` tone still reaching physical `INST 2`, moving
UMC22 `GAIN 2` across its complete range produced no change in REW's `Ref In`
bargraph. A Preferences screenshot shows output `L` active at `-20.00 dBFS`,
measurement input `L`, loopback input `R`, and both `In` and `Ref In` at the
approximately `-93.72 dBFS` noise floor. It also shows the output device with
the `EXCL:` prefix but the current input device without it, contrary to the
earlier reported exclusive-device selection for both directions. This does not
invalidate the external AC-level pass, but the actual Java/USB input endpoint
and channel map are not yet proved. The earlier channel/timing decision is
therefore only a **no-excitation UI-assignment pass**, not a live reference-
capture pass.

Do not permanently change the main measurement input to `R` merely because
physical `INST 2` is expected to be the right channel: the main `Input` selector
is intended for the future Input 1 microphone, while the separate `Loopback
input` selector is intended for Input 2. First restore or disprove the earlier
exclusive-input selection with the amplifier absent:

1. Stop Generator and return `GAIN 2` fully down. Keep the DMM connected and all
   hardware unchanged.
2. Open the `Input device` list. If the exact `EXCL: Behringer UMC22 (USB Audio
   CODEC)` entry is available, select it. Retain main input `L`, loopback input
   `R`, `48 kHz`, and input volume `1.00`; report if any of those options change
   or disappear.
3. Restart the same output-L, `1 kHz`, `-20 dBFS` tone and move `GAIN 2` only
   far enough to determine whether `Ref In` now follows it. Retain the
   `0.050 V RMS`, `-6 dBFS`, clipping, and abnormality stop limits.
4. Stop Generator and report the exact selected input-device name, whether
   `Ref In` saw the tone, and whether it followed `GAIN 2`.

If no `EXCL:` input endpoint is available, or selecting it does not restore
capture, stop there. A temporary main-input `R` test will then distinguish a
channel-map problem from an endpoint/capture problem without increasing the
analogue level.

**LIVE REFERENCE-CAPTURE RESOLUTION - PASS, 2026-09-05:** the non-exclusive
input endpoint was the complete cause of the apparent failure. Selecting
`EXCL: Behringer UMC22 (USB Audio CODEC)` immediately restored `Ref In` capture,
and its indicated level then followed `GAIN 2` linearly in decibels over the
control range. No main-input channel swap was required. This supersedes the
hold above while retaining it as useful diagnostic history.

`GAIN 2` is now set for a stable `Ref In` RMS level of `-20.88 dBFS`, fluctuating
by only approximately `0.01 dB`. The external tip-to-ring voltage is steady at
`0.0218 V RMS`. Gate A established that ring and sleeve are the same Input 2
return node, so this tip-to-ring reading is equivalent to the earlier tip-to-
sleeve reference for present purposes. It is approximately `0.45 dB` above the
earlier `0.0207 V RMS` reading and still approximately `33.0 dB` below the
published `0.976 V RMS` input maximum; neither difference warrants retuning the
output level.

**REFERENCE-CHANNEL LEVEL DECISION - PASS:** retain the exact exclusive input
and output endpoints, `GAIN 2`, `OUTPUT`, `48 kHz`, input volume `1.00`, and L/R
assignments. Input 1/USB-L must now be proved independently with the microphone
before the full-duplex sweep gate can close. The amplifier remains absent and
unapproved.

For the Input 1 microphone-channel check:

1. Stop Generator. Do not move `OUTPUT` or `GAIN 2`; note the approximate
   `GAIN 2` knob position for the record. Keep the SU-V570 fully disconnected.
2. With phantom off and `GAIN 1` fully down, connect the ECM8000 to Input 1 by
   its normal XLR cable. Keep the existing protected Input 2 loopback connected.
3. Enable `+48 V`, confirm the phantom indicator illuminates, and wait about
   `15 s`. Stop for any clip indication, instability, heat, smell, or other
   abnormality.
4. With Generator still stopped, observe REW's main `In` meter while speaking
   normally near the microphone or rubbing fingers near it; do not strike the
   microphone. Raise only `GAIN 1` enough to show a clear input response and
   confirm that the indicated level follows the control.
5. Avoid peaks above `-12 dBFS` for this mapping check. Return `GAIN 1` fully
   down, then report the approximate noise-floor and stimulus levels, whether
   they followed `GAIN 1`, the phantom/clip indications, the retained `GAIN 2`
   position, and any abnormality. Do not run Check Levels or Measure yet.

**VERIFIED INPUT 1 MICROPHONE-CHANNEL CHECK - 2026-09-05:** `GAIN 2` remains
between approximately 3 and 4 o'clock. With `GAIN 1` at minimum, REW `In`
indicated approximately `-83 dBFS`, usually moving by about `+/-3 dB` and
occasionally reaching about `-76 dBFS`. With `GAIN 1` raised to approximately
2 o'clock, the indicated background averaged roughly `-56 dBFS`, usually moving
by about `+/-4 dB`, while nearby speech reached approximately `-18 dBFS`.
Speech, finger clicks, and other nearby test sounds all produced the expected
response. No clipping or abnormality was observed.

The room was not silent: a PC case fan was continuous, with intermittent
birdsong and aircraft audible outside. These readings therefore establish
microphone-channel function and gain response, not the UMC22's intrinsic input-
noise performance. The approximately `27 dB` shift in indicated background
between minimum gain and the raised setting, together with the local-sound
response, proves the intended Input 1/USB-L route.

**INPUT 1 MICROPHONE-CHANNEL DECISION - PASS:** both ADC channels, their
physical gain controls, and the intended REW L/R assignments now respond. A
coherent acoustic signal must still reach the microphone during the first
full-duplex sweep. Use the UMC22 headphone output as a low-energy temporary
source if known-good wired headphones or earbuds are available; this is a
functional checkout, not reusable acoustic-response evidence:

1. Keep the SU-V570 fully disconnected. Stop Generator, keep phantom on and the
   ECM8000 connected, return `GAIN 1` fully down, and do not move `OUTPUT` or
   `GAIN 2`. Retain the DMM across breakout tip-to-ring in AC-voltage mode.
2. With no signal playing and with the headphones **not worn**, connect known-
   good wired stereo headphones or earbuds to the UMC22 headphone socket. Place
   the left earpiece initially about `100 mm` from the microphone capsule and
   keep the right earpiece farther away.
3. Restart the same output-L, `1 kHz`, `-20 dBFS` sine. Confirm that `Ref In`
   remains near `-20.88 dBFS` and that the external reference remains stable
   and below `0.050 V RMS`.
4. Raise only `GAIN 1`, or reduce the earpiece-to-capsule distance, until main
   `In` RMS is approximately `-24` to `-18 dBFS`. Do not change `OUTPUT` or
   `GAIN 2`, and do not chase an exact value.
5. Stop immediately for either input peak at or above `-6 dBFS`, any clip
   indication, reference-voltage instability, dropout, or other abnormality.
   After about `10 s` of stable indication, stop Generator and record `In` and
   `Ref In` levels, external voltage, `GAIN 1` position, approximate earpiece
   distance, and observations. Do not run Measure yet.

If no suitable headphones or earbuds are available, stop here rather than
substituting an unqualified powered device.

**VERIFIED HEADPHONE-TO-MICROPHONE LEVEL SETUP - 2026-09-05:** with the left
earpiece approximately `150 mm` from the ECM8000, `GAIN 1` between approximately
2 and 3 o'clock, and the retained `GAIN 2` between approximately 3 and 4
o'clock, REW indicated:

| Channel/point | Indication |
| --- | ---: |
| Main `In` RMS | `-19.5 dBFS`, very stable; occasional movement to approximately `-19 dBFS` |
| `Ref In` RMS | `-20.84 dBFS`, very stable within approximately `+/-0.01 dB` |
| Breakout tip-to-ring | steady `0.0230 V RMS` |

No clipping, dropout, or other abnormality was observed. A separate numeric
sample-peak result was not reported; for undistorted sine waves the RMS figures
imply peaks of approximately `-16.5 dBFS` and `-17.8 dBFS` respectively, leaving
ample margin. The two RMS channel levels differ by only `1.34 dB`.

The external reference is approximately `0.46 dB` above the preceding
`0.0218 V RMS` observation and remains approximately `32.6 dB` below the
published `0.976 V RMS` instrument-input maximum:

```text
20 log10(0.0230 / 0.0218) = 0.46 dB
20 log10(0.976 / 0.0230) = 32.6 dB
```

This small, stable change after adding the headphone load does not justify
retuning either level control.

**FULL-DUPLEX LEVEL-SETUP DECISION - PASS:** retain all controls, endpoint and
channel assignments, the microphone/earpiece geometry, and the protected
reference wiring. One amplifier-disconnected sweep may now be run:

1. Keep the headphones unworn, the SU-V570 fully disconnected, the microphone
   and phantom supply active, and every physical control unchanged. Secure the
   breakout and meter leads so they cannot contact another node.
2. Before starting, confirm both input and output devices are the exact `EXCL:
   Behringer UMC22 (USB Audio CODEC)` endpoint at `48 kHz`; measurement output
   and input are `L`; reference input is `R`; loopback-as-cal-and-timing and IR
   merge are selected; timing offset is `0.0000 ms`; and soundcard calibration
   is `None`. The first sweep historically retained reference output `R`; that
   setting is superseded by the correction below.
3. Confirm measurement name `UMC22 low-voltage loopback 1`, range
   `20-20000 Hz`, level `-20 dBFS`, length `1M`, and one repetition. Do not run
   Check Levels or alter a gain to satisfy a new prompt.
4. Start exactly one measurement. Do not move either earpiece or microphone.
   Abort for any clip warning/indicator, timing-reference failure, dropout,
   discontinuous sound, USB error, or other abnormality. Do not raise any level
   if REW reports a weak frequency extreme.
5. When the sweep ends, do not run a repeat yet. Record whether it completed,
   every warning, the reported System Delay, any visible clipping indication,
   and whether the impulse has one clear dominant arrival rather than several
   comparable peaks. This headphone response is functional gate evidence, not
   reusable loudspeaker FRD data.

**VERIFIED FIRST FULL-DUPLEX SWEEP EXECUTION - 2026-09-05:** the single
amplifier-disconnected `1M`, `20-20000 Hz`, `-20 dBFS` headphone-to-microphone
sweep completed successfully. REW produced no warning or error; no interface
clip indicator illuminated; no discontinuity was heard; and no other
abnormality was reported.

The supplied Impulse screenshot shows one unmistakable dominant red arrival at
approximately `t = 0`, followed by a much lower decaying response that trends
toward the noise floor. It does not show several comparable impulse peaks. The
blue curve and the green `R` marker at approximately `500 ms` are the applied
impulse-window overlay and right-window marker, not additional measured
arrivals. At this broad `-100 ms` to `1 s` view, the approximately `0.44 ms`
air-travel time for the nominal `150 mm` earpiece distance would appear very
close to zero, so the displayed peak position is physically plausible.

**SWEEP-EXECUTION DECISION - PASS FOR STREAM STABILITY ONLY:** this is the first
verified dropout-free REW full-duplex sweep on the UMC22 and closes the
principal stream-stability uncertainty. Gate D timing validity remained open
pending the stored measurement metadata. With the measurement selected,
`Tools -> Info` (`Ctrl+N`) exposes `System Delay`, `Timing offset`, `Timing ref
mode`, and `Clock adjustment`.
REW documents `System Delay` in the measurement Info panel; see
[Making Measurements](https://www.roomeqwizard.com/help/help_en-GB/html/makingmeasurements.html)
and the [`Tools -> Info` command](https://www.roomeqwizard.com/help/help_en-GB/html/tools.html).

**VERIFIED FIRST-SWEEP TIMING METADATA - 2026-09-05:** the Info panel records:

| Field | Stored result |
| --- | --- |
| Peak | `0.4292 ms` |
| IR start | `0.3750 ms` (`129 mm`, `5.06 in`) |
| Timing ref index | `N/A` |
| System Delay | `Not available` |
| Timing offset | `N/A` |
| Clock adjustment | `0.0 ppm` |
| Timing ref mode | `Loopback as cal ref` |
| Timing ref output | `R` |
| Timing ref input | `MICROPHONE (Master Volume) R` |

The Info panel proves that the requested mode was stored but a timing-reference
event was not acquired: `Timing ref index` is `N/A`, so `System Delay` cannot be
calculated. The reason is now explicit. The protected reference input receives
physical UMC22 Output 1, USB output `L`, while REW was told to emit its timing-
reference signal on output `R`; physical Output 2/R was intentionally empty.
The loopback input could capture the main L sweep for response correction, but
not the timing event emitted on the unconnected R output.

The untimed result's `0.3750 ms` IR start corresponds to approximately `129 mm`
at `343 m/s`, and its `0.4292 ms` peak corresponds to approximately `147 mm`,
both physically consistent with the nominal `150 mm` earpiece distance. That is
a useful sanity check but does not replace a valid loopback System Delay.

**CORRECTED TIMING-ROUTING DECISION - 2026-09-05:** this mismatch came from the
documented setup, not a user wiring error. For this amplifier-output-reference
topology, both measurement output and timing-reference output must be `L`,
because that is the single physical output sensed by the fixture. Measurement
input remains `L` and loopback/reference input remains `R`. One repeat is
necessary and sufficient:

1. Stop all signals and leave every physical connection and control unchanged.
2. Change only `Timing reference output` from `R` to `L`. Retain measurement
   output `L`, measurement input `L`, loopback input `R`, both `EXCL:` devices,
   `48 kHz`, loopback-as-cal-and-timing, IR merge, and `0.0000 ms` offset. If REW
   will not permit measurement output and reference output both to be `L`, stop
   and report that rather than rewiring anything.
3. Briefly restart the `1 kHz`, `-20 dBFS` tone. Verify both input levels remain
   in their established ranges and tip-to-ring remains below `0.050 V RMS`;
   stop for any unexpected level increase, clipping, or abnormality. Stop the
   tone after the check.
4. Name the repeat `UMC22 low-voltage loopback timing-fixed`, retain
   `20-20000 Hz`, `-20 dBFS`, `1M`, and one repetition, then run exactly one
   sweep without moving anything or changing a gain.
5. Record warnings/errors, clipping/dropouts, and the new Info-panel `Timing ref
   index`, `System Delay`, `Timing offset`, `Clock adjustment`, `Timing ref
   mode`, output, and input. Do not alter or rerun the first measurement.

**VERIFIED CORRECTED-ROUTING UI BEHAVIOUR - 2026-09-05:** REW accepted `L` as
both the measurement and timing-reference output. On starting the measurement
it displayed `Ref output is the same as measurement output` and explained that
the outputs would usually differ for a loopback timing reference. This warning
is expected in the present topology: the protected Input 2 reference is
deliberately a sample of the same physical Output 1/L that supplies the
measurement stimulus. Select `Yes` without rewiring or changing a gain, provided
the immediately preceding external AC check is still below `0.050 V RMS` and
shows no abnormality. The user subsequently confirmed that the latest reading
was `0.0222 V AC` (`22.2 mV AC`), not `0.0222 mV AC`; it therefore remained
comfortably inside the established range.

**VERIFIED SECOND FULL-DUPLEX SWEEP EXECUTION - 2026-09-05:** the corrected-
output `1M`, `20-20000 Hz`, `-20 dBFS` sweep completed with no warning other
than the expected same-output confirmation, and with no clipping or dropout.
Its Info panel records:

| Field | Stored result |
| --- | --- |
| Name | `UMC22 low-voltage loopback fixed` |
| Peak | `0.0002 ms` |
| IR start | `-0.0417 ms` (`-14 mm`, `-0.56 in`) |
| Timing ref index | `N/A` |
| System Delay | `Not available` |
| Timing offset | `N/A` |
| Clock adjustment | `0.0 ppm` |
| Timing ref mode | `Loopback as cal ref` |
| Timing ref output | `L` |
| Timing ref input | `MICROPHONE (Master Volume) L` |

This second sweep is further dropout-free full-duplex evidence, but it is not
valid response, phase, or timing evidence. The stored reference input is the
same Input 1/L microphone channel used for the measurement instead of the
fixture signal on Input 2/R. Merging a channel with itself as the loopback
calibration reference naturally produces the reported almost-unity, almost-
flat magnitude and phase, while no independent timing reference can be found.
The flat trace is therefore diagnostic of the input-selection error, not a
measured headphone response.

**EXACT-ROUTING REPEAT DECISION - 2026-09-05:** one further amplifier-
disconnected sweep is necessary and sufficient. Keep all wiring, physical gain
controls, level, frequency range, sweep length, and sample rate unchanged. In
the Measure window set and visually verify all four selectors together:

| Role | Required channel |
| --- | --- |
| Measurement output | `L` |
| Timing-reference output | `L` |
| Measurement input | `L` |
| Loopback/reference input | `R` |

The exact `EXCL:` UMC22 input and output devices must remain selected. Name the
measurement `UMC22 low-voltage loopback timing-fixed Rref`, start one sweep,
and accept the same-output warning with `Yes`. Stop if either input meter is
abnormal, but do not alter a gain merely to optimise an immaterial fraction of
a decibel. Afterward record the Info-panel fields listed above and confirm that
`Timing ref input` is `MICROPHONE (Master Volume) R` before treating any graph
or System Delay as valid.

**VERIFIED REW EXCEPTION AND POST-RESTART SETTINGS AUDIT - 2026-09-05:** when
the Measure-window reference input was changed to `R` after the invalid self-
referenced sweep, REW V5.40 beta 133 raised this exception before a further
valid measurement was established:

```text
java.lang.ArrayIndexOutOfBoundsException: Index 1 out of bounds for length 1
    roomeqwizard.audio.Q.A(y:1251)
    roomeqwizard.audio.Q.run(y:1499)
```

REW was restarted. The three post-restart screenshots then show the following
coherent state:

| Area | Verified setting | Decision |
| --- | --- | --- |
| Soundcard | Java; exact `EXCL:` UMC22 input and output; `48 kHz`; both buffers `32k` | PASS |
| Soundcard routing | output L; timing-reference output L; measurement input L; loopback input R | PASS |
| Soundcard options | virtual balanced, invert, high-pass, and output-volume control off; input-volume control on at `1.00`; calibration `None` | PASS for this gate |
| Java channel request | `Stereo only` off | Not intrinsically invalid, but the only visible setting directly relevant to forcing a two-channel capture |
| Analysis | automatic IR widths; no FDW/MTW; loopback delay reference at IR peak; no loopback clock adjustment; align IR peak and t=0 to a sample | PASS for the full-range headphone check |
| Measure | SPL sweep; `1M`; one repetition; loopback as calibration/timing reference; merge loopback response; zero offset; From REW; single measurement; `20-20000 Hz`; `-20 dBFS`; output/ref-output L; input L; ref-input R | PASS |

`Adjust clock with acoustic ref` is enabled but is inactive in the selected
loopback-reference mode. Leaving `Adjust clock with loopback` off is appropriate
because UMC22 playback and capture share the same hardware clock. `Control input
volume` at unity is not evidence of the exception and is retained for the next
attempt so that only one variable changes.

The exception's attempted index `1` in an array of length `1` is consistent with
REW trying to access the right channel while a live Java capture object still
contained only a mono channel. The obfuscated stack trace does not prove that
internal cause, but the interpretation matches both the preceding one-input
self-reference state and the fact that a restart accepted the correct `R`
selection. It does not indicate a UMC22 electrical fault.

**STEREO-CAPTURE RETRY DECISION - 2026-09-05:** with all signals stopped and
the amplifier still absent, select `Stereo only` in Soundcard Preferences. If
REW refreshes its device lists, reselect the exact `EXCL:` UMC22 input and
output, then reverify the L/L/L/R matrix. Do not alter input volume, either
physical gain, wiring, or sweep level. Briefly run the established output-L
`1 kHz`, `-20 dBFS` tone and confirm that `Ref In` again receives Input 2/R,
the main input remains normal, and the external reference stays below
`0.050 V RMS`; then stop the tone. If that passes, run the one exact-routing
`1M` sweep and accept the expected same-output warning. If the same exception
recurs, stop without another sweep, retain the stack trace, and use `Generate
debug file...` for a REW bug report; do not continue changing settings blindly.

**VERIFIED STEREO-CAPTURE EXACT-ROUTING RESULT - 2026-09-05:** after enabling
`Stereo only`, the next sweep completed and the preceding channel-index
exception did not recur. The Info panel proves that REW stored the intended
reference routing rather than either earlier erroneous assignment:

| Field | Stored result |
| --- | --- |
| Peak | `0.5100 ms` |
| IR start | `0.4792 ms` (`164 mm`, `6.47 in`) |
| Timing ref index | `N/A` |
| System Delay | `Not available` |
| Timing offset | `N/A` |
| Clock adjustment | `0.0 ppm` |
| Timing ref mode | `Loopback as cal ref` |
| Timing ref output | `L` |
| Timing ref input | `MICROPHONE (Master Volume) R` |

At `343 m/s`, the peak and start correspond to approximately `175 mm` and
`164 mm` respectively:

```text
343 m/s * 0.0005100 s = 0.1749 m
343 m/s * 0.0004792 s = 0.1644 m
```

Those values are physically plausible for the nominal `150 mm` earpiece-
capsule spacing, but that sanity check alone cannot prove stable loopback-
referenced timing. The result eliminates a stored L/R assignment error and
shows that forcing stereo prevented the exception, but it does not explain why
REW withheld the timing metadata. Absence of a separately reported warning,
clip, or dropout for this attempt is not silently inferred from completion.

**SCOPE CORRECTION AND TIMING-ONLY DIAGNOSTIC DECISION - 2026-09-05:** the
previously proposed `Captured`/`Ref Captured` inspection is withdrawn. Current
REW Scope is a live two-channel oscilloscope; it does not expose the preceding
measurement's raw capture buffers. The absence of those selector entries is
expected and is not a user setting error. A live Scope run would merely repeat
the already-established fact that Input 2/R responds to the low-voltage tone,
so it has insufficient additional value.

The next proportionate discriminator is one short amplifier-disconnected A/B
sweep. Keep the current physical wiring, `OUTPUT`, `GAIN 1`, `GAIN 2`, exact
`EXCL:` devices, `48 kHz`, `Stereo only`, measurement output L, reference output
L, measurement input L, reference input R, `20-20000 Hz`, `-20 dBFS`, and one
repetition unchanged. Change only the timing function from `Use loopback as cal
and timing reference` to ordinary `Use loopback as timing reference`; leave
`Merge loopback response into IR` off/inactive, select `256k`, and name the
measurement `UMC22 timing-only diagnostic`. Accept the same-output warning and
run the single sweep through the protected low-voltage loop.

This result is diagnostic rather than a calibrated FRD. Record warnings,
clipping/dropout observations, and the Info-panel timing-reference mode, output,
input, index, System Delay, timing offset, clock adjustment, peak, and IR start.
If a numeric System Delay appears, ordinary L/R loopback timing works and the
remaining problem is confined to the combined calibration/merge path. If timing
is still unavailable or another exception occurs, stop signal generation,
retain the measurement and a REW debug file, and take the issue to current REW
rather than continuing blind setting changes. Neither outcome authorises the
SU-V570 to be connected or powered.

**VERIFIED TIMING-ONLY DIAGNOSTIC - 2026-09-05:** the physical setup was
reconfirmed as the known-good desktop USB path; UMC22 Output 1/L through the
source adaptor, complete clamp/attenuator, and breakout to `INST 2`; ECM8000 to
`MIC / LINE 1`; headphones to the headphone socket; and phantom active. This is
the intended Gate D circuit. `DIRECT MONITOR` must remain off. The ECM8000
calibration file was not loaded, which is immaterial to this routing/timing
diagnostic but prevents its magnitude response from becoming reusable acoustic
evidence.

The `UMC22 timing-only diagnostic` completed with no warning, clipping,
dropout, exception, or other reported abnormality. Its Info panel records:

| Field | Stored result |
| --- | --- |
| REW | `V5.40 beta 133` |
| Excitation | `256k` log swept sine, one sweep at `-20.0 dBFS` |
| Frequency range | `20-20000 Hz` |
| Sample rate | `48000.0 Hz` |
| Timing ref mode | `Loopback` |
| Timing ref output | `L` |
| Timing ref input | `MICROPHONE (Master Volume) R` |
| Timing ref index | `47970.52` |
| System Delay | `0.6141 ms` (`211 mm`, `8.29 in`) |
| Timing offset | `0.0000 ms` |
| Clock adjustment | `0.0 ppm` |
| Peak | `0.6141 ms` |
| IR start | `0.5208 ms` (`179 mm`, `7.03 in`) |
| Signal-to-noise | `41.6 dB` |
| Signal-to-distortion | `70.5 dB` |
| Microphone calibration | None loaded |
| Soundcard calibration | None loaded |

At `343 m/s`, the independent time conversions agree with REW:

```text
343 m/s * 0.0005208 s = 0.1786 m = 179 mm
343 m/s * 0.0006141 s = 0.2106 m = 211 mm
```

The non-`N/A` reference index proves that REW detected the Input 2/R reference,
and the numeric System Delay proves that it referenced the acoustic Input 1/L
arrival to that capture. The result therefore establishes the intended
two-channel routing and ordinary loopback timing. The `0.0 ppm` adjustment is
also coherent with input and output sharing the UMC22 hardware clock.

**GATE D DECISION - PASS:** Gates A-D now qualify the UMC22 for the controlled
powered no-signal and `1.00 V RMS` woofer checks in Gate E. The earlier
`Loopback as cal ref` results remain invalid and show that beta 133's combined
loopback-calibration/IR-merge path is not presently qualified on this setup.
Gate D does not promote the timing-only trace to calibrated acoustic evidence.
Before a reusable powered sweep, load the appropriate ECM8000 calibration file
for the chosen microphone orientation and establish a valid UMC22/electrical-
reference magnitude-calibration route. Do not silently use `No cal file` data
for crossover design.

**CALIBRATION-ROUTE NEXT STEP - 2026-09-05:** before dismantling the successful
low-voltage setup or wiring the SU-V570, run one final `256k` A/B with all
physical controls, wiring, exact devices, sample rate, L/L/L/R routing,
frequency range, level, and repetition count unchanged. Select `Use loopback as
cal and timing reference`, but choose `Make calibration data from loopback
response` instead of `Merge loopback response into IR`. Name it `UMC22
loopback-cal-data diagnostic`. The ECM8000 calibration may remain unloaded for
this diagnostic so that only the reference treatment changes.

Record the same timing fields, warnings/clipping/dropout/exception state, and
whether the Info panel shows calibration data generated from the loopback. If
the reference index and numeric System Delay remain valid and the loopback
calibration data are created, this becomes the candidate mode for Gate E; load
the ECM8000 file before reusable acoustic capture. If timing again becomes
`N/A`, stop low-voltage testing and preserve the session plus a debug file for
current REW. Do not return to the already-failed IR-merge option.

**VERIFIED LOOPBACK-CAL-DATA DIAGNOSTIC - 2026-09-05:** the unchanged
amplifier-disconnected test completed with no warning or reported abnormality.
The headphone was held by hand at approximately `150 mm` from the microphone,
so differences of a few centimetres among inferred path lengths are expected
and are not repeatability evidence. The Info panel records:

| Field | Stored result |
| --- | --- |
| Name | `UMC22 loopback-cal-data diagnostic` |
| REW | `V5.40 beta 133` |
| Excitation | `256k` log swept sine, one sweep at `-20.0 dBFS` |
| Frequency range | `20-20000 Hz` |
| Sample rate | `48000.0 Hz` |
| Microphone calibration | None loaded |
| Soundcard calibration | `Loopback cal` |
| Timing ref mode | `Loopback as cal ref` |
| Timing ref output | `L` |
| Timing ref input | `MICROPHONE (Master Volume) R` |
| Timing ref index | `47975.52` |
| System Delay | `0.5100 ms` (`175 mm`, `6.89 in`) |
| Timing offset | `0.0000 ms` |
| Clock adjustment | `0.0 ppm` |
| Peak | `0.5100 ms` |
| IR start | `0.4375 ms` (`150 mm`, `5.91 in`) |
| Signal-to-noise | `43.5 dB` |
| Signal-to-distortion | `70.0 dB` |

The distance conversions again agree with REW:

```text
343 m/s * 0.0004375 s = 0.1501 m = 150 mm
343 m/s * 0.0005100 s = 0.1749 m = 175 mm
```

The IR start happens to match the hand-estimated spacing, while the peak is
approximately `25 mm` later. Neither figure should be treated as a precise
distance measurement because the acoustic source was hand-held. More
importantly, `Soundcard: Loopback cal` proves that REW generated calibration
data from Input 2/R, while reference index `47975.52` and the numeric System
Delay prove that the same capture also supplied timing.

**CALIBRATION-ROUTE DECISION - PASS:** for the UMC22 route, use `Use loopback as
cal and timing reference` with `Make calibration data from loopback response`.
Do not select `Merge loopback response into IR` on the present beta-133 setup.
This closes the amplifier-disconnected qualification and establishes the
candidate live electrical-reference treatment for Gate E. The separate ECM8000
calibration remains mandatory before any reusable acoustic-response sweep.

The raw Gate D REW session is retained as `UMC22 loopback-cal-data
diagnostic.mdat` (`2,426,614` bytes as observed on 2026-09-05). It is
qualification/debug evidence, not loudspeaker FRD. It was committed with the
completed qualification record at the user's request; do not treat it as
disposable generated output.

### 3.5 Gate E - Controlled Powered Woofer Checkout

Only after Gates A-D pass, adapt the switched-off connection and minimum-volume
startup in the now-superseded procedure retained in
[`FRD_REPEATABILITY_DEVELOPMENT_2026-09-03_TO_05.md`](FRD_REPEATABILITY_DEVELOPMENT_2026-09-03_TO_05.md) to
the documented UMC22 contacts. Use the woofer only. Confirm no-signal behaviour,
raise the woofer to `1.00 V RMS`, confirm a gross reference level near
`0.10 V RMS` without clipping, then complete three unmoved repeats. The final
reference level may differ slightly if the verified UMC22 input topology makes
the fixture operate single-ended; record and use the measured result.

#### 3.5.1 Switched-Off Transition To The Full-Dual Circuit

Gate D and the calibration-data route now pass, but do not power either device
while changing topology:

1. Save the useful Gate D measurements, stop every REW signal, turn phantom off,
   wait approximately `15 s`, and disconnect UMC22 USB.
2. Turn UMC22 `OUTPUT`, `GAIN 1`, and `GAIN 2` fully down. Keep `DIRECT MONITOR`
   off. Disconnect the headphones and remove the temporary Output 1 source-
   adaptor connection used for Gate D.
3. Confirm the SU-V570 is off with volume fully down. Select `AUX`, keep `POWER
   AMP DIRECT` off so the normal input selector remains active, centre the
   balance, disable tone/loudness processing, and select speaker bank `B` only.
4. Connect UMC22 Output 1 through the passed TS-to-RCA cable to SU-V570 `AUX`
   left. Leave UMC22 Output 2 and the amplifier's right input unused.
5. Connect only the woofer to SU-V570 speaker-bank `B` left. Keep the tweeter
   electrically disconnected.
6. At the same `B`-left amplifier terminals, connect fixture red/`In+` to
   positive and black/`In-` to negative. Retain the passed breakout between the
   fixture output and UMC22 `INST 2`, with the terminal block restrained and
   insulated.
7. Keep the ECM8000 connected to `MIC / LINE 1` by XLR. Do not enable phantom,
   reconnect USB, or power the SU-V570 yet.

Report this complete switched-off state before proceeding. The next reviewed
stage will power the UMC22 first, restore microphone phantom, confirm no clip or
abnormality, and only then perform the SU-V570 minimum-volume no-signal startup.

**VERIFIED PARTIAL SWITCHED-OFF GATE E STATE - 2026-09-05:** the user reports
the following coherent state:

- UMC22 USB disconnected; phantom off; `GAIN 1`, `GAIN 2`, and `OUTPUT` at
  minimum; `DIRECT MONITOR` off;
- ECM8000 connected to `MIC / LINE 1`;
- `INST 2` connected through the passed breakout and complete fixture to
  SU-V570 speaker-bank `B` left;
- UMC22 Output 1/L connected to SU-V570 `AUX` left;
- SU-V570 off with volume minimum, `AUX` selected, balance centred, tone
  `DEFEAT`, loudness off, bank B enabled, and bank A disabled.

Those reported controls and paths pass. Before USB or amplifier power, confirm
the load and connector details not explicitly included in the report: the
woofer alone is connected to B-left and the tweeter is disconnected; fixture
red/`In+` is on B-left positive and black/`In-` on B-left negative; the breakout
terminal block is restrained and insulated; and headphones, UMC22 Output 2, and
the amplifier right input are unused. The Gate E power-up remains held pending
those confirmations.

**VERIFIED COMPLETE SWITCHED-OFF GATE E STATE - 2026-09-05:** the remaining
connections are now explicit. SU-V570 B-left red/positive feeds both fixture
red/`In+` and woofer positive; B-left black/negative feeds both fixture
black/`In-` and woofer negative. No tweeter or other load is present. UMC22
Output 2, its headphone socket, and SU-V570 `AUX` right are empty. The breakout
terminal block is restrained and insulated so neither its contacts nor
associated conductors can touch a person or unintended object. The user's term
`breaker block` is interpreted here as that already-documented breakout
terminal block.

**SWITCHED-OFF CONNECTION DECISION - PASS:** the full-dual topology, load,
polarity, inactive controls, insulation, and unused sockets are now confirmed.
Keep the SU-V570 off at minimum volume. The next bounded stage is UMC22-only
power-up: keep all REW signals stopped and all UMC22 controls unchanged; connect
the known-good USB cable; then enable phantom for the already-connected ECM8000
and wait approximately `15 s`. Confirm that the phantom indicator illuminates
and report any clip indication, unexpected sound, instability, heat, smell, or
other abnormality. Do not power the SU-V570 yet.

**VERIFIED UMC22-ONLY USB/PHANTOM NO-SIGNAL OBSERVATION - 2026-09-05:** with
the SU-V570 off at minimum volume and all REW signals stopped, the known-good
USB cable was connected and phantom power was enabled without changing the
UMC22 controls or wiring. The phantom indicator illuminated. Neither channel
showed a clip indication; there was no unexpected sound, instability, smell,
heating, or other abnormality.

**UMC22-ONLY POWER-UP DECISION - PASS:** retain the unchanged full-dual wiring,
USB connection, active phantom supply, minimum UMC22 `GAIN 1`, `GAIN 2`, and
`OUTPUT` controls, and `DIRECT MONITOR` off. The next bounded stage is the
SU-V570 minimum-volume no-signal startup:

1. Keep every REW signal stopped. Do not use Generator, Check Levels, or
   Measure.
2. Reconfirm SU-V570 volume at minimum, `AUX` selected, tone `DEFEAT`, loudness
   off, balance centred, bank B enabled, and bank A disabled. Do not change any
   wiring while the amplifier is powered.
3. Switch on the SU-V570 without adjusting its volume or any UMC22 control.
4. Observe for approximately `15 s`. Report whether the woofer remains silent,
   whether either UMC22 channel shows a clip indication, and whether there is
   any unexpected sustained hum/buzz, transient sound, instability, unusual
   heating, smell, smoke, or other abnormality.
5. Switch the SU-V570 off immediately for sustained or otherwise concerning
   sound, clipping, instability, smell, smoke, unusual heating, or any other
   abnormality. Even after a clean observation, do not generate a signal or
   adjust a level until the result is reviewed.

**VERIFIED SU-V570 MINIMUM-VOLUME NO-SIGNAL POWER-UP - 2026-09-05:** the
documented `AUX`, tone `DEFEAT`, loudness-off, centred-balance, bank-B-only
state was reconfirmed. With every REW signal stopped, all UMC22 controls
unchanged, and the complete Gate E wiring retained, the SU-V570 was powered at
minimum volume for approximately one minute. The woofer produced no detectable
sound of any kind. Neither UMC22 channel showed a clip indication, and there
was no transient or persistent hum/buzz, instability, heating, smell, smoke, or
other abnormality.

**SU-V570 NO-SIGNAL DECISION - PASS:** this closes the staged powered no-signal
startup. The next bounded stage is the `1.00 V RMS` woofer-level and gross
reference-level check. The ECM8000 calibration file is not needed for these
two electrical-voltage observations, but it remains mandatory before any
reusable acoustic sweep.

1. Stop every REW signal, switch the SU-V570 off, retain its volume at minimum,
   and make no connection change until it is off. Secure a true-RMS meter in
   AC-voltage mode directly across the woofer terminals without disturbing the
   woofer, amplifier, or fixture wiring.
2. In REW, retain the exact `EXCL:` UMC22 input and output endpoints, `48 kHz`,
   and Java `Stereo only`. Prepare Generator for a `1 kHz` sine on output `L`
   at `-10 dBFS`, but keep Generator stopped.
3. With the amplifier off and Generator stopped, turn only UMC22 `OUTPUT`
   fully clockwise for a repeatable source setting. Retain `GAIN 1` and
   `GAIN 2` at minimum, `DIRECT MONITOR` off, phantom on, and all wiring
   unchanged.
4. Switch on the SU-V570 at minimum volume and confirm the established quiet
   no-signal state. Start Generator, then raise only SU-V570 volume slowly until
   the woofer meter reads `1.00 V RMS`; approximately `0.98-1.02 V RMS` is
   sufficient and avoids needless knob chasing. Stop Generator immediately.
   Stop earlier for any abrupt level jump, UMC22 clip indication, dropout,
   unexpected sound, instability, or other abnormality.
5. With Generator stopped, record the woofer voltage and approximate SU-V570
   volume position. Move the meter to breakout tip-to-ring in AC-voltage mode.
   Do not move any level control.
6. Restart the same tone briefly and confirm the protected reference is broadly
   `0.10 V RMS`; `0.080-0.120 V RMS` passes this gross range check. Stop
   immediately outside that range, for either UMC22 clip indication, a
   reference dropout, or any other abnormality. Stop Generator before moving
   the meter again.
7. Report the woofer voltage, breakout tip-to-ring voltage, approximate
   SU-V570 volume position, clip/dropout state, and any abnormality. Do not run
   Check Levels or Measure yet.

**VERIFIED CONTROLLED WOOFER LEVEL - 2026-09-05:** with the documented source,
amplifier, woofer, and fixture configuration restored, the Agilent U1282A read
`1.0000 V AC` across the woofer terminals with the SU-V570 volume control at
exactly the `-38 dB` mark on its scale. Generator was then stopped and the
system was silent. The scale mark is a reproducibility landmark, not a
calibrated voltage setting; the U1282A remains the authority when restoring the
test level. This passes the absolute woofer-voltage target. The gross protected-
reference voltage and clip/dropout observations remain to be recorded before
input-gain setting or any sweep.

**WOOFER-LEVEL DECISION - PASS:** do not move the UMC22 `OUTPUT` control or
SU-V570 volume. With Generator stopped, move the U1282A to breakout tip-to-ring
in AC-voltage mode and secure the leads. Briefly restart the unchanged `1 kHz`,
`-10 dBFS`, output-L tone. Confirm `0.080-0.120 V RMS`, then stop Generator.
Stop immediately for either UMC22 clip indication, a reference dropout,
instability, or any other abnormality. Report the stable reference voltage,
both clip indications, dropout/instability state, and any other observation.
Do not run Check Levels or Measure yet.

**VERIFIED GROSS PROTECTED-REFERENCE VOLTAGE - 2026-09-05:** with the unchanged
`1 kHz` tone and both level controls fixed, the Agilent U1282A in auto-ranging
AC-voltage mode measured a stable `98.53 mV AC` from breakout tip to ring. With
the woofer level established at `1.0000 V AC`, the measured transfer and
attenuation are:

```text
kmeasured = 0.09853 V / 1.0000 V = 0.09853

attenuation = 20 log10(0.09853) = -20.129 dB
```

Compared with the resistance-derived `0.09892` transfer, the result is only
`-0.39%` (`-0.034 dB`) lower. This is excellent agreement and comfortably
inside the gross `0.080-0.120 V RMS` pass band.

**REFERENCE-VOLTAGE DECISION - PASS FOR LEVEL:** stop Generator if it is still
running and do not change either level control. Before removing the breakout or
advancing to the final direct Input 2 connection, confirm whether either UMC22
clip indicator illuminated during the reference tone and whether there was any
dropout, instability, or other abnormality. None is inferred from the stable
voltage report alone. Do not run Check Levels or Measure yet.

**VERIFIED REFERENCE OBSERVATIONS - 2026-09-05:** Generator was stopped after
the voltage reading. Neither UMC22 clip indicator illuminated during the test,
and there was no dropout, instability, or other abnormality.

**GROSS PROTECTED-REFERENCE DECISION - PASS:** the measured level, agreement
with prediction, clipping margin, and stability all pass. Advance to the final
direct-reference connection without changing either level control:

1. Keep Generator, Check Levels, and Measure stopped. Switch the SU-V570 off
   while retaining its `-38 dB` volume-scale position, and wait for it to
   settle before touching any connection.
2. Remove the U1282A from the breakout. Remove the passed breakout cable from
   between the fixture output and UMC22 `INST 2`, then insert the fixture's TRS
   output plug directly into `INST 2`. Do not disturb the amplifier-terminal
   fixture leads, woofer cable, playback cable, or any level control.
3. If retaining the meter for the next level confirmation, secure it back
   across the woofer terminals in AC-voltage mode while the amplifier is off.
   Leave no exposed breakout contact or loose conductor in the powered setup.
4. Reconfirm UMC22 USB connected, phantom on, `GAIN 1` and `GAIN 2` at minimum,
   `OUTPUT` fully clockwise, and `DIRECT MONITOR` off. Keep every REW signal
   stopped.
5. Switch on the SU-V570 at the retained `-38 dB` position and observe for
   approximately `15 s`. Report whether the woofer remains silent, whether
   either UMC22 clip indicator illuminates, and whether there is any transient
   or persistent hum/buzz, dropout, instability, heating, smell, smoke, or
   other abnormality. Switch off immediately for anything concerning.

Do not generate a signal, change either level control, run Check Levels, or run
Measure until the direct-connection no-signal result is reviewed.

**VERIFIED FINAL DIRECT-REFERENCE NO-SIGNAL STATE - 2026-09-05:** the breakout
was removed, the fixture TRS output was connected directly to UMC22 `INST 2`,
the U1282A was secured back across the woofer, and the specified UMC22/SU-V570
configuration was confirmed. The SU-V570 was powered with every REW signal
stopped. The user reported no abnormalities.

**FINAL DIRECT-CONNECTION DECISION - PASS:** the intended measurement topology
now passes its powered no-signal observation. Retain all physical connections,
UMC22 `OUTPUT` fully clockwise, SU-V570 volume at its `-38 dB` scale mark, the
U1282A across the woofer, `GAIN 1` at minimum, phantom on, and `DIRECT MONITOR`
off. Set only the reference-input gain:

1. In REW, confirm both devices remain the exact `EXCL:` UMC22 endpoints at
   `48 kHz`, Java `Stereo only`, with measurement output L and reference input
   R. Open Level Meters; do not run Check Levels or Measure.
2. With `GAIN 2` at minimum, restart the unchanged output-L `1 kHz`, `-10 dBFS`
   tone. Confirm the U1282A remains within `0.98-1.02 V AC` at the woofer. Stop
   and report rather than adjusting either output level if it lies outside that
   range.
3. Raise only UMC22 `GAIN 2` until `Ref In` RMS is within approximately `-24`
   to `-18 dBFS`; do not chase an exact value. Retain at least `6 dB` peak
   headroom.
4. Stop immediately for a `Ref In` peak at or above `-6 dBFS`, either hardware
   clip indication, a woofer-voltage change outside the stated band, dropout,
   instability, or any other abnormality.
5. After approximately `10 s` of stable indication, stop Generator. Report
   `Ref In` RMS and peak, approximate `GAIN 2` position, U1282A woofer voltage,
   both clip indications, and any dropout or abnormality. Do not change
   `GAIN 1`, run Check Levels, or run Measure yet.

**VERIFIED FINAL REFERENCE-INPUT GAIN - 2026-09-05:** the exact `EXCL:` UMC22
endpoints, `48 kHz`, Java `Stereo only`, measurement output L, and reference
input R were confirmed. With the unchanged tone, the U1282A indicated a stable
`1.0003 V AC` across the woofer, only `+0.03%` (`+0.0026 dB`) above the
established target. Raising only `GAIN 2` to approximately 2 o'clock produced a
stable `Ref In` RMS indication of `-20.87 dBFS`, fluctuating by approximately
`+/-0.01 dB`. The user confirmed at least `6 dB` peak headroom, although no
numeric peak value was recorded. Neither channel clipped; voltages remained
stable; and there was no dropout or other anomaly. Generator was then stopped.

**REFERENCE-INPUT GAIN DECISION - PASS:** retain `GAIN 2` at approximately
2 o'clock, UMC22 `OUTPUT` fully clockwise, SU-V570 at its `-38 dB` scale mark,
`GAIN 1` at minimum, the U1282A across the woofer, all final direct-reference
wiring, and every signal stopped. Before setting microphone gain or capturing
any reusable response, identify the exact ECM8000 calibration filename/source
and whether it is intended for 0-degree or 90-degree incidence. That
identification is recorded in the next checkpoint. Do not run Check Levels or
Measure yet.

**PROVISIONAL GENERIC MICROPHONE CALIBRATION - 2026-09-05:** the supplied
`../calibration/ECM8000_calibration_data.csv` is identified as a generic
`0-degree` ECM8000 response. It contains `124` strictly ascending numeric rows
from `20` to `21999 Hz`, gain values from `-4.920` to `+1.015 dB`, and phase.
Its as-supplied SHA-256 was
`c64553a2ff0e2f2799bf1bd8a275ea649c3a1aae7ff2dd39fba1b572953b4d6d`.
REW documents comma-delimited calibration rows as requiring at least one space
after each comma. Spaces were therefore added after the commas without changing
any numeric value. The retained, directly REW-compatible CSV now has SHA-256
`bb8fba5b6ae58b5a84d4ba47807ca61d49cc291325a0c3b43fae7294407c5e23`.

This is not a serial-number-specific calibration and contains no microphone
sensitivity. It is acceptable as a clearly identified, provisional correction
for this hobby measurement series, but it does not establish unit-specific
magnitude/phase accuracy or calibrated absolute SPL. In particular, its
approximately `-4.92 dB` endpoint at `21999 Hz` would make REW apply a large
positive upper-treble correction, where unknown microphone-to-microphone
variation is most consequential. Preserve that limitation in exported FRD
provenance.

**VERIFIED REPORTED MICROPHONE/ROTATION GEOMETRY - 2026-09-05:** the microphone
tip is `1000 mm` from the baffle plane, its body is perpendicular to that plane
and aimed at the cabinet, and it is level with the centre of the woofer dome
and horizontally centred on the baffle. The loudspeaker is secured on a sturdy-
table jig that rotates it about the horizontal centre of the baffle plane and
is marked in 10-degree increments. The microphone incidence therefore matches
the generic `0-degree` calibration. Keep the microphone fixed for the later
off-axis series.

**CALIBRATION-LOAD NEXT STEP:** keep Generator and every REW measurement signal
stopped and retain all established hardware controls. In REW, enable separate
calibration by input if needed, load
`calibration/ECM8000_calibration_data.csv` for measurement input L only, and
leave electrical-reference input R without microphone calibration. Confirm the
filename and input assignment shown by REW and report any warning. Do not run
Check Levels or Measure until that assignment is reviewed.

**VERIFIED PRE-CONSOLIDATION CALIBRATION LOAD - PASS (2026-09-05):** REW showed
no warning while loading the derived calibration. Closing and reopening
Preferences showed that it persisted for the left channel only of the exact
`EXCL:` UMC22 microphone input; the right channel showed `None`. This verifies
the calibration parser and per-input assignment mechanism.

**CANONICAL-FILE DECISION - 2026-09-05:** at the user's request the compatible
format was folded into `../calibration/ECM8000_calibration_data.csv` and the
redundant `.cal` copy was deleted. Numeric calibration values are unchanged.
At that checkpoint REW's persisted entry named the removed file, so the retained
CSV had to be reselected on input L before setting `GAIN 1` or producing any
signal. The completed re-selection is recorded immediately below.

**VERIFIED CANONICAL CALIBRATION ASSIGNMENT - PASS (2026-09-05):** the retained
`../calibration/ECM8000_calibration_data.csv` was selected for the left channel
of the exact `EXCL:` UMC22 microphone input. Closing and reopening Preferences
showed that the new filename persisted; the right channel remained `None`.
The generic 0-degree microphone correction is therefore active only on the
acoustic measurement channel.

**MICROPHONE-GAIN CHECK LEVELS NEXT STEP:** this authorises only a bounded REW
Check Levels observation, not a measurement sweep:

1. Keep Generator stopped and retain every physical connection and control:
   UMC22 `OUTPUT` fully clockwise, `GAIN 2` approximately 2 o'clock, `GAIN 1`
   minimum, Direct Monitor off, phantom on, SU-V570 at its `-38 dB` scale mark,
   and the U1282A across the woofer.
2. In Measure, reconfirm Java `Stereo only`, exact `EXCL:` UMC22 input/output,
   `48 kHz`, measurement and reference outputs L, measurement input L,
   reference input R, `Use loopback as cal and timing reference`, `Make
   calibration data from loopback response`, and `Merge loopback response into
   IR` off. Confirm the retained CSV is shown for input L only.
3. Set the level to the established final `-10 dBFS`. Do not change the UMC22
   Output control or SU-V570 volume. Run `Check Levels`; while it is active,
   raise only `GAIN 1` slowly until main-input peaks are approximately `-18` to
   `-12 dBFS`. About `-15 dBFS` is a convenient centre, not a target to chase.
4. Retain at least `6 dB` main-input peak headroom. Stop immediately for an
   input peak at or above `-6 dBFS`, either hardware clip indication, dropout,
   unexpected rubbing/buzzing, instability, unusual heating, smell, or any
   other abnormality. The normal broadband Check Levels sound is not itself an
   abnormality.
5. After approximately `10 s` of stable levels, stop Check Levels. Report main
   `In` RMS and peak, `Ref In` RMS and peak, approximate `GAIN 1` position, both
   UMC22 clip indications, and any dropout or other abnormality. Do not alter a
   gain or run Measure afterward.

**VERIFIED MICROPHONE-GAIN CHECK LEVELS - PASS (2026-09-05):** with the
specified settings confirmed, raising only `GAIN 1` to approximately 4 o'clock
produced main `In` near `-15.5 dBFS`. `Ref In` was near `-33.8 dBFS`; both
indications varied by less than approximately `+/-1 dB`. Neither UMC22 clip
indicator illuminated, and there was no dropout or other anomaly.

The main level is comfortably within REW's documented acceptable `-30` to
`-12 dBFS` RMS range for an analogue microphone/preamp input. Do not raise
`GAIN 2` to match the Check Levels pink-noise indication: its direct coherent
`1 kHz` result is already `-20.87 dBFS`, REW defines loopback calibration level
at `1 kHz`, and no reference control has moved. The first sweep will directly
test whether actual reference headroom, timing detection, and calibration data
are valid.

**MICROPHONE-GAIN DECISION - PASS:** retain both gains and all output-level and
physical settings. One bounded acoustic checkout sweep is now approved:

1. Confirm the woofer is still the only connected drive unit and the room and
   `1000 mm` on-axis geometry are unchanged. Keep the U1282A connected but do
   not interpret its changing swept-signal display as a calibrated broadband
   RMS reading.
2. In Measure, use the exact `EXCL:` UMC22 endpoints, Java `Stereo only`,
   `48 kHz`, measurement/reference outputs L, measurement input L, reference
   input R, `Use loopback as cal and timing reference`, `Make calibration data
   from loopback response`, and `Merge loopback response into IR` off. Confirm
   the canonical ECM8000 CSV is active on input L only.
3. Set SPL sweep, `20-20000 Hz`, `-10 dBFS`, `256k`, one repetition, timing
   offset `0.0000 ms`, clipping abort enabled, and name
   `SB17 UMC22 acoustic checkout 1`.
4. Run exactly one measurement. Stop immediately for a hardware clip
   indication, REW clipping warning, severe rubbing/buzzing, dropout,
   instability, unusual heating, smell, or any other abnormality.
5. If it completes, do not run another sweep or alter any control. Report the
   main and reference headroom shown during measurement; numeric timing-
   reference index and System Delay; IR peak and IR start; output and reference-
   input channels; microphone and soundcard-calibration entries; whether the
   impulse has one clear dominant arrival; whether the magnitude curve is
   grossly woofer-like rather than almost flat; and any warning or abnormality.

**VERIFIED ACOUSTIC CHECKOUT ATTEMPTS - 2026-09-05:** the first run at
`-10 dBFS` raised a distortion warning and showed inadequate available
headroom. The user therefore repeated the same bounded checkout at `-20 dBFS`.
That suppressed the warning, but the Measure dialog still showed minimum
headroom occasionally approaching approximately `3.8 dB`; the screenshots do
not identify which channel supplied that minimum. Neither attempt produced a
hardware clip indication, dropout, or other abnormality.

The `-20 dBFS` Measurement Info and plots establish:

- REW `V5.40 beta 133`, `20-20000 Hz`, one `256k` log sweep, `48 kHz`;
- exact UMC22 measurement input L and output L, reference output L/input R;
- `Soundcard: Loopback cal`, timing-reference index `47850.03`, System Delay
  and IR peak `3.1243 ms`, IR start `3.0000 ms`, and clock adjustment `0.0 ppm`;
- SNR `43.8 dB` and signal-to-distortion `23.1 dB`;
- one clear dominant impulse arrival and a grossly woofer-like, non-flat
  magnitude response; and
- critically, `Mic: No cal file`.

**CALIBRATION-APPLICATION CORRECTION:** the previous canonical-file conclusion
is narrowed. It proved Preferences persistence on the left channel but not
application to the active source. The Cal files screenshot associates the CSV
with the exact device's `Default Input`, while Soundcard and Measurement Info
show the active source as `MICROPHONE (Master Volume), L`. The `-20 dBFS` run
therefore passes as routing, loopback-calibration, timing, and gross acoustic-
path evidence only. Neither run is reusable microphone-calibrated FRD.

**HEADROOM INFERENCE, NOW RESOLVED FOR THE NEXT CONTROL:** the screenshot did
not capture which channel supplied the approximately `3.8 dB` minimum, so that
number alone did not initially authorise a gain change. The independent
reference result does discriminate the channels: `Ref In` was `-20.87 dBFS` at
the higher `-10 dBFS` excitation, hence approximately `-30.87 dBFS` is expected
after reducing excitation to `-20 dBFS`. The electrical reference therefore
has far more than `3.8 dB` nominal margin and `GAIN 2` remains qualified. The
limiting path is consequently the microphone input. Reducing `GAIN 1` by
approximately `4 dB` should move the observed margin to approximately `7.8 dB`;
the next sweep must verify that prediction.

**COMPLETED NO-SIGNAL CALIBRATION CHECK:** keep Generator, Check Levels, and Measure
stopped and change no physical control. In Soundcard, confirm the selected
input is the exact `EXCL:` UMC22 device with `MICROPHONE (Master Volume)`, L.
In Cal files, locate the entry for that complete active input identity—not
`Default Input`—enable separate calibration per input, load
`calibration/ECM8000_calibration_data.csv` on L only, and leave R as `None`.
The active entry should be highlighted. Then use Measure's Cal files button to
confirm the microphone file is listed for the pending measurement. Report the
complete entry labels shown. Signal and gains remained unchanged while this
check was performed.

**VERIFIED CORRECTED ACTIVE-SOURCE PREFERENCES ASSOCIATION - PASS
(2026-09-05):** with all signals stopped, Soundcard shows input device
`EXCL: Behringer UMC22 (USB Audio CODEC)`, input selector
`MICROPHONE (Master Volume)`, and channel L. The ECM8000 CSV is now assigned to
that specific input on the left channel only, and the configuration persists
across Preferences close/reopen. This passes the Preferences half of the
correction. Signal remained held pending the measurement-level check below.

**VERIFIED PENDING-MEASUREMENT CALIBRATION APPLICATION - PASS (2026-09-05):**
Measure's `Calibration data` display identifies the exact UMC22
`MICROPHONE (Master Volume)` source and shows `ECM8000_calibration_data.csv`
under Mic calibration files for L. The pending Measure dialog explicitly uses
`MICROPHONE (Master Volume) L` as its input and
`MICROPHONE (Master Volume) R` as its timing-reference input. REW does not show
a separate microphone-calibration row for the timing-reference channel in this
view. The file is therefore confirmed for the pending measurement input, with
no displayed evidence of application to the electrical reference. The
soundcard-calibration row showing `None` before the sweep is expected because
the selected mode makes calibration data dynamically from the loopback
response rather than loading a stored soundcard file.

**NEXT CONTROLLED MICROPHONE-GAIN CORRECTION:** retain the `-20 dBFS` Measure
level, `GAIN 2`, UMC22 Output, SU-V570 volume, wiring, and physical geometry.
Run `Check Levels`, allow the main-input indication to settle, and record its
starting level. Reduce only `GAIN 1` until the main indication is approximately
`4 dB` below that starting level; do not chase better than about `+/-0.5 dB`.
Stop Check Levels and report the before/after main and reference indications,
approximate final `GAIN 1` position, and any warning or abnormality. A `4 dB`
input-gain reduction should turn the previously observed approximately
`3.8 dB` minimum sweep headroom into approximately `7.8 dB`. This is a
prediction, not a pass: one subsequent bounded `-20 dBFS` sweep must confirm
at least `6 dB` actual headroom and a Measurement Info mic-file entry.

**VERIFIED MICROPHONE-GAIN ADJUSTMENT - PASS (2026-09-05):** during
the authorised `-20 dBFS` Check Levels observation, main `In` moved from
approximately `-15.5 dBFS` to approximately `-19.3 dBFS` after reducing only
`GAIN 1`. The achieved reduction is therefore:

```text
-19.3 dBFS - (-15.5 dBFS) = -3.8 dB

predicted minimum sweep headroom = 3.8 dB + 3.8 dB = 7.6 dB
```

The knob moved only a few degrees and remains approximately at its 4 o'clock
position; the measured level change, not the coarse clock description, defines
the adjustment. The predicted `7.6 dB` exceeds the `6 dB` target but is not yet
a measured sweep result. `Ref In` was stable at `-33.58 dBFS` with only
`+/-0.01 dB` fluctuation. There was no warning, clipping, dropout, or other
abnormality. Retain `GAIN 1` at this new position. This closes the gain-
adjustment gate and authorises only the verification sweep below.

**NEXT CALIBRATED HEADROOM-VERIFICATION SWEEP:**

1. Retain the woofer-only connection, `1000 mm` on-axis geometry, U1282A,
   SU-V570 `-38 dB` setting, UMC22 Output, both input gains, and all wiring.
2. Confirm Java `Stereo only`, the exact `EXCL:` UMC22 endpoints, `48 kHz`,
   measurement/reference outputs L, measurement input L, reference input R,
   `Use loopback as cal and timing reference`, `Make calibration data from
   loopback response`, and `Merge loopback response into IR` off.
3. Confirm Measure's Calibration data still names
   `ECM8000_calibration_data.csv` for microphone input L. Use SPL sweep,
   `20-20000 Hz`, `-20 dBFS`, `256k`, one repetition, timing offset
   `0.0000 ms`, and clipping abort enabled. Name it
   `SB17 UMC22 calibrated headroom checkout 1`.
4. Run exactly one sweep. Watch the headroom indication and note the value
   closest to zero, retaining REW's displayed sign. Stop immediately for any
   clipping or distortion warning, hardware clip indication, severe rubbing or
   buzzing, dropout, instability, unusual heating, smell, or other abnormality.
5. After completion, do not alter any control or run another sweep. Report the
   closest-to-zero headroom value, every warning or abnormality, and the
   Measurement Info entries for `Mic`, `Soundcard`, timing-reference index,
   System Delay, output channel, timing-reference output/input, SNR, and signal
   to distortion. A screenshot of Measurement Info is sufficient.

**VERIFIED CALIBRATED HEADROOM-CHECKOUT EXECUTION - PARTIAL PASS / HEADROOM
FAIL (2026-09-05):** the user confirmed the ECM8000 file was still in place and
ran exactly one authorised sweep. It completed without warning or anomaly. The
captured Measure display shows `3.6 dB` main-input headroom in red and
`32.9 dB` reference headroom in green. The reference channel is therefore not
limiting; the microphone input remains below the required `6 dB` margin.

The predicted `7.6 dB` margin is superseded by this direct sweep observation.
The approximately `3.8 dB` change seen with broadband Check Levels did not
produce the predicted improvement at the sweep's narrow worst-case peak. That
does not by itself establish whether the discrepancy arose from stimulus
spectrum/statistics, level-reading variability, or control resolution. Do not
repeat Check Levels or another sweep merely to investigate it. Keep all signals
stopped and controls unchanged while the completed measurement's Info panel and
peak frequency are reviewed. The Info panel must still prove that the mic file
was stored with this measurement.

**VERIFIED CALIBRATED CHECKOUT METADATA AND PEAK - PASS FOR DIAGNOSIS
(2026-09-05):** Measurement Info confirms the requested name, exact UMC22
`MICROPHONE (Master Volume), L` source, one `256k` `20-20000 Hz` sweep at
`-20.0 dBFS`, `48 kHz`, `Mic: ECM8000_calibration_data.csv`, and
`Soundcard: Loopback cal`. It records timing-reference index `47849.89`, System
Delay and IR peak `3.1273 ms`, IR start `3.0000 ms`, timing-reference output L,
timing-reference input `MICROPHONE (Master Volume) R`, timing offset `0.0000 ms`,
and clock adjustment `0.0 ppm`. SNR is `44.4 dB` and signal-to-distortion is
`34.3 dB`. The user located the highest response peak at `6.07 kHz`.

This proves microphone-calibration application, routing, loopback calibration,
and timing for the checkout. It does not override the `3.6 dB` main-headroom
failure, so the response remains diagnostic rather than the retained FRD
baseline.

**NEXT TARGETED MICROPHONE-GAIN SETTING:** use the measured `6.07 kHz` peak to
set worst-case gain directly, without another broadband trial:

1. Keep every control, connection, and physical position unchanged initially.
   Keep any measurement sweep stopped.
2. Open REW Generator and select sine, `6070 Hz`, `-20 dBFS`, output L only.
   Open the Levels tool so main `In` RMS and peak and `Ref In` can be read.
3. Start the tone. Record the initial main-input peak, then reduce only
   `GAIN 1` slowly until the stable main-input peak is approximately
   `-9` to `-10 dBFS`. Do not chase better than approximately `+/-0.5 dB`.
4. Stop the tone as soon as the setting is stable, and in any case after no
   more than approximately `10 s` of continuous output. A pure high-frequency
   tone is expected. Stop immediately for a hardware clip indication,
   distortion or abnormal sound, dropout, instability, unusual heating, smell,
   or any other abnormality.
5. Report initial and final main `In` RMS and peak, final `Ref In` RMS and peak,
   approximate `GAIN 1` position, and any warning or abnormality. Do not run a
   sweep afterward.

The target deliberately provides `9-10 dB` peak headroom rather than merely
meeting `6 dB`. Relative to the measured `3.6 dB`, it may require approximately
`5.4-6.4 dB` further microphone-gain reduction. Current SNR `44.4 dB` suggests
that cost is proportionate; the next sweep must nevertheless verify both
headroom and usable SNR.

**VERIFIED TARGETED MICROPHONE-GAIN SETTING - PASS (2026-09-05):** at the
measured `6.07 kHz` response maximum and `-20 dBFS` generator level, main-input
peak was initially approximately `-2 dBFS`. Reducing only `GAIN 1` to
approximately 2 o'clock produced a final main-input peak of approximately
`-10.3 dBFS`, an observed reduction of:

```text
-10.3 dBFS - (-2.0 dBFS) = -8.3 dB
```

This directly establishes approximately `10.3 dB` main-input peak headroom at
the identified worst-case frequency. No equipment or signal abnormality was
reported. The unchanged reference path already demonstrated `32.9 dB`
headroom during the preceding full sweep, so another reference reading is not
required for this proportionate gate. Retain `GAIN 1` at 2 o'clock and change
no other control.

**NEXT FINAL HEADROOM-VERIFICATION SWEEP:** repeat the exact calibrated checkout
once, using the existing physical setup and `20-20000 Hz`, `-20 dBFS`, `256k`,
one repetition, zero timing offset, clipping abort, Java `Stereo only`, exact
`EXCL:` UMC22 endpoints, L/L/L/R routing, loopback calibration/timing,
calibration data made from the loopback response, IR merge off, and the
ECM8000 CSV on microphone input L. Name it
`SB17 UMC22 calibrated headroom checkout 2`. Watch and report both headroom
values. Stop for any warning, hardware clip, abnormal sound, dropout,
instability, heating, smell, or other abnormality. After exactly one sweep,
change no control and provide Measurement Info; do not repeat before review.

**VERIFIED FINAL CALIBRATED CHECKOUT - PASS / REPEATABILITY RUN 1
(2026-09-05):** `SB17 UMC22 calibrated headroom checkout 2` completed with its
highest displayed main-input level `-10.7 dBFS` and reference level
`-33 dBFS`, equivalent to `10.7 dB` and `33 dB` headroom respectively. Both
remained green throughout; there was no warning or abnormality.

Measurement Info confirms one `256k`, `20-20000 Hz`, `-20.0 dBFS` sweep at
`48 kHz`, exact UMC22 `MICROPHONE (Master Volume), L` source, output L,
`Mic: ECM8000_calibration_data.csv`, and `Soundcard: Loopback cal`. It records
timing-reference index `47849.96`, System Delay and IR peak `3.1257 ms`, IR
start `3.0000 ms`, timing-reference output L/input R, timing offset `0.0000 ms`,
clock adjustment `0.0 ppm`, SNR `43.5 dB`, and signal-to-distortion `62.5 dB`.
The checkout therefore passes calibration, routing, timing, headroom, signal
quality, and stable execution at the final gain setting.

This capture already has every final setting required for the repeatability
set, so it is designated run 1 rather than making an immaterial fourth sweep.
Do not change any control, wiring, or physical position. Run exactly two more
identical sweeps named `SB17 UMC22 repeat 2` and `SB17 UMC22 repeat 3`. After
each, record both headroom values and any warning or abnormality. After both,
save the session under a new filename
`rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat` without overwriting or
deleting the existing diagnostic `.mdat`. Provide Measurement Info for runs 2
and 3 and do not proceed to windowing or another measurement before review.

**VERIFIED REPEATABILITY RUNS 2 AND 3 - METADATA PASS (2026-09-05):** the two
requested Measurement Info panels show:

| Run | Measurement | Timing index | System Delay / IR peak | SNR | Signal to distortion |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | `SB17 UMC22 calibrated headroom checkout 2` | `47849.96` | `3.1257 ms` | `43.5 dB` | `62.5 dB` |
| 2 | `SB17 UMC22 repeat 2` | `47849.92` | `3.1267 ms` | `44.3 dB` | `60.2 dB` |
| 3 | `SB17 UMC22 repeat 3` | `47849.93` | `3.1264 ms` | `44.3 dB` | `64.0 dB` |

All three store `Mic: ECM8000_calibration_data.csv`, `Soundcard: Loopback cal`,
`48 kHz`, output L, timing-reference output L/input R, IR start `3.0000 ms`,
timing offset `0.0000 ms`, and clock adjustment `0.0 ppm`. Relative to run 1,
runs 2 and 3 differ by `+1.0 us` and `+0.7 us`; total System Delay spread is
`1.0 us`, comfortably passing the preferred `5 us` limit.

Runs 2 and 3 also stayed green throughout their live sweeps and produced no
warning, clipping, dropout, or other abnormality. The live-execution and
headroom review therefore passes for all three final-setting runs.

The session is retained as
`rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat`, size `19138881` bytes,
SHA-256 `b47e6aca826a4a95d77dfcab731edac95c2c6bf21be56f8bf249fcf23bd5e3c1`.
It is unique raw evidence and was committed with the completed qualification
record at the user's request; do not delete or ignore it.

**DERIVED API EXTRACTION AND UNWINDOWED COMPARISON - 2026-09-05:** the project's
REW API client successfully extracted all eight measurements from the saved
session with no manifest warnings, `None` smoothing, and a common native
`0.3662109673 Hz` grid of `54559` points. The manifest reproduces the raw-file
size and SHA-256 above. For the three final-settings captures over `1-5 kHz`,
the pointwise magnitude range has median `1.056 dB`, 95th percentile
`4.354 dB`, and maximum `32.364 dB`; circular phase range has median
`7.045 degrees`, 95th percentile `33.742 degrees`, and maximum
`179.819 degrees`. These values do not pass the final repeatability targets.

**INFERENCE - NOT YET A HARDWARE FAILURE:** each run still has its long default
IR windows: Tukey `0.25`, left `311.9167 ms`, right `500 ms`. The largest
magnitude difference occurs at a deep, narrow cancellation near `1339.23 Hz`,
where the three extracted values are approximately `43.08`, `75.45`, and
`73.50 dB`. That pattern is consistent with an unstable unwindowed room-
reflection null and is not proportionate evidence of a `32 dB` interface-gain
change, especially given the `0.037 dB` spread of the three IR peak amplitudes
and `1.0 us` delay spread. At that checkpoint the comparison required one
common reflection-excluding IR window before accepting or rejecting the
measurement chain. The three raw IRs were therefore extracted without another
signal or measurement change, producing the superseding result below.

**DERIVED RAW-IR DIRECT-WINDOW COMPARISON - PASS (2026-09-05):** a second,
explicit extraction selected only the three final-setting measurement UUIDs and
included their unwindowed impulse responses. The manifest records measurements
`22`/`23`/`24`, `131072` impulse samples per run at `48 kHz`, the same source
size and SHA-256 as above, and no warnings. The ignored, reconstructible export
is `outputs/rew-api/sb17nrx2c35-8_umc22_repeatability-final-ir/`; the `.mdat`
remains the raw authority.

For the qualification comparison, each impulse was windowed relative to its own
direct peak with the same support: `2.0 ms` left and `1.0 ms` right. The outer
half of each side used a raised-cosine taper and the inner half remained unity.
A full `131072`-point FFT retained the native `0.3662109375 Hz` bin spacing;
phase included each CSV's absolute time origin, so the measured inter-run delay
differences were not removed. Over `1-5 kHz`, with no smoothing, the three-run
magnitude range has median `0.0635 dB`, 95th percentile `0.0736 dB`, and maximum
`0.0743 dB` at `2191.41 Hz`. The circular phase range has median
`0.994 degrees`, 95th percentile `1.815 degrees`, and maximum `1.931 degrees`
at `4999.88 Hz`. These pass the approximately `0.2 dB` magnitude target and the
nearly-coincident phase requirement by clear margins. At the intended
`2.3 kHz` crossover region, magnitude spread is `0.0735 dB` and phase spread is
`0.697 degrees`.

**WINDOW-SENSITIVITY INFERENCE:** the direct-window result remains similarly
tight with right-window values from `0.8` through `1.2 ms`; admitting later
energy progressively degrades the three-run comparison, and a `1.5 ms` right
window already exceeds the magnitude target. Runs 2 and 3 remain extremely
close even with a `3.0 ms` right window, while run 1 diverges in the later
field. This supports changing room/reflection energy after the direct arrival,
not interface instability. It does not identify one particular reflecting
surface.

The `3.0 ms` total window span has approximately `333 Hz` nominal resolution.
It is adequate for this `1-5 kHz` interface/repeatability gate and the intended
`2.2-2.4 kHz` crossover region, but it is not adopted as the final production
FRD window. Reusable woofer FRD must use one documented REW-native window chosen
from the actual impulse/ETC and required bandwidth. No raw measurement or saved
REW window was modified by this derived analysis.

## 4. Release Decision

| Decision | State |
| --- | --- |
| Reuse qualified fixture components | YES |
| Accept possible UMC22 input damage in an amplifier fault | YES - user risk acceptance, 2026-09-05 |
| UMC22 rear-output internal contact topology | PASS - user-observed PCB inspection; physical TRS, ring/sleeve common, TS-equivalent, 2026-09-05 |
| UMC22 `INST 2` unpowered contact map | PASS - tip isolated; ring/sleeve/USB shell common, 2026-09-05 |
| UMC22 `INST 2` phantom isolation | PASS - off maximum `0.0005 V DC`; on maximum observed settling approximately `0.0020 V DC`, all pairs settled to zero, 2026-09-05 |
| Gate C amplifier-positive isolation | PASS - `9125 ohm` to tip and `10127 ohm` to every mapped return; no R1 bypass, 2026-09-05 |
| Gate C low-resistance return map | PASS - amplifier local `0.137 ohm`; complete mapped returns `0.290-0.311 ohm`, stable, 2026-09-05 |
| Gate D amplifier-disconnected no-signal check | PASS - `0.0015 V DC` initial, settled to zero; no clipping or abnormality, 2026-09-05 |
| Gate D REW device enumeration | PASS - Java exclusive UMC22 input/output, independent L/R, `48 kHz`, calibration `None`, 2026-09-05 |
| Gate D channel/timing UI assignment | CORRECTED - measurement output/input L, timing-reference output L, reference input R; prior no-excitation reference-output R assignment was invalid, 2026-09-05 |
| Gate D pre-excitation settings | PASS - input scalar `1.00`, name `UMC22 low-voltage loopback 1`, `20-20000 Hz`, `-20 dBFS`, `1M`, one repetition, 2026-09-05 |
| Gate D controlled `1 kHz` AC level | PASS - `0.0207 V RMS`, slowly `0.0205-0.0210 V RMS`, `OUTPUT` approximately 3 o'clock, no clipping/dropout/abnormality, 2026-09-05 |
| Gate D live reference capture | PASS - selecting the missing `EXCL:` input endpoint restored linear `GAIN 2` response; `Ref In` `-20.88 dBFS`, external `0.0218 V RMS`, 2026-09-05 |
| Gate D Input 1 microphone channel | PASS - normal response to local sound and `GAIN 1`; approximately `-83 dBFS` at minimum, speech approximately `-18 dBFS` with gain at 2 o'clock; no clipping/abnormality, 2026-09-05 |
| Gate D headphone-to-microphone full-duplex level setup | PASS - `In` `-19.5 dBFS`, `Ref In` `-20.84 dBFS`, external `0.0230 V RMS`; stable with no clipping/dropout/abnormality, 2026-09-05 |
| Gate D first `1M` full-duplex sweep execution | PASS for stream stability - completed without warning, error, clipping, audible discontinuity, or abnormality; one dominant impulse arrival, 2026-09-05 |
| Gate D first-sweep timing validity | FAIL - timing ref index `N/A`, System Delay `Not available`; reference output R was unconnected while the fixture sensed output L, 2026-09-05 |
| Gate D second `1M` full-duplex sweep execution | PASS for stream stability - `0.0222 V AC`; no unexpected warning, clipping, or dropout, 2026-09-05 |
| Gate D second-sweep response/timing validity | FAIL - stored timing-reference input L duplicated measurement input L, producing an invalid almost-flat self-referenced trace; timing index `N/A`, System Delay `Not available`, 2026-09-05 |
| Gate D exact-routing attempt | HELD - changing reference input to R raised a REW V5.40 beta 133 `Index 1 out of bounds for length 1` exception; no valid result, 2026-09-05 |
| Gate D post-restart settings audit | PASS - exact `EXCL:` endpoints, `48 kHz`, L/L/L/R routing, loopback merge/timing, zero offset and sweep fields visually correct, 2026-09-05 |
| Gate D stereo-capture exact-routing sweep | FAIL for timing metadata - completed without the prior exception and stored output L/reference input R, but timing index `N/A` and System Delay `Not available`; peak `0.5100 ms`, IR start `0.4792 ms`, 2026-09-05 |
| Gate D retained-capture diagnostic | WITHDRAWN - current REW Scope is live-only and cannot display a preceding measurement's raw captures, 2026-09-05 |
| Gate D timing-only diagnostic | PASS - reference index `47970.52`, System Delay `0.6141 ms`, L/L/L/R routing, no warning/clipping/dropout/exception, 2026-09-05 |
| Gate D overall | PASS - low-voltage hardware, two-channel stream, routing and ordinary loopback timing qualified; IR merging remains excluded |
| ECM8000 calibration for Gate D diagnostic | NOT LOADED - immaterial to Gate D timing |
| ECM8000 calibration source | IDENTIFIED - generic `0-degree` CSV, not unit-specific and without sensitivity; commas made directly REW-compatible without numeric change, 2026-09-05 |
| Initial microphone/rotation geometry | PASS AS REPORTED - `1000 mm`, aimed at cabinet on woofer axis; fixed microphone and secured 10-degree loudspeaker jig, 2026-09-05 |
| ECM8000 calibration parser/per-input mechanism | PASS - no warning; pre-consolidation file persisted on exact `EXCL:` UMC22 input L only while R showed `None`, 2026-09-05 |
| Canonical ECM8000 CSV Preferences persistence | PASS, NARROWED - retained CSV persisted on exact device `Default Input`, L, with R `None`; this did not match the active input selector, 2026-09-05 |
| Prior canonical ECM8000 application to acoustic measurement | FAIL - Measurement Info says `Mic: No cal file`; the old `Default Input` association did not apply |
| Corrected active-source ECM8000 Preferences association | PASS - CSV persists on exact `EXCL:` UMC22 `MICROPHONE (Master Volume), L` only, 2026-09-05 |
| Pending-measurement ECM8000 application | PASS - Measure's Calibration data display names `ECM8000_calibration_data.csv` for active microphone input L; pending Measure input is `MICROPHONE (Master Volume) L` and timing-reference input is R, 2026-09-05 |
| UMC22/electrical-reference calibration route | PASS - `Soundcard: Loopback cal`, reference index `47975.52`, System Delay `0.5100 ms`, no warning/abnormality, 2026-09-05 |
| Gate E switched-off full-dual assembly | PASS - woofer/fixture parallel with correct polarity; controls inactive; breakout insulated; headphone, Output 2, and AUX right empty, 2026-09-05 |
| Gate E UMC22-only USB/phantom no-signal observation | PASS - phantom indicator illuminated; neither channel clipped; no unexpected sound, instability, heating, smell, or other abnormality, 2026-09-05 |
| Gate E SU-V570 minimum-volume no-signal power-up | PASS - approximately one minute; woofer silent; no UMC22 clipping, transient or persistent hum/buzz, instability, heating, smell, smoke, or other abnormality, 2026-09-05 |
| Gate E woofer level | PASS - Agilent U1282A measured `1.0000 V AC` at the woofer with SU-V570 volume on its `-38 dB` scale mark; Generator then stopped and system silent, 2026-09-05 |
| Gate E gross protected-reference voltage | PASS - stable `98.53 mV AC` tip-to-ring, measured transfer `0.09853` (`-20.129 dB`), only `-0.39%` from prediction; no clipping, dropout, instability, or other abnormality, 2026-09-05 |
| Gate E final direct-reference no-signal state | PASS - breakout removed, fixture connected directly to `INST 2`, U1282A returned to woofer, configuration confirmed, and no abnormality after SU-V570 power-up, 2026-09-05 |
| Gate E final reference-input gain | PASS - stable `Ref In` `-20.87 dBFS` (`+/-0.01 dB`) with `GAIN 2` approximately 2 o'clock and woofer `1.0003 V AC`; at least `6 dB` peak headroom, no clipping/dropout/anomaly, 2026-09-05 |
| Gate E microphone-input gain | PASS, FINAL - `GAIN 1` approximately 2 o'clock; targeted `6.07 kHz` peak `-10.3 dBFS`, subsequent full-sweep main headroom `10.7 dB`; reference `33 dB`; no warning/abnormality, 2026-09-05 |
| Gate E acoustic checkout at `-10 dBFS` | FAIL - distortion warning and inadequate headroom; no hardware anomaly, 2026-09-05 |
| Gate E acoustic diagnostic at `-20 dBFS` | PARTIAL PASS - warning-free routing/timing/loopback-cal evidence with numeric timing and plausible impulse; only about `3.8 dB` minimum headroom and `Mic: No cal file`, so not reusable FRD |
| Gate E calibrated headroom checkout at `-20 dBFS` | FAIL FOR MAIN HEADROOM, PASS FOR DIAGNOSTIC METADATA - completed without warning/anomaly; main `3.6 dB`, reference `32.9 dB`; mic CSV, loopback cal, L/L/R routing and numeric timing confirmed; highest peak `6.07 kHz`, 2026-09-05 |
| Gate E targeted `6.07 kHz` microphone-gain setting | PASS - main peak reduced from about `-2` to `-10.3 dBFS` (`-8.3 dB`) with `GAIN 1` approximately 2 o'clock; no equipment/signal abnormality, 2026-09-05 |
| Gate E final calibrated checkout / repeatability run 1 | PASS - main `-10.7 dBFS`, reference `-33 dBFS`, both green; mic CSV and loopback cal stored; timing index `47849.96`, System Delay `3.1257 ms`, SNR `43.5 dB`, signal-to-distortion `62.5 dB`; no warning/abnormality, 2026-09-05 |
| Gate E repeatability run 2 metadata | PASS - mic CSV/loopback cal/L-L-R route; timing index `47849.92`, System Delay `3.1267 ms`, SNR `44.3 dB`, signal-to-distortion `60.2 dB`, 2026-09-05 |
| Gate E repeatability run 3 metadata | PASS - mic CSV/loopback cal/L-L-R route; timing index `47849.93`, System Delay `3.1264 ms`, SNR `44.3 dB`, signal-to-distortion `64.0 dB`, 2026-09-05 |
| Gate E repeatability runs 2 and 3 live execution | PASS - both stayed green throughout with no warning, clipping, dropout, or other abnormality, 2026-09-05 |
| Three-run System Delay spread | PASS - `1.0 us`, versus preferred maximum `5 us` |
| Three-run magnitude/phase repeatability | PASS - common derived `2.0 ms` left / `1.0 ms` right direct window; `1-5 kHz` maximum magnitude spread `0.0743 dB`, maximum circular phase spread `1.931 degrees`; stored long-window failure retained as room-dominated evidence |
| Gate E overall | PASS - controlled installed-woofer FRD route qualified at the final settings and geometry, subject to the stated microphone-calibration, absolute-SPL, and window limitations |
| Assume UMC202HD contact/phantom findings apply to UMC22 | NO |
| Connect UMC22 to USB now | COMPLETE - known-good USB path and ECM8000 phantom are active with normal no-signal behaviour |
| Generate a signal now | NO FOR QUALIFICATION - the gate is complete; start another signal only as part of an identified woofer measurement under the common procedure |
| Carry the temporary Gate D loopback wiring into Gate E | NO - reconfigure only with the SU-V570 off and follow the full-dual connection map |
| Power the SU-V570 now | YES - retain the established state, but keep all signals stopped |
| Proceed to installed-driver FRD now | YES FOR THE INSTALLED WOOFER - retain the qualified route/settings and document the REW-native window for each reusable series; NO for the raw tweeter or polar series pending their separate protection/procedure |

The UMC202HD live-Linux diagnosis remains worthwhile but is no longer on the
critical path to the first installed-driver FRD set.
