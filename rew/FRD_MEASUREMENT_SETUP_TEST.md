# FRD Measurement Setup Repeatability Test - UMC202HD

Date prepared: 2026-08-30

Last revised: 2026-09-05

Status: **UMC202HD PROCEDURE SUSPENDED BY DESKTOP DROPOUT; FIXTURE RELEASE
REMAINS VALID; UMC22 GATES A-D, ITS COMPLETE SWITCHED-OFF GATE E ASSEMBLY, AND
ITS USB/PHANTOM AND SU-V570 MINIMUM-VOLUME NO-SIGNAL OBSERVATIONS PASS; THE
CONTROLLED UMC22 WOOFER LEVEL PASSES AT `1.0000 V AC` WITH SU-V570 VOLUME AT
ITS `-38 dB` SCALE MARK; THE GROSS PROTECTED REFERENCE PASSES AT A STABLE
`98.53 mV AC` WITH NO CLIPPING, DROPOUT, INSTABILITY, OR OTHER ABNORMALITY;
FINAL DIRECT-REFERENCE RECONNECTION AND NO-SIGNAL OBSERVATION PASS; REFERENCE-
INPUT GAIN SETTING PASSES AT `-20.87 dBFS`; THE GENERIC `0-DEGREE` ECM8000 CSV
IS REW-COMPATIBLE AND NOW PERSISTS AGAINST THE EXACT ACTIVE `MICROPHONE (MASTER
VOLUME), L` SOURCE; `-10 dBFS` CHECKOUT FAILED DISTORTION/HEADROOM; `-20 dBFS`
REPEAT PASSES ROUTING/TIMING ONLY; MEASURE'S CAL-FILE DISPLAY NOW CONFIRMS THE
ECM8000 CSV FOR THE PENDING INPUT-L MEASUREMENT; `GAIN 1` HAS BEEN REDUCED BY
APPROXIMATELY `3.8 dB` WITH THE REFERENCE STABLE AND NO ABNORMALITY; ONE
CALIBRATED `-20 dBFS` VERIFICATION SWEEP COMPLETED CLEANLY BUT FAILED INPUT
HEADROOM AT `3.6 dB`; REFERENCE HEADROOM PASSES AT `32.9 dB`; POST-MEASUREMENT
METADATA PASSES AND THE PEAK IS `6.07 kHz`; ONE SHORT TARGETED
GAIN-SETTING TONE PASSES AT `-10.3 dBFS` MAIN PEAK WITH `GAIN 1` AT 2 O'CLOCK;
THE FINAL CALIBRATED CHECKOUT PASSES WITH `10.7 dB` MAIN AND `33 dB` REFERENCE
HEADROOM; REPEATABILITY RUNS 2 AND 3 ALSO STAYED GREEN WITH NO WARNING OR
ABNORMALITY; THREE-RUN DELAY SPREAD IS `1.0 us`; RAW SESSION SAVED; THE LONG-
WINDOW ROOM RESPONSE IS INAPPLICABLE TO THE HARDWARE GATE, WHILE A COMMON
DERIVED `2.0 ms` LEFT / `1.0 ms` RIGHT DIRECT WINDOW PASSES `1-5 kHz` AT
`0.0743 dB` MAXIMUM MAGNITUDE AND `1.931 degrees` MAXIMUM PHASE SPREAD; UMC22
GATE E AND THE CONTROLLED INSTALLED-WOOFER FRD ROUTE PASS**

Every electrical release prerequisite has passed: SU-V570 common-ground
topology, UMC202HD Input 2 phantom isolation, complete-fixture
resistance/DC/physical qualification, the unpowered ground audit, and rear-
output topology. The inspected UMC202HD rear outputs are mechanically TRS but
electrically tip plus a ring/sleeve common. The fixture's short unscreened tail
was included in the powered no-signal pass.

The proportionate safety/connectivity review in
[REFERENCE_FIXTURE_AC_COMMISSIONING.md](REFERENCE_FIXTURE_AC_COMMISSIONING.md)
passes, and the fixture authority says `Approved for amplifier use: YES` for
controlled UMC202HD bench work. That electrical release remains valid, but
UMC202HD measurement use is suspended by the separate dropout. This is not a
raw-tweeter or final polar-measurement procedure.

