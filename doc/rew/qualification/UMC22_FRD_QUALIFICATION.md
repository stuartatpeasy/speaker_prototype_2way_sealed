# UMC22 Installed-Woofer FRD Qualification

Lifecycle: **QUALIFICATION EVIDENCE**
Qualification date: 2026-09-05
Release: **PASS for controlled installed-woofer FRD**
Current procedure:
[`../procedures/UMC22_INSTALLED_WOOFER_FRD.md`](../procedures/UMC22_INSTALLED_WOOFER_FRD.md)
Detailed chronology:
[`../history/UMC22_FRD_QUALIFICATION_LOG_2026-09-05.md`](../history/UMC22_FRD_QUALIFICATION_LOG_2026-09-05.md)

## 1. Scope, Decision, And Limitations

This record owns the concise evidence supporting use of the UMC22 for
controlled full-dual acoustic measurement of the installed SB17 woofer. It
does not serve as an operating procedure and does not authorise a new signal.
The detailed file linked above retains every intermediate instruction, failed
route, correction, partial gate, and superseding conclusion.

**USER DECISION — 2026-09-05:** the user accepted a known but unquantified
possibility of damage to the approximately GBP 25 UMC22 during an amplifier
fault. Normal operation has ample nominal level margin, but a fault can exceed
the interface's published maximum input level. This risk acceptance does not
waive checks protecting the person, amplifier, PC, loudspeaker, or measurement
validity and cannot guarantee containment of a destructive input failure.

**FINAL RELEASE:** Gates A-E pass. Three final-setting sweeps completed without
warning, clipping, dropout, or other abnormality. System Delay spread was
`1.0 us`. Under one common derived direct-sound window, maximum `1-5 kHz`
magnitude spread was `0.0743 dB` and maximum circular-phase spread was
`1.931 degrees`.

The release is limited by:

- the supplied ECM8000 data being generic 0-degree response correction, not
  serial-number-specific and not absolute-sensitivity calibration;
- no absolute-SPL calibration;
- the qualification's `2.0 ms` left / `1.0 ms` right window being a derived
  analysis window, not a stored REW-native production window;
- a final production window still needing selection from each reusable
  capture's impulse/ETC; and
- no release for raw-tweeter or polar measurements.

## 2. Engineering Basis

The UMC22 specification identifies Input 2 as a `1 Mohm` instrument input with
a maximum input level of `+2 dBu`. Direct user-observed PCB inspection found
that each rear output socket has separate mechanical tip, ring, and sleeve
contacts, but ring and sleeve join the same copper fill. The outputs are
physically TRS and electrically two-node, TS-equivalent: tip is signal and
ring/sleeve are common. This established contact topology, not USB routing or
stream stability.

The fixture's pre-stress unloaded floating differential transfer was `0.09892`
(`-20.094 dB`); its post-stress prediction was approximately `0.09894`
(`-20.092 dB`). At the `1.00 V RMS` woofer level:

```text
Vreference = 1.00 V RMS x 0.09892 = 0.09892 V RMS
+2 dBu = 0.775 V RMS x 10^(2/20) = 0.976 V RMS
normal headroom = 20 log10(0.976 / 0.09892) = 19.9 dB
```

The normal reference therefore sits approximately `19.9 dB` below the
published maximum. In the bounded amplifier-fault case, approximately
`+/-45.5 V` rails can place approximately `4.50 V peak` (`3.18 V RMS`,
`+12.3 dBu`) on one fixture node, about `10.3 dB` above the published maximum.
The fixture clamp range of `5.5-6.2 V peak` is higher still. Published maximum
input level is not a destruction threshold, so survival or damage cannot be
inferred.

The `9.1 kohm` primary resistors nevertheless bound approximate current into a
node held near zero:

```text
Imaximum,approx = 45.5 V / 9.1 kohm = 5.0 mA per leg
```

That preserves current limiting and benign amplifier loading but does not make
the UMC22 input compliant under every fault.

## 3. Gates A-E Summary

