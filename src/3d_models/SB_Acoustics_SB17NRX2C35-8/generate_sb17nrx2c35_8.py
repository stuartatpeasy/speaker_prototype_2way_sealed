#!/usr/bin/env python3
"""Generate a coloured, SketchUp-friendly SB Acoustics SB17NRX2C35-8.

The model is intended for enclosure layout and realistic visualisation rather
than manufacturing the driver itself. Published envelope and mounting
dimensions are reproduced exactly; undocumented construction details are
estimated from the manufacturer's photographs and public product imagery.

Coordinate convention:
  * millimetres
  * Z_UP
  * origin at the acoustic axis on the rear mounting face of the front flange
  * the cone projects towards +Z
  * the motor extends towards -Z
"""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
from math import cos, pi, sin, sqrt
from pathlib import Path
import xml.etree.ElementTree as ET


MODEL_NAME = "SB_Acoustics_SB17NRX2C35-8"

# Manufacturer-published dimensions, mm.
FRAME_DIAMETER = 171.0
MOUNTING_PCD = 159.0
MOUNT_RECESS_DIAMETER = 8.5
MOUNT_THROUGH_DIAMETER = 4.3
BASKET_ENVELOPE_DIAMETER = 144.9
MAGNET_DIAMETER = 100.0
FLANGE_THICKNESS = 6.5
MOUNTING_DEPTH = 75.0
OVERALL_DEPTH = 85.9
FRONT_PROJECTION = OVERALL_DEPTH - MOUNTING_DEPTH  # 10.9
VOICE_COIL_DIAMETER = 35.5
VOICE_COIL_HEIGHT = 16.0

# A 64-sided main circumference is smooth in SketchUp while remaining light.
MAIN_SEGMENTS = 64
DIAPHRAGM_SEGMENTS = 48
MOTOR_SEGMENTS = 48
SPIDER_SEGMENTS = 32
SMALL_SEGMENTS = 24

PREVIEW_CONFIG = {
    "title": "SB Acoustics SB17NRX2C35-8 - SketchUp model QA",
    "views": (
        {"label": "Front three-quarter", "direction": (1.45, -1.75, 1.10)},
        {"label": "Rear three-quarter", "direction": (-1.35, -1.60, -1.10)},
    ),
    "view_height": 670,
}


MATERIALS = {
    "frame_black": {
        "diffuse": (0.055, 0.062, 0.064, 1.0),
        "specular": (0.12, 0.13, 0.13, 1.0),
        "shininess": 10.0,
    },
    "surround_rubber": {
        "diffuse": (0.030, 0.033, 0.033, 1.0),
        "specular": (0.055, 0.060, 0.060, 1.0),
        "shininess": 5.0,
    },
    "norex_cone": {
        "diffuse": (0.105, 0.112, 0.108, 1.0),
        "specular": (0.035, 0.038, 0.037, 1.0),
        "shininess": 3.0,
    },
    "dustcap": {
        "diffuse": (0.075, 0.080, 0.078, 1.0),
        "specular": (0.060, 0.064, 0.063, 1.0),
        "shininess": 7.0,
    },
    "ferrite": {
        "diffuse": (0.255, 0.265, 0.270, 1.0),
        "specular": (0.075, 0.080, 0.082, 1.0),
        "shininess": 5.0,
    },
    "zinc_plate": {
        "diffuse": (0.620, 0.645, 0.655, 1.0),
        "specular": (0.350, 0.370, 0.380, 1.0),
        "shininess": 24.0,
    },
    "spider_cloth": {
        "diffuse": (0.480, 0.315, 0.120, 1.0),
        "specular": (0.055, 0.040, 0.015, 1.0),
        "shininess": 3.0,
    },
    "copper_coil": {
        "diffuse": (0.610, 0.310, 0.095, 1.0),
        "specular": (0.270, 0.130, 0.035, 1.0),
        "shininess": 16.0,
    },
    "fiberglass": {
        "diffuse": (0.410, 0.350, 0.235, 1.0),
        "specular": (0.045, 0.040, 0.025, 1.0),
        "shininess": 4.0,
    },
    "terminal_board": {
        "diffuse": (0.105, 0.075, 0.045, 1.0),
        "specular": (0.035, 0.025, 0.015, 1.0),
        "shininess": 3.0,
    },
    "brass": {
        "diffuse": (0.690, 0.485, 0.135, 1.0),
        "specular": (0.320, 0.235, 0.070, 1.0),
        "shininess": 18.0,
    },
    "silver_wire": {
        "diffuse": (0.710, 0.720, 0.710, 1.0),
        "specular": (0.410, 0.420, 0.410, 1.0),
        "shininess": 25.0,
    },
    "recess": {
        "diffuse": (0.090, 0.096, 0.097, 1.0),
        "specular": (0.060, 0.064, 0.065, 1.0),
        "shininess": 6.0,
    },
    "void": {
        "diffuse": (0.008, 0.009, 0.009, 1.0),
        "specular": (0.0, 0.0, 0.0, 1.0),
        "shininess": 1.0,
    },
    "label_dark": {
        "diffuse": (0.080, 0.085, 0.086, 1.0),
        "specular": (0.025, 0.026, 0.026, 1.0),
        "shininess": 2.0,
    },
    "label_light": {
        "diffuse": (0.770, 0.770, 0.730, 1.0),
        "specular": (0.080, 0.080, 0.070, 1.0),
        "shininess": 4.0,
    },
    "brand_red": {
        "diffuse": (0.720, 0.035, 0.035, 1.0),
        "specular": (0.060, 0.005, 0.005, 1.0),
        "shininess": 3.0,
    },
}


