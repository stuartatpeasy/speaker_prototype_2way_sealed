# FRD Measurement Setup Repeatability Test - UMC202HD

Date prepared: 2026-08-30

Last revised: 2026-09-03

Status: **PROVISIONAL ACOUSTIC SETUP-VALIDATION PROCEDURE; REFERENCE FIXTURE
NOT YET COMMISSIONED**

The SU-V570 output-topology and UMC202HD Input 2 TRS phantom-isolation gates
have passed. The reference fixture's post-rebuild complete-unit resistance
matrix has passed. All four powered DC curves pass clamp, symmetry, current,
CV, and thermal checks with an explicitly accepted `45.5 V` soft-knee deviation
from the approximate `1%` target. The cooled post-stress resistance matrix also
passes, closing the integrated DC gate. The physical record now passes for
controlled bench use; AC transfer/noise commissioning remains open. The
ground-path audit has verified a
`0.035 ohm` Input 2 sleeve-to-USB-shell bond and, using a `0.013 ohm` positive
control, DC isolation of the enclosure from that node. The interface-alone
stage passes, and the intended USB cable has `0.130 ohm` shell-to-shell
continuity. The isolated-PC stage also passes: Input 2 sleeve measures
`0.412 ohm` to PC chassis and `0.379 ohm` directly to the free mains plug's PE
pin. The mapped playback cable is mono TS-to-RCA; it was placed on hold because
its TS plug connects the output jack's ring contact to sleeve. Powered driven-
channel tests now verify that both rear outputs are already ring-grounded: Output 1
measured `78.69/0.002/78.73 mV` and Output 2 measured
`78.9/0.000/78.84 mV` tip-sleeve/ring-sleeve/tip-ring. The mapped TS cable
therefore adds no new cold-leg short, and its output-compatibility hold is
lifted. Internal inspection further shows that the distinct ring and sleeve
pads of both physical TRS output sockets share the same PCB copper fill: the
rear outputs have electrically TS, tip-plus-common topology. Use Output 2 tip
and the R/S common for the fixture-transfer source; do not treat it as a two-
active-leg balanced output. The fixture-alone ground check is
already satisfied by the disconnected post-stress matrix's `10.130 kohm` and
`10.146 kohm` input-to-sleeve readings. The connected playback path also passes:
with the intended dual cable fitted between the otherwise isolated, unpowered
devices, Input 2 sleeve measured `0.061 ohm` to the corresponding SU-V570 RCA
shell and `0.174 ohm` to the corresponding speaker-negative terminal. The
complete unpowered ground-path audit is therefore closed. The physical record
now records and accepts the individually insulated, multilayer heat-shrink
construction and its
approximately `5 cm` unscreened twisted output tail. That tail requires an
explicit no-signal pickup comparison during the remaining AC commissioning. Do
not use the full-dual connection until the fixture record marks it approved.
This procedure validates the woofer measurement chain; it is not a raw-tweeter
test or the final polar-measurement procedure.

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

Use REW's `Use loopback as cal and timing reference` mode with `Merge loopback
response into IR` enabled. Input 2 then references the acoustic response to the
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
UMC202HD Output 2 -> balanced TRS patch cable -> UMC202HD Input 2, LINE
```

Select `Use loopback as timing reference`. This preserves common timing but
leaves DAC and amplifier response in the acoustic measurement. Do not mix
semi-dual and full-dual data in a final driver set without first demonstrating
equivalent results.

## 3. Prerequisites And Equipment

### 3.1 Mandatory Release Gates

Before making the full-dual connection, confirm:

1. the SU-V570 record passes the unpowered common-ground topology gate;
2. the UMC202HD Input 2 central-TRS phantom-isolation gate passes;
3. every construction, resistance, integrated DC clamp, ground-path, and AC
   transfer gate in
   [`SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md`](SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md)
   passes; and
4. the fixture record explicitly says `Approved for amplifier use: YES`.

The fixture file is the sole detailed authority for its schematic, component
values, wiring, test history, and commissioning. This procedure does not repeat
those details.

### 3.2 Required Equipment

- Behringer ECM8000 and XLR microphone cable;
- Behringer UMC202HD and USB cable;
- current Behringer Windows driver;
- measured cable from UMC202HD Output 1 to the selected SU-V570 line input;
- fully commissioned SU-V570-to-UMC202HD reference fixture;
- Technics SU-V570;
- unchanged speaker cable from the selected SU-V570 output to the woofer;
- true-RMS voltmeter suitable at `1 kHz`;
- microphone stand, tape or laser measure, and cabinet support; and
- PC running REW.

