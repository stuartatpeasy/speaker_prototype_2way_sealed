# Listening Room — Geometry, Placement, and Acoustic Record

This file is the room-specific companion to [README.md](README.md). It records what is present in the canonical model **`3d_models/Listening room.dae`**, what has been supplied separately by the user, what can be derived from those facts, and what still needs measurement or confirmation.

Status labels used below:

- **VERIFIED FILE GEOMETRY** — read directly from the canonical DAE and checked computationally;
- **USER-CONFIRMED INSTALLATION** — stated by the user but not necessarily encoded in the room model;
- **USER-CONFIRMED ARCHITECTURE** — an unusual as-built feature explicitly confirmed by the user;
- **DERIVED** — calculated from the geometry or stated placement;
- **ILLUSTRATIVE** — a bounded example, not an as-built result;
- **OPEN ITEM** — required before reliable prediction or final tuning.

## 1. Source and interpretation

- **VERIFIED FILE GEOMETRY (2026-08-30):** canonical source file **`3d_models/Listening room.dae`**; SketchUp 26.2.0 COLLADA 1.4.1 export; SHA-256 `F22A4803086773D76A08A38B37D88EB6519662FC5D77762B6AB36B7525DAA526`.
- **VERIFIED FILE GEOMETRY:** the DAE declares `Z_UP` and an explicit unit of one inch (`meter="0.0254"`). The scene now contains eleven triangle meshes and two line geometries: the expanded architectural shell, window patch and frame outline, shelf, desk, three door leaves, two speaker envelopes, listening-position marker, shower panels, and a short door-edge line.
- **VERIFIED FILE GEOMETRY:** the architectural shell now includes the listening room, bedroom, bathroom, the original hallway segment, a further 4.875 m hallway extension, one further side volume, and their connecting apertures. It is dimensionally usable but is not one watertight simulation volume: after coincident vertices are merged, the shell mesh has 33 boundary edges and 45 non-manifold edges where room surfaces, apertures, and shared boundaries meet. A wave or finite-element solver would need separate non-overlapping air volumes or a rebuilt coupled domain.
- **USER-CONFIRMED INSTALLATION:** the 4.820 m long dimension is correct. The DAE therefore resolves the former STL unit ambiguity and reproduces its geometry to harmless export-rounding precision.
- Coordinate convention used in this record: `z` is height above the floor; `y` is the long axis, increasing from the doorway/cutout end toward the intended speaker wall; `x` is the cross-room direction. The intended speaker wall is therefore `y = 4.820 m`, and the speakers face toward decreasing `y`.
- **USER-CONFIRMED INSTALLATION:** the doorway is on the `x = 1.600 m` notch boundary, so its closed plane is parallel to the long axis. The door swings into the room; its normal open angle is limited by the sloped ceiling, with its outer top corner resting near the natural door/roof intersection.
- **VERIFIED FILE GEOMETRY:** the clear doorway apertures, door leaves, expanded connected spaces, shower panels, window boundary/frame outline, speaker shelf, nominal speaker envelopes, L-shaped desktop, and listening marker are now present. Three boundary openings remain without downstream air volumes or door leaves; individual window panes, bathroom furniture other than the shower, desk clutter/supports, and office chair are not modelled.

## 2. Verified geometry

### 2.1 Envelope, area, and volume

| Quantity | Value |
|---|---:|
| Maximum cross-room span (`x`) | 2.550 m |
| Long-axis span (`y`) | 4.820 m |
| Maximum ceiling height (`z`) | 2.080 m |
| Height at both short end walls | 1.630 m |
| Floor area | 11.056 m² |
| Closed-envelope volume before contents | 22.63153 m³ |
| Mean height (`volume / floor area`) | 2.047 m |
| Floor surface | 11.056 m² |
| Ceiling surface, including both slopes | 11.9105 m² |
| Vertical boundary surface | 28.4317 m² |
| Closed-envelope surface | 51.3982 m² |
| Open doorway aperture | 0.790 × 1.870 m = 1.4773 m² |
| Window boundary patch | 1.485 × 0.735 m = 1.0915 m² |
| Boundary surface excluding the open doorway | 49.9209 m² |
| Modelled solid displacement inside the room | approximately 0.2198 m³ |
| Remaining geometric room air before chair/clutter | approximately 22.4117 m³ |

