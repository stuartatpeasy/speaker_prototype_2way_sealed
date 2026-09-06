# Listening Room — Current Summary

> - **Lifecycle:** ACTIVE ROOM AND INSTALLATION SUMMARY
> - **Owns:** compact current room state, installation context, placement candidates, and routing to detailed authorities
> - **Does not own:** full DAE geometry audit, acoustic-screening derivations, detailed path calculations, or measurement procedure
> - **Current decision:** retain the near-wall shelf installation and compare the current, 75 mm, and 150 mm-left right-speaker positions before choosing a final placement
> - **Next gate:** confirm the listener marker and door/opening states, then run the first controlled placement measurement series
> - **Limitations:** the nominal listener marker is not yet confirmed as the actual ear position; three remote apertures and several boundary constructions remain uncertain
> - **As of:** 2026-09-06

This is the room-specific dashboard for [README.md](../README.md). Detailed geometry, provenance, boundary assumptions, acoustic screening, and DAE history are in [ROOM_GEOMETRY_AND_SCREENING.md](room/ROOM_GEOMETRY_AND_SCREENING.md). Speaker/listener coordinates, reversible placement candidates, direct-path calculations, and the first room-measurement series are in [ROOM_PLACEMENT_AND_MEASUREMENT.md](room/ROOM_PLACEMENT_AND_MEASUREMENT.md).

## 1. Current room and installation snapshot

- **VERIFIED FILE GEOMETRY:** the canonical source is [`3d_models/Listening room.dae`](../3d_models/Listening%20room.dae), a dimensionally usable SketchUp COLLADA model of the listening room and connected spaces. It is not a watertight single solver domain.
- The listening room is an L-shaped 11.056 m² plan, 4.820 m long and up to 2.550 m wide, with a 1.630–2.080 m sloped/flat ceiling and a 22.6315 m³ closed-envelope volume before contents.
- The model represents 134.8812 m³ across the listening room, two hallway portions, bedroom, bathroom, and a further side volume. Three remaining open boundaries mean this total must not be treated as a sealed acoustic volume.
- **USER-CONFIRMED INSTALLATION:** the floor is carpeted; walls and ceiling are plasterboard; both cabinets sit on soft feet on a full-width shelf.
- The 280 × 300 × 430 mm cabinets have nominal 100 mm rear and nearest-side clearances. Their baffles are at `y = 4.420 m`, facing decreasing `y`.
- The nominal listening marker is at `(1.200, 3.700, 1.250) m`, only 0.720 m forward of the baffle plane. Confirmation that this represents the midpoint between the ears remains an **OPEN ITEM**.

## 2. Placement candidates

The current geometry gives an unusually wide approximately 110.2° included angle and a 0.123 m left/right path difference. The reversible right-speaker comparisons are:

| Candidate | Right-speaker centre x | Direct-path consequence | Boundary consequence |
|---|---:|---|---|
| Current DAE | 2.310 m | right path 1.323 m; 0.36 ms later and about 0.85 dB lower | equal nominal 100 mm side clearances |
| 75 mm left | 2.235 m | right path 1.261 m; 0.18 ms later and about 0.43 dB lower | intermediate condition |
| 150 mm left | 2.160 m | equal 1.200 m paths and direct angles | right side clearance increases to 250 mm |
| Listener 75 mm right | listener x = 1.275 m | equal paths with current speaker positions | preserves both 100 mm side clearances |

The 150 mm speaker shift is the **direct-symmetry candidate**, not an automatic optimum. The current placement is the **boundary-symmetry candidate**. Measurement must decide between them.

## 3. Current acoustic consequences

- Near-wall/corner loading supports the intended alignment but makes in-room peak/null measurement essential; do not add passive bass lift from geometric expectation alone.
- The baffle plane is nominally 0.400 m from the speaker wall, giving a simple rigid-wall quarter-wave warning near 214 Hz, not a prediction.
- The shelf, L-shaped desktop, single-glazed window, open doorway, and connected spaces are material acoustic features. Small remote furniture is lower priority than uncertain boundary states.
- Do not correct narrow room-mode or speaker-boundary nulls in the passive crossover. Establish the installed loudspeaker response first, then assess placement, broad DSP, or a future subwoofer from spatial measurements.
- Boundary state now matters more than adding centimetre-level remote geometry. Stop exact modelling at a normally closed door or when measured/predicted response becomes insensitive to extending the model.

## 4. Current next gate and reading routes

1. Confirm the listener marker, normal bedroom/bathroom door states, and identities/states of the three remaining openings.
2. For room-model or DAE work, read [ROOM_GEOMETRY_AND_SCREENING.md](room/ROOM_GEOMETRY_AND_SCREENING.md).
3. For placement selection or room measurements, read [ROOM_PLACEMENT_AND_MEASUREMENT.md](room/ROOM_PLACEMENT_AND_MEASUREMENT.md).
4. Keep installed-baffle crossover measurements distinct from the later listening-position room series.