Do not use the UMC202HD headphone output to drive a loudspeaker.

## 4. UMC202HD And REW Configuration

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

### 4.2 Initial REW Settings

| Setting | Value |
| --- | --- |
| Driver | Behringer UMC ASIO driver |
| Sample format | `24 bit` |
| Sample rate | `88.2 kHz` |
| Measurement input | Input L / UMC202HD Input 1 |
| Measurement output | Output L / UMC202HD Output 1 |
| Reference input | Input R / UMC202HD Input 2 |
| Reference output | Output R / UMC202HD Output 2 |
| Timing mode | Use loopback as cal and timing reference |
| Merge loopback response into IR | Enabled |
| Separate soundcard calibration file | None |
| Timing offset | `2.915 ms` for `1000 mm` at `343 m/s` |
| Sweep range | `5 Hz-41 kHz` |
| Initial sweep level | `-20 dBFS` |
| Final level after voltage setting | `-10 dBFS` |
| Sweep length | `1M` |
| Repetitions | `1` |
| Abort if heavy input clipping occurs | Enabled |

REW sends the sweep to both selected outputs when loopback reference is used.
Output 2 remains physically unconnected in the full-dual arrangement; Input 2
receives the amplifier-output reference instead. The timing offset removes the
nominal `1000 mm` propagation time while retaining the driver's physical delay.
Do not independently align woofer and tweeter impulse peaks later.

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

### 5.3 Full-Dual Connections

Make every amplifier, loudspeaker, fixture, and TRS connection with the
SU-V570 off:

1. Connect UMC202HD Output 1 to the selected SU-V570 line input.
2. Connect the matching SU-V570 speaker-output pair to the woofer.
3. At those same rear amplifier terminals, connect fixture red to positive and
   fixture black to negative. Do not use another channel or speaker bank.
4. Insert the fixture TRS plug into the central jack of UMC202HD Input 2.
5. Connect the ECM8000 to Input 1 by XLR.
6. Leave UMC202HD Output 2 physically unconnected.
7. Connect USB, enable `+48 V`, and reconfirm Input 2 `LINE` and Direct Monitor
   off.

```text
ECM8000 -> UMC202HD Input 1 / USB input L -> REW measurement input

REW output L -> UMC202HD Output 1 -> SU-V570 -> speaker cable -> woofer

SU-V570 rear speaker terminals -> commissioned reference fixture
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
   input and speaker bank. Observe the Input 2 no-signal spectrum using the same
   RTA/FFT settings retained from fixture commissioning. Stop and investigate
   any new `50/100 Hz` family, coherent spur, instability, or noise rise that
   materially reduces reference-channel margin; the UMC202HD-only fixture test
   cannot reveal pickup introduced only by the powered complete system.
6. Start the generator and raise SU-V570 volume slowly until the meter reads
   `1.00 V RMS`, then stop the
   generator immediately.
7. Confirm the amplifier-output reference is close to `99 mV RMS`, allowing for
   any small speaker-cable drop between the fixture and voltmeter reference
   planes. Stop for gross disagreement or clipping.
8. Mark the SU-V570 volume position with removable tape. Do not move it or the
   UMC202HD Output control during the series.

The fixture reference does not replace the true-RMS meter for absolute driver
voltage. REW removes the fixture's constant gain from relative response, but
the acoustic excitation still requires an independent voltage setting.

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
5. Sample rate, ASIO device, and channel selections remain unchanged.
6. Interface output, both input gains, and amplifier volume have not moved.
7. Microphone, cabinet, cables, fixture, and stands have not moved.
8. The fixture record shows the commissioned attenuation, polarity, and smooth
   `5 Hz-41 kHz` response.
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
- SU-V570 output-topology gate:
  [`SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md`](SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md)
- Project-wide measurement workflow:
  [`../MEASUREMENT_WORKFLOW.md`](../MEASUREMENT_WORKFLOW.md)
- Behringer UMC202HD quick-start guide:
  <https://mediadl.musictribe.com/media/PLM/data/docs/UMC/QSG_BE_0805-AAR_U-PHORIA-Series_WW.pdf>
- REW measurement and loopback-reference documentation:
  <https://www.roomeqwizard.com/help/help_en-GB/html/makingmeasurements.html>
- VituixCAD REW measurement guide:
  <https://kimmosaunisto.net/Software/VituixCAD/VituixCAD_Measurement_REW.pdf>