The closed-envelope volume lies inside the project's existing 20–50 m³ design range, but near its lower end. The approximately 0.97% displacement from the modelled desk top, shelf, speakers, and open door leaf is small for first modal estimates. Because the doorway normally opens into the now-modelled hallway, which itself ends at a large opening to unmodelled space, neither 22.6315 m³ nor 22.4117 m³ is a complete low-frequency acoustic volume.

### 2.2 Floor plan

In metres, the floor-plan vertices are:

```text
(0, 0) -> (1.600, 0) -> (1.600, 1.300) ->
(2.550, 1.300) -> (2.550, 4.820) -> (0, 4.820)
```

This is a 2.550 m × 4.820 m bounding rectangle with a 0.950 m × 1.300 m corner removed from the doorway end. Those are plan dimensions of the missing region, not verified clear-opening dimensions for the door.

### 2.3 Ceiling profile

The ceiling is constant across `x` at each occupied `y` position. Its height is:

- 1.630 m at the doorway-end wall (`y = 0`);
- a linear rise of 0.450 m over the first 0.440 m of room length;
- flat at 2.080 m from `y = 0.440 m` to `y = 4.460 m`;
- a linear fall of 0.450 m over the final 0.360 m to the speaker wall;
- 1.630 m at the speaker wall (`y = 4.820 m`).

### 2.4 Adjoining spaces and acoustic openings

The expanded shell gives the following simple geometric volumes. They are **DERIVED FROM VERIFIED FILE GEOMETRY** by integrating the modelled floor plans and ceiling profiles; they are not automatically one acoustic volume because the connecting apertures have finite acoustic impedance and some door states remain unconfirmed.

| Region | Modelled plan and height | Floor area | Geometric volume |
|---|---|---:|---:|
| Listening room | L-shaped plan in Section 2.2; 1.630–2.080 m ceiling | 11.056 m² | 22.6315 m³ |
| Hallway segment | `x = 1.600–5.730 m`, `y = 0–1.300 m`; mixed sloped/flat ceiling | 5.369 m² | 10.9002 m³ |
| Bathroom | `x = 2.550–4.550 m`, `y = 1.300–4.820 m`; 1.630–2.080 m ceiling | 7.040 m² | 14.4812 m³ |
| Bedroom | `x = 0–4.300 m`, `y = -4.700–0 m`; floor at `z = -0.500 m`, ceiling at `z = 1.630 m` | 20.210 m² | 43.0473 m³ |
| Extended hallway | `x = 5.730–10.605 m`, `y = 0–1.300 m`; floor at `z = -0.140 m`, flat 2.080 m ceiling | 6.3375 m² | 14.0693 m³ |
| Further side volume; name not preserved in export | `x = 4.550–8.635 m`, `y = 1.300–4.820 m`; floor at `z = -0.140 m`, 1.630–1.940 m ceiling | 14.3792 m² | 29.7517 m³ |
| **Total represented architectural air before contents** | — | **64.3917 m²** | **134.8812 m³** |

The apertures which determine whether those volumes behave independently or as coupled rooms are more important than centimetre-level detail in distant furniture:

| Connection | Clear opening inferred from shell | Area |
|---|---:|---:|
| Listening room to hallway | 0.790 × 1.870 m | 1.4773 m² |
| Hallway to bedroom | 0.765 × 1.500 m | 1.1475 m² |
| Hallway to bathroom | 0.760 × 1.840 m | 1.3984 m² |
| Original hallway to extended hallway | 0.920 × 1.940 m | 1.7848 m² |
| Extended hallway to further side volume | 0.745 × 1.810 m | 1.3485 m² |
| Extended hallway to unmodelled side opening A | 0.760 × 1.960 m | 1.4896 m² |
| Extended hallway to unmodelled side opening B | 0.670 × 1.960 m | 1.3132 m² |
| Extended hallway far end to unmodelled continuation | 0.750 × 1.800 m | 1.3500 m² |

The formerly terminal hallway opening is now internal and leads into the modelled extension. The current outer boundary still has three unclosed apertures totalling approximately 4.153 m², so 134.88 m³ must not be treated as a sealed acoustic volume. Whether those remaining openings represent normally open passages or omitted closed doors matters more than extending every remote wall by another centimetre. The DAE also contains two additional open-position door leaves at the bedroom and bathroom connections, but their normal operating states have not yet been user-confirmed.

