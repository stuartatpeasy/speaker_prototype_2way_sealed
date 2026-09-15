# Seed A As-Built Impedance and EPDR — 2026-09-09

| State | Value |
| --- | --- |
| Lifecycle | **QUALIFICATION EVIDENCE — LOAD GATE PASSED** |
| Owns | Retained file identity, measurement metadata, as-built impedance/phase results, EPDR derivation, model comparison, and load-gate consequence |
| Does not own | Routine jig operation, crossover topology, acoustic validation, or the later distortion/compression/thermal procedure |
| Read when | Auditing the measured Seed A load, EPDR calculation, amplifier burden, or a later crossover change |
| Current conclusion | Seed A passes the `3.5 ohm` magnitude gate; its minimum EPDR is about `2.56 ohm` near `1.94 kHz`. The subsequent bounded level/distortion and surface-thermal gates also pass |
| Next gate | Matched speaker-two build and validation; see the later level/thermal qualification |
| Last reviewed | 2026-09-10 |

## 1. Retained evidence and conditions

**USER-REPORTED CAPTURE PASS:** the one qualified Seed A sweep completed with
no anomalies. REW retained the measurement as
`SPK_impedance_WT_1_20260909`.

| Artefact | Size | SHA-256 |
| --- | ---: | --- |
| [`rew/SPK_impedance_WT_1_20260909.mdat`](../../../rew/SPK_impedance_WT_1_20260909.mdat) | `970,839 bytes` | `66a6ba0c366fc0937ae6d2a3bdff36801b606b1376e76915621a3ff2790364b6` |
| [`rew/SPK_impedance_both_drivers_run1_2026-09-09.zma`](../../../rew/SPK_impedance_both_drivers_run1_2026-09-09.zma) | `1,637,188 bytes` | `4180e799dc6d26a663fde6655c22a47b32e9271d014ffa562a517881ce7503ed` |

The ZMA header independently confirms REW `V5.40 beta 133`, the exclusive
StarTech input, measurement input `L`, one `1M` logarithmic sweep at
`-12.0 dBFS`, `48 kHz`, `100.0 ohm` sense resistor, zero entered lead
resistance, `20 kohm` input resistance, calibration factor `0.9782`, no
smoothing, measurement name `SPK_impedance_WT_1_20260909`, and capture time
`2026-09-09 22:11:01`.

The export contains `54,586` native, linearly spaced data points from
`9.8877 Hz` to `19,999.878 Hz`. Load metrics below use the conventional audible
analysis span from the first point at or above `20 Hz` through the final point.
The dense unsmoothed export is retained as stronger evidence than a reduced
points-per-octave export.

The qualified route, calibration, `6.755 ohm` control result, channel mapping,
and prior `14.7 mV RMS` Seed A level check are owned by the
[StarTech route qualification](STARTECH_IMPEDANCE_ROUTE_QUALIFICATION_2026-09-09.md).

## 2. Measured load results

**VERIFIED FROM RETAINED ZMA / DERIVED:**

| Metric | Result |
| --- | ---: |
| Minimum impedance magnitude | `4.366 ohm` at `9.617 kHz` |
| Phase at magnitude minimum | `+1.278 degrees` |
| Minimum real part, `|Z| cos(phi)` | `4.284 ohm` at `2.156 kHz` |
| Most positive phase | `+54.046 degrees` at `54.565 Hz`, where `|Z|=23.295 ohm` |
| Most negative phase | `-69.596 degrees` at `73.975 Hz`, where `|Z|=21.990 ohm` |
| Minimum EPDR | `2.563 ohm` at `1.942 kHz` |
| Load at minimum EPDR | `4.905 ohm`, `-25.113 degrees`; real part `4.441 ohm` |

A `1/96`-octave logarithmic-grid interpolation gives essentially the same
rounded conclusions: approximately `4.37 ohm` minimum magnitude near
`9.74 kHz`, `4.29 ohm` minimum real part near `2.18 kHz`, and `2.57 ohm`
minimum EPDR near `1.92 kHz`. The reported values are therefore broad-curve
features rather than isolated point noise.

## 3. EPDR derivation

EPDR is the purely resistive load producing the same peak output-transistor
dissipation as the measured complex load in an ideal full-rail class-B output
stage. Let `a=|phi|` in radians. Maximising the conducting device's
instantaneous dissipation over a sine cycle and equating it to the resistive
case gives

```text
EPDR = |Z| /
       {4 [1 - sin(5*pi/6 + 2*a/3)] sin(5*pi/6 - a/3)}.
```

At zero phase the brace evaluates to `1`, so EPDR correctly reduces to `|Z|`.
At the measured minimum:

```text
|Z| = 4.905 ohm
a   = 25.113 degrees = 0.4383 rad
brace factor = 1.9135
EPDR = 4.905 ohm / 1.9135 = 2.563 ohm.
```

The units remain ohms because the brace is dimensionless. This EPDR describes
idealised class-B/AB output-device peak heating. Actual output current is still
set by the measured `4.905 ohm` magnitude, not by treating the loudspeaker as a
literal `2.563 ohm` impedance.

REW identifies EPDR as a combined impedance-magnitude/phase load-severity
metric and cites E. Benjamin, “Audio Power Amplifiers for Loudspeaker Loads,”
JAES Vol. 42 No. 9 (1994). Keith Howard's description likewise defines it as
the resistive load giving the same peak class-B device dissipation.

## 4. Model comparison and decision

The practical measured-component model predicted a `3.805 ohm` minimum near
`2.792 kHz` at about `-9.4 degrees`. The as-built measurement gives
`4.637 ohm` at that frequency and a global minimum of `4.366 ohm`:

```text
measured global minimum - predicted minimum
= 4.366 ohm - 3.805 ohm
= +0.561 ohm  (+14.8% relative to the model prediction)

measured global minimum - prototype gate
= 4.366 ohm - 3.500 ohm
= +0.866 ohm  (+24.8% relative to the gate)
```

**QUALIFICATION DECISION — PASS:** the as-built load clears the project's
minimum-impedance gate with useful margin and is less current-demanding than
the practical model predicted. The `2.56 ohm` minimum EPDR shows a moderate
reactive peak-dissipation burden around the crossover; it informed the
subsequent bounded amplifier-level and thermal test and does not justify a
crossover change by itself.

The SU-V570 is specified for one `4-16 ohm` loudspeaker pair and has published
`4 ohm` power specifications. Seed A's actual impedance magnitude remains above
`4.36 ohm`. The subsequent bounded level/distortion and surface-thermal gates
pass in the [later qualification](SEED_A_FULL_SYSTEM_LEVEL_AND_THERMAL_QUALIFICATION_2026-09-10.md); matched speaker-two validation is now next.

## 5. Method references

- [REW SPL and phase graph documentation](https://www.roomeqwizard.com/betahelp/help/html/graph_splphase.html)
- [Keith Howard, “Heavy Load: How Loudspeakers Torture Amplifiers,” page 2](https://www.stereophile.com/content/heavy-load-how-loudspeakers-torture-amplifiers-page-2)
- [Technics SU-V570 service-manual scan](https://audiocircuit.dk/downloads/technics/Technics-SUV570-int-sm.pdf)
