#!/usr/bin/env python3
"""Generate a SketchUp-friendly Type D M4 x 10 mm threaded insert.

The output is a closed triangle mesh in COLLADA (.dae). Coordinates are
millimetres. The centre of the flange face is the origin and the insert extends
along negative Z, which makes placement on a SketchUp face straightforward.

Envelope dimensions follow The Insert Company headed zinc hex-drive / Type D
table for M4 x 10 mm: D1=8.5 mm, D2=5.5 mm, K=4.0 mm, L=10 mm.  Features not
specified in that table (flange thickness, thread crest form, and drive depth)
are representative of common die-cast Type D inserts and are kept as named
parameters below.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
from math import atan2, cos, pi, sin, sqrt
from pathlib import Path
import xml.etree.ElementTree as ET


MODEL_NAME = "M4x10_Type_D_Flanged_Threaded_Insert"
DISPLAY_NAME = "M4 x 10 mm Type D flanged threaded insert"

# Published envelope / interface dimensions, millimetres.
LENGTH = 10.0
FLANGE_DIAMETER = 8.5       # D1
BODY_ROOT_DIAMETER = 5.5    # D2; also agrees with the pilot-hole guidance
HEX_ACROSS_FLATS = 4.0      # K
INTERNAL_THREAD_MAJOR = 4.0
INTERNAL_THREAD_PITCH = 0.7

# Representative detail dimensions where the published table is silent.
FLANGE_THICKNESS = 0.72
FLANGE_BLEND_END = 1.08
EXTERNAL_CREST_DIAMETER = 8.18
EXTERNAL_THREAD_PITCH = 2.40
EXTERNAL_RUNOUT = 0.68
HEX_STRAIGHT_DEPTH = 1.60
HEX_TRANSITION_END = 2.15
M4_INTERNAL_MINOR_DIAMETER = 3.24

# 72 radial segments gives a smooth small part without making SketchUp heavy.
RADIAL_SEGMENTS = 72
EXTERNAL_Z_STEP = 0.12
INTERNAL_Z_STEP = 0.075

PREVIEW_CONFIG = {
    "title": "M4 x 10 mm | Type D insert | detailed",
    "views": (
        {"label": "Front three-quarter", "direction": (1.35, -1.70, 0.92)},
    ),
    "view_width": 900,
    "view_height": 630,
    "base_colour": (170.0, 179.0, 184.0),
}


def triangle_wave(phase: float, half_width: float = 0.33) -> float:
    """A sharp crest with a short flat root, periodic over 0..1."""
    f = phase % 1.0
    return max(0.0, 1.0 - abs(f - 0.5) / half_width)


def external_radius(theta: float, z: float) -> float:
    depth = -z
    flange_r = FLANGE_DIAMETER / 2.0
    root_r = BODY_ROOT_DIAMETER / 2.0
    crest_r = EXTERNAL_CREST_DIAMETER / 2.0

    # Right-hand, single-start coarse self-tapping thread.
    phase = ((depth - FLANGE_BLEND_END) / EXTERNAL_THREAD_PITCH
             + theta / (2.0 * pi))
    thread = triangle_wave(phase)
    amplitude = crest_r - root_r

    # Let the final crest run out while retaining the specified D2 root body.
    remaining = LENGTH - depth
    bottom_runout = min(1.0, max(0.0, remaining / EXTERNAL_RUNOUT))
    threaded_r = root_r + amplitude * thread * bottom_runout

    if depth <= FLANGE_THICKNESS:
        return flange_r
    if depth < FLANGE_BLEND_END:
        blend = (depth - FLANGE_THICKNESS) / (FLANGE_BLEND_END - FLANGE_THICKNESS)
        return flange_r * (1.0 - blend) + threaded_r * blend
    return threaded_r


def internal_thread_radius(theta: float, z: float) -> float:
    depth = -z
    minor_r = M4_INTERNAL_MINOR_DIAMETER / 2.0
    major_r = INTERNAL_THREAD_MAJOR / 2.0
    phase = ((depth - HEX_TRANSITION_END) / INTERNAL_THREAD_PITCH
             - theta / (2.0 * pi))
    return minor_r + (major_r - minor_r) * triangle_wave(phase, half_width=0.42)


def hex_radius(theta: float) -> float:
    """Radius to a regular hexagon with the requested width across flats."""
    apothem = HEX_ACROSS_FLATS / 2.0
    local = ((theta + pi / 6.0) % (pi / 3.0)) - pi / 6.0
    return apothem / cos(local)


def z_levels(start: float, end: float, step: float) -> list[float]:
    count = max(1, int(round(abs(end - start) / step)))
    return [start + (end - start) * i / count for i in range(count + 1)]


class Mesh:
    def __init__(self) -> None:
        self.vertices: list[tuple[float, float, float]] = []
        self.faces: list[tuple[int, int, int]] = []
        self.groups: list[str] = []
        self._vertex_cache: dict[tuple[int, int, int], int] = {}

    def vertex(self, xyz: tuple[float, float, float]) -> int:
        key = tuple(round(v * 1_000_000) for v in xyz)
        existing = self._vertex_cache.get(key)
        if existing is not None:
            return existing
        index = len(self.vertices)
        self.vertices.append(xyz)
        self._vertex_cache[key] = index
        return index

    def face(self, a: int, b: int, c: int, group: str) -> None:
        if len({a, b, c}) != 3:
            return
        self.faces.append((a, b, c))
        self.groups.append(group)


def make_ring(mesh: Mesh, z: float, radius_fn) -> list[int]:
    ring = []
    for i in range(RADIAL_SEGMENTS):
        theta = 2.0 * pi * i / RADIAL_SEGMENTS
        radius = radius_fn(theta, z)
        ring.append(mesh.vertex((radius * cos(theta), radius * sin(theta), z)))
    return ring


def connect_rings(
    mesh: Mesh,
    rings: list[list[int]],
    inward: bool,
    group_fn,
) -> None:
    n = RADIAL_SEGMENTS
    for layer in range(len(rings) - 1):
        upper = rings[layer]
        lower = rings[layer + 1]
        for i in range(n):
            j = (i + 1) % n
            a, b, c, d = upper[i], upper[j], lower[i], lower[j]
            group = group_fn(layer, i)
            if inward:
                mesh.face(a, d, c, group)
                mesh.face(a, b, d, group)
            else:
                mesh.face(a, c, d, group)
                mesh.face(a, d, b, group)


def add_top_annulus(mesh: Mesh, outer: list[int], inner: list[int]) -> None:
    n = RADIAL_SEGMENTS
    for i in range(n):
        j = (i + 1) % n
        mesh.face(outer[i], outer[j], inner[j], "top_face")
        mesh.face(outer[i], inner[j], inner[i], "top_face")


def add_bottom_annulus(mesh: Mesh, outer: list[int], inner: list[int]) -> None:
    n = RADIAL_SEGMENTS
    for i in range(n):
        j = (i + 1) % n
        mesh.face(outer[i], inner[j], outer[j], "bottom_face")
        mesh.face(outer[i], inner[i], inner[j], "bottom_face")


def build_mesh() -> Mesh:
    mesh = Mesh()

    outer_z = sorted(
        set(z_levels(0.0, -LENGTH, EXTERNAL_Z_STEP)
            + [0.0, -FLANGE_THICKNESS, -FLANGE_BLEND_END, -LENGTH]),
        reverse=True,
    )
    outer_rings = [make_ring(mesh, z, external_radius) for z in outer_z]
    connect_rings(mesh, outer_rings, inward=False,
                  group_fn=lambda _layer, _i: "exterior")

    hex_z = [0.0, -HEX_STRAIGHT_DEPTH]
    hex_rings = [make_ring(mesh, z, lambda theta, _z: hex_radius(theta)) for z in hex_z]

    def hex_group(_layer: int, angular_index: int) -> str:
        # Preserve the six crisp Allen-key flats while smoothing within each flat.
        theta_mid = 2.0 * pi * (angular_index + 0.5) / RADIAL_SEGMENTS
        side = int(((theta_mid + pi / 6.0) % (2.0 * pi)) / (pi / 3.0))
        return f"hex_wall_{side}"

    connect_rings(mesh, hex_rings, inward=True, group_fn=hex_group)

    transition_bottom = make_ring(mesh, -HEX_TRANSITION_END, internal_thread_radius)
    connect_rings(mesh, [hex_rings[-1], transition_bottom], inward=True,
                  group_fn=lambda _layer, _i: "drive_transition")

    internal_z = z_levels(-HEX_TRANSITION_END, -LENGTH, INTERNAL_Z_STEP)
    internal_rings = [transition_bottom]
    internal_rings.extend(make_ring(mesh, z, internal_thread_radius) for z in internal_z[1:])
    connect_rings(mesh, internal_rings, inward=True,
                  group_fn=lambda _layer, _i: "internal_thread")

    add_top_annulus(mesh, outer_rings[0], hex_rings[0])
    add_bottom_annulus(mesh, outer_rings[-1], internal_rings[-1])
    return mesh


def sub(a, b):
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def normal(a, b, c):
    raw = cross(sub(b, a), sub(c, a))
    length = sqrt(sum(value * value for value in raw))
    if length == 0:
        return 0.0, 0.0, 1.0
    return tuple(value / length for value in raw)


def smooth_group_normals(mesh: Mesh):
    accum = defaultdict(lambda: [0.0, 0.0, 0.0])
    face_normals = []
    for face, group in zip(mesh.faces, mesh.groups):
        n = normal(*(mesh.vertices[index] for index in face))
        face_normals.append(n)
        for index in face:
            key = (index, group)
            accum[key][0] += n[0]
            accum[key][1] += n[1]
            accum[key][2] += n[2]

    result = {}
    for key, value in accum.items():
        length = sqrt(sum(component * component for component in value))
        result[key] = tuple(component / length for component in value)
    return result, face_normals


def write_dae(mesh: Mesh, path: Path) -> None:
    smooth_normals, _ = smooth_group_normals(mesh)

    # COLLADA uses one index for POSITION+NORMAL here.  Split only at named
    # smoothing boundaries; this keeps sharp flange/hex edges and a compact file.
    remap = {}
    dae_positions = []
    dae_normals = []
    dae_faces = []
    for face, group in zip(mesh.faces, mesh.groups):
        remapped_face = []
        for index in face:
            key = (index, group)
            if key not in remap:
                remap[key] = len(dae_positions)
                dae_positions.append(mesh.vertices[index])
                dae_normals.append(smooth_normals[key])
            remapped_face.append(remap[key])
        dae_faces.append(tuple(remapped_face))

    ns = "http://www.collada.org/2005/11/COLLADASchema"
    ET.register_namespace("", ns)
    q = lambda tag: f"{{{ns}}}{tag}"

    root = ET.Element(q("COLLADA"), version="1.4.1")
    asset = ET.SubElement(root, q("asset"))
    contributor = ET.SubElement(asset, q("contributor"))
    ET.SubElement(contributor, q("authoring_tool")).text = "Codex parametric mesh generator"
    stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    ET.SubElement(asset, q("created")).text = stamp
    ET.SubElement(asset, q("modified")).text = stamp
    ET.SubElement(asset, q("unit"), meter="0.001", name="millimeter")
    ET.SubElement(asset, q("up_axis")).text = "Z_UP"

    effects = ET.SubElement(root, q("library_effects"))
    effect = ET.SubElement(effects, q("effect"), id="zinc_effect")
    profile = ET.SubElement(effect, q("profile_COMMON"))
    technique = ET.SubElement(profile, q("technique"), sid="common")
    phong = ET.SubElement(technique, q("phong"))
    diffuse = ET.SubElement(phong, q("diffuse"))
    ET.SubElement(diffuse, q("color")).text = "0.72 0.74 0.75 1"
    specular = ET.SubElement(phong, q("specular"))
    ET.SubElement(specular, q("color")).text = "0.34 0.36 0.38 1"
    shininess = ET.SubElement(phong, q("shininess"))
    ET.SubElement(shininess, q("float")).text = "22"

    materials = ET.SubElement(root, q("library_materials"))
    material = ET.SubElement(materials, q("material"), id="zinc_material", name="Zinc alloy")
    ET.SubElement(material, q("instance_effect"), url="#zinc_effect")

    geometries = ET.SubElement(root, q("library_geometries"))
    geometry = ET.SubElement(
        geometries, q("geometry"), id="insert_geometry", name=DISPLAY_NAME
    )
    xml_mesh = ET.SubElement(geometry, q("mesh"))

    def add_source(source_id: str, array_id: str, values, params):
        source = ET.SubElement(xml_mesh, q("source"), id=source_id)
        flat = [component for value in values for component in value]
        array = ET.SubElement(source, q("float_array"), id=array_id, count=str(len(flat)))
        array.text = " ".join(f"{value:.7g}" for value in flat)
        common = ET.SubElement(source, q("technique_common"))
        accessor = ET.SubElement(common, q("accessor"), source=f"#{array_id}",
                                 count=str(len(values)), stride=str(len(params)))
        for param in params:
            ET.SubElement(accessor, q("param"), name=param, type="float")

    add_source("position_source", "position_array", dae_positions, ("X", "Y", "Z"))
    add_source("normal_source", "normal_array", dae_normals, ("X", "Y", "Z"))
    vertices = ET.SubElement(xml_mesh, q("vertices"), id="insert_vertices")
    ET.SubElement(vertices, q("input"), semantic="POSITION", source="#position_source")
    ET.SubElement(vertices, q("input"), semantic="NORMAL", source="#normal_source")
    triangles = ET.SubElement(xml_mesh, q("triangles"), count=str(len(dae_faces)),
                              material="ZincMaterial")
    ET.SubElement(triangles, q("input"), semantic="VERTEX", source="#insert_vertices", offset="0")
    ET.SubElement(triangles, q("p")).text = " ".join(str(i) for face in dae_faces for i in face)

    scenes = ET.SubElement(root, q("library_visual_scenes"))
    visual_scene = ET.SubElement(scenes, q("visual_scene"), id="Scene", name="Scene")
    node = ET.SubElement(
        visual_scene, q("node"), id=MODEL_NAME, name=DISPLAY_NAME, type="NODE"
    )
    instance = ET.SubElement(node, q("instance_geometry"), url="#insert_geometry")
    bind = ET.SubElement(instance, q("bind_material"))
    common = ET.SubElement(bind, q("technique_common"))
    ET.SubElement(common, q("instance_material"), symbol="ZincMaterial",
                  target="#zinc_material")
    scene = ET.SubElement(root, q("scene"))
    ET.SubElement(scene, q("instance_visual_scene"), url="#Scene")

    ET.indent(root, space="  ")
    ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)


def validate(mesh: Mesh) -> dict[str, float | int]:
    edges = Counter()
    for a, b, c in mesh.faces:
        edges[tuple(sorted((a, b)))] += 1
        edges[tuple(sorted((b, c)))] += 1
        edges[tuple(sorted((c, a)))] += 1
    non_manifold = sum(count != 2 for count in edges.values())

    volume6 = 0.0
    for a_i, b_i, c_i in mesh.faces:
        a, b, c = mesh.vertices[a_i], mesh.vertices[b_i], mesh.vertices[c_i]
        volume6 += sum(a[k] * cross(b, c)[k] for k in range(3))
    signed_volume = volume6 / 6.0

    xs, ys, zs = zip(*mesh.vertices)
    return {
        "vertices": len(mesh.vertices),
        "triangles": len(mesh.faces),
        "non_manifold_edges": non_manifold,
        "signed_volume_mm3": signed_volume,
        "x_size_mm": max(xs) - min(xs),
        "y_size_mm": max(ys) - min(ys),
        "z_size_mm": max(zs) - min(zs),
    }


def main() -> None:
    output_dir = Path(__file__).resolve().parents[3] / "3d_models" / MODEL_NAME
    output_dir.mkdir(parents=True, exist_ok=True)
    dae_path = output_dir / f"{MODEL_NAME}.dae"
    mesh = build_mesh()
    stats = validate(mesh)
    if stats["non_manifold_edges"] != 0:
        raise RuntimeError(f"Mesh is not watertight: {stats}")
    if stats["signed_volume_mm3"] <= 0:
        raise RuntimeError(f"Mesh winding is inverted: {stats}")
    write_dae(mesh, dae_path)
    print(f"Wrote {dae_path}")
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
