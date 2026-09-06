# Room Placement and Measurement

> - **Lifecycle:** ACTIVE PLACEMENT AND ROOM-MEASUREMENT AUTHORITY
> - **Owns:** speaker, shelf, and listener coordinates; current/75 mm/150 mm placement candidates; direct-path calculations; placement consequences; and the first listening-position room-measurement series
> - **Does not own:** canonical DAE audit, coupled-volume calculations, boundary construction assumptions, installed-baffle driver FRD procedure, or crossover design
> - **Current decision:** compare current boundary symmetry against 75 mm and 150 mm-left right-speaker trials; do not promote geometric symmetry to a final placement without measurement
> - **Next gate:** confirm the nominal ear marker and run separate-channel impulse/ETC and magnitude comparisons with all other conditions fixed
> - **Limitations:** source/ear acoustic-centre coordinates and normal remote-door states are not yet fully confirmed; room results must not be folded directly into the passive crossover
> - **As of:** 2026-09-06

This file is the placement and room-measurement companion to [ROOM_DETAILS.md](../ROOM_DETAILS.md). Canonical geometry, provenance, boundary assumptions, and screening are in [ROOM_GEOMETRY_AND_SCREENING.md](ROOM_GEOMETRY_AND_SCREENING.md).

## 1. Coordinate and evidence basis

Coordinates use metres: `z` is height; `y` increases toward the speaker wall; `x` runs across the room. The speaker wall is `y = 4.820 m`, and the speakers face decreasing `y`.

Values marked **VERIFIED FILE GEOMETRY** were read from the canonical DAE. **USER-CONFIRMED INSTALLATION** records information supplied separately by the user. **DERIVED** values follow from those inputs. **OPEN ITEM** marks information still required before a final decision.

## 2. Speakers and shelf

The following coordinates are now **VERIFIED FILE GEOMETRY**, rather than placement inferred from the cabinet dimensions:

| Item | DAE coordinate or span |
|---|---:|
| Cabinet nearest the `x = 0` wall | `x = 0.100–0.380 m` |
| Cabinet nearest the `x = 2.550 m` wall | `x = 2.170–2.450 m` |
| Both cabinet bodies, baffle to rear | `y = 4.420–4.720 m` |
| Both cabinet bodies, bottom to top | `z = 1.015–1.445 m` |
| Cabinet envelope | 0.280 m wide × 0.300 m deep × 0.430 m high |
| Rear and nearest-side clearances | 0.100 m |
| Baffle planes and normals | `y = 4.420 m`, facing negative `y` |
| Cabinet-centre spacing | 2.070 m |
| Shelf | `x = 0.100–2.450 m`, `y = 4.420–4.720 m`, `z = 0.970–1.000 m` |
| Shelf dimensions | 2.350 m wide × 0.300 m deep × 0.030 m thick |

- **USER-CONFIRMED INSTALLATION:** the shelf top is 1.000 m above the floor and soft rubber feet provide the 15 mm gap to the cabinet bottoms.
- The speakers and shelf share the same front and rear planes. The shelf is therefore a broad, nearly wall-to-wall horizontal surface directly beneath both baffles, not two small isolated supports.
- **DERIVED:** the ceiling over each cabinet is approximately 1.755 m high at the rear and 2.080 m at the baffle. Minimum nominal clearance above the 1.445 m cabinet top is about 0.310 m at the rear edge.
- **OPEN ITEM:** record shelf material, attachment, and measured deflection or resonance behaviour. The rubber feet may reduce structure-borne transmission and rattles, but they do not guarantee that this large shelf will be non-radiating.

## 3. Listening position and direct-path alternatives

