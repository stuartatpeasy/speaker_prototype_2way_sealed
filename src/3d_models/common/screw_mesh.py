#!/usr/bin/env python3
"""Shared low-poly countersunk-screw geometry and COLLADA export support."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from math import atan2, ceil, cos, pi, sin, sqrt, tan
from pathlib import Path
import xml.etree.ElementTree as ET


MATERIALS = {
    "black_steel": {
        "diffuse": (0.035, 0.040, 0.043, 1.0),
        "specular": (0.150, 0.155, 0.158, 1.0),
        "shininess": 18.0,
    }
}


@dataclass(frozen=True)
class ScrewSpec:
    model_name: str
    display_name: str
    length: float
    major_diameter: float
    root_diameter: float
    thread_pitch: float
    head_diameter: float
    head_height: float
    countersunk_angle_degrees: float
    drive_reach: float
    drive_depth: float
    point_length: float = 0.0
    top_thread_run_in: float = 0.70
    bottom_thread_run_out: float = 0.70
    radial_segments: int = 24
    axial_samples_per_pitch: float = 2.0
    point_segments: int = 6


class Mesh:
    def __init__(self) -> None:
        self.vertices: list[tuple[float, float, float]] = []
        self.faces: list[tuple[int, int, int]] = []
        self.groups: list[str] = []
        self.materials: list[str] = []
        self._vertex_cache: dict[tuple[int, int, int], int] = {}

    def vertex(self, xyz: tuple[float, float, float]) -> int:
        key = tuple(round(value * 1_000_000) for value in xyz)
        existing = self._vertex_cache.get(key)
        if existing is not None:
            return existing
        index = len(self.vertices)
        self.vertices.append(tuple(float(value) for value in xyz))
        self._vertex_cache[key] = index
        return index

    def face(self, a: int, b: int, c: int, group: str) -> None:
        if len({a, b, c}) != 3:
            return
        self.faces.append((a, b, c))
        self.groups.append(group)
        self.materials.append("black_steel")


def triangle_wave(phase: float, half_width: float = 0.36) -> float:
    fraction = phase % 1.0
    return max(0.0, 1.0 - abs(fraction - 0.5) / half_width)


def angle_distance(theta: float, direction: float) -> float:
    return abs((theta - direction + pi) % (2.0 * pi) - pi)


def pozi_radius(theta: float, reach: float) -> float:
    """Stylised PZ2 boundary with four main and four secondary wings."""
    base = reach * 0.34
    main = 0.0
    secondary = 0.0
    for index in range(4):
        main_direction = index * pi / 2.0
        secondary_direction = pi / 4.0 + index * pi / 2.0
        main = max(
            main,
            max(0.0, 1.0 - angle_distance(theta, main_direction) / (pi / 10.0)),
        )
        secondary = max(
            secondary,
            max(
                0.0,
                1.0
                - angle_distance(theta, secondary_direction) / (pi / 18.0),
            ),
        )
    main_radius = base + (reach - base) * main
    secondary_radius = base + (reach * 0.68 - base) * secondary
    return max(base, main_radius, secondary_radius)


def make_ring(mesh: Mesh, z: float, radius_fn, segments: int) -> list[int]:
    ring = []
    for index in range(segments):
        theta = 2.0 * pi * index / segments
        radius = radius_fn(theta, z)
        ring.append(mesh.vertex((radius * cos(theta), radius * sin(theta), z)))
    return ring


def connect_rings(
    mesh: Mesh,
    rings: list[list[int]],
    inward: bool,
    group: str,
) -> None:
    segments = len(rings[0])
    for layer in range(len(rings) - 1):
        upper = rings[layer]
        lower = rings[layer + 1]
        for index in range(segments):
            following = (index + 1) % segments
            a, b = upper[index], upper[following]
            c, d = lower[index], lower[following]
            if inward:
                mesh.face(a, d, c, group)
                mesh.face(a, b, d, group)
            else:
                mesh.face(a, c, d, group)
                mesh.face(a, d, b, group)


def add_top_annulus(mesh: Mesh, outer: list[int], inner: list[int]) -> None:
    segments = len(outer)
    for index in range(segments):
        following = (index + 1) % segments
        mesh.face(outer[index], outer[following], inner[following], "head_top")
        mesh.face(outer[index], inner[following], inner[index], "head_top")


def cap_ring(
    mesh: Mesh,
    ring: list[int],
    z: float,
    group: str,
    normal_positive_z: bool,
) -> None:
    center = mesh.vertex((0.0, 0.0, z))
    for index in range(len(ring)):
        following = (index + 1) % len(ring)
        if normal_positive_z:
            mesh.face(center, ring[index], ring[following], group)
        else:
            mesh.face(center, ring[following], ring[index], group)


def z_levels(start: float, end: float, maximum_step: float) -> list[float]:
    count = max(1, int(ceil(abs(end - start) / maximum_step)))
    return [start + (end - start) * index / count for index in range(count + 1)]


def build_screw(spec: ScrewSpec) -> Mesh:
    if spec.radial_segments % 8:
        raise ValueError("radial_segments must be divisible by 8 for the PZ drive")
    mesh = Mesh()
    segments = spec.radial_segments
    head_radius = spec.head_diameter / 2.0
    major_radius = spec.major_diameter / 2.0
    root_radius = spec.root_diameter / 2.0

    cone_depth = (head_radius - major_radius) / tan(
        spec.countersunk_angle_degrees * pi / 360.0
    )
    edge_depth = max(0.08, spec.head_height - cone_depth)
    head_profile = (
        (head_radius, 0.0, "head_edge"),
        (head_radius, -edge_depth, "head_edge"),
        (major_radius, -spec.head_height, "head_countersink"),
    )
    head_rings = [
        make_ring(mesh, z, lambda _theta, _z, radius=radius: radius, segments)
        for radius, z, _group in head_profile
    ]
    connect_rings(mesh, head_rings[:2], inward=False, group="head_edge")
    connect_rings(mesh, head_rings[1:], inward=False, group="head_countersink")

    drive_top = make_ring(
        mesh,
        0.0,
        lambda theta, _z: pozi_radius(theta, spec.drive_reach),
        segments,
    )
    drive_bottom = make_ring(
        mesh,
        -spec.drive_depth,
        lambda theta, _z: pozi_radius(theta, spec.drive_reach) * 0.76,
        segments,
    )
    add_top_annulus(mesh, head_rings[0], drive_top)
    connect_rings(mesh, [drive_top, drive_bottom], inward=True, group="pozi_wall")
    cap_ring(
        mesh,
        drive_bottom,
        -spec.drive_depth,
        "pozi_floor",
        normal_positive_z=True,
    )

    thread_start_depth = spec.head_height
    point_start_depth = spec.length - spec.point_length
    thread_step = spec.thread_pitch / spec.axial_samples_per_pitch
    thread_z = z_levels(-thread_start_depth, -point_start_depth, thread_step)

    def thread_radius(theta: float, z: float) -> float:
        depth = -z
        phase = (depth - thread_start_depth) / spec.thread_pitch + theta / (2.0 * pi)
        crest = triangle_wave(phase)
        top_scale = min(
            1.0,
            max(0.0, (depth - thread_start_depth) / spec.top_thread_run_in),
        )
        if spec.point_length:
            bottom_scale = 1.0
        else:
            remaining = spec.length - depth
            bottom_scale = min(
                1.0, max(0.0, remaining / spec.bottom_thread_run_out)
            )
        base = major_radius * (1.0 - top_scale) + root_radius * top_scale
        if not spec.point_length and depth > spec.length - spec.bottom_thread_run_out:
            end_fraction = max(0.0, (spec.length - depth) / spec.bottom_thread_run_out)
            base *= 0.82 + 0.18 * end_fraction
        return base + (major_radius - root_radius) * crest * top_scale * bottom_scale

    thread_rings = [make_ring(mesh, z, thread_radius, segments) for z in thread_z]
    # Reuse the last head ring at the exact shared interface.
    thread_rings[0] = head_rings[-1]
    connect_rings(mesh, thread_rings, inward=False, group="external_thread")

    if spec.point_length:
        point_rings = [thread_rings[-1]]
        for index in range(1, spec.point_segments):
            fraction = index / spec.point_segments
            z = -point_start_depth - spec.point_length * fraction

            def point_radius(theta: float, _z: float, fraction=fraction) -> float:
                phase = (
                    point_start_depth / spec.thread_pitch
                    + fraction * spec.point_length / spec.thread_pitch
                    + theta / (2.0 * pi)
                )
                taper = (1.0 - fraction) ** 0.82
                return taper * (
                    root_radius
                    + (major_radius - root_radius) * triangle_wave(phase)
                )

            point_rings.append(make_ring(mesh, z, point_radius, segments))
        connect_rings(mesh, point_rings, inward=False, group="tapered_thread_point")
        tip = mesh.vertex((0.0, 0.0, -spec.length))
        final_ring = point_rings[-1]
        for index in range(segments):
            following = (index + 1) % segments
            mesh.face(final_ring[index], tip, final_ring[following], "tip")
    else:
        cap_ring(
            mesh,
            thread_rings[-1],
            -spec.length,
            "machine_screw_end",
            normal_positive_z=False,
        )

    return mesh


def subtract(a, b):
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def normal(a, b, c):
    value = cross(subtract(b, a), subtract(c, a))
    length = sqrt(sum(component * component for component in value))
    if length == 0.0:
        return 0.0, 0.0, 1.0
    return tuple(component / length for component in value)


def smooth_group_normals(mesh: Mesh):
    accumulated = defaultdict(lambda: [0.0, 0.0, 0.0])
    for face, group in zip(mesh.faces, mesh.groups):
        face_normal = normal(*(mesh.vertices[index] for index in face))
        for index in face:
            key = index, group
            for axis in range(3):
                accumulated[key][axis] += face_normal[axis]
    result = {}
    for key, value in accumulated.items():
        length = sqrt(sum(component * component for component in value))
        result[key] = tuple(component / length for component in value)
    return result


def write_dae(mesh: Mesh, path: Path, spec: ScrewSpec) -> None:
    smooth_normals = smooth_group_normals(mesh)
    remap = {}
    positions = []
    normals = []
    faces = []
    for face, group in zip(mesh.faces, mesh.groups):
        remapped = []
        for index in face:
            key = index, group
            if key not in remap:
                remap[key] = len(positions)
                positions.append(mesh.vertices[index])
                normals.append(smooth_normals[key])
            remapped.append(remap[key])
        faces.append(tuple(remapped))

    namespace = "http://www.collada.org/2005/11/COLLADASchema"
    ET.register_namespace("", namespace)
    q = lambda tag: f"{{{namespace}}}{tag}"
    root = ET.Element(q("COLLADA"), version="1.4.1")
    asset = ET.SubElement(root, q("asset"))
    contributor = ET.SubElement(asset, q("contributor"))
    ET.SubElement(contributor, q("authoring_tool")).text = (
        "Codex dimension-controlled low-poly screw generator"
    )
    stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )
    ET.SubElement(asset, q("created")).text = stamp
    ET.SubElement(asset, q("modified")).text = stamp
    ET.SubElement(asset, q("unit"), name="millimeter", meter="0.001")
    ET.SubElement(asset, q("up_axis")).text = "Z_UP"

    effects = ET.SubElement(root, q("library_effects"))
    effect = ET.SubElement(effects, q("effect"), id="black_steel_effect")
    profile = ET.SubElement(effect, q("profile_COMMON"))
    technique = ET.SubElement(profile, q("technique"), sid="common")
    phong = ET.SubElement(technique, q("phong"))
    definition = MATERIALS["black_steel"]
    diffuse = ET.SubElement(phong, q("diffuse"))
    ET.SubElement(diffuse, q("color")).text = " ".join(
        str(value) for value in definition["diffuse"]
    )
    specular = ET.SubElement(phong, q("specular"))
    ET.SubElement(specular, q("color")).text = " ".join(
        str(value) for value in definition["specular"]
    )
    shininess = ET.SubElement(phong, q("shininess"))
    ET.SubElement(shininess, q("float")).text = str(definition["shininess"])
    materials_xml = ET.SubElement(root, q("library_materials"))
    material = ET.SubElement(
        materials_xml,
        q("material"),
        id="black_steel_material",
        name="Black steel",
    )
    ET.SubElement(material, q("instance_effect"), url="#black_steel_effect")

    geometries = ET.SubElement(root, q("library_geometries"))
    geometry = ET.SubElement(
        geometries,
        q("geometry"),
        id="screw_geometry",
        name=spec.display_name,
    )
    xml_mesh = ET.SubElement(geometry, q("mesh"))

    def add_source(source_id, array_id, values, parameters):
        source = ET.SubElement(xml_mesh, q("source"), id=source_id)
        flat = [component for value in values for component in value]
        array = ET.SubElement(
            source, q("float_array"), id=array_id, count=str(len(flat))
        )
        array.text = " ".join(f"{value:.7g}" for value in flat)
        common = ET.SubElement(source, q("technique_common"))
        accessor = ET.SubElement(
            common,
            q("accessor"),
            source=f"#{array_id}",
            count=str(len(values)),
            stride=str(len(parameters)),
        )
        for parameter in parameters:
            ET.SubElement(accessor, q("param"), name=parameter, type="float")

    add_source("position_source", "position_array", positions, ("X", "Y", "Z"))
    add_source("normal_source", "normal_array", normals, ("X", "Y", "Z"))
    vertices = ET.SubElement(xml_mesh, q("vertices"), id="screw_vertices")
    ET.SubElement(vertices, q("input"), semantic="POSITION", source="#position_source")
    ET.SubElement(vertices, q("input"), semantic="NORMAL", source="#normal_source")
    triangles = ET.SubElement(
        xml_mesh,
        q("triangles"),
        count=str(len(faces)),
        material="black_steel_symbol",
    )
    ET.SubElement(
        triangles, q("input"), semantic="VERTEX", source="#screw_vertices", offset="0"
    )
    ET.SubElement(triangles, q("p")).text = " ".join(
        str(index) for face in faces for index in face
    )

    scenes = ET.SubElement(root, q("library_visual_scenes"))
    visual_scene = ET.SubElement(scenes, q("visual_scene"), id="Scene", name="Scene")
    node = ET.SubElement(
        visual_scene,
        q("node"),
        id=spec.model_name,
        name=spec.display_name,
        type="NODE",
    )
    instance = ET.SubElement(node, q("instance_geometry"), url="#screw_geometry")
    bind = ET.SubElement(instance, q("bind_material"))
    common = ET.SubElement(bind, q("technique_common"))
    ET.SubElement(
        common,
        q("instance_material"),
        symbol="black_steel_symbol",
        target="#black_steel_material",
    )
    scene = ET.SubElement(root, q("scene"))
    ET.SubElement(scene, q("instance_visual_scene"), url="#Scene")
    ET.indent(root, space="  ")
    ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)


def validate(mesh: Mesh) -> dict[str, float | int]:
    edges = Counter()
    degenerate = 0
    volume_times_six = 0.0
    for face in mesh.faces:
        a_index, b_index, c_index = face
        for edge in ((a_index, b_index), (b_index, c_index), (c_index, a_index)):
            edges[tuple(sorted(edge))] += 1
        a, b, c = (mesh.vertices[index] for index in face)
        area_twice = sqrt(sum(value * value for value in cross(subtract(b, a), subtract(c, a))))
        if area_twice < 1e-10:
            degenerate += 1
        b_cross_c = cross(b, c)
        volume_times_six += sum(a[axis] * b_cross_c[axis] for axis in range(3))
    xs, ys, zs = zip(*mesh.vertices)
    return {
        "vertices": len(mesh.vertices),
        "triangles": len(mesh.faces),
        "degenerate_triangles": degenerate,
        "non_manifold_edges": sum(count != 2 for count in edges.values()),
        "signed_volume_mm3": volume_times_six / 6.0,
        "x_size_mm": max(xs) - min(xs),
        "y_size_mm": max(ys) - min(ys),
        "z_size_mm": max(zs) - min(zs),
        "z_min_mm": min(zs),
        "z_max_mm": max(zs),
    }


def generate(spec: ScrewSpec, source_file: str) -> tuple[Path, dict[str, float | int]]:
    output_dir = Path(source_file).resolve().parents[3] / "3d_models" / spec.model_name
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{spec.model_name}.dae"
    mesh = build_screw(spec)
    stats = validate(mesh)
    expected = {
        "degenerate_triangles": 0,
        "non_manifold_edges": 0,
        "x_size_mm": spec.head_diameter,
        "y_size_mm": spec.head_diameter,
        "z_size_mm": spec.length,
        "z_min_mm": -spec.length,
        "z_max_mm": 0.0,
    }
    if stats["signed_volume_mm3"] <= 0.0:
        raise RuntimeError(f"Mesh winding is inverted: {stats}")
    for key, expected_value in expected.items():
        if abs(float(stats[key]) - expected_value) > 1e-6:
            raise RuntimeError(f"{key} is {stats[key]}, expected {expected_value}")
    write_dae(mesh, output, spec)
    return output, stats