- **USER-CONFIRMED ARCHITECTURE:** the bedroom floor being 0.500 m below the hallway/listening-room floor and its doorway being only 1.500 m high are correct Tudor-era features. Exact stair or threshold detail remains low priority acoustically.
- **VERIFIED FILE GEOMETRY:** the extended hallway and further side volume have floors 0.140 m below the original hallway. The original 0.920 × 1.940 m opening therefore implies a 140 mm step down; confirm this further level change when convenient.

## 3. Modelled installation geometry

### 3.1 Speakers and shelf

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

### 3.2 Window, doorway, and door

| Item | DAE geometry |
|---|---:|
| Window plane | `x = 0`, `y = 1.755–3.240 m`, `z = 0.900–1.635 m` |
| Window size and area | 1.485 m × 0.735 m; 1.0915 m² |
| Doorway aperture | `x = 1.600 m`, `y = 0.360–1.150 m`, `z = 0–1.870 m` |
| Doorway size and area | 0.790 m × 1.870 m; 1.4773 m² |
| Open door-leaf envelope | `x = 0.810–1.600 m`, `y = 0.276–0.400 m`, `z = 0.005–1.870 m` |
| Door-leaf nominal size | 0.790 m wide × 1.865 m high × 0.040 m thick |

- **USER-CONFIRMED INSTALLATION:** the window has three single-glazed panes. The DAE represents the complete glazed region as one unsplit zero-thickness rectangle and adds a four-line hardwood-frame outline; individual panes, mullions, thickness, and reveal geometry are not present.
- **VERIFIED FILE GEOMETRY:** the door leaf is approximately 96.1° from its closed direction, or 6.1° beyond parallel with the opposite end wall. It leaves the clear aperture unobstructed and has 5 mm floor clearance.
- **DERIVED:** the roof above the lowest outer top corner is approximately 1.912 m high, giving about 42 mm vertical clearance or 30 mm measured normal to the slope. With the present hinge and door width, only roughly another 3° of opening would bring that corner to the idealized roof plane. This is consistent with the user-reported roof-limited resting position; small trim, hardware, and measurement differences are comparable with the remaining clearance.

### 3.3 Desk and omitted chair

- **VERIFIED FILE GEOMETRY:** the desktop is an L-shaped 20 mm-thick solid with `z = 0.715–0.735 m`.
- Its plan vertices are `(0.352, 3.950)`, `(0.352, 4.735)`, `(2.550, 4.735)`, `(2.550, 1.750)`, `(1.800, 1.750)`, and `(1.800, 3.950)` metres.
- The top area is approximately 3.3754 m² and now terminates exactly at the nominal `x = 2.550 m` wall plane.
- The desk supports, under-desk storage, and ordinary desktop clutter are not modelled.
- **USER-CONFIRMED INSTALLATION:** a standard office swivel chair normally sits near the inner corner of the L but is not yet modelled. It is unlikely to dominate the lowest room modes, but its seat/back and position can affect local mid/high-frequency reflection and absorption.

### 3.4 Listening-position marker

- **VERIFIED FILE GEOMETRY:** the marker is a 0.200 m-diameter vertical disc in the `x-z` plane at `y = 3.700 m`; its centre is `(x, y, z) = (1.200, 3.700, 1.250) m`.
- **OPEN ITEM:** confirm whether its centre is intended to be the midpoint between the listener's ears and whether 1.250 m is the normal seated ear height. Until then it is a nominal head region, not a verified microphone coordinate.
- **DERIVED:** using the speaker baffle-plan centres `(0.240, 4.420)` and `(2.310, 4.420) m`, the marker centre is only 0.720 m forward of the baffle plane. Plan distances are approximately 1.200 m to the left cabinet centre and 1.323 m to the right; the corresponding straight-ahead off-axis angles are approximately 53.1° and 57.0°.
- **DERIVED:** those two sight lines subtend approximately 110.2° at the listener, far wider than a conventional approximately 60° stereo triangle. The 0.123 m path difference corresponds to approximately 0.36 ms and 0.85 dB of spherical distance loss before room effects. These calculations use cabinet-plan centres, not the as-built driver acoustic centres, but the unusually wide angle is too large to be explained by that approximation. Confirm that this near-field, wide-angle arrangement is intentional before finalising listening-axis crossover decisions.

#### 3.4.1 Right-speaker lateral alternatives

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

### 3.5 Resolved checks and remaining model notes