This procedure's base settings and release statements are UMC202HD-specific.
The risk-accepted UMC22 alternative has now passed the separate gates in
[UMC22_RISK_ACCEPTED_FRD_FALLBACK.md](UMC22_RISK_ACCEPTED_FRD_FALLBACK.md);
its qualified `48 kHz` configuration, contact mapping, calibration, gains, and
measured reference level supersede the corresponding UMC202HD details below
whenever that fallback is used.
Direct PCB inspection has established that both UMC22 rear outputs are likewise
two-node unbalanced sources: tip is signal and ring/sleeve share one copper
return. Its unpowered `INST 2` contact map has also passed: tip is isolated and
ring/sleeve/USB shell are common. Its Gate B phantom isolation also passes:
all on/off readings remained at or below approximately `0.0020 V DC` and
settled to zero. Gate C also measures `9125 ohm` from speaker positive to input
tip and `10127 ohm` to ring, sleeve, and USB shell, proving there is no primary-
resistor bypass. Its stable `0.290-0.311 ohm` complete returns then establish
the intended common bond and close Gate C. The fallback procedure remains
authoritative for the interface-specific low-voltage and powered gates. Its amplifier-
disconnected Gate D no-signal path started at `0.0015 V DC`, settled to zero,
and showed no clipping or abnormality. REW then enumerated Java exclusive-mode
UMC22 input/output with independent L/R channels at `48 kHz` and calibration
`None`. Measurement output/input L, reference input R, loopback calibration/
timing, IR merge, and zero offset are confirmed. The original no-excitation
setup also selected reference output R; that is superseded below. Unity input
scaling, the UMC22-specific measurement
name, and the `20-20000 Hz` first-checkout range are also confirmed. The
amplifier-disconnected `1 kHz` level check then passed at `0.0207 V RMS`, with
only `0.0205-0.0210 V RMS` slow movement and no clipping, dropout, or
abnormality. Live REW capture was initially held at the next step: with that
external tone present, `Ref In` remained near `-93.72 dBFS` throughout the full
`GAIN 2` range. The current screenshot also shows a non-`EXCL:` input endpoint despite the earlier
reported exclusive selection. Selecting the `EXCL:` input variant immediately
resolved the problem: `Ref In` then followed `GAIN 2` linearly and is set to a
stable `-20.88 dBFS` with `0.0218 V RMS` measured externally. Input 1's
microphone channel then responded normally to ambient sound, nearby speech, and
its gain control without clipping. The room-noise indications are contextual,
not an intrinsic interface-noise measurement. The controlled headphone-to-
microphone setup then produced `-19.5 dBFS` main and `-20.84 dBFS` reference at
a stable external `0.0230 V RMS`, with no clipping, dropout, or abnormality.
The first amplifier-disconnected `1M` sweep then completed without warning,
error, clipping, audible discontinuity, or abnormality and shows one dominant
impulse arrival. Its timing index is nevertheless `N/A` and System Delay is not
available: reference output R was selected while the fixture actually sensed
measurement output L. A second sweep with both output selections L also ran
without clipping or dropout at a confirmed `0.0222 V AC`, but its Info panel
stored the timing-reference input as L instead of R. Its nearly flat magnitude
and phase are the invalid result of self-referencing measurement Input 1/L,
and its timing index remains `N/A`. At that checkpoint one further amplifier-
disconnected repeat was required with output and reference output L, measurement input L, and
loopback/reference input R. Changing the Measure-window reference input to R
then raised `Index 1 out of bounds for length 1` in REW V5.40 beta 133. After a
restart, the exact `EXCL:` endpoints, `48 kHz`, L/L/L/R routing, loopback mode,
merge, zero offset, and sweep fields all pass visual audit. The fallback record
authorises one retry after enabling Java `Stereo only` to force a two-channel
capture; recurrence of the exception stops testing for a debug-file bug report.
That retry completed without the exception and its Info panel stored timing-
reference output L and input R, but its timing index remains `N/A` and System
Delay remains unavailable. Its `0.5100 ms` peak and `0.4792 ms` IR start are
physically plausible for the nominal `150 mm` headphone check, but are not by
themselves sufficient timing proof. The proposed retained-capture inspection has
been withdrawn: current REW Scope is a live two-channel oscilloscope and cannot
display the preceding measurement's raw captures. The subsequent amplifier-
disconnected `256k` timing-only sweep passed with timing-reference index
`47970.52`, System Delay `0.6141 ms`, IR start `0.5208 ms`, and no warning,
clipping, dropout, or exception. Gates A-D therefore qualify the UMC22 to enter
Gate E's documented staged checkout. The IR-merge
treatment remains excluded, and reusable FRD is held until the
ECM8000 calibration is loaded and the UMC22/electrical-reference magnitude-
calibration route is valid. The final unchanged `256k` check now qualifies
`Make calibration data from loopback response`: REW stored `Soundcard: Loopback
cal`, reference index `47975.52`, System Delay `0.5100 ms`, and no warning or
abnormality. Use that treatment for UMC22 Gate E, keep IR merging excluded, and
load the ECM8000 calibration before reusable acoustic capture.
UMC22 Output 1 uses the same already-mapped TS-to-RCA cable to
SU-V570 `AUX` left, so the isolated cable map need not be repeated.

## 1. Purpose And Pass Criteria

Use three repeated, unmoved woofer measurements to establish whether the
UMC202HD, ECM8000, Technics SU-V570, amplifier-output reference fixture, REW,
and room setup provide repeatable magnitude, phase, and timing around the
intended crossover region.

Pass criteria over `1-5 kHz`:

- magnitude spread no greater than approximately `0.2 dB`;
- system-delay spread preferably no greater than `5 us`;
- phase traces nearly coincident, with no unexplained jumps or drift; and
- no clipping or reference dropout.

Passing this test permits the same chain to be used for the first installed-
driver FRD measurements. Tweeter protection and sweep limits remain a separate
prerequisite.

## 2. Measurement Topology

### 2.1 Full-Dual Arrangement

| UMC202HD channel | Assignment |
| --- | --- |
| Input 1 / USB input L | ECM8000 microphone |
| Input 2 / USB input R | Protected SU-V570 amplifier-output reference |
| Output 1 / USB output L | SU-V570 and woofer under test |
| Output 2 / USB output R | Physically unconnected |

Use REW's `Use loopback as cal and timing reference` mode with
`Merge loopback response into IR` enabled. Input 2 then references the acoustic response to the
voltage at the selected SU-V570 rear speaker terminals and supplies common
timing.

The current fixture reference plane is the amplifier output, not the driver
terminals. The true-RMS meter still establishes `1.00 V RMS` at the woofer.
Keep the loudspeaker cable unchanged throughout the driver set and record any
later change of reference plane.

### 2.2 Safe Semi-Dual Fallback

If the complete fixture is not approved, do not connect either amplifier
terminal to the UMC202HD. Instead use:

```text
UMC202HD Output 2 -> straight-through TRS patch cable -> UMC202HD Input 2, LINE
```

Select `Use loopback as timing reference`. This preserves common timing but
leaves DAC and amplifier response in the acoustic measurement. Do not mix
semi-dual and full-dual data in a final driver set without first demonstrating
equivalent results. The cable retains separate TRS contacts because Input 2
ring is distinct, even though this interface's Output 2 ring and sleeve are
internally common.

## 3. Prerequisites And Equipment

### 3.1 Mandatory Release Gates

Before making the full-dual connection, confirm:

1. the SU-V570 record passes the unpowered common-ground topology gate;
2. the UMC202HD Input 2 central-TRS phantom-isolation gate passes;
3. the proportionate AC sanity/release gate in
   [`REFERENCE_FIXTURE_AC_COMMISSIONING.md`](REFERENCE_FIXTURE_AC_COMMISSIONING.md)
   passes; and
4. the fixture record explicitly says `Approved for amplifier use: YES`.

The fixture file owns its schematic, component values, wiring, and release
state; the qualification archive owns completed test evidence. This acoustic
procedure does not repeat either.

### 3.2 Required Equipment

- Behringer ECM8000 and XLR microphone cable;
- Behringer UMC202HD and USB cable;
- an interface driver/host path that has first passed the separate stability
  diagnosis; the former Behringer Windows driver is uninstalled and is not a
  current prerequisite;
