#!/usr/bin/env python3
"""Generate a low-poly black-passivated No. 4 x 3/4 in self-tapper."""

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


MODEL_NAME = (
    "No4x3-4in_2.9x19mm_Pozi_Countersunk_"
    "Self_Tapping_Screw_Black_Passivated"
)
MATERIALS = SCREW_MATERIALS

SPEC = ScrewSpec(
    model_name=MODEL_NAME,
    display_name=(
        "No. 4 x 3/4 in (2.9 x 19 mm) black-passivated Pozi "
        "countersunk self-tapping screw"
    ),
    length=19.0,
    major_diameter=2.90,
    root_diameter=2.08,
    thread_pitch=1.10,
    head_diameter=5.50,
    head_height=1.70,
    countersunk_angle_degrees=80.0,
    drive_reach=1.40,
    drive_depth=1.60,
    point_length=2.60,
    top_thread_run_in=0.75,
    bottom_thread_run_out=0.0,
    radial_segments=24,
    axial_samples_per_pitch=2.00,
    point_segments=6,
)

PREVIEW_CONFIG = {
    "title": "No. 4 x 3/4 in black-passivated Pozi countersunk self-tapper",
    "views": (
        {"label": "Front three-quarter", "direction": (1.25, -1.55, 1.20)},
        {"label": "Rear three-quarter", "direction": (-1.25, -1.55, -1.05)},
    ),
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