def vec_add(a, b):
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]


def vec_sub(a, b):
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def vec_scale(a, scalar):
    return a[0] * scalar, a[1] * scalar, a[2] * scalar


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def length(a):
    return sqrt(dot(a, a))


def unit(a):
    magnitude = length(a)
    if magnitude == 0:
        return 0.0, 0.0, 1.0
    return vec_scale(a, 1.0 / magnitude)


def triangle_normal(a, b, c):
    return unit(cross(vec_sub(b, a), vec_sub(c, a)))


class Mesh:
    def __init__(self) -> None:
        self.vertices: list[tuple[float, float, float]] = []
        self.faces: list[tuple[int, int, int]] = []
        self.materials: list[str] = []
        self.groups: list[str] = []

    def vertex(self, xyz) -> int:
        self.vertices.append(tuple(float(value) for value in xyz))
        return len(self.vertices) - 1

    def face(self, a: int, b: int, c: int, material: str, group: str) -> None:
        if len({a, b, c}) < 3:
            return
        self.faces.append((a, b, c))
        self.materials.append(material)
        self.groups.append(group)

    def quad(self, a, b, c, d, material, group) -> None:
        self.face(a, b, c, material, group)
        self.face(a, c, d, material, group)

    def oriented_face(self, a, b, c, material, group, solid_center) -> None:
        points = [self.vertices[index] for index in (a, b, c)]
        centroid = tuple(sum(point[axis] for point in points) / 3.0 for axis in range(3))
        normal = triangle_normal(*points)
        if dot(normal, vec_sub(centroid, solid_center)) < 0:
            b, c = c, b
        self.face(a, b, c, material, group)

    def oriented_quad(self, a, b, c, d, material, group, solid_center) -> None:
        self.oriented_face(a, b, c, material, group, solid_center)
        self.oriented_face(a, c, d, material, group, solid_center)