- measured cable from UMC202HD Output 1 to the selected SU-V570 line input;
- fully commissioned SU-V570-to-UMC202HD reference fixture;
- Technics SU-V570;
- unchanged speaker cable from the selected SU-V570 output to the woofer;
- true-RMS voltmeter suitable at `1 kHz`;
- microphone stand, tape or laser measure, and cabinet support; and
- PC running REW.

Do not use the UMC202HD headphone output to drive a loudspeaker.

## 4. Suspended UMC202HD Checkout Configuration

The settings below preserve the exact configuration used for the completed
2026-09-03 checkout. They are not a current instruction to reinstall the
Behringer driver or resume UMC202HD sweeps. Re-establish this path only after
the stability issue in
[UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md](UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md)
has been resolved and the selected driver/host combination has passed a
dropout-free control.

### 4.1 Interface Controls

1. Connect the UMC202HD directly to a reliable USB port and select its ASIO
   driver, not an old UMC22 endpoint or generic shared-mode device.
2. Select `24 bit`, `88.2 kHz` operation and confirm two independent inputs and
   outputs.
3. Prevent Windows and other applications from sending audio to the UMC202HD.
4. Clear any UMC22 or different-sample-rate soundcard calibration file.
5. Load the ECM8000 calibration file for the exact active device, input
   selector, and Input 1 channel. Confirm it in Measure's Cal files display and
   require the first Measurement Info panel to name it rather than `No cal
   file`; Preferences persistence against another selector is insufficient.
6. Set `DIRECT MONITOR` off, both pads off, both gains fully down, and `OUTPUT`
   fully down.
7. Set Input 2 to `LINE`. Its outer XLR contacts remain unused; the fixture uses
   only the central 1/4-inch TRS jack.
8. Connect the ECM8000 by XLR to Input 1 before enabling `+48 V`.

The `88.2 kHz` rate permits a nearly full-band `5 Hz-41 kHz` reference sweep.
It does not improve the low-frequency resolution of the short reflection-free
window.

### 4.2 Historical REW Checkout Settings

| Setting | Value |
| --- | --- |
| Driver | Behringer UMC ASIO driver |
| Converter/sample handling | UMC202HD `24 bit`; `Treat 32-bit data as 24-bit` enabled if the ASIO driver presents a 32-bit container |
| Sample rate | `88.2 kHz` |
| Measurement input | Input L / UMC202HD Input 1 |
| Measurement output | Output L / UMC202HD Output 1 |
| Loopback input | Input R / UMC202HD Input 2 |
| Timing-reference output | **SUPERSEDED:** Output R / UMC202HD Output 2 was the historical no-excitation selection; for the amplifier-output reference use Output L / Output 1 |
| Timing mode | Use loopback as cal and timing reference |
| Merge loopback response into IR | Enabled |
| Separate soundcard calibration file | None |
| Timing offset | `0.000 ms` for the first checkout; after validating the first impulse, apply one verified offset consistently to the repeat series (nominal time of flight `2.915 ms` for `1000 mm` at `343 m/s`) |
| Sweep range | `5 Hz-41 kHz` |
| Initial sweep level | `-20 dBFS` |
| Final level after voltage setting | `-10 dBFS` |
| Sweep length | `1M` |
| Repetitions | `1` |
| Abort if heavy input clipping occurs | Enabled |

In REW V5.40 Beta 133, the physical input/output routing is on
`Preferences -> Soundcard`, while the timing-reference mode and loopback-
response treatment are selected on the main `Measure` panel. Choose
`Use loopback as cal and timing reference`; then choose
`Merge loopback response into IR` rather than making calibration data from the
loopback response. The `Preferences -> Analysis` tab contains related
post-processing choices such as `Adjust clock with loopback`, but does not
enable the loopback measurement mode in this beta.

**VERIFIED REW ROUTING - 2026-09-03:** the user's Soundcard screenshot shows
the UMC ASIO driver at `88.2 kHz`, measurement Output `1: Out 1`, measurement
Input `1: In 1`, timing-reference output `2: Out 2`, loopback input `2: In 2`,
`Treat 32-bit data as 24-bit` enabled, and soundcard calibration `None`. The
displayed sweep level was `-12.0 dBFS`; because the amplifier remained off and
no signal was requested, this is only a dormant setting and must be changed to
the documented initial level before excitation.

**CORRECTED UI LOCATION - 2026-09-03:** a subsequent screenshot of the complete
Analysis tab confirmed that neither timing-reference mode nor loopback-response
merge selection is present there in V5.40 Beta 133. The earlier instruction to
find them under Analysis is superseded by the Measure-panel route above. No
signal was generated while locating the controls.

**VERIFIED MEASURE-PANEL STATE - 2026-09-03:** the Measure dialog exposes two
dropdowns beside `Timing`; they initially showed `No timing reference` and
`Set t=0 at IR peak`. The same screenshot confirms SPL/sweep mode, `1M`, one
repetition, `-20 dBFS`, `88.2 kHz`, single measurement, Output `1: Out 1`,
Input `In 1`, noise-floor capture enabled, and clipping abort enabled. The
displayed `0-24 kHz` range and inherited run-in measurement name are dormant
old values and are not approved as the full-dual measurement settings. No
signal was generated.

**VERIFIED LOOPBACK SELECTION - 2026-09-03:** the Measure panel subsequently
showed `Use loopback as cal and timing reference`, `Merge loopback response into
IR`, timing offset `0.0000 ms`, Ref output `2: Out 2`, and Ref input `2: In 2`.
The secondary output remained disabled. This records the historical UI state;
the reference-output assignment is not valid for the amplifier-output-reference
topology and is superseded below.
The first checkout deliberately retains zero timing offset; establish and
inspect one valid impulse before applying a common propagation-time correction
to the repeat series. The inherited name and `0-24 kHz` range remain to be
replaced before measurement. No signal was generated at this checkpoint.

**CORRECTED TIMING-REFERENCE OUTPUT - 2026-09-05:** the later UMC22 full-duplex
sweep proved that selecting reference output R while leaving physical Output 2
empty yields timing index `N/A` and no System Delay, even though the main sweep
and reference-response capture complete. For this amplifier-output-reference
topology the fixture senses Output 1/L, so both measurement output and timing-
reference output must be L; loopback/reference input remains R. This correction
also applies if the otherwise-dormant UMC202HD full-dual procedure is resumed.

