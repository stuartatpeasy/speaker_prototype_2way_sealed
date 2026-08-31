#!/usr/bin/env python3
"""Generate a coloured SketchUp model of the SB Acoustics SB26STWGC-4.

Published mounting and envelope dimensions are reproduced exactly. Details
not dimensioned by SB Acoustics are visually inferred from manufacturer and
public product photographs.

Coordinate convention:
  * millimetres, Z_UP
  * origin at the acoustic axis on the rear mounting face of the waveguide
  * front is +Z; motor/rear chamber is -Z
"""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
from math import cos, pi, sin, sqrt
from pathlib import Path
import xml.etree.ElementTree as ET


MODEL_NAME = "SB_Acoustics_SB26STWGC-4"

# Manufacturer-published dimensions, millimetres.
FACEPLATE_DIAMETER = 103.8
MOUNTING_PCD = 92.0
MOUNT_RECESS_DIAMETER = 8.0
MOUNT_THROUGH_DIAMETER = 4.2
REAR_ENVELOPE_DIAMETER = 82.8
MOTOR_DIAMETER = 70.0
FACEPLATE_THICKNESS = 6.0
MOUNTING_DEPTH = 42.1
OVERALL_DEPTH = 48.1
VOICE_COIL_DIAMETER = 25.4
VOICE_COIL_HEIGHT = 1.3

# Estimated from the physical production unit; not dimensioned in the
# manufacturer drawing.
WAVEGUIDE_BODY_FILLET_RADIUS = 3.0
ADAPTER_BOSS_RADIUS = 32.0
ADAPTER_BOSS_DEPTH = 8.8
FILLET_PROFILE_SEGMENTS = 4

MAIN_SEGMENTS = 64
INNER_SEGMENTS = 48
MOTOR_SEGMENTS = 48
SMALL_SEGMENTS = 20

PREVIEW_CONFIG = {
    "title": "SB Acoustics SB26STWGC-4 - SketchUp model QA",
    "views": (
        {"label": "Front three-quarter", "direction": (1.25, -1.55, 1.20)},
        {"label": "Side profile", "direction": (0.0, -1.0, -0.08)},
        {"label": "Rear three-quarter", "direction": (-1.25, -1.55, -1.05)},
    ),
    "view_width": 560,
}


MATERIALS = {
    "waveguide_black": {
        "diffuse": (0.055, 0.058, 0.058, 1.0),
        "specular": (0.100, 0.105, 0.105, 1.0),
        "shininess": 12.0,
    },
    "dome_fabric": {
        "diffuse": (0.085, 0.090, 0.089, 1.0),
        "specular": (0.130, 0.135, 0.132, 1.0),
        "shininess": 9.0,
    },
    "dome_surround": {
        "diffuse": (0.025, 0.028, 0.028, 1.0),
        "specular": (0.055, 0.058, 0.058, 1.0),
        "shininess": 5.0,
    },
    "adapter_black": {
        "diffuse": (0.045, 0.050, 0.051, 1.0),
        "specular": (0.055, 0.060, 0.062, 1.0),
        "shininess": 6.0,
    },
    "ferrite": {
        "diffuse": (0.230, 0.238, 0.240, 1.0),
        "specular": (0.060, 0.065, 0.066, 1.0),
        "shininess": 4.0,
    },
    "zinc_plate": {
        "diffuse": (0.600, 0.625, 0.635, 1.0),
        "specular": (0.320, 0.340, 0.350, 1.0),
        "shininess": 23.0,
    },
    "rear_label": {
        "diffuse": (0.075, 0.080, 0.081, 1.0),
        "specular": (0.025, 0.027, 0.027, 1.0),
        "shininess": 2.0,
    },
    "brass": {
        "diffuse": (0.700, 0.490, 0.140, 1.0),
        "specular": (0.330, 0.235, 0.070, 1.0),
        "shininess": 18.0,
    },
    "copper": {
        "diffuse": (0.630, 0.300, 0.075, 1.0),
        "specular": (0.260, 0.115, 0.025, 1.0),
        "shininess": 14.0,
    },
    "label_light": {
        "diffuse": (0.790, 0.790, 0.750, 1.0),
        "specular": (0.070, 0.070, 0.065, 1.0),
        "shininess": 3.0,
    },
    "recess": {
        "diffuse": (0.105, 0.110, 0.110, 1.0),
        "specular": (0.075, 0.080, 0.080, 1.0),
        "shininess": 7.0,
    },
    "void": {
        "diffuse": (0.006, 0.007, 0.007, 1.0),
        "specular": (0.0, 0.0, 0.0, 1.0),
        "shininess": 1.0,
    },
}


