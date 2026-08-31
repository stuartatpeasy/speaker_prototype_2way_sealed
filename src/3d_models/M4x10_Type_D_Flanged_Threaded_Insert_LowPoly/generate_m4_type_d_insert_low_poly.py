#!/usr/bin/env python3
"""Generate the lightweight SketchUp version of the M4 x 10 Type D insert.

This profile retains the published envelope, flange, hex drive, through bore,
and coarse helical external thread.  It omits only the normally invisible M4
internal helical surface and uses a 24-sided circular approximation.  The
result is intended for repeated component instances in an enclosure model.
"""

from pathlib import Path
import sys

DETAILED_SOURCE = (
    Path(__file__).resolve().parents[1]
    / "M4x10_Type_D_Flanged_Threaded_Insert"
)
sys.path.insert(0, str(DETAILED_SOURCE))
import generate_m4_type_d_insert as detailed


MODEL_NAME = "M4x10_Type_D_Flanged_Threaded_Insert_LowPoly"

PREVIEW_CONFIG = {
    "title": "M4 x 10 mm | Type D insert | low-poly",
    "views": (
        {"label": "Front three-quarter", "direction": (1.35, -1.70, 0.92)},
    ),
    "view_width": 900,
    "view_height": 630,
    "base_colour": (170.0, 179.0, 184.0),
}


def build_low_poly_mesh():
    # A 24-gon retains exact diameters at X/Y and differs from the true flange
    # radius by at most 0.036 mm between vertices.  Eight axial samples per
    # coarse thread pitch preserve the external helical silhouette.
    detailed.RADIAL_SEGMENTS = 24
    detailed.EXTERNAL_Z_STEP = 0.30

    # The female M4 thread is hidden in normal cabinet views and accounted for
    # most of the original triangles.  Retain its 3.24 mm minor-diameter bore.
    detailed.INTERNAL_Z_STEP = 100.0
    detailed.internal_thread_radius = (
        lambda _theta, _z: detailed.M4_INTERNAL_MINOR_DIAMETER / 2.0
    )
    return detailed.build_mesh()


def main() -> None:
    output_dir = Path(__file__).resolve().parents[3] / "3d_models" / MODEL_NAME
    output_dir.mkdir(parents=True, exist_ok=True)
    dae_path = output_dir / f"{MODEL_NAME}.dae"
    mesh = build_low_poly_mesh()
    stats = detailed.validate(mesh)
    if stats["non_manifold_edges"] != 0:
        raise RuntimeError(f"Mesh is not watertight: {stats}")
    if stats["signed_volume_mm3"] <= 0:
        raise RuntimeError(f"Mesh winding is inverted: {stats}")
    detailed.write_dae(mesh, dae_path)
    print(f"Wrote {dae_path}")
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