**VERIFIED DORMANT MEASUREMENT SETTINGS - 2026-09-03:** before any amplifier
power or signal generation, the user confirmed the inherited fields were
replaced with name `SB17 UMC202HD checkout 1`, range `5-41000 Hz`, level
`-20 dBFS`, and timing offset `0.0000 ms`. All previously verified loopback,
channel, sample-rate, sweep-length, repetition, noise-floor, and clipping-abort
settings remained in place.

REW sends the sweep to both selected outputs when loopback reference is used.
Output 2 remains physically unconnected in the full-dual arrangement; Input 2
receives the amplifier-output reference instead. After the first impulse is
validated, one common timing offset removes the chosen reference-plane
propagation time while retaining relative driver delay. Do not independently
align woofer and tweeter impulse peaks later.

## 5. Physical Setup And Cabling

### 5.1 Geometry

Nominal geometry:

- microphone capsule to baffle-plane reference point: `1000 mm`;
- preferred microphone and woofer-centre height: `1040 mm`;
- room height: `2080 mm`;
- cabinet reference point to wall behind cabinet: `670 mm`;
- microphone to wall behind microphone: `970 mm`; and
- source/microphone line to nearest side wall: `1530 mm`.

At `1040 mm` height, the first calculated floor and ceiling reflections arrive
at approximately `3.81 ms`; the wall behind the cabinet follows at about
`3.91 ms`. Begin with a `3.5-3.7 ms` right window, then place it from the
measured ETC. At `950 mm` height, begin around `3.0-3.2 ms` because the
calculated floor reflection is approximately `3.34 ms`.

### 5.2 Safe Initial State

1. Switch the SU-V570 off and turn its volume fully down.
2. Set UMC202HD `OUTPUT`, `GAIN 1`, and `GAIN 2` fully down.
3. Set both interface inputs to `LINE`, both pads off, and `DIRECT MONITOR` off.
   Input 1's selector does not affect its XLR microphone connection.
4. Leave phantom power off while connecting the microphone.
5. Connect only the woofer; leave the tweeter electrically disconnected.
6. Select one SU-V570 speaker bank only.
7. For the documented `AUX` route, keep `POWER AMP DIRECT` off so the normal
   input selector remains active; select tone `DEFEAT` and switch loudness off.
   Use the separate Power Amp Direct input only under an explicitly revised
   connection and level-setting procedure.
8. Reconfirm the fixture release gate before connecting it.

**VERIFIED SETUP STATE - 2026-09-03:** the user confirmed the generator
stopped; UMC202HD `OUTPUT`, `GAIN 1`, and `GAIN 2` fully down; phantom off; USB
disconnected; SU-V570 off with volume fully down; Output 2 source adaptor
removed; and the passed breakout cable retained between the clamp/attenuator
output and Input 2. No powered-amplifier connection had yet been made at this
checkpoint.

**VERIFIED UNPOWERED CONNECTION STATE - 2026-09-03:** UMC202HD Output 1 is
connected to the SU-V570 `AUX` left line input. The woofer and
clamp/attenuator are connected in parallel to speaker-bank `B` left, with
`In+`/red on positive and `In-`/black on negative. The user reported all
connections secure. The SU-V570 remained off; no powered result is inferred.
The input was initially reported as `TAPE 1`, then corrected by the user before
measurement: `AUX` was the intentional physical connection and will remain in
use. The current setup fact is therefore `AUX`, not `TAPE 1`.

**VERIFIED INTERFACE POWER-UP STATE - 2026-09-03:** with the SU-V570 still off,
the ECM8000 was connected to Input 1 before USB power and `+48 V` were enabled.
The phantom indicator illuminated, neither clip LED illuminated, Output 2
remained physically empty, and Input 2 remained `LINE`, pad off, gain fully
down. `DIRECT MONITOR` remained off; both gain controls and `OUTPUT` remained
fully down as specified.

### 5.3 Full-Dual Connections

Make every amplifier, loudspeaker, fixture, and TRS connection with the
SU-V570 off:

1. Connect UMC202HD Output 1 to the selected SU-V570 line input.
2. Connect the matching SU-V570 speaker-output pair to the woofer.
3. At those same rear amplifier terminals, connect clamp/attenuator `In+` (red)
   to positive and `In-` (black) to negative. Do not use another channel or
   speaker bank.
4. For the first checkout, retain the passed breakout cable between the
   clamp/attenuator TRS output plug and UMC202HD Input 2 so its T/R nodes remain
   accessible for the gross reference-level check. Restrain and insulate the
   terminal block.
5. Connect the ECM8000 to Input 1 by XLR.
6. Leave UMC202HD Output 2 physically unconnected.
7. Connect USB, enable `+48 V`, and reconfirm Input 2 `LINE` and Direct Monitor
   off.

```text
ECM8000 -> UMC202HD Input 1 / USB input L -> REW measurement input

REW output L -> UMC202HD Output 1 -> SU-V570 -> speaker cable -> woofer

SU-V570 rear speaker terminals -> commissioned reference fixture
                                -> passed breakout cable (first check only)
                                -> UMC202HD Input 2 / USB input R
                                -> REW calibration and timing reference
```

### 5.4 Microphone And Cabinet Placement

1. Put the microphone capsule `1000 mm` from the baffle-plane reference point.
2. If practical, place the capsule and woofer centre `1040 mm` above the floor.
   Raise the cabinet rather than changing microphone position between drivers.
3. Orient the microphone as required by its calibration file; record if no
   calibration file is available.
4. Keep woofer centre, microphone capsule, and baffle reference point on one
   line for the zero-degree measurement.
5. Do not move the cabinet, microphone, stands, cables, fixture, or nearby
   objects between repeats.

**VERIFIED REPORTED INITIAL GEOMETRY - 2026-09-05:** the microphone tip is
`1000 mm` from the baffle plane. Its body is perpendicular to that plane and
aimed at the cabinet, so the incidence matches the available generic
`0-degree` calibration. The capsule is level with the centre of the woofer
dome and horizontally centred on the baffle. The loudspeaker stands on a jig
secured to a sturdy table; the jig rotates it about the horizontal centre of
the baffle plane and is marked in 10-degree increments. Retain the microphone
position and rotate only the loudspeaker for the later horizontal series.