| Gate | Purpose | Decisive evidence | Decision |
| --- | --- | --- | --- |
| A | Map unpowered `INST 2` contacts | Tip open to ring, sleeve, and USB shell; ring-sleeve `0.314 ohm`, ring-shell `0.050 ohm`, sleeve-shell `0.030 ohm` | **PASS** — single-ended ring/sleeve/shell common established |
| B | Check `INST 2` phantom isolation | Phantom-off maximum `0.0005 V DC`; phantom-on readings briefly about `0.0020 V DC` and all settled to `0.0000 V DC`; stop threshold `0.1 V DC` | **PASS** |
| C | Prove final active-path resistance and common return | B-left positive to tip `9125 ohm`; to ring, sleeve, and USB shell `10127 ohm`; B-left negative to AUX shell `0.137 ohm`, ring `0.311 ohm`, sleeve `0.290 ohm`, shell `0.299 ohm` | **PASS** — R1 remains in every positive path; intended common only |
| D | Qualify low-voltage hardware, routing, full-duplex stream, timing, and calibration treatment without amplifier | No-signal DC settled from `0.0015 V` to zero; exact exclusive `48 kHz` two-channel route; ordinary loopback timing stored numeric index/System Delay; soundcard calibration data generated from loopback; IR merge excluded | **PASS** |
| E | Qualify switched-off full-dual build, controlled powered level, active microphone calibration, headroom, and acoustic repeatability | Correct parallel wiring; clean no-signal power-up; `1.0000 V AC` woofer and `98.53 mV AC` reference; final gains/headroom pass; three clean runs; delay/magnitude/phase targets pass | **PASS** |

## 4. Gates A-C Electrical Evidence

### 4.1 Gate A — Unpowered Contact Map

Conditions: SU-V570 off and disconnected; UMC22 USB disconnected; phantom off;
all other UMC22 sockets empty; passed breakout in `INST 2`; U1282A auto-ranging
resistance with leads nulled. All readings were stable and polarity-insensitive.

| Measurement | Result |
| --- | ---: |
| Tip to ring | open |
| Tip to sleeve | open |
| Tip to USB Type-B shell | open |
| Ring to sleeve | `0.314 ohm` |
| Ring to USB Type-B shell | `0.050 ohm` |
| Sleeve to USB Type-B shell | `0.030 ohm` |

The sub-ohm values are topology evidence, not precision resistance results;
probe/contact and residual-zero uncertainty dominate. They unambiguously show
an isolated tip and mutually common ring, sleeve, and USB shell.

### 4.2 Gate B — Phantom Isolation

Conditions: UMC22 connected only to USB and the breakout in `INST 2`; amplifier,
fixture, microphone, and every other analogue cable disconnected. No
instability occurred.

| Red probe to black probe | Phantom off | Phantom on after settling |
| --- | ---: | ---: |
| Tip to sleeve | `0.0005 V DC` | `0.0000 V DC` |
| Ring to sleeve | `0.0000 V DC` | `0.0000 V DC` |
| Tip to ring | `0.0004 V DC` | `0.0000 V DC` |

On enabling phantom, each pair initially displayed approximately `0.0020 V DC`
and settled to zero in approximately `10 s`. The largest transient was 50 times
below the `0.1 V DC` stop threshold and was common to all probe placements.

### 4.3 Gate C — Final Ground-Path Audit

Conditions: complete selected playback and fixture paths assembled; UMC22
unpowered and USB-disconnected; phantom off; SU-V570 off; no loudspeaker; U1282A
auto-ranging resistance with nulled leads. Output 1 used the previously mapped
TS-to-RCA cable to `AUX` left.

| From B-left positive to | Result |
| --- | ---: |
| Breakout tip | `9125 ohm` |
| Breakout ring | `10127 ohm` |
| Breakout sleeve | `10127 ohm` |
| UMC22 USB shell | `10127 ohm` |

The return values exceed the active tip path by:

```text
10127 ohm - 9125 ohm = 1002 ohm
```

This is the measured R3 shunt; it proves there is no low-resistance bypass of
R1. From B-left negative, the amplifier-local AUX shell was `0.137 ohm`; the
complete paths were `0.311 ohm` to ring, `0.290 ohm` to sleeve, and `0.299 ohm`
to USB shell. Those stable sub-ohm paths are consistent with the intended
playback return plus plug, interface, breakout, and probe resistance.