- **VERIFIED FILE GEOMETRY:** the marker is a 0.200 m-diameter vertical disc in the `x-z` plane at `y = 3.700 m`; its centre is `(x, y, z) = (1.200, 3.700, 1.250) m`.
- **OPEN ITEM:** confirm whether its centre is intended to be the midpoint between the listener's ears and whether 1.250 m is the normal seated ear height. Until then it is a nominal head region, not a verified microphone coordinate.
- **DERIVED:** using the speaker baffle-plan centres `(0.240, 4.420)` and `(2.310, 4.420) m`, the marker centre is only 0.720 m forward of the baffle plane. Plan distances are approximately 1.200 m to the left cabinet centre and 1.323 m to the right; the corresponding straight-ahead off-axis angles are approximately 53.1° and 57.0°.
- **DERIVED:** those two sight lines subtend approximately 110.2° at the listener, far wider than a conventional approximately 60° stereo triangle. The 0.123 m path difference corresponds to approximately 0.36 ms and 0.85 dB of spherical distance loss before room effects. These calculations use cabinet-plan centres, not the as-built driver acoustic centres, but the unusually wide angle is too large to be explained by that approximation. Confirm that this near-field, wide-angle arrangement is intentional before finalising listening-axis crossover decisions.

### 3.1 Right-speaker lateral alternatives

The left cabinet centre is fixed at `x = 0.240 m`; the nominal listener is at `x = 1.200 m`, and both baffles remain at `y = 4.420 m`. Moving only the right speaker can reduce the included angle, but it cannot create a conventional symmetric 60° triangle because the left speaker alone is already 53.1° from the forward axis.

| Right cabinet centre `x` | Move left from DAE | Included angle | Right path | Right direct level vs left | Right arrival vs left |
|---:|---:|---:|---:|---:|---:|
| 2.310 m; current DAE | — | 110.2° | 1.323 m | −0.85 dB | 0.36 ms later |
| 2.235 m; intermediate trial | 75 mm | 108.3° | 1.261 m | −0.43 dB | 0.18 ms later |
| **2.160 m; symmetry baseline** | **150 mm** | **106.3°** | **1.200 m** | **0.00 dB** | **0.00 ms** |
| 1.740 m; 90° total | 570 mm | 90.0° | 0.900 m | +2.50 dB | 0.88 ms earlier |
| 1.489 m; 75° total | 821 mm | 75.0° | 0.776 m | +3.79 dB | 1.24 ms earlier |
| 1.287 m; 60° total | 1.023 m | 60.0° | 0.725 m | +4.37 dB | 1.38 ms earlier |

The **150 mm leftward shift** is the direct-path and off-axis symmetry candidate, not an automatic overall optimum. It centres the speaker pair on the listener, equalises the geometric path lengths, and leaves the right cabinet at `x = 2.020–2.300 m`, giving 250 mm clearance to the right wall while retaining the 100 mm rear clearance. That also sacrifices the present equal side-wall spacing: the speaker-centre distances to the nearest side walls change from 0.240/0.240 m to 0.240/0.390 m. Current placement is therefore the boundary-symmetry candidate, 150 mm left is the direct-symmetry candidate, and 75 mm left is a useful intermediate A/B position. Measurement must choose among them.

If the listening position can move laterally, shifting its centre **75 mm right to `x = 1.275 m`** is an especially clean comparison: it equalises the current speaker path lengths while preserving both 100 mm cabinet-to-side-wall gaps. It leaves the wide approximately 110.3° included angle, but avoids trading one asymmetry for another.

If the listener can instead move farther from the baffle plane after the 150 mm right-speaker correction, symmetric included angles of 90°, 75°, and 60° occur at approximately `y = 3.460 m`, `3.169 m`, and `2.757 m` respectively—moves of 240, 531, and 943 mm away from the speaker wall. Any toe-in decision must then be based on the measured installed-baffle off-axis responses and physical shelf clearances.

## 4. Placement consequences