## 6. Establish Levels

### 6.1 Set `1.00 V RMS` At The Woofer

1. Leave the SU-V570 volume fully down.
2. With the amplifier off, set UMC202HD `OUTPUT` fully clockwise for a
   repeatable, low-noise source setting.
3. In REW Generator select a `1 kHz` sine, Output L, at `-10 dBFS`.
4. Place the true-RMS meter directly across the woofer terminals.
5. With the generator stopped, switch on the SU-V570 and select the intended
   input and speaker bank. Check for sustained audible hum/buzz and for an Input
   2 clip indication. If REW provides an active no-signal RTA/FFT view, retain
   it for comparison; an inactive Preferences bargraph is not a failure and
   does not justify separate UI troubleshooting. Stop and investigate any
   audible problem, clipping, or clearly active instability that materially
   reduces reference-channel margin.
6. Start the generator and raise SU-V570 volume slowly until the meter reads
   `1.00 V RMS`, then stop the generator immediately.
7. Stop the generator before moving the meter. Move it to breakout T/R, restart
   the same tone without changing any level control, and confirm the reference
   is broadly `0.10 V RMS` (approximately `99 mV` predicted). This is a gross
   range check, not a tenth-of-a-decibel calibration. Stop for a reading outside
   `80-120 mV RMS`, clipping, or an observable reference dropout. Stop the tone
   and return the meter to the woofer before any further level change.
8. Mark the SU-V570 volume position with removable tape. Do not move it or the
   UMC202HD Output control during the series.
9. With the generator stopped, switch the SU-V570 off. Remove the breakout
   cable and connect the clamp/attenuator output plug directly to Input 2 for
   the repeatability measurements.
10. Switch the SU-V570 on again with the generator still stopped and repeat the
    Input 2 no-signal observation. Proceed only if the direct final connection
    has useful margin and no clipping, dropout, or material noise problem.

The fixture reference does not replace the true-RMS meter for absolute driver
voltage. REW removes the fixture's constant gain from relative response, but
the acoustic excitation still requires an independent voltage setting.

**VERIFIED UMC202HD CHECKOUT RESULT - 2026-09-03:** the powered no-signal
observation passed: the woofer was silent, no clip indicator illuminated, and
switching the SU-V570 on/off produced no observed instability. The level-setting
check then reached a clean `1.00 V RMS` across the woofer, but the source stream
muted for roughly `100-300 ms` every `1-3 s`. This blocks UMC202HD sweeps but
does not revoke the passive fixture's electrical release.

The subsequent diagnosis is maintained in
[UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md](UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md).
In summary, the same fault occurred with REW ASIO, REW Java/WASAPI, and ordinary
Windows music; it survived rate, buffer, USB-port, cable, peripheral, disk, and
power-plan controls. The same UMC202HD played continuously on a Windows 11
laptop. Microsoft's desktop UAC2 driver reduced but did not eliminate the
fault. A live-Linux boot on the desktop is the next useful discriminator.

Do not reinstall the Behringer driver or resume UMC202HD sweeps merely to follow
the dormant settings below. The risk-accepted UMC22 path is now the acoustic-
work critical path; its Input 2 contact map passes and Gate B phantom isolation
also passes. Both stages of Gate C pass; the amplifier-disconnected low-voltage
loopback's no-signal check and device enumeration also pass. Channel/timing
assignment and pre-excitation settings pass as well; the bounded amplifier-
disconnected `1 kHz` voltage level also passes. The Input 2 reference-channel
gain setting now passes after selecting the exclusive input endpoint, and the
separate Input 1 microphone-channel check passes. Controlled headphone-to-
microphone full-duplex level setup also passes. Earlier `1M` sweeps provide
dropout-free execution evidence but not valid timing. The final `256k`, exact-
routing, timing-only diagnostic passes with a numeric reference index and
`0.6141 ms` System Delay. Gate D is complete; Gate E may proceed only in its
documented sequence. The final low-voltage calibration-
data diagnostic also passes; establish and review Gate E's complete switched-off
wiring before applying amplifier power, as detailed in
[UMC22_RISK_ACCEPTED_FRD_FALLBACK.md](UMC22_RISK_ACCEPTED_FRD_FALLBACK.md).
The complete switched-off assembly now passes: woofer and fixture are in
parallel at B-left with correct polarity; the breakout is insulated; and the
headphone, Output 2, and AUX-right sockets are unused. The following UMC22-only
USB/phantom no-signal observation also passes: phantom indication was normal,
neither channel clipped, and there was no unexpected sound, instability,
heating, smell, or other abnormality. The subsequent minimum-volume SU-V570
no-signal power-up also passes after approximately one minute: the woofer
remained silent, neither UMC22 channel clipped, and there was no transient or
persistent hum/buzz, instability, heating, smell, smoke, or other abnormality.
The controlled `1.00 V RMS` woofer and gross `0.080-0.120 V RMS` reference-
level check then began under the UMC22 fallback record. The woofer target now
passes with `1.0000 V AC` indicated on the Agilent U1282A at the SU-V570's
`-38 dB` volume-scale mark; Generator was then stopped and the system was
silent. With both controls unchanged, the gross protected-reference voltage
also passes at a stable `98.53 mV AC`. That is a transfer of `0.09853`
(`-20.129 dB`), only `-0.39%` (`-0.034 dB`) from prediction. Generator was
stopped, neither channel clipped, and there was no dropout, instability, or
other abnormality. The breakout has now been removed, the fixture is connected
directly to `INST 2`, the U1282A is back across the woofer, and the powered
final connection shows no abnormality. Reference-input gain also passes at a
stable `-20.87 dBFS` (`+/-0.01 dB`) with `GAIN 2` approximately 2 o'clock,
U1282A woofer voltage `1.0003 V AC`, at least `6 dB` peak headroom, and no
clipping, dropout, or anomaly. The supplied
`../calibration/ECM8000_calibration_data.csv` has now been identified as a
generic `0-degree` response. Spaces were added after its commas to meet REW's
documented grammar without changing numeric values. It is not specific to this
microphone and contains no sensitivity calibration. A pre-consolidation copy
loaded without warning and persisted only on microphone input L while input R
showed `None`. At the user's request that redundant copy was removed. The
retained CSV has now also been selected and persists under its new filename on
the left channel only of the exact `EXCL:` UMC22 input; the right channel
remains `None`. Microphone-gain Check Levels was clean: main `In` was near
`-15.5 dBFS`, `Ref In` near `-33.8 dBFS`, both moving less than approximately
`+/-1 dB`, with `GAIN 1` near 4 o'clock and no clipping, dropout, or anomaly.
The subsequent sweep narrowed that apparent gain and calibration pass. At
`-10 dBFS` REW raised distortion/headroom warnings. A user-initiated
`-20 dBFS` repeat removed the warning but still approached about `3.8 dB`
headroom. Measurement Info recorded valid loopback calibration and timing but
`Mic: No cal file`; the CSV had persisted against `Default Input`, not the
active `MICROPHONE (Master Volume), L` source. At that checkpoint no acoustic
magnitude or phase was reusable; the corrected association, gain, final sweep,
and repeatability result are recorded in the superseding sections below.

