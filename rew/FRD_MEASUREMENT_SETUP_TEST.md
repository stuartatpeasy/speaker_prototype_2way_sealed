# FRD Measurement Setup Repeatability Test - UMC202HD

Date prepared: 2026-08-30

Last revised: 2026-09-05

Status: **UMC202HD PROCEDURE SUSPENDED BY DESKTOP DROPOUT; FIXTURE RELEASE
REMAINS VALID; UMC22 FALLBACK IS AT ITS UNPOWERED CONTACT-MAP GATE**

Every electrical release prerequisite has passed: SU-V570 common-ground
topology, UMC202HD Input 2 phantom isolation, complete-fixture
resistance/DC/physical qualification, the unpowered ground audit, and rear-
output topology. The inspected rear outputs are mechanically TRS but
electrically tip plus a ring/sleeve common. The fixture's short unscreened tail
was included in the powered no-signal pass.

The proportionate safety/connectivity review in
[REFERENCE_FIXTURE_AC_COMMISSIONING.md](REFERENCE_FIXTURE_AC_COMMISSIONING.md)
passes, and the fixture authority says `Approved for amplifier use: YES` for
controlled UMC202HD bench work. That electrical release remains valid, but
UMC202HD measurement use is suspended by the separate dropout. This is not a
raw-tweeter or final polar-measurement procedure.

This procedure's current settings and release statements are UMC202HD-specific.
The risk-accepted UMC22 alternative is eligible only after the separate gates
in [UMC22_RISK_ACCEPTED_FRD_FALLBACK.md](UMC22_RISK_ACCEPTED_FRD_FALLBACK.md)
pass; its `48 kHz` configuration, contact mapping, calibration, and measured
reference level must then supersede the corresponding UMC202HD details below.

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
5. Load the ECM8000 calibration file for Input 1 if available.
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
| Timing-reference output | Output R / UMC202HD Output 2 |
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
The secondary output remained disabled. This is the correct full-dual routing.
The first checkout deliberately retains zero timing offset; establish and
inspect one valid impulse before applying a common propagation-time correction
to the repeat series. The inherited name and `0-24 kHz` range remain to be
replaced before measurement. No signal was generated at this checkpoint.

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
7. Disable tone and loudness processing, or use Power Amp Direct if appropriate.
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
work critical path and remains at Gate A in
[UMC22_RISK_ACCEPTED_FRD_FALLBACK.md](UMC22_RISK_ACCEPTED_FRD_FALLBACK.md).

### 6.2 Set Input Gains

1. Open REW's measurement dialog and run `Check Levels`.
2. Raise `GAIN 1` only enough for a clean microphone signal, initially aiming
   for approximately `-12` to `-18 dBFS` peaks.
3. Raise `GAIN 2` from minimum until the reference is reliable with at least
   `6 dB` headroom. Engage its pad only if minimum gain is still excessive.
4. Confirm both front-panel clip LEDs remain off and neither REW input clips.
5. Do not alter either gain after this point.

Absolute SPL calibration is unnecessary for this repeatability test. When the
SL-200 is available, calibrate REW with the meter on C weighting and SLOW
without subsequently changing Gain 1.

## 7. Capture And Window Three Repeats

### 7.1 Capture

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

Do not proceed to the raw tweeter, full polar series, near-field merge, or final
FRD export until this test passes. The tweeter requires a separately agreed
sweep range, voltage, and protective high-pass component.

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