- Corner placement gives strong low-frequency boundary loading and tends to couple efficiently to modes whose pressure maxima lie at the boundaries. This suits the near-wall design direction, but it increases the need to measure peaks and nulls at the actual seat rather than designing extra passive bass lift.
- The normally open 1.4773 m² doorway strongly couples the listening room to the hallway rather than leaving a sealed 22.63 m³ cavity. The newly modelled spaces can shift resonances and decay times and introduce coupled-cavity behaviour, but their volumes must not simply be added as though the internal walls and apertures did not exist.
- The local adjoining geometry now extends through the former 1.7848 m² terminal opening. Three smaller unclosed boundary apertures remain at the far end/side of the extended hall; their normal states and the effective downstream volume now dominate the remaining geometric uncertainty.
- The baffle plane is nominally 0.400 m from the speaker wall. The simplest rigid-wall image model therefore puts the first rear-wall cancellation near `c/(4d)`, approximately 214 Hz. This is a warning frequency, not a prediction: the real result depends on source position, wall construction, cabinet diffraction, crossover, and listening position.
- The nominal listening marker makes the installation a very wide-angle near-field arrangement unless it has been misinterpreted; Section 3 gives the derived geometry. The exact woofer, tweeter, ear, and microphone coordinates are still required to predict floor, ceiling, desk, and shelf-reflection path differences.
- **USER-CONFIRMED INSTALLATION:** the complete floor is carpeted and the walls and ceiling are plasterboard. Carpet will mainly affect mid/high-frequency reflection and decay; it should not be assumed to control the principal bass modes. Plasterboard can provide frequency-dependent low-frequency absorption or transmission; use the two-case provisional bracket in [Section 3.4 of the geometry authority](ROOM_GEOMETRY_AND_SCREENING.md#34-provisional-boundary-assumptions) rather than treating an assumed build-up as quantitatively exact.
- The soft feet provide only about 15 mm clearance above a 2.35 m-wide shelf whose front edge is flush with the baffle planes. Treat the shelf as an acoustic extension/reflection surface as well as a mechanical support, and test it for vibration or buzz at the intended playback level. Installed-baffle measurements should include the final shelf.
- The 3.38 m² in-room desktop is a much larger reflection surface than ordinary desk clutter. Its L shape and position on the `x = 2.550 m` side make early reflections and channel balance asymmetric; the omitted swivel chair and clutter are secondary refinements rather than reasons to defer first measurements.
- The 1.0915 m² single-glazed window replaces a substantial patch of the `x = 0` plasterboard wall. It is likely to differ from the opposite wall in reflection, transmission, and possible pane/frame vibration. For the nominal listening marker, simple image geometry puts the `x = 0` first-reflection points at approximately `y = 4.30 m` for the left speaker and `y = 3.95 m` for the right speaker—both beyond the window's `y = 3.240 m` end. Pane and mullion subdivision is therefore low priority for direct first reflections at this seat. Approximate pane sizes, glass thickness, frame/reveal depth, and normal curtain/blind state are more useful than detailed 3D frame profiles; investigate finer structure if the window rattles or the seat changes materially.
- Do not correct narrow room-mode or speaker-boundary nulls in the passive crossover. Establish the free-field/in-enclosure loudspeaker response first, then assess placement, modest broad DSP, and any future subwoofer from spatially averaged in-room measurements.

## 5. First room-measurement series

Once the prototype and positions are repeatable:

1. Measure each speaker separately at the main ear position, then both together.
2. Repeat at a small grid around the head position, for example centre plus approximately ±150–250 mm left/right, forward/back, and up/down where practical. This distinguishes a broad balance error from a narrow spatial null.
3. With toe angle and all other conditions fixed, compare the current right-speaker position with 75 mm and 150 mm left shifts; if feasible, also compare the current speakers with the listening point moved 75 mm right. Capture separate-channel impulse/ETC and magnitude data so direct-path symmetry can be distinguished from changed side-wall reflections.
4. Use the fully open listening-room doorway as the baseline state. Repeat diagnostic low-frequency sweeps with the bedroom and bathroom doors changed one at a time; if practical, also compare the listening-room door closed briefly to quantify total adjoining-space coupling.
5. Retain impulse/ETC and decay data as well as magnitude response; record all source, microphone, door, window, and furnishing coordinates with each measurement.
6. Use the measurements to decide placement and broad room correction before attempting any room-specific passive-crossover change.

## 6. Open placement decisions

1. Confirm whether the DAE marker centre is the midpoint between the ears and whether `1.250 m` is the normal seated ear height.
2. Choose among current, 75 mm-left, and 150 mm-left right-speaker positions from repeatable measurements, not geometry alone.
3. Decide whether the 75 mm-right listener trial and farther-back symmetric trials are physically useful.
4. Establish toe-in only after installed-baffle off-axis evidence and shelf clearances are known.
5. Decide any broad DSP or future-subwoofer treatment only after spatially sampled room evidence exists.
