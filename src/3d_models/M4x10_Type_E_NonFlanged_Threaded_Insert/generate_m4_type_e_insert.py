#!/usr/bin/env python3
"""Generate a low-poly M4 x 10 mm Type E threaded insert.

The Type E shares the Type D insert's published thread envelope and hex drive
but omits its sealing flange, allowing the insert to be driven below the wood
surface. The visible coarse external helix is retained while the normally
hidden M4 female thread is represented by its smooth minor-diameter bore.
"""

from __future__ import annotations

from math import cos, hypot, pi
from pathlib import Path
import sys


DETAILED_SOURCE = (
    Path(__file__).resolve().parents[1]
    / "M4x10_Type_D_Flanged_Threaded_Insert"
)
sys.path.insert(0, str(DETAILED_SOURCE))
import generate_m4_type_d_insert as shared


MODEL_NAME = "M4x10_Type_E_NonFlanged_Threaded_Insert"
DISPLAY_NAME = "M4 x 10 mm Type E non-flanged threaded insert"

# Manufacturer-published dimensions, millimetres.
LENGTH = 10.0
MAXIMUM_THREAD_DIAMETER = 8.5  # D1
BODY_ROOT_DIAMETER = 5.5       # D2
HEX_ACROSS_FLATS = 4.0         # K
INTERNAL_THREAD_MAJOR = 4.0
INTERNAL_THREAD_PITCH = 0.7

# Representative production details not dimensioned in the product table.
EXTERNAL_THREAD_PITCH = 2.40
EXTERNAL_RUNOUT = 0.68
HEX_STRAIGHT_DEPTH = 1.60
HEX_TRANSITION_END = 2.15
M4_INTERNAL_MINOR_DIAMETER = 3.24

# Matches the earlier SketchUp-optimised Type D model.
RADIAL_SEGMENTS = 24
EXTERNAL_Z_STEP = 0.30

PREVIEW_CONFIG = {
    "title": "M4 x 10 mm | Type E insert | low-poly",
    "views": (
        {"label": "Front three-quarter", "direction": (1.35, -1.70, 0.92)},
    ),
    "view_width": 900,
    "view_height": 630,
    "base_colour": (170.0, 179.0, 184.0),
}


def configure_shared_geometry() -> None:
    shared.MODEL_NAME = MODEL_NAME
    shared.DISPLAY_NAME = DISPLAY_NAME
    shared.LENGTH = LENGTH
    shared.BODY_ROOT_DIAMETER = BODY_ROOT_DIAMETER
    shared.HEX_ACROSS_FLATS = HEX_ACROSS_FLATS
    shared.INTERNAL_THREAD_MAJOR = INTERNAL_THREAD_MAJOR
    shared.INTERNAL_THREAD_PITCH = INTERNAL_THREAD_PITCH
    shared.EXTERNAL_THREAD_PITCH = EXTERNAL_THREAD_PITCH
    shared.EXTERNAL_RUNOUT = EXTERNAL_RUNOUT
    shared.HEX_STRAIGHT_DEPTH = HEX_STRAIGHT_DEPTH
    shared.HEX_TRANSITION_END = HEX_TRANSITION_END
    shared.M4_INTERNAL_MINOR_DIAMETER = M4_INTERNAL_MINOR_DIAMETER
    shared.RADIAL_SEGMENTS = RADIAL_SEGMENTS


def external_radius(theta: float, z: float) -> float:
    """Right-hand coarse helix without the Type D flange or flange blend."""
    depth = -z
    root_radius = BODY_ROOT_DIAMETER / 2.0
    crest_radius = MAXIMUM_THREAD_DIAMETER / 2.0
    phase = depth / EXTERNAL_THREAD_PITCH + theta / (2.0 * pi)
    thread = shared.triangle_wave(phase)
    remaining = LENGTH - depth
    bottom_runout = min(1.0, max(0.0, remaining / EXTERNAL_RUNOUT))
    return root_radius + (crest_radius - root_radius) * thread * bottom_runout


def top_external_radius(theta: float, _z: float) -> float:
    """Balanced four-lobed top contour shown in the manufacturer drawing."""
    root_radius = BODY_ROOT_DIAMETER / 2.0
    crest_radius = MAXIMUM_THREAD_DIAMETER / 2.0
    phase = 4.0 * theta / (2.0 * pi) + 0.5
    lobe = shared.triangle_wave(phase, half_width=0.48)
    return root_radius + (crest_radius - root_radius) * lobe


