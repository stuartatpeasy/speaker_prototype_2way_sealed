#!/usr/bin/env python3
"""Generate a low-poly black No. 8 x 1 in countersunk self-tapper."""

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


MODEL_NAME = "No8x1in_4.2x25mm_Pozi_Countersunk_Self_Tapping_Screw_Black"
MATERIALS = SCREW_MATERIALS

SPEC = ScrewSpec(
    model_name=MODEL_NAME,
    display_name="No. 8 x 1 in (4.2 x 25 mm) black Pozi countersunk self-tapping screw",
    length=25.0,
    major_diameter=4.20,
    root_diameter=3.10,
    thread_pitch=1.40,
    head_diameter=8.10,
    head_height=2.50,
    countersunk_angle_degrees=80.0,
    drive_reach=2.20,
    drive_depth=2.20,
    point_length=3.70,
    top_thread_run_in=1.00,
    bottom_thread_run_out=0.0,
    radial_segments=24,
    axial_samples_per_pitch=2.00,
    point_segments=6,
)

PREVIEW_CONFIG = {
    "title": "No. 8 x 1 in black Pozi countersunk self-tapping screw",
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