1. The speaker cubes have the intended 100 mm rear and side clearances; this correction is present and internally consistent.
2. The former 32 mm desktop/wall overlap is corrected; the outer desk edge is now exactly `x = 2.550 m`.
3. The listening-room door leaf begins at `z = 0.005 m`; the earlier unintended floor contact is resolved.
4. The modelled roof clearance and opening angle are consistent with the door being stopped by the sloped ceiling region. The model shows near-contact rather than an exact surface intersection, which is appropriate for physical clearance.
5. Object naming is substantially improved: the shelf, speakers, desk, window/frame, listening marker, and shower can now be identified directly. The export still presents the entire architectural shell as the unnamed top-level `SketchUp` mesh and all three door leaves as `Door`. Unique names such as `DOOR_LISTENING`, `DOOR_BEDROOM`, and `DOOR_BATHROOM`, plus separate named air volumes, would remove the remaining ambiguity.
6. The walk-in shower is represented by two full-height perpendicular panels spanning `x = 2.550–3.360 m`, `y = 2.840–3.950 m`, and `z = 0–2.080 m`. Their total modelled area is approximately 3.994 m². This is useful hard-surface geometry when the bathroom door is open; smaller bathroom furniture is unlikely to justify detailed modelling for bass work.

### 3.6 Provisional boundary assumptions

Destructive investigation of the plasterboard build-up is not justified at this stage. Use the following as **PROVISIONAL ASSUMPTIONS**, not verified construction:

- one 12.5 mm painted/skimmed plasterboard layer on timber framing at approximately 400–600 mm centres;
- a roughly 75–100 mm stud or joist cavity, partly or fully filled with mineral wool;
- the sloped and flat ceilings treated similarly, backed by an insulated roof/ceiling void;
- carpet and ordinary underlay over an unknown structural floor, with the bass boundary bracketed between a rigid floor and a more compliant suspended timber floor until the substrate is known.

For low-frequency modelling, run at least two boundary cases: a nearly rigid limit and a more compliant/lossy single-plasterboard-on-studs case. If the predicted conclusion changes materially between them, measurements—not a guessed intermediate coefficient—must decide it. The measured in-room decay and spatial response will be more useful than making holes merely to improve a speculative material model.

## 4. First acoustic screening

### 4.1 Low-frequency length scales

For a rigid rectangular dimension `L`, the first axial standing wave fits half a wavelength, so

```text
f1 = c / (2L)
```

Using `c = 343 m/s` at approximately 20 °C gives the following screening values:

| Geometric scale | First half-wave frequency | Interpretation |
|---|---:|---|
| 4.820 m long axis | 35.6 Hz | Approximate first length-mode scale; harmonics are 71.2 and 106.7 Hz |
| 2.550 m full width | 67.3 Hz | Approximate first width-mode scale in the main room |
| 2.080 m flat height | 82.5 Hz | Approximate first height-mode scale in the central region |
| 1.630 m end-wall height | 105.2 Hz | Local height scale at the two low ends, not a global axial mode |
| 1.600 m narrow doorway-end width | 107.2 Hz | Local width scale in the short L-shaped leg, not a global axial mode |

These are **DERIVED screening values, not solved room eigenfrequencies**. The L-shaped plan, sloped ceiling, doorway boundary, furnishings, and lossy wall constructions perturb and split the rectangular-room modes. They do not guarantee that the nominal 67–82 Hz or 105–107 Hz groupings disappear. Final bass decisions require in-room measurements.

### 4.2 Placement consequences