### 6.2 Set Input Gains

1. Open REW's measurement dialog and run `Check Levels`.
2. Raise `GAIN 1` only enough for a clean microphone signal, initially aiming
   for approximately `-12` to `-18 dBFS` peaks.
3. Raise `GAIN 2` from minimum until the reference is reliable with at least
   `6 dB` headroom. Engage its pad only if minimum gain is still excessive.
4. Confirm both front-panel clip LEDs remain off and neither REW input clips.
5. Do not alter either gain after this point.

**VERIFIED UMC22 MICROPHONE-GAIN RESULT - 2026-09-05:** at the established
`-10 dBFS` level, Check Levels showed main `In` approximately `-15.5 dBFS` and
`Ref In` approximately `-33.8 dBFS`, each varying by less than about
`+/-1 dB`. `GAIN 1` was approximately 4 o'clock. Neither channel clipped, and
there was no dropout or other anomaly. Retain both input gains. The lower
pink-noise reference indication does not supersede the direct `1 kHz`
reference-gain result; the first sweep must nevertheless confirm adequate
reference headroom and valid timing before repeats.

**SUPERSEDING UMC22 SWEEP-HEADROOM/CALIBRATION RESULT - 2026-09-05:** the
`-10 dBFS` first acoustic attempt raised distortion and inadequate-headroom
warnings. Repeating at `-20 dBFS` suppressed the warning, but minimum displayed
headroom still approached approximately `3.8 dB`. No hardware clip, dropout,
or other abnormality occurred. The repeat stored reference index `47850.03`,
System Delay and IR peak `3.1243 ms`, IR start `3.0000 ms`, SNR `43.8 dB`,
correct L/L/L/R routing, and `Soundcard: Loopback cal`; its impulse has one
dominant arrival and its response is grossly woofer-like. It is not reusable
magnitude/phase evidence because Measurement Info states `Mic: No cal file`.
Preferences had attached the CSV to `Default Input, L`, while the active source
was `MICROPHONE (Master Volume), L`. Hold further sweeps until the Measure
dialogue's `Cal files` display confirms that calibration is applied to the
pending measurement and the microphone gain is corrected.

**VERIFIED CORRECTED ACTIVE-SOURCE ASSOCIATION - 2026-09-05:** with all signals
stopped, Soundcard showed exact input device
`EXCL: Behringer UMC22 (USB Audio CODEC)`, selector
`MICROPHONE (Master Volume)`, and channel L. The ECM8000 CSV was assigned to
that specific input on L only and persisted across Preferences close/reopen.
Measure's `Calibration data` display then showed
`ECM8000_calibration_data.csv` under Mic calibration files for L while the
pending measurement explicitly used `MICROPHONE (Master Volume) L`; its timing
reference remained `MICROPHONE (Master Volume) R`. REW did not display a
separate microphone-calibration row for that timing-reference channel in this
view. The soundcard-calibration row remains `None` before measurement because
the selected route creates calibration data dynamically from the loopback
response. This passes the pre-measurement microphone-calibration application
check.

**NEXT UMC22 MICROPHONE-GAIN CORRECTION:** retain `-20 dBFS`, all output-level
settings, `GAIN 2`, wiring, and geometry. Run `Check Levels`, note the stable
main-input level, and reduce only `GAIN 1` until the main indication is about
`4 dB` below that starting value. Stop Check Levels and report the before/after
main and reference indications, approximate final `GAIN 1` position, and any
warning or abnormality. This relative adjustment should increase the observed
minimum sweep headroom from about `3.8 dB` to about `7.8 dB`; the following
single `-20 dBFS` sweep must verify the actual margin.

**VERIFIED UMC22 MICROPHONE-GAIN ADJUSTMENT - PASS (2026-09-05):**
at `-20 dBFS` Check Levels, reducing only `GAIN 1` moved main `In` from
approximately `-15.5 dBFS` to approximately `-19.3 dBFS`, an achieved
`3.8 dB` reduction. The control moved only a few degrees and remains reasonably
described as approximately 4 o'clock; the input readings are authoritative.
Applied to the previous approximately `3.8 dB` minimum sweep margin, the change
predicts approximately `7.6 dB` headroom. `Ref In` remained stable at
`-33.58 dBFS` with `+/-0.01 dB` fluctuation, and there was no warning, clipping,
dropout, or other abnormality. Retain the new position. One calibrated
`20-20000 Hz`, `-20 dBFS`, `256k`, single sweep is approved under the fallback
record solely to verify at least `6 dB` actual headroom and the Measurement Info
mic-calibration entry; do not repeat or change controls before review.

**VERIFIED UMC22 CALIBRATED HEADROOM CHECKOUT - PARTIAL PASS / HEADROOM FAIL
(2026-09-05):** the calibration file was confirmed in place and exactly one
authorised sweep ran without warning or anomaly. Its Measure display recorded
main-input headroom `3.6 dB` in red and reference headroom `32.9 dB` in green.
The electrical reference is not limiting, but the main input still fails the
`6 dB` target. This direct result supersedes the predicted `7.6 dB` margin: the
broadband Check Levels change did not predict the narrow sweep maximum. Keep
signals stopped and controls unchanged pending the completed measurement's Info
panel and identification of the main-response peak frequency; another sweep is
not yet approved.