def add_revolved(
    mesh: Mesh,
    profile: list[tuple[float, float]],
    material: str,
    group: str,
    segments: int = MAIN_SEGMENTS,
    smooth_profile: bool = True,
) -> None:
    """Revolve a counter-clockwise closed profile in the r-z plane."""
    rings: list[list[int]] = []
    for radius, z in profile:
        if abs(radius) < 1e-9:
            pole = mesh.vertex((0.0, 0.0, z))
            rings.append([pole] * segments)
            continue
        ring = []
        for index in range(segments):
            angle = 2.0 * pi * index / segments
            ring.append(mesh.vertex((radius * cos(angle), radius * sin(angle), z)))
        rings.append(ring)

    for profile_index in range(len(profile)):
        next_profile = (profile_index + 1) % len(profile)
        ring_a = rings[profile_index]
        ring_b = rings[next_profile]
        segment_group = group if smooth_profile else f"{group}_profile_{profile_index}"
        radius_a = profile[profile_index][0]
        radius_b = profile[next_profile][0]
        for angular_index in range(segments):
            angular_next = (angular_index + 1) % segments
            a = ring_a[angular_index]
            b = ring_a[angular_next]
            c = ring_b[angular_index]
            d = ring_b[angular_next]
            if radius_a < 1e-9:
                mesh.face(a, d, c, material, segment_group)
            elif radius_b < 1e-9:
                mesh.face(a, b, c, material, segment_group)
            else:
                mesh.quad(a, b, d, c, material, segment_group)


def add_open_disc(
    mesh: Mesh,
    center_xy: tuple[float, float],
    radius: float,
    z: float,
    material: str,
    group: str,
    segments: int = SMALL_SEGMENTS,
    normal_positive_z: bool = True,
) -> None:
    center = mesh.vertex((center_xy[0], center_xy[1], z))
    ring = []
    for index in range(segments):
        angle = 2.0 * pi * index / segments
        ring.append(mesh.vertex((
            center_xy[0] + radius * cos(angle),
            center_xy[1] + radius * sin(angle),
            z,
        )))
    for index in range(segments):
        nxt = (index + 1) % segments
        if normal_positive_z:
            mesh.face(center, ring[index], ring[nxt], material, group)
        else:
            mesh.face(center, ring[nxt], ring[index], material, group)


def add_open_annulus(
    mesh: Mesh,
    center_xy: tuple[float, float],
    outer_radius: float,
    inner_radius: float,
    z: float,
    material: str,
    group: str,
    segments: int = SMALL_SEGMENTS,
    normal_positive_z: bool = True,
) -> None:
    outer = []
    inner = []
    for index in range(segments):
        angle = 2.0 * pi * index / segments
        ca, sa = cos(angle), sin(angle)
        outer.append(mesh.vertex((
            center_xy[0] + outer_radius * ca,
            center_xy[1] + outer_radius * sa,
            z,
        )))
        inner.append(mesh.vertex((
            center_xy[0] + inner_radius * ca,
            center_xy[1] + inner_radius * sa,
            z,
        )))
    for index in range(segments):
        nxt = (index + 1) % segments
        if normal_positive_z:
            mesh.quad(outer[index], outer[nxt], inner[nxt], inner[index],
                      material, group)
        else:
            mesh.quad(outer[index], inner[index], inner[nxt], outer[nxt],
                      material, group)