def smooth_bore_radius(_theta: float, _z: float) -> float:
    return M4_INTERNAL_MINOR_DIAMETER / 2.0


def build_mesh():
    configure_shared_geometry()
    mesh = shared.Mesh()

    # Exact 0.3 mm levels also include every 0.6 mm phase-alignment plane,
    # guaranteeing exact ±X/±Y D1 crest extents with one compact sampling grid.
    outer_z = [
        -(EXTERNAL_Z_STEP * index)
        for index in range(int(LENGTH / EXTERNAL_Z_STEP) + 1)
    ]
    if outer_z[-1] > -LENGTH:
        outer_z.append(-LENGTH)
    outer_rings = [
        shared.make_ring(
            mesh,
            z,
            top_external_radius if abs(z) < 1e-9 else external_radius,
        )
        for z in outer_z
    ]
    shared.connect_rings(
        mesh,
        outer_rings,
        inward=False,
        group_fn=lambda _layer, _index: "exterior",
    )

    hex_z = [0.0, -HEX_STRAIGHT_DEPTH]
    hex_rings = [
        shared.make_ring(mesh, z, lambda theta, _z: shared.hex_radius(theta))
        for z in hex_z
    ]

    def hex_group(_layer: int, angular_index: int) -> str:
        theta_mid = 2.0 * pi * (angular_index + 0.5) / RADIAL_SEGMENTS
        side = int(((theta_mid + pi / 6.0) % (2.0 * pi)) / (pi / 3.0))
        return f"hex_wall_{side}"

    shared.connect_rings(mesh, hex_rings, inward=True, group_fn=hex_group)

    transition_bottom = shared.make_ring(
        mesh, -HEX_TRANSITION_END, smooth_bore_radius
    )
    shared.connect_rings(
        mesh,
        [hex_rings[-1], transition_bottom],
        inward=True,
        group_fn=lambda _layer, _index: "drive_transition",
    )
    bore_bottom = shared.make_ring(mesh, -LENGTH, smooth_bore_radius)
    shared.connect_rings(
        mesh,
        [transition_bottom, bore_bottom],
        inward=True,
        group_fn=lambda _layer, _index: "smooth_m4_bore",
    )

    shared.add_top_annulus(mesh, outer_rings[0], hex_rings[0])
    shared.add_bottom_annulus(mesh, outer_rings[-1], bore_bottom)
    return mesh


def validate(mesh):
    stats = shared.validate(mesh)
    radii = [hypot(x, y) for x, y, _z in mesh.vertices]
    top_radii = [hypot(x, y) for x, y, z in mesh.vertices if abs(z) < 1e-9]
    stats.update({
        "maximum_thread_diameter_mm": 2.0 * max(radii),
        "top_outer_maximum_radius_mm": max(top_radii),
        "radial_chord_error_at_d1_mm": (
            (MAXIMUM_THREAD_DIAMETER / 2.0)
            * (1.0 - cos(pi / RADIAL_SEGMENTS))
        ),
    })
    return stats


def main() -> None:
    output_dir = Path(__file__).resolve().parents[3] / "3d_models" / MODEL_NAME
    output_dir.mkdir(parents=True, exist_ok=True)
    dae_path = output_dir / f"{MODEL_NAME}.dae"

    mesh = build_mesh()
    stats = validate(mesh)
    expected = {
        "non_manifold_edges": 0,
        "x_size_mm": MAXIMUM_THREAD_DIAMETER,
        "y_size_mm": MAXIMUM_THREAD_DIAMETER,
        "z_size_mm": LENGTH,
        "maximum_thread_diameter_mm": MAXIMUM_THREAD_DIAMETER,
    }
    if stats["signed_volume_mm3"] <= 0:
        raise RuntimeError(f"Mesh winding is inverted: {stats}")
    for key, value in expected.items():
        if abs(float(stats[key]) - value) > 1e-6:
            raise RuntimeError(f"{key} is {stats[key]}, expected {value}")

    configure_shared_geometry()
    shared.write_dae(mesh, dae_path)
    print(f"Wrote {dae_path}")
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