**VERIFIED UMC22 CHECKOUT METADATA AND PEAK - PASS FOR DIAGNOSIS
(2026-09-05):** Measurement Info stores `Mic: ECM8000_calibration_data.csv`,
`Soundcard: Loopback cal`, exact microphone input L, timing-reference output L
and input R, timing-reference index `47849.89`, System Delay and IR peak
`3.1273 ms`, IR start `3.0000 ms`, clock adjustment `0.0 ppm`, SNR `44.4 dB`,
and signal-to-distortion `34.3 dB`. The highest response peak is `6.07 kHz`.
Calibration, routing, and timing therefore pass for this diagnostic, but the
headroom failure prevents retaining it as FRD evidence.

The fallback record now authorises one short `6070 Hz`, `-20 dBFS` output-L
sine while observing the Levels tool. Reduce only `GAIN 1` until main-input
peak is approximately `-9` to `-10 dBFS`, then stop and report before any
further sweep. Retain every other setting and connection.

**VERIFIED UMC22 TARGETED GAIN SETTING - PASS (2026-09-05):** at `6.07 kHz`
and `-20 dBFS`, main-input peak moved from approximately `-2` to
`-10.3 dBFS` when only `GAIN 1` was reduced to approximately 2 o'clock. This is
an `8.3 dB` reduction and directly establishes `10.3 dB` main-input headroom at
the measured worst-case frequency. No equipment or signal abnormality occurred.
The preceding full sweep already established `32.9 dB` reference headroom and
`GAIN 2` has not moved. Retain all controls. The fallback record authorises one
final calibrated `20-20000 Hz`, `-20 dBFS`, `256k` sweep named
`SB17 UMC22 calibrated headroom checkout 2`; do not repeat before review.

**VERIFIED UMC22 FINAL CALIBRATED CHECKOUT - PASS / REPEATABILITY RUN 1
(2026-09-05):** highest displayed levels were main `-10.7 dBFS` and reference
`-33 dBFS`, providing `10.7 dB` and `33 dB` headroom; both remained green and
there was no warning or abnormality. Measurement Info stores the ECM8000 CSV,
loopback calibration, exact L/L/R route, timing-reference index `47849.96`,
System Delay and IR peak `3.1257 ms`, IR start `3.0000 ms`, SNR `43.5 dB`,
signal-to-distortion `62.5 dB`, and clock adjustment `0.0 ppm`. This passes the
final checkout and is accepted as repeatability run 1. The fallback record
authorises only two unchanged sweeps for runs 2 and 3 before review.

Absolute SPL calibration is unnecessary for this repeatability test. When the
SL-200 is available, calibrate REW with the meter on C weighting and SLOW
without subsequently changing Gain 1.

## 7. Capture And Window Three Repeats

### 7.1 Capture

**Current UMC22 override:** count `SB17 UMC22 calibrated headroom checkout 2`
as run 1; it already uses every final setting. Without changing any control,
wiring, or position, capture only `SB17 UMC22 repeat 2` and
`SB17 UMC22 repeat 3` with the same `20-20000 Hz`, `-20 dBFS`, `256k`, one-
repetition configuration and UMC22 calibration/routing settings. Record both
headroom values and System Delay for each. Do not apply windows until all three
captures have been reviewed. After run 3, save the session as the distinct raw
file `rew/SB17NRX2C35-8_UMC22_full_dual_repeatability.mdat`; do not overwrite or
delete the existing UMC22 diagnostic `.mdat`.

**VERIFIED UMC22 CAPTURE RESULT (2026-09-05):** runs 1/2/3 store System Delays
`3.1257`/`3.1267`/`3.1264 ms`, so their differences from run 1 are
`0`/`+1.0`/`+0.7 us` and total spread is `1.0 us`. This passes the preferred
`5 us` limit. All three store the mic CSV, loopback calibration, exact route,
numeric timing, `3.0000 ms` IR start, and `0.0 ppm` clock adjustment. Their SNR
values are `43.5`/`44.3`/`44.3 dB` and signal-to-distortion values are
`62.5`/`60.2`/`64.0 dB`. Runs 2 and 3 also stayed green throughout, with no
warning, clipping, dropout, or other abnormality. The distinct raw session is
saved at the stated UMC22 path, size `19138881` bytes, SHA-256
`b47e6aca826a4a95d77dfcab731edac95c2c6bf21be56f8bf249fcf23bd5e3c1`.

**DERIVED UMC22 NATIVE-GRID COMPARISON (2026-09-05):** REW API extraction
passes with no manifest warnings, `None` smoothing, and `54559` samples on the
same `0.3662109673 Hz` grid. Over `1-5 kHz`, the unwindowed/default-window
magnitude range has median `1.056 dB`, 95th percentile `4.354 dB`, and maximum
`32.364 dB`; circular phase range has median `7.045 degrees`, 95th percentile
`33.742 degrees`, and maximum `179.819 degrees`. This does not pass, but the
stored Tukey `0.25` windows are still `311.9167 ms` left and `500 ms` right.
The maximum is a narrow `1339.23 Hz` cancellation, not a broadband level shift;
the IR peak-amplitude spread is only `0.037 dB`. This is an inapplicable room-
dominated comparison, not a fixture failure. At that checkpoint the three raw
IRs had to be extracted and compared under one common reflection-excluding
window without another signal; the superseding result follows.

**SUPERSEDING DERIVED UMC22 DIRECT-WINDOW COMPARISON - PASS (2026-09-05):**
the API client selected only the three final-setting measurements and exported
each raw `131072`-sample, `48 kHz` impulse without warning. A common analysis
window was applied relative to each direct peak: `2.0 ms` left, `1.0 ms` right,
with a raised-cosine taper over the outer half of each side and unity over the
inner half. A full-length FFT preserved `0.3662109375 Hz` bin spacing and each
CSV's absolute time origin, hence preserving the measured delay differences.
Over `1-5 kHz`, unsmoothed magnitude spread has median `0.0635 dB`, 95th
percentile `0.0736 dB`, and maximum `0.0743 dB`; circular phase spread has
median `0.994 degrees`, 95th percentile `1.815 degrees`, and maximum
`1.931 degrees`. At `2.3 kHz`, the spreads are `0.0735 dB` and
`0.697 degrees`. Together with the `1.0 us` delay spread and clean live runs,
this passes UMC22 repeatability.