- Corner placement gives strong low-frequency boundary loading and tends to couple efficiently to modes whose pressure maxima lie at the boundaries. This suits the near-wall design direction, but it increases the need to measure peaks and nulls at the actual seat rather than designing extra passive bass lift.
- The normally open 1.4773 m² doorway strongly couples the listening room to the hallway rather than leaving a sealed 22.63 m³ cavity. The newly modelled spaces can shift resonances and decay times and introduce coupled-cavity behaviour, but their volumes must not simply be added as though the internal walls and apertures did not exist.
- The local adjoining geometry now extends through the former 1.7848 m² terminal opening. Three smaller unclosed boundary apertures remain at the far end/side of the extended hall; their normal states and the effective downstream volume now dominate the remaining geometric uncertainty.
- The baffle plane is nominally 0.400 m from the speaker wall. The simplest rigid-wall image model therefore puts the first rear-wall cancellation near `c/(4d)`, approximately 214 Hz. This is a warning frequency, not a prediction: the real result depends on source position, wall construction, cabinet diffraction, crossover, and listening position.
- The nominal listening marker makes the installation a very wide-angle near-field arrangement unless it has been misinterpreted; Section 3.4 gives the derived geometry. The exact woofer, tweeter, ear, and microphone coordinates are still required to predict floor, ceiling, desk, and shelf-reflection path differences.
- **USER-CONFIRMED INSTALLATION:** the complete floor is carpeted and the walls and ceiling are plasterboard. Carpet will mainly affect mid/high-frequency reflection and decay; it should not be assumed to control the principal bass modes. Plasterboard can provide frequency-dependent low-frequency absorption or transmission; use the two-case provisional bracket in Section 3.6 rather than treating an assumed build-up as quantitatively exact.
- The soft feet provide only about 15 mm clearance above a 2.35 m-wide shelf whose front edge is flush with the baffle planes. Treat the shelf as an acoustic extension/reflection surface as well as a mechanical support, and test it for vibration or buzz at the intended playback level. Installed-baffle measurements should include the final shelf.
- The 3.38 m² in-room desktop is a much larger reflection surface than ordinary desk clutter. Its L shape and position on the `x = 2.550 m` side make early reflections and channel balance asymmetric; the omitted swivel chair and clutter are secondary refinements rather than reasons to defer first measurements.
- The 1.0915 m² single-glazed window replaces a substantial patch of the `x = 0` plasterboard wall. It is likely to differ from the opposite wall in reflection, transmission, and possible pane/frame vibration. For the nominal listening marker, simple image geometry puts the `x = 0` first-reflection points at approximately `y = 4.30 m` for the left speaker and `y = 3.95 m` for the right speaker—both beyond the window's `y = 3.240 m` end. Pane and mullion subdivision is therefore low priority for direct first reflections at this seat. Approximate pane sizes, glass thickness, frame/reveal depth, and normal curtain/blind state are more useful than detailed 3D frame profiles; investigate finer structure if the window rattles or the seat changes materially.
- Do not correct narrow room-mode or speaker-boundary nulls in the passive crossover. Establish the free-field/in-enclosure loudspeaker response first, then assess placement, modest broad DSP, and any future subwoofer from spatially averaged in-room measurements.

### 4.3 Model scope and diminishing returns

The updated model extends through the previously open hallway boundary and now represents approximately 134.88 m³ before contents. It has reached the point where **boundary state matters more than geometric detail**. A practical stopping rule is:

1. Treat the current listening room, two hallway segments, bedroom, bathroom, and further side volume as the exact local geometry.
2. Classify the three remaining boundary openings by their normal state. If they are normally open and very-low-frequency coupled-volume prediction is an explicit goal, represent the next major downstream region as one simplified equivalent volume rather than modelling the whole house room by room. Otherwise use lossy/open terminations and determine their effect from measurements.
3. Stop exact room-by-room modelling at a normally closed door, or after the response becomes insensitive to extending the remote volume. A full-house model is warranted only for very-low-frequency/subwoofer work with several permanently open spaces, not for crossover design or ordinary stereo placement.
4. Include large, hard surfaces near the speakers, listener, or a first-reflection path. Remote small furniture and clutter are below the useful precision of the boundary assumptions.

A useful scale check is `λ = c/f`. A feature generally has to approach roughly `λ/4` before its exact shape strongly affects scattering: approximately 0.86 m at 100 Hz, 0.17 m at 500 Hz, and 43 mm at 2 kHz. At bass frequencies this favours modelling rooms, apertures, the desk, and shower panels—not taps, sanitary ware, or window-frame profiles. At kilohertz frequencies small details matter geometrically, but measured impulse/ETC data is much more efficient and reliable than a full-wave model of the house.

The cheapest sensitivity test is an REW sweep at the listening marker with the bedroom and bathroom doors changed one at a time between their normal and alternate states. Compare magnitude and decay below approximately 200 Hz. If a remote space produces no repeatable material change over the listening-position grid, additional exact geometry for that branch has reached diminishing returns.

## 5. Further information requested

The following would materially improve the room model, in priority order:

