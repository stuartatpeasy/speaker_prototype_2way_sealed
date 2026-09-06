#!/usr/bin/env python3
"""Convert the supplied Neutrik NL4MPXX STEP solid to a SketchUp-ready DAE.

Conversion requires the OpenCascade Python bindings supplied by
``cadquery-ocp-novtk``. Preview rendering reads the generated DAE directly and
therefore does not require OpenCascade.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
from math import sqrt
from pathlib import Path
import xml.etree.ElementTree as ET


MODEL_NAME = "Neutrik_NL4MPXX"
SOURCE_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = Path(__file__).resolve().parents[3]
STEP_PATH = PROJECT_ROOT / "3d_models" / "nl4mpxx.stp"
OUTPUT_DIR = PROJECT_ROOT / "3d_models" / MODEL_NAME
DAE_PATH = OUTPUT_DIR / f"{MODEL_NAME}.dae"

LINEAR_DEFLECTION_MM = 0.35
ANGULAR_DEFLECTION_RAD = 0.65

MATERIALS = {
    "graphite_housing": {
        "diffuse": (0.055, 0.060, 0.065, 1.0),
        "specular": (0.18, 0.19, 0.20, 1.0),
        "shininess": 22.0,
    }
}

PREVIEW_CONFIG = {
    "title": "Neutrik NL4MPXX connector - converted STEP geometry",
    "views": (
        {"label": "Front three-quarter", "direction": (1.25, -1.55, 1.15)},
        {"label": "Rear three-quarter", "direction": (-1.25, -1.55, -1.05)},
    ),
    "view_margin": 42,
    "light_offset": (-0.45, -0.65, 1.35),
}


@dataclass
class MeshData:
    vertices: list[tuple[float, float, float]]
    faces: list[tuple[int, int, int]]
    normals: list[tuple[float, float, float]]
    materials: list[str]


def subtract(a, b):
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def length(vector):
    return sqrt(sum(component * component for component in vector))


def tessellate_step(
    step_path: Path,
    linear_deflection: float = LINEAR_DEFLECTION_MM,
    angular_deflection: float = ANGULAR_DEFLECTION_RAD,
) -> MeshData:
    try:
        from OCP.BRep import BRep_Tool
        from OCP.BRepMesh import BRepMesh_IncrementalMesh
        from OCP.IFSelect import IFSelect_RetDone
        from OCP.STEPControl import STEPControl_Reader
        from OCP.TopAbs import TopAbs_FACE, TopAbs_REVERSED
        from OCP.TopExp import TopExp_Explorer
        from OCP.TopLoc import TopLoc_Location
        from OCP.TopoDS import TopoDS
    except ImportError as error:
        raise RuntimeError(
            "STEP conversion requires cadquery-ocp-novtk. Install it or add "
            "its target directory to PYTHONPATH."
        ) from error

    reader = STEPControl_Reader()
    status = reader.ReadFile(str(step_path))
    if status != IFSelect_RetDone:
        raise RuntimeError(f"OpenCascade could not read {step_path}: {status}")
    if reader.TransferRoots() < 1:
        raise RuntimeError(f"No transferable shapes were found in {step_path}")
    shape = reader.OneShape()

    mesher = BRepMesh_IncrementalMesh(
        shape,
        linear_deflection,
        False,
        angular_deflection,
        True,
    )
    if not mesher.IsDone():
        raise RuntimeError("OpenCascade did not complete STEP tessellation")

    vertices: list[tuple[float, float, float]] = []
    faces: list[tuple[int, int, int]] = []
    normals: list[tuple[float, float, float]] = []
    explorer = TopExp_Explorer(shape, TopAbs_FACE)

    while explorer.More():
        face = TopoDS.Face_s(explorer.Current())
        location = TopLoc_Location()
        triangulation = BRep_Tool.Triangulation_s(face, location)
        if triangulation is None:
            explorer.Next()
            continue

        transform = location.Transformation()
        base_index = len(vertices)
        local_vertices = []
        for node_index in range(1, triangulation.NbNodes() + 1):
            point = triangulation.Node(node_index).Transformed(transform)
            local_vertices.append((point.X(), point.Y(), point.Z()))

        local_faces = []
        for triangle_index in range(1, triangulation.NbTriangles() + 1):
            a, b, c = triangulation.Triangle(triangle_index).Get()
            a -= 1
            b -= 1
            c -= 1
            if face.Orientation() == TopAbs_REVERSED:
                b, c = c, b
            raw_normal = cross(
                subtract(local_vertices[b], local_vertices[a]),
                subtract(local_vertices[c], local_vertices[a]),
            )
            if length(raw_normal) < 1e-12:
                continue
            local_faces.append((a, b, c))

        local_normal_sums = [[0.0, 0.0, 0.0] for _ in local_vertices]
        for a, b, c in local_faces:
            raw_normal = cross(
                subtract(local_vertices[b], local_vertices[a]),
                subtract(local_vertices[c], local_vertices[a]),
            )
            for index in (a, b, c):
                local_normal_sums[index][0] += raw_normal[0]
                local_normal_sums[index][1] += raw_normal[1]
                local_normal_sums[index][2] += raw_normal[2]

        vertices.extend(local_vertices)
        for normal_sum in local_normal_sums:
            magnitude = length(normal_sum)
            if magnitude < 1e-12:
                normals.append((0.0, 0.0, 1.0))
            else:
                normals.append(tuple(component / magnitude for component in normal_sum))
        faces.extend(
            (base_index + a, base_index + b, base_index + c)
            for a, b, c in local_faces
        )
        explorer.Next()

    if not faces:
        raise RuntimeError("STEP tessellation produced no triangles")

    mesh = MeshData(
        vertices=vertices,
        faces=faces,
        normals=normals,
        materials=["graphite_housing"] * len(faces),
    )
    stats = validate_mesh(mesh)
    if stats["signed_volume_mm3"] < 0.0:
        mesh.faces = [(a, c, b) for a, b, c in mesh.faces]
        mesh.normals = [tuple(-component for component in normal) for normal in mesh.normals]
    return mesh


def validate_mesh(mesh: MeshData) -> dict[str, object]:
    xs, ys, zs = zip(*mesh.vertices)
    degenerate = 0
    signed_volume_times_six = 0.0
    welded = {}
    welded_indices = []
    for vertex in mesh.vertices:
        key = tuple(round(component, 6) for component in vertex)
        if key not in welded:
            welded[key] = len(welded)
        welded_indices.append(welded[key])

    edge_counts = Counter()
    for a_index, b_index, c_index in mesh.faces:
        a, b, c = (
            mesh.vertices[a_index],
            mesh.vertices[b_index],
            mesh.vertices[c_index],
        )
        normal = cross(subtract(b, a), subtract(c, a))
        if length(normal) < 1e-12:
            degenerate += 1
        signed_volume_times_six += sum(
            a[axis] * cross(b, c)[axis] for axis in range(3)
        )
        wa, wb, wc = (
            welded_indices[a_index],
            welded_indices[b_index],
            welded_indices[c_index],
        )
        for edge in ((wa, wb), (wb, wc), (wc, wa)):
            edge_counts[tuple(sorted(edge))] += 1

    return {
        "vertices": len(mesh.vertices),
        "welded_vertices": len(welded),
        "triangles": len(mesh.faces),
        "degenerate_triangles": degenerate,
        "non_manifold_edges_after_weld": sum(
            count != 2 for count in edge_counts.values()
        ),
        "signed_volume_mm3": signed_volume_times_six / 6.0,
        "bounds_mm": (
            (min(xs), min(ys), min(zs)),
            (max(xs), max(ys), max(zs)),
        ),
        "dimensions_mm": (
            max(xs) - min(xs),
            max(ys) - min(ys),
            max(zs) - min(zs),
        ),
    }


def write_dae(mesh: MeshData, output_path: Path, source_hash: str) -> None:
    namespace = "http://www.collada.org/2005/11/COLLADASchema"
    ET.register_namespace("", namespace)
    q = lambda tag: f"{{{namespace}}}{tag}"
    root = ET.Element(q("COLLADA"), version="1.4.1")

    asset = ET.SubElement(root, q("asset"))
    contributor = ET.SubElement(asset, q("contributor"))
    ET.SubElement(contributor, q("authoring_tool")).text = (
        "Codex OpenCascade STEP-to-COLLADA converter"
    )
    stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )
    ET.SubElement(asset, q("created")).text = stamp
    ET.SubElement(asset, q("modified")).text = stamp
    ET.SubElement(asset, q("unit"), name="millimeter", meter="0.001")
    ET.SubElement(asset, q("up_axis")).text = "Z_UP"
    ET.SubElement(asset, q("subject")).text = (
        f"Converted from nl4mpxx.stp; SHA-256 {source_hash}"
    )

    effects = ET.SubElement(root, q("library_effects"))
    effect = ET.SubElement(effects, q("effect"), id="graphite_housing_effect")
    profile = ET.SubElement(effect, q("profile_COMMON"))
    technique = ET.SubElement(profile, q("technique"), sid="common")
    phong = ET.SubElement(technique, q("phong"))
    material = MATERIALS["graphite_housing"]
    diffuse = ET.SubElement(phong, q("diffuse"))
    ET.SubElement(diffuse, q("color")).text = " ".join(
        str(value) for value in material["diffuse"]
    )
    specular = ET.SubElement(phong, q("specular"))
    ET.SubElement(specular, q("color")).text = " ".join(
        str(value) for value in material["specular"]
    )
    shininess = ET.SubElement(phong, q("shininess"))
    ET.SubElement(shininess, q("float")).text = str(material["shininess"])

    library_materials = ET.SubElement(root, q("library_materials"))
    material_xml = ET.SubElement(
        library_materials,
        q("material"),
        id="graphite_housing_material",
        name="Graphite connector housing",
    )
    ET.SubElement(
        material_xml, q("instance_effect"), url="#graphite_housing_effect"
    )

    geometries = ET.SubElement(root, q("library_geometries"))
    geometry = ET.SubElement(
        geometries,
        q("geometry"),
        id="nl4mpxx_geometry",
        name="Neutrik NL4MPXX",
    )
    xml_mesh = ET.SubElement(geometry, q("mesh"))

    def add_source(source_id, array_id, values, parameters):
        source = ET.SubElement(xml_mesh, q("source"), id=source_id)
        flat = [component for value in values for component in value]
        array = ET.SubElement(
            source, q("float_array"), id=array_id, count=str(len(flat))
        )
        array.text = " ".join(f"{value:.9g}" for value in flat)
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

    add_source("position_source", "position_array", mesh.vertices, ("X", "Y", "Z"))
    add_source("normal_source", "normal_array", mesh.normals, ("X", "Y", "Z"))
    vertices = ET.SubElement(xml_mesh, q("vertices"), id="nl4mpxx_vertices")
    ET.SubElement(vertices, q("input"), semantic="POSITION", source="#position_source")
    triangles = ET.SubElement(
        xml_mesh,
        q("triangles"),
        count=str(len(mesh.faces)),
        material="graphite_housing_symbol",
    )
    ET.SubElement(
        triangles,
        q("input"),
        semantic="VERTEX",
        source="#nl4mpxx_vertices",
        offset="0",
    )
    ET.SubElement(
        triangles,
        q("input"),
        semantic="NORMAL",
        source="#normal_source",
        offset="1",
    )
    ET.SubElement(triangles, q("p")).text = " ".join(
        str(value)
        for face in mesh.faces
        for vertex_index in face
        for value in (vertex_index, vertex_index)
    )

    scenes = ET.SubElement(root, q("library_visual_scenes"))
    visual_scene = ET.SubElement(scenes, q("visual_scene"), id="Scene", name="Scene")
    node = ET.SubElement(
        visual_scene,
        q("node"),
        id=MODEL_NAME,
        name="Neutrik NL4MPXX",
        type="NODE",
    )
    instance = ET.SubElement(node, q("instance_geometry"), url="#nl4mpxx_geometry")
    bind = ET.SubElement(instance, q("bind_material"))
    common = ET.SubElement(bind, q("technique_common"))
    ET.SubElement(
        common,
        q("instance_material"),
        symbol="graphite_housing_symbol",
        target="#graphite_housing_material",
    )
    scene = ET.SubElement(root, q("scene"))
    ET.SubElement(scene, q("instance_visual_scene"), url="#Scene")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    ET.indent(root, space="  ")
    ET.ElementTree(root).write(output_path, encoding="utf-8", xml_declaration=True)


def load_generated_dae(path: Path = DAE_PATH) -> MeshData:
    """Load the generated DAE for the shared preview renderer."""
    root = ET.parse(path).getroot()
    position_array = root.find(".//{*}float_array[@id='position_array']")
    triangles = root.find(".//{*}triangles")
    if position_array is None or triangles is None:
        raise RuntimeError(f"Expected geometry arrays were not found in {path}")
    values = [float(value) for value in position_array.text.split()]
    vertices = [tuple(values[index:index + 3]) for index in range(0, len(values), 3)]
    inputs = triangles.findall("./{*}input")
    stride = max(int(item.attrib.get("offset", "0")) for item in inputs) + 1
    vertex_offset = next(
        int(item.attrib.get("offset", "0"))
        for item in inputs
        if item.attrib.get("semantic") == "VERTEX"
    )
    p = triangles.find("./{*}p")
    if p is None:
        raise RuntimeError(f"Triangle index data was not found in {path}")
    indices = [int(value) for value in p.text.split()]
    corners = indices[vertex_offset::stride]
    faces = [tuple(corners[index:index + 3]) for index in range(0, len(corners), 3)]
    return MeshData(
        vertices=vertices,
        faces=faces,
        normals=[],
        materials=["graphite_housing"] * len(faces),
    )


def build_preview_mesh():
    return load_generated_dae()


def convert(
    linear_deflection: float = LINEAR_DEFLECTION_MM,
    angular_deflection: float = ANGULAR_DEFLECTION_RAD,
) -> tuple[Path, dict[str, object]]:
    source_hash = hashlib.sha256(STEP_PATH.read_bytes()).hexdigest()
    mesh = tessellate_step(STEP_PATH, linear_deflection, angular_deflection)
    stats = validate_mesh(mesh)
    if stats["degenerate_triangles"]:
        raise RuntimeError(f"Degenerate triangles remain: {stats}")
    if stats["signed_volume_mm3"] <= 0.0:
        raise RuntimeError(f"Mesh winding/volume is invalid: {stats}")
    write_dae(mesh, DAE_PATH, source_hash)
    return DAE_PATH, stats


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--linear-deflection",
        type=float,
        default=LINEAR_DEFLECTION_MM,
        help="Maximum chordal deflection in millimetres (default: %(default)s)",
    )
    parser.add_argument(
        "--angular-deflection",
        type=float,
        default=ANGULAR_DEFLECTION_RAD,
        help="Maximum angular deflection in radians (default: %(default)s)",
    )
    args = parser.parse_args()
    output, stats = convert(args.linear_deflection, args.angular_deflection)
    dimensions = stats["dimensions_mm"]
    print(f"Wrote {output}")
    print(
        f"Mesh: {stats['vertices']} face-local vertices, "
        f"{stats['welded_vertices']} welded vertices, "
        f"{stats['triangles']} triangles"
    )
    print(
        f"Dimensions: {dimensions[0]:.6f} x {dimensions[1]:.6f} x "
        f"{dimensions[2]:.6f} mm; bounds {stats['bounds_mm']}"
    )
    print(
        f"Validation: {stats['degenerate_triangles']} degenerate triangles, "
        f"{stats['non_manifold_edges_after_weld']} non-manifold edges after weld, "
        f"signed volume {stats['signed_volume_mm3']:.3f} mm^3"
    )


if __name__ == "__main__":
    main()