def add(a, b):
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def scale(a, value):
    return a[0] * value, a[1] * value, a[2] * value


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def magnitude(a):
    return sqrt(dot(a, a))


def unit(a):
    size = magnitude(a)
    if size == 0:
        return 0.0, 0.0, 1.0
    return scale(a, 1.0 / size)


def normal(a, b, c):
    return unit(cross(sub(b, a), sub(c, a)))


class Mesh:
    def __init__(self):
        self.vertices: list[tuple[float, float, float]] = []
        self.faces: list[tuple[int, int, int]] = []
        self.materials: list[str] = []
        self.groups: list[str] = []

    def vertex(self, point):
        self.vertices.append(tuple(float(value) for value in point))
        return len(self.vertices) - 1

    def face(self, a, b, c, material, group):
        if len({a, b, c}) < 3:
            return
        self.faces.append((a, b, c))
        self.materials.append(material)
        self.groups.append(group)

    def quad(self, a, b, c, d, material, group):
        self.face(a, b, c, material, group)
        self.face(a, c, d, material, group)

    def oriented_face(self, a, b, c, material, group, solid_center):
        points = [self.vertices[index] for index in (a, b, c)]
        centroid = tuple(
            sum(point[axis] for point in points) / 3.0 for axis in range(3)
        )
        if dot(normal(*points), sub(centroid, solid_center)) < 0:
            b, c = c, b
        self.face(a, b, c, material, group)

    def oriented_quad(self, a, b, c, d, material, group, solid_center):
        self.oriented_face(a, b, c, material, group, solid_center)
        self.oriented_face(a, c, d, material, group, solid_center)


def add_revolved(
    mesh: Mesh,
    profile: list[tuple[float, float]],
    material: str,
    group: str,
    segments: int = MAIN_SEGMENTS,
    smooth_profile: bool = True,
):
    """Revolve a counter-clockwise closed profile in the radius/Z plane."""
    rings = []
    for radius, z in profile:
        if abs(radius) < 1e-10:
            pole = mesh.vertex((0.0, 0.0, z))
            rings.append([pole] * segments)
            continue
        ring = []
        for index in range(segments):
            angle = 2.0 * pi * index / segments
            ring.append(mesh.vertex((
                radius * cos(angle), radius * sin(angle), z
            )))
        rings.append(ring)

    for profile_index in range(len(profile)):
        next_profile = (profile_index + 1) % len(profile)
        ring_a = rings[profile_index]
        ring_b = rings[next_profile]
        radius_a = profile[profile_index][0]
        radius_b = profile[next_profile][0]
        segment_group = (
            group if smooth_profile else f"{group}_profile_{profile_index}"
        )
        for angular_index in range(segments):
            angular_next = (angular_index + 1) % segments
            a = ring_a[angular_index]
            b = ring_a[angular_next]
            c = ring_b[angular_index]
            d = ring_b[angular_next]
            if radius_a < 1e-10:
                mesh.face(a, d, c, material, segment_group)
            elif radius_b < 1e-10:
                mesh.face(a, b, c, material, segment_group)
            else:
                mesh.quad(a, b, d, c, material, segment_group)


def add_revolved_surface(
    mesh: Mesh,
    profile: list[tuple[float, float]],
    material: str,
    group: str,
    segments: int = MAIN_SEGMENTS,
):
    """Revolve an open profile, retaining shared normals along the profile."""
    rings = []
    for radius, z in profile:
        ring = []
        for index in range(segments):
            angle = 2.0 * pi * index / segments
            ring.append(mesh.vertex((
                radius * cos(angle), radius * sin(angle), z
            )))
        rings.append(ring)

    for profile_index in range(len(profile) - 1):
        ring_a = rings[profile_index]
        ring_b = rings[profile_index + 1]
        for angular_index in range(segments):
            angular_next = (angular_index + 1) % segments
            mesh.quad(
                ring_a[angular_index],
                ring_a[angular_next],
                ring_b[angular_next],
                ring_b[angular_index],
                material,
                group,
            )


