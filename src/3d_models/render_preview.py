#!/usr/bin/env python3
"""Render a QA preview for any generated model in ``src/3d_models``.

Each generator may expose a ``PREVIEW_CONFIG`` dictionary to customise its
camera views, title, material fallback, and canvas size. The rasterisation,
lighting, labels, output naming, and artifact-path handling stay here so new
models do not need their own copy of the rendering code.
"""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont


SOURCE_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = SOURCE_ROOT.parents[1]
ARTIFACT_ROOT = PROJECT_ROOT / "3d_models"


def unit(vector):
    vector = np.asarray(vector, dtype=float)
    length = np.linalg.norm(vector)
    if length == 0.0:
        raise ValueError("Cannot normalise a zero-length vector")
    return vector / length


def load_generator(model_name):
    model_source = SOURCE_ROOT / model_name
    candidates = sorted(model_source.glob("generate_*.py"))
    if len(candidates) != 1:
        raise RuntimeError(
            f"Expected one generator under {model_source}, found {len(candidates)}"
        )
    generator_path = candidates[0]
    # Generator modules may share code with a sibling model source directory.
    sys.path.insert(0, str(SOURCE_ROOT))
    sys.path.insert(0, str(model_source))
    spec = importlib.util.spec_from_file_location(
        f"model_generator_{model_name}", generator_path
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {generator_path}")
    module = importlib.util.module_from_spec(spec)
    # Some standard-library features (notably ``dataclasses``) resolve type
    # metadata through ``sys.modules`` while a module is executing. Mirror the
    # normal import machinery instead of executing an unregistered module.
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        sys.modules.pop(spec.name, None)
        raise
    return module


def build_mesh(generator):
    for function_name in (
        "build_preview_mesh",
        "build_model",
        "build_low_poly_mesh",
        "build_mesh",
    ):
        function = getattr(generator, function_name, None)
        if callable(function):
            return function()
    raise RuntimeError("Generator exposes no recognised mesh-building function")


def face_colour(mesh, face_index, materials, base_colour, normal, light, view):
    if materials and hasattr(mesh, "materials"):
        definition = materials[mesh.materials[face_index]]
        base = np.array(definition["diffuse"][:3], dtype=float) * 255.0
        shininess = float(definition.get("shininess", 8.0))
    else:
        base = np.asarray(base_colour, dtype=float)
        shininess = 18.0
    diffuse = max(0.0, float(np.dot(normal, light)))
    half_vector = unit(light + view)
    specular = max(0.0, float(np.dot(normal, half_vector)))
    specular **= max(3.0, shininess * 0.55)
    return np.clip(
        base * (0.38 + 0.72 * diffuse) + 75.0 * specular,
        0,
        255,
    ).astype(np.uint8)


def render_view(mesh, direction, width, height, config, materials):
    vertices = np.asarray(mesh.vertices, dtype=float).copy()
    faces = np.asarray(mesh.faces, dtype=int)
    view = unit(direction)
    helper = np.array((0.0, 0.0, 1.0))
    if abs(np.dot(helper, view)) > 0.94:
        helper = np.array((0.0, 1.0, 0.0))
    right = unit(np.cross(helper, view))
    up = unit(np.cross(view, right))
    projected = np.column_stack((vertices @ right, vertices @ up, vertices @ view))

    margin = int(config.get("view_margin", 34))
    x_min, y_min = projected[:, :2].min(axis=0)
    x_max, y_max = projected[:, :2].max(axis=0)
    scale = min(
        (width - 2 * margin) / (x_max - x_min),
        (height - 2 * margin) / (y_max - y_min),
    )
    screen = np.empty_like(projected)
    screen[:, 0] = width / 2 + (projected[:, 0] - (x_min + x_max) / 2) * scale
    screen[:, 1] = height / 2 - (projected[:, 1] - (y_min + y_max) / 2) * scale
    screen[:, 2] = projected[:, 2]

    yy = np.linspace(0.0, 1.0, height)[:, None, None]
    top = np.array(config.get("background_top", (250, 251, 252)), dtype=float)
    bottom = np.array(config.get("background_bottom", (221, 228, 232)), dtype=float)
    pixels = np.repeat(
        top[None, None, :] * (1.0 - yy) + bottom[None, None, :] * yy,
        width,
        axis=1,
    ).astype(np.uint8)
    z_buffer = np.full((height, width), -np.inf, dtype=float)

    triangles = vertices[faces]
    raw_normals = np.cross(
        triangles[:, 1] - triangles[:, 0],
        triangles[:, 2] - triangles[:, 0],
    )
    lengths = np.linalg.norm(raw_normals, axis=1)
    if np.any(lengths == 0.0):
        raise RuntimeError("Preview mesh contains a degenerate triangle")
    normals = raw_normals / lengths[:, None]
    light_offset = unit(config.get("light_offset", (-0.35, -0.55, 1.15)))
    light = unit(view + light_offset)
    base_colour = config.get("base_colour", (170.0, 179.0, 184.0))

    for face_index in np.argsort(np.mean(screen[faces, 2], axis=1)):
        face = faces[face_index]
        face_normal = normals[face_index]
        if np.dot(face_normal, view) <= 0.0:
            continue
        triangle = screen[face]
        x0, y0, z0 = triangle[0]
        x1, y1, z1 = triangle[1]
        x2, y2, z2 = triangle[2]
        min_x = max(0, int(np.floor(min(x0, x1, x2))))
        max_x = min(width - 1, int(np.ceil(max(x0, x1, x2))))
        min_y = max(0, int(np.floor(min(y0, y1, y2))))
        max_y = min(height - 1, int(np.ceil(max(y0, y1, y2))))
        if min_x > max_x or min_y > max_y:
            continue
        denominator = (y1 - y2) * (x0 - x2) + (x2 - x1) * (y0 - y2)
        if abs(denominator) < 1e-10:
            continue
        xs = np.arange(min_x, max_x + 1, dtype=float) + 0.5
        ys = np.arange(min_y, max_y + 1, dtype=float) + 0.5
        xx, yy_grid = np.meshgrid(xs, ys)
        w0 = ((y1 - y2) * (xx - x2) + (x2 - x1) * (yy_grid - y2)) / denominator
        w1 = ((y2 - y0) * (xx - x2) + (x0 - x2) * (yy_grid - y2)) / denominator
        w2 = 1.0 - w0 - w1
        inside = (w0 >= -1e-8) & (w1 >= -1e-8) & (w2 >= -1e-8)
        if not inside.any():
            continue
        depth = w0 * z0 + w1 * z1 + w2 * z2
        old_depth = z_buffer[min_y:max_y + 1, min_x:max_x + 1]
        visible = inside & (depth > old_depth)
        if not visible.any():
            continue
        colour = face_colour(
            mesh,
            face_index,
            materials,
            base_colour,
            face_normal,
            light,
            view,
        )
        crop = pixels[min_y:max_y + 1, min_x:max_x + 1]
        crop[visible] = colour
        old_depth[visible] = depth[visible]

    return Image.fromarray(pixels, mode="RGB")


def render_preview(model_name):
    generator = load_generator(model_name)
    mesh = build_mesh(generator)
    materials = getattr(generator, "MATERIALS", None)
    config = dict(getattr(generator, "PREVIEW_CONFIG", {}))
    views = config.get(
        "views",
        (
            {"label": "Front three-quarter", "direction": (1.25, -1.55, 1.20)},
            {"label": "Rear three-quarter", "direction": (-1.25, -1.55, -1.05)},
        ),
    )
    view_width = int(config.get("view_width", 720))
    view_height = int(config.get("view_height", 650))
    header_height = int(config.get("header_height", 90))
    canvas = Image.new(
        "RGB",
        (view_width * len(views), view_height + header_height),
        config.get("canvas_colour", (244, 247, 249)),
    )
    draw = ImageDraw.Draw(canvas)
    title_font = ImageFont.load_default(size=int(config.get("title_size", 24)))
    label_font = ImageFont.load_default(size=int(config.get("label_size", 17)))
    title = config.get("title", model_name.replace("_", " "))
    draw.text((28, 22), title, fill=(38, 44, 48), font=title_font)

    for index, view_config in enumerate(views):
        image = render_view(
            mesh,
            view_config["direction"],
            view_width,
            view_height,
            config,
            materials,
        )
        x = index * view_width
        canvas.paste(image, (x, header_height))
        draw.text(
            (x + 28, 58),
            view_config.get("label", f"View {index + 1}"),
            fill=(78, 86, 91),
            font=label_font,
        )
        if index:
            draw.line(
                (x, header_height - 2, x, canvas.height - 20),
                fill=(185, 192, 196),
                width=1,
            )

    output_dir = ARTIFACT_ROOT / model_name
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / config.get("output_name", f"{model_name}_preview.png")
    canvas.save(output, optimize=True)
    print(f"Wrote {output}: {canvas.width} x {canvas.height}")
    return output


def main():
    parser = argparse.ArgumentParser(
        description="Render the QA preview for a generated 3D model."
    )
    parser.add_argument(
        "model_name",
        help="Model folder name beneath src/3d_models and 3d_models.",
    )
    args = parser.parse_args()
    render_preview(args.model_name)


if __name__ == "__main__":
    main()
