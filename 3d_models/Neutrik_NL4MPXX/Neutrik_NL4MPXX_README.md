# Neutrik NL4MPXX connector

The SketchUp import file is `Neutrik_NL4MPXX.dae`. It is a direct
OpenCascade tessellation of the Creo-generated `nl4mpxx.stp` supplied in the
project root.

## Import and placement

- In SketchUp, use **File > Import > COLLADA (`*.dae`)**.
- The DAE explicitly declares millimetres and Z-up coordinates.
- No scaling, rotation, centring, or origin relocation was applied. The
  original STEP coordinate system is preserved.
- Overall tessellated dimensions are 25.9 x 30.9 x 34.3 mm.
- Coordinate bounds are X -12.95 to 12.95 mm, Y -15.45 to 15.45 mm, and
  Z -27.25 to 7.05 mm.
- Make the imported object a SketchUp component before placing multiple
  instances.

## Conversion details

The source identifies itself as `NL4MPXX-4`, authored in Creo Parametric, and
declares millimetres. OpenCascade reads it as one valid solid containing 1,108
analytic B-rep faces. It does not contain STEP colour or presentation-style
records, so a dark graphite housing material was added to the DAE rather than
inventing per-part colour boundaries.

The mesh uses a 0.35 mm maximum linear deflection and 0.65 radian maximum
angular deflection. It contains 18,262 triangles, 17,428 face-local vertices,
and no degenerate triangles. Periodic CAD seams are retained as coincident
mesh seams; the source B-rep itself passes OpenCascade's validity check.

Source STEP SHA-256:

```text
AA7DDF218941F2284EE6E9C9E7E2591CA32B3B0ED0E6CA1A27EAEDB660CD6748
```

## Regeneration

The converter requires the no-VTK OpenCascade bindings:

```console
python -m pip install cadquery-ocp-novtk
python src/3d_models/Neutrik_NL4MPXX/generate_neutrik_nl4mpxx.py
python src/3d_models/render_preview.py Neutrik_NL4MPXX
```

The shared preview renderer reads the generated DAE directly, so OpenCascade
is needed only when converting the STEP source again.