def add_open_disc(
    mesh: Mesh,
    center_xy,
    radius,
    z,
    material,
    group,
    segments=SMALL_SEGMENTS,
    normal_positive_z=True,
):
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
    center_xy,
    outer_radius,
    inner_radius,
    z,
    material,
    group,
    segments=SMALL_SEGMENTS,
    normal_positive_z=True,
):
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
            mesh.quad(
                outer[index], outer[nxt], inner[nxt], inner[index],
                material, group,
            )
        else:
            mesh.quad(
                outer[index], inner[index], inner[nxt], outer[nxt],
                material, group,
            )


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
):
    u = scale(unit(axis_u), size_u / 2.0)
    v = scale(unit(axis_v), size_v / 2.0)
    w = scale(unit(axis_w), size_w / 2.0)
    points = []
    for su, sv, sw in (
        (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
        (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
    ):
        points.append(add(center, add(
            scale(u, su), add(scale(v, sv), scale(w, sw))
        )))
    vertices = [mesh.vertex(point) for point in points]
    for quad in (
        (0, 3, 2, 1), (4, 5, 6, 7),
        (0, 1, 5, 4), (1, 2, 6, 5),
        (2, 3, 7, 6), (3, 0, 4, 7),
    ):
        mesh.oriented_quad(
            *[vertices[index] for index in quad],
            material, group, center,
        )


def add_surface_quad(mesh, points, material, group, reverse=False):
    indices = [mesh.vertex(point) for point in points]
    if reverse:
        mesh.quad(indices[0], indices[3], indices[2], indices[1], material, group)
    else:
        mesh.quad(indices[0], indices[1], indices[2], indices[3], material, group)


def build_model():
    mesh = Mesh()

    # Solid aluminium waveguide/faceplate. Its outside edge and Z limits are
    # constrained by the published Ø103.8 and 6.0 mm dimensions.
    add_revolved(
        mesh,
        [
            (51.2, FACEPLATE_THICKNESS),
            (47.0, 5.95),
            (41.0, 5.60),
            (35.0, 4.90),
            (29.0, 3.80),
            (24.0, 2.55),
            (19.0, 1.45),
            (16.4, 1.10),
            (16.4, 0.0),
            (51.2, 0.0),
            (FACEPLATE_DIAMETER / 2.0, 0.70),
            (FACEPLATE_DIAMETER / 2.0, 5.35),
        ],
        "waveguide_black", "waveguide", MAIN_SEGMENTS, smooth_profile=True,
    )

    # Fine-weave fabric dome and its narrow rubber-coated suspension.
    add_revolved(
        mesh,
        [
            (16.3, 1.10), (15.7, 1.55), (14.6, 1.80), (13.8, 1.45),
            (13.8, 0.90), (14.7, 1.20), (15.7, 1.20), (16.3, 0.85),
        ],
        "dome_surround", "dome_surround", INNER_SEGMENTS, smooth_profile=True,
    )
    add_revolved(
        mesh,
        [
            (13.9, 1.50),
            (12.5, 2.20),
            (9.5, 3.35),
            (5.0, 4.35),
            (0.0, 4.75),
            (0.0, 4.10),
            (5.0, 3.70),
            (9.5, 2.85),
            (12.5, 1.95),
            (13.9, 1.25),
        ],
        "dome_fabric", "fabric_dome", INNER_SEGMENTS, smooth_profile=True,
    )

    # The production unit has a narrow central boss beneath the motor rather
    # than an Ø82.8 annular skirt. Its root blends into the flat rear face of
    # the waveguide with the user's estimated 3 mm concave fillet. The Ø70
    # motor then overhangs this boss; opposed terminals define the published
    # Ø82.8 rear envelope.
    fillet_center_radius = ADAPTER_BOSS_RADIUS + WAVEGUIDE_BODY_FILLET_RADIUS
    boss_profile = []
    for index in range(FILLET_PROFILE_SEGMENTS + 1):
        angle = pi / 2.0 + (pi / 2.0) * index / FILLET_PROFILE_SEGMENTS
        boss_profile.append((
            fillet_center_radius
            + WAVEGUIDE_BODY_FILLET_RADIUS * cos(angle),
            -WAVEGUIDE_BODY_FILLET_RADIUS
            + WAVEGUIDE_BODY_FILLET_RADIUS * sin(angle),
        ))
    boss_profile.append((ADAPTER_BOSS_RADIUS, -ADAPTER_BOSS_DEPTH))
    add_revolved_surface(
        mesh,
        boss_profile,
        "adapter_black",
        "adapter_boss_and_root_fillet",
        MAIN_SEGMENTS,
    )

    # Small motor/front plate and the 25.4 mm CCAW voice coil.
    add_revolved(
        mesh,
        [(36.0, -8.80), (13.2, -8.80), (13.2, -13.20), (36.0, -13.20)],
        "zinc_plate", "motor_top_plate", MOTOR_SEGMENTS, smooth_profile=False,
    )
    coil_radius = VOICE_COIL_DIAMETER / 2.0
    add_revolved(
        mesh,
        [
            (coil_radius + 0.35, -10.80),
            (coil_radius - 0.20, -10.80),
            (coil_radius - 0.20, -10.80 - VOICE_COIL_HEIGHT),
            (coil_radius + 0.35, -10.80 - VOICE_COIL_HEIGHT),
        ],
        "copper", "voice_coil", SMALL_SEGMENTS, smooth_profile=False,
    )

    # Ferrite motor, silver rear plate, and damped rear chamber.
    add_revolved(
        mesh,
        [
            (MOTOR_DIAMETER / 2.0, -13.20),
            (12.0, -13.20),
            (12.0, -31.20),
            (MOTOR_DIAMETER / 2.0, -31.20),
        ],
        "ferrite", "ferrite_motor", MOTOR_SEGMENTS, smooth_profile=False,
    )
    add_revolved(
        mesh,
        [(35.0, -31.20), (10.0, -31.20), (10.0, -35.50), (35.0, -35.50)],
        "zinc_plate", "rear_plate", MOTOR_SEGMENTS, smooth_profile=False,
    )
    add_revolved(
        mesh,
        [
            (34.0, -35.50), (4.6, -35.50),
            (4.6, -MOUNTING_DEPTH), (34.0, -MOUNTING_DEPTH),
        ],
        "rear_label", "rear_chamber", MOTOR_SEGMENTS, smooth_profile=False,
    )
    # The annular rear chamber leaves a genuine central pole vent.

    # Mounting recess and through-hole reference surfaces on the exact Ø92 PCD.
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
            FACEPLATE_THICKNESS - 0.020,
            "recess", f"mount_recess_{index}", SMALL_SEGMENTS,
        )
        add_open_disc(
            mesh, center, MOUNT_THROUGH_DIAMETER / 2.0,
            FACEPLATE_THICKNESS - 0.015,
            "void", f"mount_hole_{index}", SMALL_SEGMENTS,
        )

    # Opposed gold-plated terminals kept inside the Ø82.8 rear envelope.
    for index, direction in enumerate((-1.0, 1.0)):
        terminal_width = 7.6
        terminal_center = (REAR_ENVELOPE_DIAMETER - terminal_width) / 2.0
        add_oriented_box(
            mesh,
            (direction * terminal_center, 0.0, -10.2),
            (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0),
            terminal_width, 5.0, 1.0,
            "brass", f"terminal_tab_{index}",
        )
        add_oriented_box(
            mesh,
            (direction * 34.2, 0.0, -8.7),
            (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0),
            2.0, 4.0, 3.8,
            "brass", f"terminal_post_{index}",
        )

    # Side barcode label and restrained barcode geometry.
    add_surface_quad(
        mesh,
        [
            (-13.5, -34.99, -18.4), (13.5, -34.99, -18.4),
            (13.5, -34.99, -25.2), (-13.5, -34.99, -25.2),
        ],
        "label_light", "barcode_label", reverse=True,
    )
    for index in range(8):
        x = -9.2 + index * 2.6
        width = 0.42 if index % 3 else 0.75
        add_surface_quad(
            mesh,
            [
                (x - width / 2.0, -35.0, -19.4),
                (x + width / 2.0, -35.0, -19.4),
                (x + width / 2.0, -35.0, -23.7),
                (x - width / 2.0, -35.0, -23.7),
            ],
            "rear_label", f"barcode_{index}", reverse=True,
        )

    return mesh


def calculate_smooth_normals(mesh):
    accum = defaultdict(lambda: [0.0, 0.0, 0.0])
    for face, group in zip(mesh.faces, mesh.groups):
        face_normal = normal(*(mesh.vertices[index] for index in face))
        for vertex_index in face:
            key = (vertex_index, group)
            accum[key][0] += face_normal[0]
            accum[key][1] += face_normal[1]
            accum[key][2] += face_normal[2]
    return {key: unit(value) for key, value in accum.items()}


def write_dae(mesh, path):
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
    stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )
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
            f"{value:.4g}" for value in definition["diffuse"]
        )
        specular = ET.SubElement(phong, q("specular"))
        ET.SubElement(specular, q("color")).text = " ".join(
            f"{value:.4g}" for value in definition["specular"]
        )
        shininess = ET.SubElement(phong, q("shininess"))
        ET.SubElement(shininess, q("float")).text = str(definition["shininess"])
        extra = ET.SubElement(effect, q("extra"))
        google = ET.SubElement(extra, q("technique"), profile="GOOGLEEARTH")
        ET.SubElement(google, q("double_sided")).text = "1"

        material = ET.SubElement(
            materials_xml, q("material"),
            id=f"{name}_material", name=name.replace("_", " ").title(),
        )
        ET.SubElement(material, q("instance_effect"), url=f"#{name}_effect")

    geometries = ET.SubElement(root, q("library_geometries"))
    geometry = ET.SubElement(
        geometries, q("geometry"),
        id="sb26stwgc_geometry", name="SB Acoustics SB26STWGC-4",
    )
    xml_mesh = ET.SubElement(geometry, q("mesh"))

    def add_source(source_id, array_id, values, params):
        source = ET.SubElement(xml_mesh, q("source"), id=source_id)
        flat = [component for value in values for component in value]
        array = ET.SubElement(
            source, q("float_array"), id=array_id, count=str(len(flat))
        )
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
    vertices = ET.SubElement(xml_mesh, q("vertices"), id="sb26stwgc_vertices")
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
            source="#sb26stwgc_vertices", offset="0",
        )
        ET.SubElement(triangles, q("p")).text = " ".join(
            str(index) for face in faces for index in face
        )

    scenes = ET.SubElement(root, q("library_visual_scenes"))
    visual_scene = ET.SubElement(scenes, q("visual_scene"), id="Scene", name="Scene")
    node = ET.SubElement(
        visual_scene, q("node"), id="SB26STWGC_4",
        name="SB Acoustics SB26STWGC-4", type="NODE",
    )
    instance = ET.SubElement(node, q("instance_geometry"), url="#sb26stwgc_geometry")
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


