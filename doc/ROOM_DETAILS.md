# Listening Room — Current Summary

> - **Lifecycle:** ACTIVE ROOM AND INSTALLATION SUMMARY
> - **Owns:** current placement decision and routing to room authorities
> - **Does not own:** canonical geometry, direct-path calculations, acoustic screening, or the measurement procedure
> - **Current decision:** compare the present right-speaker position with reversible 75 mm and 150 mm-left trials before choosing placement
> - **Next gate:** confirm the nominal listener marker and normal door/opening states, then run the first controlled placement series
> - **Limitations:** listener-ear coordinates and three remote opening states remain uncertain; the DAE is not a watertight solver domain
> - **As of:** 2026-09-15

The canonical [`Listening room.dae`](../3d_models/Listening%20room.dae) and its verified dimensions, axes, hash, coupled-space limitations, and boundary assumptions are owned by [Room Geometry and Acoustic Screening](room/ROOM_GEOMETRY_AND_SCREENING.md). Speaker/listener coordinates, direct-path calculations, and the bounded comparison procedure are owned by [Room Placement and Measurement](room/ROOM_PLACEMENT_AND_MEASUREMENT.md).

## 1. Current placement decision

**USER-CONFIRMED INSTALLATION:** the sealed speakers sit on soft feet on a full-width shelf near the rear wall and side boundaries. **DERIVED FROM THE DAE:** the nominal listener marker makes this a wide-angle near-field layout. Moving the right speaker 150 mm left equalises the direct paths but changes its side-wall spacing; the present position keeps equal nominal side-wall clearances. A 75 mm-left speaker trial and, if practical, a 75 mm-right listener trial provide intermediate comparisons. None is a final acoustic optimum without matched measurements.

## 2. Next gate and stop rule

Confirm that the DAE marker represents the seated ear position, record the normal bedroom/bathroom door and three remote opening states, then compare separate-channel impulse/ETC and magnitude responses under fixed conditions. Keep installed-baffle crossover measurements separate from listening-position room evidence. Do not correct narrow room or boundary nulls in the passive crossover; assess placement and broad room treatment from spatial measurements. Extend remote geometry only if boundary-state sensitivity or a decision-relevant measurement justifies it.
