# UMC22 Risk-Accepted FRD Fallback

Date prepared: 2026-09-05

Status: **ACCEPTED IN PRINCIPLE; UMC22-SPECIFIC CONNECTION AND PHANTOM GATES
REMAIN; POWERED-AMPLIFIER USE IS NOT YET APPROVED**

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

The fixture's resistance-derived, unloaded floating differential transfer is
`0.09892` (`-20.094 dB`; pre-stress values). The post-stress prediction differs
immaterially at approximately `0.09894` (`-20.092 dB`). At the established
`1.00 V RMS` woofer test level:

```text
Vreference = 1.00 V RMS x 0.09892 = 0.09892 V RMS

+2 dBu = 0.775 V RMS x 10^(2/20) = 0.976 V RMS

normal headroom = 20 log10(0.976 / 0.09892) = 19.9 dB
```

Normal operation therefore has ample nominal level margin if the UMC22 input
loads and senses the fixture as expected. Its `1 Mohm` impedance is negligible
beside each `1 kohm` fixture shunt, but the actual tip/ring/sleeve topology must
still be measured because an instrument input may be single-ended despite the
mechanical TRS socket.

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
| Tip to ring | pending |
| Tip to sleeve | pending |
| Ring to sleeve | pending |
| Tip to USB Type-B shell | pending |
| Ring to USB Type-B shell | pending |
| Sleeve to USB Type-B shell | pending |

Record a stable resistance, `open`, or a description of any settling or
polarity-sensitive reading. Gate A requires that tip is not hard-shorted to
ring, sleeve, or USB shell. Ring-to-sleeve and sleeve-to-shell results determine
the final adaptor/ground arrangement rather than passing or failing in
isolation. Do not connect USB or generate a signal before this map is reviewed.

### 3.2 Gate B - Input 2 Phantom Isolation

After Gate A defines the contacts, power the otherwise unloaded UMC22 by USB
and measure DC voltage at tip-sleeve, ring-sleeve, and tip-ring with phantom off
and then on. The microphone, amplifier, fixture, and every other analogue cable
remain disconnected. Stop if any pair exceeds `0.1 V DC`, is unstable, or
behaves materially differently when phantom is enabled. This is one direct
isolation check, not a repeat of the UMC202HD's exhaustive qualification.

### 3.3 Gate C - Final Unpowered Ground-Path Audit

With the UMC22 contact behaviour known, assemble the intended final cables with
the SU-V570 switched off. Confirm that amplifier positive cannot reach the
UMC22 active input contact without the intended `9.1 kohm` series resistance.
Map amplifier negative, ring, sleeve, USB shell, and the playback-cable ground;
record any deliberate ring-to-sleeve or system-ground commoning and confirm it
does not create an unexpected active-signal path. Stop for an unexplained low-
resistance amplifier-positive to interface-ground path.

### 3.4 Gate D - Low-Voltage UMC22 Full-Duplex Checkout

At `48 kHz`, prove the actual UMC22 output channel, Input 1 microphone channel,
Input 2 reference channel, REW timing-reference mode, gain range, and dropout-
free operation without the powered amplifier. A direct or fixture-mediated
low-voltage loopback must remain below the UMC22 input maximum. Recreate any
soundcard calibration for this interface and rate; do not reuse UMC202HD
calibration or level settings. The historical UMC22 evidence is dropout-free
ordinary playback. In addition, a current matched five-minute media control on
this desktop produced zero audible dropouts with Microsoft `USBAUDIO.sys`
(`10.0.26100.8972`). No UMC22 REW full-duplex sweep has yet passed.

### 3.5 Gate E - Controlled Powered Woofer Checkout

Only after Gates A-D pass, adapt the switched-off connection and minimum-volume
startup in [`FRD_MEASUREMENT_SETUP_TEST.md`](FRD_MEASUREMENT_SETUP_TEST.md) to
the documented UMC22 contacts. Use the woofer only. Confirm no-signal behaviour,
raise the woofer to `1.00 V RMS`, confirm a gross reference level near
`0.10 V RMS` without clipping, then complete three unmoved repeats. The final
reference level may differ slightly if the verified UMC22 input topology makes
the fixture operate single-ended; record and use the measured result.

## 4. Release Decision

| Decision | State |
| --- | --- |
| Reuse qualified fixture components | YES |
| Accept possible UMC22 input damage in an amplifier fault | YES - user risk acceptance, 2026-09-05 |
| Assume UMC202HD contact/phantom findings apply to UMC22 | NO |
| Connect UMC22 to USB or generate a signal now | NO - Gate A first |
| Connect or power the SU-V570 now | NO - Gates A-D first |
| Proceed to installed-driver FRD after all gates pass | YES |

The UMC202HD live-Linux diagnosis remains worthwhile but is no longer on the
critical path to the first installed-driver FRD set.