## 5. Gate D — Stream, Routing, Timing, And Calibration

The amplifier-disconnected protected loopback connected UMC22 Output 1 through
the passed source adaptor, complete fixture, and breakout to `INST 2`. With
USB connected and all software audio stopped, tip-sleeve started at
`0.0015 V DC` and settled to `0.0000 V DC` after approximately `15 s`; no clip
or instability occurred.

REW enumerated Java exclusive UMC22 input/output at `48 kHz` with independent
L/R channels. A bounded `1 kHz` test produced `0.0207 V RMS`, moving slowly only
between `0.0205` and `0.0210 V RMS`, with no clipping, dropout, or abnormality.
Selecting the previously omitted `EXCL:` input endpoint restored linear
`GAIN 2` response: `Ref In` was `-20.88 dBFS` at an external `0.0218 V RMS`.
Input 1 responded normally to microphone gain and sound. A controlled
headphone-to-microphone setup reached `-19.5 dBFS` main and `-20.84 dBFS`
reference at `0.0230 V RMS`, without clipping or dropout.

The corrected channel matrix is:

| Role | Qualified selection |
| --- | --- |
| Measurement output | L |
| Timing-reference output | L |
| Measurement input | L |
| Reference input | R |

Earlier output-R timing and input-L self-reference routes failed and are
retained in history. In REW V5.40 beta 133, Java `Stereo only` and exact
exclusive endpoints were required for coherent two-channel operation. An exact
L/L/L/R `256k` sweep using ordinary loopback timing completed without warning,
clipping, dropout, or exception and stored timing-reference index `47970.52`,
System Delay `0.6141 ms`, and IR start `0.5208 ms`.

The final unchanged calibration-data check selected `Make calibration data
from loopback response` and stored `Soundcard: Loopback cal`, reference index
`47975.52`, and System Delay `0.5100 ms`, with no warning. `Merge loopback
response into IR` is excluded for this route because that treatment did not
produce valid timing metadata in the present beta-133 setup.

## 6. Gate E — Powered Full-Dual And Acoustic Evidence

The switched-off full-dual assembly passed: woofer and fixture were in parallel
at B-left with correct polarity, breakout restrained and insulated, and
headphones, Output 2, and AUX right empty. With UMC22 USB and phantom active,
neither channel clipped and there was no unexpected sound, instability,
heating, smell, or other abnormality. The subsequent SU-V570 minimum-volume
power-up remained silent and stable for approximately one minute with no hum,
buzz, heating, smell, or smoke.

At the SU-V570's `-38 dB` volume mark the U1282A read `1.0000 V AC` across the
woofer. The gross protected reference was a stable `98.53 mV AC`, giving:

```text
transfer = 0.09853 / 1.0000 = 0.09853
gain = 20 log10(0.09853) = -20.129 dB
```

This differs from the `0.09892` prediction by `-0.39%` (`-0.034 dB`). After the
breakout was removed and the fixture connected directly to `INST 2`, no
abnormality appeared. `Ref In` was stable at `-20.87 dBFS` (`+/-0.01 dB`) with
`GAIN 2` approximately 2 o'clock and woofer voltage `1.0003 V AC`.

The retained `calibration/ECM8000_calibration_data.csv` was made REW-compatible
by adding required whitespace after commas without changing numeric values. It
is generic 0-degree response data. Persistence against `Default Input` did not
apply it to the active measurement; the final association used the exact
exclusive `MICROPHONE (Master Volume), L` source. Measure named the CSV for L;
reference R remained uncalibrated. Measurement Info then confirmed the active
file.

Early acoustic attempts were diagnostic only: `-10 dBFS` caused a
distortion/headroom warning; a warning-free `-20 dBFS` sweep had only about
`3.8 dB` headroom and `Mic: No cal file`; the first calibrated `-20 dBFS`
checkout had main headroom `3.6 dB` while reference headroom passed at
`32.9 dB`. A targeted `6070 Hz` tone established the response maximum and
reducing `GAIN 1` to approximately 2 o'clock moved main peak from about
`-2 dBFS` to `-10.3 dBFS`. No equipment abnormality occurred.