def add_oriented_box(
    mesh: Mesh,
    center,
    axis_u,
    axis_v,
    axis_w,
    size_u,
    size_v,
    size_w,
    material,
    group,
) -> None:
    u = vec_scale(unit(axis_u), size_u / 2.0)
    v = vec_scale(unit(axis_v), size_v / 2.0)
    w = vec_scale(unit(axis_w), size_w / 2.0)
    vertices = []
    for su, sv, sw in (
        (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
        (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
    ):
        point = vec_add(center, vec_add(vec_scale(u, su),
                        vec_add(vec_scale(v, sv), vec_scale(w, sw))))
        vertices.append(mesh.vertex(point))
    for quad in (
        (0, 3, 2, 1), (4, 5, 6, 7),
        (0, 1, 5, 4), (1, 2, 6, 5),
        (2, 3, 7, 6), (3, 0, 4, 7),
    ):
        mesh.oriented_quad(*[vertices[index] for index in quad],
                           material, group, center)


def add_tapered_spoke(
    mesh: Mesh,
    angle: float,
    sections: list[tuple[float, float, float, float]],
    material: str,
    group: str,
) -> None:
    """Add a solid beam; sections are r, z, tangential width, radial thickness."""
    radial = (cos(angle), sin(angle), 0.0)
    tangential = (-sin(angle), cos(angle), 0.0)
    rings = []
    all_points = []
    for radius, z, width, radial_thickness in sections:
        center = (radius * radial[0], radius * radial[1], z)
        radial_half = vec_scale(radial, radial_thickness / 2.0)
        tangent_half = vec_scale(tangential, width / 2.0)
        points = [
            vec_add(center, vec_add(radial_half, tangent_half)),
            vec_add(center, vec_add(vec_scale(radial_half, -1.0), tangent_half)),
            vec_add(center, vec_add(vec_scale(radial_half, -1.0),
                                    vec_scale(tangent_half, -1.0))),
            vec_add(center, vec_add(radial_half, vec_scale(tangent_half, -1.0))),
        ]
        ring = [mesh.vertex(point) for point in points]
        rings.append(ring)
        all_points.extend(points)
    solid_center = tuple(
        sum(point[axis] for point in all_points) / len(all_points)
        for axis in range(3)
    )
    for section_index in range(len(rings) - 1):
        current = rings[section_index]
        nxt = rings[section_index + 1]
        for side in range(4):
            side_next = (side + 1) % 4
            mesh.oriented_quad(current[side], current[side_next],
                               nxt[side_next], nxt[side],
                               material, group, solid_center)
    mesh.oriented_quad(rings[0][0], rings[0][1], rings[0][2], rings[0][3],
                       material, group, solid_center)
    mesh.oriented_quad(rings[-1][0], rings[-1][3], rings[-1][2], rings[-1][1],
                       material, group, solid_center)


def add_cylinder_between(
    mesh: Mesh,
    start,
    end,
    radius,
    material,
    group,
    segments=10,
) -> None:
    axis = unit(vec_sub(end, start))
    helper = (0.0, 0.0, 1.0)
    if abs(dot(axis, helper)) > 0.9:
        helper = (1.0, 0.0, 0.0)
    basis_u = unit(cross(helper, axis))
    basis_v = cross(axis, basis_u)
    start_ring = []
    end_ring = []
    for index in range(segments):
        angle = 2.0 * pi * index / segments
        offset = vec_add(vec_scale(basis_u, radius * cos(angle)),
                         vec_scale(basis_v, radius * sin(angle)))
        start_ring.append(mesh.vertex(vec_add(start, offset)))
        end_ring.append(mesh.vertex(vec_add(end, offset)))
    for index in range(segments):
        nxt = (index + 1) % segments
        mesh.quad(start_ring[index], start_ring[nxt],
                  end_ring[nxt], end_ring[index], material, group)
    start_center = mesh.vertex(start)
    end_center = mesh.vertex(end)
    for index in range(segments):
        nxt = (index + 1) % segments
        mesh.face(start_center, start_ring[nxt], start_ring[index], material, group)
        mesh.face(end_center, end_ring[index], end_ring[nxt], material, group)


def build_model() -> Mesh:
    mesh = Mesh()

    # Cast front flange. The outermost rounded edge reaches the exact Ø171 mm.
    add_revolved(
        mesh,
        [
            (84.8, FLANGE_THICKNESS),
            (73.2, FLANGE_THICKNESS),
            (72.45, 5.35),
            (72.45, 0.0),
            (84.8, 0.0),
            (85.5, 0.70),
            (85.5, 5.80),
        ],
        "frame_black", "front_flange", MAIN_SEGMENTS, smooth_profile=False,
    )

    # Underside basket rim, constrained by the published Ø144.9 envelope.
    add_revolved(
        mesh,
        [(72.45, 0.0), (67.0, 0.0), (66.2, -5.6), (70.2, -6.5), (72.45, -4.8)],
        "frame_black", "basket_outer_ring", MAIN_SEGMENTS, smooth_profile=False,
    )

    # Rubber half-roll surround. Its crest sets the exact +10.9 mm front limit.
    add_revolved(
        mesh,
        [
            (73.0, 5.45),
            (71.4, 6.75),
            (68.2, 9.10),
            (64.0, FRONT_PROJECTION),
            (60.0, 8.95),
            (57.2, 6.20),
            (57.2, 5.10),
            (60.2, 7.75),
            (64.0, 9.65),
            (68.0, 8.05),
            (71.3, 5.85),
            (73.0, 4.85),
        ],
        "surround_rubber", "surround", DIAPHRAGM_SEGMENTS, smooth_profile=True,
    )

    # Natural-fibre cone.
    add_revolved(
        mesh,
        [
            (58.0, 6.15),
            (49.0, 5.55),
            (39.0, 4.65),
            (27.0, 3.25),
            (27.0, 2.55),
            (39.0, 3.90),
            (49.0, 4.85),
            (58.0, 5.35),
        ],
        "norex_cone", "cone", DIAPHRAGM_SEGMENTS, smooth_profile=True,
    )

    # Convex dust cap.
    add_revolved(
        mesh,
        [
            (27.2, 3.30),
            (24.0, 4.05),
            (18.5, 6.45),
            (10.0, 8.95),
            (0.0, 10.15),
            (0.0, 9.25),
            (10.0, 8.05),
            (18.5, 5.65),
            (24.0, 3.50),
            (27.2, 2.65),
        ],
        "dustcap", "dustcap", DIAPHRAGM_SEGMENTS, smooth_profile=True,
    )

    # Fibreglass former and the published 35.5 x 16 mm voice-coil winding.
    add_revolved(
        mesh,
        [(17.0, -11.0), (16.25, -11.0), (16.25, -44.0), (17.0, -44.0)],
        "fiberglass", "voice_coil_former", SMALL_SEGMENTS, smooth_profile=False,
    )
    add_revolved(
        mesh,
        [
            (VOICE_COIL_DIAMETER / 2.0, -24.0),
            (17.05, -24.0),
            (17.05, -24.0 - VOICE_COIL_HEIGHT),
            (VOICE_COIL_DIAMETER / 2.0, -24.0 - VOICE_COIL_HEIGHT),
        ],
        "copper_coil", "voice_coil_winding", SMALL_SEGMENTS, smooth_profile=False,
    )

    # Corrugated cloth spider, visible through the open cast basket.
    spider_top = []
    radii = [45.0, 41.0, 37.0, 33.0, 29.0, 25.0, 21.0, 18.7]
    for index, radius in enumerate(radii):
        spider_top.append((radius, -28.7 + (0.85 if index % 2 else -0.35)))
    spider_bottom = [(radius, z - 0.9) for radius, z in reversed(spider_top)]
    add_revolved(
        mesh, spider_top + spider_bottom,
        "spider_cloth", "spider", SPIDER_SEGMENTS, smooth_profile=True,
    )

    # Eight broad cast-aluminium basket spokes.
    spoke_sections = [
        (68.0, -3.2, 8.5, 4.2),
        (63.0, -13.0, 8.0, 4.3),
        (55.0, -29.0, 7.0, 4.2),
        (46.0, -47.0, 6.0, 4.0),
    ]
    for index in range(8):
        angle = 2.0 * pi * index / 8.0
        add_tapered_spoke(
            mesh, angle, spoke_sections,
            "frame_black", f"basket_spoke_{index}",
        )

    # Lower basket throat and motor assembly.
    add_revolved(
        mesh,
        [(47.0, -45.0), (38.0, -45.0), (38.0, -52.0), (47.0, -52.0)],
        "frame_black", "basket_throat", MOTOR_SEGMENTS, smooth_profile=False,
    )
    add_revolved(
        mesh,
        [(48.5, -49.0), (18.2, -49.0), (18.2, -54.0), (48.5, -54.0)],
        "zinc_plate", "motor_top_plate", MOTOR_SEGMENTS, smooth_profile=False,
    )
    add_revolved(
        mesh,
        [(MAGNET_DIAMETER / 2.0, -54.0), (11.5, -54.0),
         (11.5, -69.8), (MAGNET_DIAMETER / 2.0, -69.8)],
        "ferrite", "ferrite_magnet", MOTOR_SEGMENTS, smooth_profile=False,
    )
    add_revolved(
        mesh,
        [(48.5, -69.8), (10.8, -69.8), (10.8, -74.8), (48.5, -74.8)],
        "zinc_plate", "rear_plate", MOTOR_SEGMENTS, smooth_profile=False,
    )

    # Rear label and pole vent. The rear surfaces sit at the exact -75 mm limit.
    add_open_annulus(
        mesh, (0.0, 0.0), 48.5, 41.0, -74.96,
        "zinc_plate", "rear_silver_ring", MOTOR_SEGMENTS, normal_positive_z=False,
    )
    add_open_annulus(
        mesh, (0.0, 0.0), 41.0, 10.8, -74.97,
        "label_dark", "rear_label", MOTOR_SEGMENTS, normal_positive_z=False,
    )
    add_open_disc(
        mesh, (0.0, 0.0), 10.8, -75.0,
        "void", "pole_vent", SMALL_SEGMENTS, normal_positive_z=False,
    )
    # Stepped mounting recesses on the exact Ø159 mm pitch circle.
    for index in range(4):
        angle = pi / 4.0 + index * pi / 2.0
        center = (
            (MOUNTING_PCD / 2.0) * cos(angle),
            (MOUNTING_PCD / 2.0) * sin(angle),
        )
        add_open_annulus(
            mesh, center,
            MOUNT_RECESS_DIAMETER / 2.0,
            MOUNT_THROUGH_DIAMETER / 2.0,
            FLANGE_THICKNESS + 0.025,
            "recess", f"mount_recess_{index}", 20,
        )
        add_open_disc(
            mesh, center, MOUNT_THROUGH_DIAMETER / 2.0,
            FLANGE_THICKNESS + 0.030,
            "void", f"mount_hole_{index}", 20,
        )

    # Terminal board and two brass tabs at the six-o'clock position.
    radial = (0.0, -1.0, 0.0)
    tangential = (1.0, 0.0, 0.0)
    vertical = (0.0, 0.0, 1.0)
    add_oriented_box(
        mesh, (0.0, -47.7, -43.5),
        tangential, radial, vertical,
        28.0, 3.0, 5.5, "terminal_board", "terminal_board",
    )
    for index, x in enumerate((-7.3, 7.3)):
        add_oriented_box(
            mesh, (x, -50.0, -43.8),
            tangential, radial, vertical,
            4.3, 8.0, 1.1, "brass", f"terminal_tab_{index}",
        )
        add_oriented_box(
            mesh, (x, -48.9, -40.8),
            tangential, radial, vertical,
            3.0, 2.0, 5.5, "brass", f"terminal_post_{index}",
        )

    # Silver tinsel leads sweeping from the terminals towards the cone.
    add_cylinder_between(
        mesh, (-7.3, -48.0, -40.2), (-10.5, -36.0, -19.0),
        0.45, "silver_wire", "lead_wire_left", 8,
    )
    add_cylinder_between(
        mesh, (7.3, -48.0, -40.2), (10.5, -36.0, -19.0),
        0.45, "silver_wire", "lead_wire_right", 8,
    )

    # Side barcode label on the ferrite ring.
    add_oriented_box(
        mesh, (0.0, -50.10, -62.0),
        tangential, radial, vertical,
        28.0, 0.35, 7.5, "label_light", "magnet_barcode_label",
    )
    for index in range(7):
        x = -9.0 + index * 3.0
        width = 0.45 if index % 2 else 0.8
        add_oriented_box(
            mesh, (x, -50.31, -62.0),
            tangential, radial, vertical,
            width, 0.08, 5.0, "label_dark", f"barcode_{index}",
        )

    return mesh


def calculate_smooth_normals(mesh: Mesh):
    accum = defaultdict(lambda: [0.0, 0.0, 0.0])
    for face, group in zip(mesh.faces, mesh.groups):
        normal = triangle_normal(*(mesh.vertices[index] for index in face))
        for vertex_index in face:
            key = (vertex_index, group)
            accum[key][0] += normal[0]
            accum[key][1] += normal[1]
            accum[key][2] += normal[2]
    return {key: unit(value) for key, value in accum.items()}


def write_dae(mesh: Mesh, path: Path) -> None:
    smooth_normals = calculate_smooth_normals(mesh)
    remap = {}
    dae_positions = []
    dae_normals = []
    material_faces = defaultdict(list)
    for face, material, group in zip(mesh.faces, mesh.materials, mesh.groups):
        remapped = []
        for vertex_index in face:
            key = (vertex_index, group)
            if key not in remap:
                remap[key] = len(dae_positions)
                dae_positions.append(mesh.vertices[vertex_index])
                dae_normals.append(smooth_normals[key])
            remapped.append(remap[key])
        material_faces[material].append(tuple(remapped))

    ns = "http://www.collada.org/2005/11/COLLADASchema"
    ET.register_namespace("", ns)
    q = lambda tag: f"{{{ns}}}{tag}"

    root = ET.Element(q("COLLADA"), version="1.4.1")
    asset = ET.SubElement(root, q("asset"))
    contributor = ET.SubElement(asset, q("contributor"))
    ET.SubElement(contributor, q("authoring_tool")).text = (
        "Codex dimension-controlled loudspeaker mesh generator"
    )
    stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    ET.SubElement(asset, q("created")).text = stamp
    ET.SubElement(asset, q("modified")).text = stamp
    ET.SubElement(asset, q("unit"), meter="0.001", name="millimeter")
    ET.SubElement(asset, q("up_axis")).text = "Z_UP"

    effects = ET.SubElement(root, q("library_effects"))
    materials_xml = ET.SubElement(root, q("library_materials"))
    for name, definition in MATERIALS.items():
        effect = ET.SubElement(effects, q("effect"), id=f"{name}_effect")
        profile = ET.SubElement(effect, q("profile_COMMON"))
        technique = ET.SubElement(profile, q("technique"), sid="common")
        phong = ET.SubElement(technique, q("phong"))
        ambient = ET.SubElement(phong, q("ambient"))
        ET.SubElement(ambient, q("color")).text = "0.08 0.08 0.08 1"
        diffuse = ET.SubElement(phong, q("diffuse"))
        ET.SubElement(diffuse, q("color")).text = " ".join(
            f"{component:.4g}" for component in definition["diffuse"]
        )
        specular = ET.SubElement(phong, q("specular"))
        ET.SubElement(specular, q("color")).text = " ".join(
            f"{component:.4g}" for component in definition["specular"]
        )
        shininess = ET.SubElement(phong, q("shininess"))
        ET.SubElement(shininess, q("float")).text = str(definition["shininess"])
        extra = ET.SubElement(effect, q("extra"))
        google = ET.SubElement(extra, q("technique"), profile="GOOGLEEARTH")
        ET.SubElement(google, q("double_sided")).text = "1"

        material = ET.SubElement(
            materials_xml, q("material"), id=f"{name}_material",
            name=name.replace("_", " ").title(),
        )
        ET.SubElement(material, q("instance_effect"), url=f"#{name}_effect")

    geometries = ET.SubElement(root, q("library_geometries"))
    geometry = ET.SubElement(
        geometries, q("geometry"), id="sb17_geometry",
        name="SB Acoustics SB17NRX2C35-8",
    )
    xml_mesh = ET.SubElement(geometry, q("mesh"))

    def add_source(source_id, array_id, values, params):
        source = ET.SubElement(xml_mesh, q("source"), id=source_id)
        flat = [component for value in values for component in value]
        array = ET.SubElement(source, q("float_array"), id=array_id, count=str(len(flat)))
        array.text = " ".join(f"{value:.7g}" for value in flat)
        common = ET.SubElement(source, q("technique_common"))
        accessor = ET.SubElement(
            common, q("accessor"), source=f"#{array_id}",
            count=str(len(values)), stride=str(len(params)),
        )
        for param in params:
            ET.SubElement(accessor, q("param"), name=param, type="float")

    add_source("position_source", "position_array", dae_positions, ("X", "Y", "Z"))
    add_source("normal_source", "normal_array", dae_normals, ("X", "Y", "Z"))
    vertices = ET.SubElement(xml_mesh, q("vertices"), id="sb17_vertices")
    ET.SubElement(vertices, q("input"), semantic="POSITION", source="#position_source")
    ET.SubElement(vertices, q("input"), semantic="NORMAL", source="#normal_source")

    for material in MATERIALS:
        faces = material_faces.get(material)
        if not faces:
            continue
        triangles = ET.SubElement(
            xml_mesh, q("triangles"), count=str(len(faces)),
            material=f"{material}_symbol",
        )
        ET.SubElement(
            triangles, q("input"), semantic="VERTEX",
            source="#sb17_vertices", offset="0",
        )
        ET.SubElement(triangles, q("p")).text = " ".join(
            str(index) for face in faces for index in face
        )

    scenes = ET.SubElement(root, q("library_visual_scenes"))
    visual_scene = ET.SubElement(scenes, q("visual_scene"), id="Scene", name="Scene")
    node = ET.SubElement(
        visual_scene, q("node"), id="SB17NRX2C35_8",
        name="SB Acoustics SB17NRX2C35-8", type="NODE",
    )
    instance = ET.SubElement(node, q("instance_geometry"), url="#sb17_geometry")
    bind = ET.SubElement(instance, q("bind_material"))
    common = ET.SubElement(bind, q("technique_common"))
    for material in material_faces:
        ET.SubElement(
            common, q("instance_material"),
            symbol=f"{material}_symbol", target=f"#{material}_material",
        )
    scene = ET.SubElement(root, q("scene"))
    ET.SubElement(scene, q("instance_visual_scene"), url="#Scene")

    ET.indent(root, space="  ")
    ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)


def validate(mesh: Mesh) -> dict[str, object]:
    xs, ys, zs = zip(*mesh.vertices)
    degenerate = 0
    for face in mesh.faces:
        area2 = length(cross(
            vec_sub(mesh.vertices[face[1]], mesh.vertices[face[0]]),
            vec_sub(mesh.vertices[face[2]], mesh.vertices[face[0]]),
        ))
        if area2 < 1e-8:
            degenerate += 1
    return {
        "vertices": len(mesh.vertices),
        "triangles": len(mesh.faces),
        "degenerate_triangles": degenerate,
        "x_size_mm": max(xs) - min(xs),
        "y_size_mm": max(ys) - min(ys),
        "z_size_mm": max(zs) - min(zs),
        "z_min_mm": min(zs),
        "z_max_mm": max(zs),
        "materials": dict(Counter(mesh.materials)),
        "main_circle_chord_error_mm": (FRAME_DIAMETER / 2.0)
        * (1.0 - cos(pi / MAIN_SEGMENTS)),
    }


def main() -> None:
    output_dir = Path(__file__).resolve().parents[3] / "3d_models" / MODEL_NAME
    output_dir.mkdir(parents=True, exist_ok=True)
    dae_path = output_dir / f"{MODEL_NAME}.dae"
    mesh = build_model()
    stats = validate(mesh)
    if stats["degenerate_triangles"]:
        raise RuntimeError(f"Degenerate triangles found: {stats}")
    expected = {
        "x_size_mm": FRAME_DIAMETER,
        "y_size_mm": FRAME_DIAMETER,
        "z_size_mm": OVERALL_DEPTH,
        "z_min_mm": -MOUNTING_DEPTH,
        "z_max_mm": FRONT_PROJECTION,
    }
    for key, value in expected.items():
        if abs(float(stats[key]) - value) > 1e-6:
            raise RuntimeError(f"{key} is {stats[key]}, expected {value}")
    write_dae(mesh, dae_path)
    print(f"Wrote {dae_path}")
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