The conservative `3.0 ms` total span has approximately `333 Hz` nominal
resolution. It is sufficient for this `1-5 kHz` qualification and the intended
`2.2-2.4 kHz` crossover region, but it is a derived analysis window rather than
a stored REW or final production-FRD window. No raw measurement was modified.
Select and record the appropriate REW-native window from the actual impulse/ETC
when producing reusable woofer FRD.

| UMC22 run | Measurement name | System Delay (ms) | Difference from run 1 (us) |
| --- | --- | ---: | ---: |
| 1 | `SB17 UMC22 calibrated headroom checkout 2` | `3.1257` | `0` |
| 2 | `SB17 UMC22 repeat 2` | `3.1267` | `+1.0` |
| 3 | `SB17 UMC22 repeat 3` | `3.1264` | `+0.7` |

1. Name the measurements `SB17 UMC202HD repeat 1`, `repeat 2`, and `repeat 3`.
2. Run one sweep for each and record REW's System Delay.
3. Touch or move nothing between sweeps.
4. Save all three together as:

   `rew/SB17NRX2C35-8_UMC202HD_full_dual_repeatability.mdat`

### 7.2 Common IR Window

1. Inspect the first measurement's Impulse and ETC views and locate the actual
   first reflection.
2. Begin with a `2.0 ms` left window and Tukey `0.5`.
3. End the right window immediately before the first reflection, initially
   `3.5-3.7 ms` at `1040 mm` height or `3.0-3.2 ms` at `950 mm`.
4. Apply exactly the same window to all three measurements and save again.

## 8. Evaluate Repeatability

1. Overlay magnitude over `1-5 kHz` with identical smoothing; `1/24` octave or
   none is suitable.
2. Overlay phase and confirm that the traces nearly coincide.
3. Calculate delay spread as maximum System Delay minus minimum.
4. Record the greatest magnitude separation over `1-5 kHz`.

At `2.3 kHz`, `5 us` corresponds to:

```text
phase = 360 degrees x 2300 Hz x 5e-6 s = 4.14 degrees
```

| Run | System Delay (ms) | Difference from Run 1 (us) | Notes |
| --- | ---: | ---: | --- |
| 1 |  | `0` |  |
| 2 |  |  |  |
| 3 |  |  |  |

| Check | Result | Pass target |
| --- | --- | --- |
| Delay spread |  | Preferably no more than `5 us` |
| Magnitude spread, `1-5 kHz` |  | No more than approximately `0.2 dB` |
| Phase overlay |  | Nearly coincident |
| Microphone clipping |  | None |
| Reference clipping/dropout |  | None |

**VERIFIED UMC22 RESULT - PASS (2026-09-05):**

| Check | UMC22 result | Pass target |
| --- | --- | --- |
| Delay spread | `1.0 us` | Preferably no more than `5 us` |
| Magnitude spread, `1-5 kHz` | `0.0743 dB` maximum under the common direct window | No more than approximately `0.2 dB` |
| Phase overlay | `1.931 degrees` maximum circular spread; `0.697 degrees` at `2.3 kHz` | Nearly coincident |
| Microphone clipping | None; all final-setting runs stayed green | None |
| Reference clipping/dropout | None; all final-setting runs stayed green | None |

This releases the qualified UMC22 route for controlled installed-woofer FRD.
It does not release raw-tweeter, full-polar, or final-FRD work beyond the
separate conditions stated below.

## 9. If The Test Fails

Check, in order:

1. Direct Monitor is off and Input 2 is in `LINE` mode.
2. REW input L is the microphone and input R is the reference.
3. `Use loopback as cal and timing reference` and response merging are enabled.
4. Both inputs have adequate level and neither clips.
5. Sample rate, selected audio device/driver, and channel selections remain
   unchanged.
6. Interface output, both input gains, and amplifier volume have not moved.
7. Microphone, cabinet, cables, fixture, and stands have not moved.
8. The fixture record shows release approval, and the actual Input 2 reference
   is close to the expected `0.10 V RMS` at `1.00 V RMS` speaker output without
   clipping or dropout.
9. The impulse does not contain multiple comparable synchronization peaks.
10. Repeat with a `512k` single sweep if noise or the long sweep is problematic.
11. Repeat with the safe semi-dual connection. If semi-dual is repeatable but
    full-dual is not, investigate the fixture and amplifier-reference path.

## 10. Deferred Work And References

The UMC22 installed-woofer repeatability test now passes, so controlled woofer
FRD may proceed with its qualified settings and a documented REW-native window.
Do not proceed to the raw tweeter or full polar series on this release. The
tweeter requires a separately agreed sweep range, voltage, and protective high-
pass component; near-field merging and final FRD export retain their own method
and provenance requirements.

Primary references:

- Complete reference-fixture authority:
  [`SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md`](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md)
- Completed fixture AC commissioning:
  [`REFERENCE_FIXTURE_AC_COMMISSIONING.md`](REFERENCE_FIXTURE_AC_COMMISSIONING.md)
- Completed fixture qualification evidence:
  [`SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md`](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md)
- SU-V570 output-topology gate:
  [`SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md`](SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md)
- Project-wide measurement workflow:
  [`../MEASUREMENT_WORKFLOW.md`](../MEASUREMENT_WORKFLOW.md)
- Behringer UMC202HD quick-start guide:
  <https://mediadl.musictribe.com/media/PLM/data/docs/UMC/QSG_BE_0805-AAR_U-PHORIA-Series_WW.pdf>
- REW measurement and loopback-reference documentation:
  <https://www.roomeqwizard.com/help/help_en-GB/html/makingmeasurements.html>
- REW soundcard and ASIO sample-rate guidance:
  <https://www.roomeqwizard.com/help/help_en-GB/html/calsoundcard.html>
- VituixCAD REW measurement guide:
  <https://kimmosaunisto.net/Software/VituixCAD/VituixCAD_Measurement_REW.pdf>
