# StarTech Impedance-Route Qualification — 2026-09-09

| State | Value |
| --- | --- |
| Lifecycle | **QUALIFICATION EVIDENCE — COMPLETE** |
| Owns | Evidence for the StarTech interface identity, effective channel selection, calibration refresh, known-resistor verification, and Seed A level check |
| Does not own | Routine operation, Seed A load results, crossover decisions, or acoustic validation |
| Read when | Auditing the route, diagnosing a failed known-load check, or changing interface hardware, gains, leads, channels, sample rate, or sense resistor |
| Conclusion | Output `R`, reference `R`, input `L`, `48 kHz`, and the `100.00 ohm` jig passed qualification; the released Seed A capture subsequently completed without anomalies |
| Limitation | The connector-level mapping is user-reported and conflicts with the apparent REW channel labels; functional resistor verification governs |
| Last reviewed | 2026-09-09 |

## 1. Fixed route

**USER-CONFIRMED:** all retained project impedance measurements used the
StarTech ICUSBAUDIO2D generic external USB sound card. REW names its endpoints
`StarTech USB audio interface (USB Audio Device)` and
`EXCL: StarTech USB audio interface (USB Audio Device)`. The qualified route
uses the exclusive endpoint for both input and output, output `R`, reference
input `R`, measurement input `L`, `48 kHz`, and the precision `100.00 ohm`
sense resistor.

The jig is powered from the StarTech's `5 V` USB supply. Ordinary DUT changes
therefore require the REW Generator to be stopped, but not a USB power cycle.

## 2. Functional channel and calibration evidence

The reported plug wiring would conventionally suggest the opposite input-role
labels, so the effective route was checked with a resistor rather than inferred
from connector descriptions.

With the previously retained calibration, a `6.779 ohm` nulled-DMM resistor
measured flat at `7.21 ohm` and `0 degrees`, without warnings:

```text
absolute error = 7.210 ohm - 6.779 ohm = +0.431 ohm
relative error = +0.431 ohm / 6.779 ohm x 100 = +6.36%
```

The flat zero-phase trace excluded gross channel reversal, while the magnitude
error justified refreshing the calibration.

**USER-REPORTED CALIBRATION PASS:** a complete open-circuit, short-circuit,
and reference-resistor calibration was then performed using a different
`6.755 ohm` resistor confirmed by a nulled measurement. The verification trace
was flat at `6.72 ohm` and `0 degrees` across the full range, with no reported
warning:

```text
absolute error = 6.720 ohm - 6.755 ohm = -0.035 ohm
relative error = -0.035 ohm / 6.755 ohm x 100 = -0.52%
```

This passes the specified `+/-2%` magnitude and approximately `+/-2 degree`
phase limits. It verifies the complete effective channel/calibration route;
no additional connector-role investigation is required.

## 3. Level and release conclusion

**USER-REPORTED LEVEL CHECK:** with Seed A connected, one REW Check Levels
action at `-12 dBFS` produced `14.7 mV RMS` at the system input. REW reported
no clipping and operation appeared normal. The tone was steady rather than
broadband.

The calibrated known-load result and this low Seed A terminal voltage released
one `1M`, `48 kHz`, `-12 dBFS` complete-system sweep. That capture subsequently
completed without anomalies and is evaluated in the
[Seed A load record](SEED_A_AS_BUILT_IMPEDANCE_AND_EPDR_2026-09-09.md). Repeat
calibration or level qualification only after a relevant path/setting change
or a specific measurement anomaly.