The final calibrated checkout became repeatability run 1. All three final runs
used one `256k`, `20-20000 Hz`, `-20.0 dBFS` sweep at `48 kHz`, exact exclusive
UMC22 endpoints, output L, timing-reference output L/input R, microphone input
L, `Soundcard: Loopback cal`, ECM8000 CSV, IR start `3.0000 ms`, timing offset
`0.0000 ms`, and clock adjustment `0.0 ppm`.

| Run | Measurement | Timing index | System Delay / IR peak | SNR | Signal to distortion |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | `SB17 UMC22 calibrated headroom checkout 2` | `47849.96` | `3.1257 ms` | `43.5 dB` | `62.5 dB` |
| 2 | `SB17 UMC22 repeat 2` | `47849.92` | `3.1267 ms` | `44.3 dB` | `60.2 dB` |
| 3 | `SB17 UMC22 repeat 3` | `47849.93` | `3.1264 ms` | `44.3 dB` | `64.0 dB` |

Run 1's displayed main/reference levels were `-10.7`/`-33 dBFS`, giving
`10.7`/`33 dB` headroom. Runs 2 and 3 also stayed green. All three completed
without warning, clipping, dropout, or other abnormality. Their System Delays
differ from run 1 by `0`, `+1.0`, and `+0.7 us`; total spread is `1.0 us`,
comfortably within the preferred `5 us` limit.

## 7. Raw Evidence And Repeatability Analysis

The authoritative session is:

```text
path: rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat
size: 19138881 bytes
SHA-256: b47e6aca826a4a95d77dfcab731edac95c2c6bf21be56f8bf249fcf23bd5e3c1
```

It is unique raw evidence and must not be deleted or ignored. The REW API
client extracted all eight session measurements without manifest warnings,
with `None` smoothing and a common `0.3662109673 Hz`, 54,559-point grid.

**SUBSEQUENT FILE-IDENTITY NOTE — 2026-09-06:** the block above identifies the
qualified archive revision retained in Git commit `0fe0c90`. The working-tree
path was later re-saved at exit after a concurrent throwaway REW instance
caused the primary instance to lose its UMC22 handles. That expected user-
reported re-save is now `94,400,301` bytes with SHA-256
`4cf148afde88732ddbccbb366a53f7601faae6c887654dafcb8d5dd7f2edd2ab` and may
contain loaded duplicates. Preserve it, but use the committed revision for the
qualified archive identity and the later UUID-selected single-measurement
archives for current production evidence.

The first `1-5 kHz` comparison under stored long default Tukey `0.25` windows
(`311.9167 ms` left, `500 ms` right) failed: median/95th/maximum magnitude range
was `1.056`/`4.354`/`32.364 dB`, and circular-phase range was
`7.045`/`33.742`/`179.819 degrees`. The maximum occurred at a narrow
`1339.23 Hz` cancellation; IR peak-amplitude spread was only `0.037 dB`.
This result is retained as room-dominated evidence, not reclassified as an
interface-gain failure.

A superseding raw-IR extraction selected only the three final measurement
UUIDs, each with `131072` samples at `48 kHz`. A common window relative to each
direct peak used `2.0 ms` left and `1.0 ms` right, a raised-cosine taper over
the outer half of each side, and unity over the inner half. A full 131,072-point
FFT retained `0.3662109375 Hz` spacing and absolute time origins.

Over `1-5 kHz`, unsmoothed magnitude spread had median `0.0635 dB`, 95th
percentile `0.0736 dB`, and maximum `0.0743 dB` at `2191.41 Hz`. Circular-phase
spread had median `0.994 degrees`, 95th percentile `1.815 degrees`, and maximum
`1.931 degrees` at `4999.88 Hz`. At `2.3 kHz`, spreads were `0.0735 dB` and
`0.697 degrees`. These pass the approximately `0.2 dB` magnitude target and
nearly-coincident-phase requirement.

Window sensitivity remained similarly tight for right-window values from
`0.8` through `1.2 ms`; admitting later energy degraded the comparison, and a
`1.5 ms` right window exceeded the magnitude target. This supports changing
reflection energy after the direct arrival but does not identify a surface.
No raw measurement or REW window was modified by the derived analysis.