1. **Listening geometry:** confirm that the marker centre `(1.200, 3.700, 1.250) m` is the midpoint between the ears; normal head-position range; whether the approximately 110° included speaker angle is intentional; any secondary seats.
2. **Coupling states and levels:** normal open/closed positions of the bedroom and bathroom doors; identities and normal states of the three remaining unclosed boundary openings; descriptive name of the new 29.75 m³ side volume; whether the 0.140 m drop into the extended hallway is intentional.
3. **Shelf:** material, wall attachment, measured deflection/resonance behaviour, and whether it carries other objects. Measure the actual compressed foot height once the cabinets are loaded.
4. **Window:** individual pane divisions and approximate glass thickness; frame material; reveal depth; normal curtain, blind, and opening state. Detailed frame cross-sections are not presently needed.
5. **Boundary build-up:** retain the provisional assumptions in Section 3.6 unless non-destructive evidence becomes available; floor substrate and ceiling/roof-void construction are more useful than destructive plasterboard inspection.
6. **Contents:** desk material and supports; the office chair; ordinary desk clutter; seating, shelving/books, radiators, curtains, and other large reflective or absorptive objects with approximate positions.
7. **Dimensional confidence:** measurement method and approximate uncertainty; whether coordinates represent finished visible surfaces; any skirting, beams, alcoves, or local features omitted from the DAE.
8. **Environmental conditions:** typical temperature and, if available, humidity, for a more precise sound-speed estimate.

For any further DAE revision, preserve separate named closed air-volume references such as `AIR_LISTENING`, `AIR_HALL_NEAR`, `AIR_HALL_FAR`, `AIR_BEDROOM`, `AIR_BATHROOM`, and a descriptive name for the further side volume, with explicit aperture surfaces between them. Keep doors and substantial contents as separate uniquely named components, and preserve the present origin, axes, and unit metadata. This makes coupled-volume calculations possible without requiring the visible architectural shell itself to be watertight.

## 6. Recommended first room measurements

Once the prototype and positions are repeatable:

1. Measure each speaker separately at the main ear position, then both together.
2. Repeat at a small grid around the head position, for example centre plus approximately ±150–250 mm left/right, forward/back, and up/down where practical. This distinguishes a broad balance error from a narrow spatial null.
3. With toe angle and all other conditions fixed, compare the current right-speaker position with 75 mm and 150 mm left shifts; if feasible, also compare the current speakers with the listening point moved 75 mm right. Capture separate-channel impulse/ETC and magnitude data so direct-path symmetry can be distinguished from changed side-wall reflections.
4. Use the fully open listening-room doorway as the baseline state. Repeat diagnostic low-frequency sweeps with the bedroom and bathroom doors changed one at a time; if practical, also compare the listening-room door closed briefly to quantify total adjoining-space coupling.
5. Retain impulse/ETC and decay data as well as magnitude response; record all source, microphone, door, window, and furnishing coordinates with each measurement.
6. Use the measurements to decide placement and broad room correction before attempting any room-specific passive-crossover change.

## 7. Change log

- **2026-08-30:** Inspected canonical DAE `F22A4803...`; confirmed the Tudor bedroom level/doorway features, recorded the extended hallway and further side volume for a total 134.88 m³ represented air, identified three remaining unclosed boundary apertures, and added reversible current/75 mm/150 mm right-speaker and 75 mm listener-shift comparisons.
- **2026-08-30:** Inspected expanded canonical DAE `6292FE6C...`; recorded the bedroom, bathroom, hallway, four coupling apertures, shower panels, and listening marker; added direct-listening geometry, solver-topology caveats, provisional plasterboard assumptions, and a diminishing-returns rule for further modelling.
- **2026-08-29:** Verified revised canonical DAE `4C73FA20...`; confirmed 5 mm door-to-floor clearance, corrected desktop termination, clean doorway-only mesh boundary, and geometry consistent with the door's roof-limited open position.
- **2026-08-29:** Inspected expanded canonical DAE `A766698C...`; verified modelled speaker clearances, shelf, 0.790 × 1.870 m doorway aperture, open door, 1.485 × 0.735 m window, and L-shaped desktop; added object coordinates, displacement estimate, acoustic implications, and mesh/model checks.
- **2026-08-29:** Replaced the now-superseded STL as authority with canonical `3d_models/Listening room.dae`; verified explicit inch units and matching geometry; added confirmed shelf/feet and 100 mm clearances, open-door orientation/state, carpet, plasterboard, and revised acoustic screening/open items.
- **2026-08-29:** Initial parse of the former `3d_models/Listening room.stl`; added geometry, placement convention, first acoustic screening, and open-information list.