def validate(mesh):
    xs, ys, zs = zip(*mesh.vertices)
    terminal_vertices = {
        vertex_index
        for face, group in zip(mesh.faces, mesh.groups)
        if group.startswith("terminal_")
        for vertex_index in face
    }
    terminal_xs = [mesh.vertices[index][0] for index in terminal_vertices]
    degenerate = 0
    for face in mesh.faces:
        doubled_area = magnitude(cross(
            sub(mesh.vertices[face[1]], mesh.vertices[face[0]]),
            sub(mesh.vertices[face[2]], mesh.vertices[face[0]]),
        ))
        if doubled_area < 1e-8:
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
        "terminal_envelope_x_mm": max(terminal_xs) - min(terminal_xs),
        "materials": dict(Counter(mesh.materials)),
        "main_circle_chord_error_mm": (
            FACEPLATE_DIAMETER / 2.0
        ) * (1.0 - cos(pi / MAIN_SEGMENTS)),
        "fillet_profile_chord_error_mm": (
            WAVEGUIDE_BODY_FILLET_RADIUS
            * (1.0 - cos(pi / (4.0 * FILLET_PROFILE_SEGMENTS)))
        ),
    }


def main():
    output_dir = Path(__file__).resolve().parents[3] / "3d_models" / MODEL_NAME
    output_dir.mkdir(parents=True, exist_ok=True)
    dae_path = output_dir / f"{MODEL_NAME}.dae"
    mesh = build_model()
    stats = validate(mesh)
    if stats["degenerate_triangles"]:
        raise RuntimeError(f"Degenerate triangles found: {stats}")
    expected = {
        "x_size_mm": FACEPLATE_DIAMETER,
        "y_size_mm": FACEPLATE_DIAMETER,
        "z_size_mm": OVERALL_DEPTH,
        "z_min_mm": -MOUNTING_DEPTH,
        "z_max_mm": FACEPLATE_THICKNESS,
        "terminal_envelope_x_mm": REAR_ENVELOPE_DIAMETER,
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
