#!/usr/bin/env python3
"""Generate a low-poly black M4 x 30 mm countersunk machine screw."""

from pathlib import Path
import sys


SOURCE_ROOT = Path(__file__).resolve().parents[1]
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from common.screw_mesh import (  # noqa: E402
    MATERIALS as SCREW_MATERIALS,
    ScrewSpec,
    build_screw,
    generate,
)


MODEL_NAME = "M4x30_Countersunk_Machine_Screw_Black"
MATERIALS = SCREW_MATERIALS

SPEC = ScrewSpec(
    model_name=MODEL_NAME,
    display_name="M4 x 30 mm black Pozi countersunk machine screw",
    length=30.0,
    major_diameter=4.0,
    root_diameter=3.14,
    thread_pitch=0.70,
    head_diameter=7.50,
    head_height=2.20,
    countersunk_angle_degrees=90.0,
    drive_reach=2.00,
    drive_depth=1.80,
    point_length=0.0,
    top_thread_run_in=0.70,
    bottom_thread_run_out=0.70,
    radial_segments=24,
    axial_samples_per_pitch=1.50,
)

PREVIEW_CONFIG = {
    "title": "M4 x 30 mm black countersunk machine screw",
    "direction": (1.35, -1.70, 0.72),
    "up": (0.0, 0.0, 1.0),
    "size": (900, 720),
    "margin": 0.10,
}


def build_model():
    return build_screw(SPEC)


def main() -> None:
    output_path, stats = generate(SPEC, __file__)
    print(f"Wrote {output_path}")
    print(
        f"Mesh: {stats['vertices']} vertices, {stats['triangles']} triangles; "
        f"dimensions {stats['x_size_mm']:.3f} x "
        f"{stats['y_size_mm']:.3f} x {stats['z_size_mm']:.3f} mm"
    )


if __name__ == "__main__":
    main()
