# Neutrik NL4MPXX Connector

[Collection import, regeneration, and retention instructions](../README.md)

## 1. Model, source, and placement

The SketchUp model is [Neutrik_NL4MPXX.dae](../../../3d_models/Neutrik_NL4MPXX/Neutrik_NL4MPXX.dae). It is an OpenCascade tessellation of the retained [3d_models/nl4mpxx.stp](../../../3d_models/nl4mpxx.stp).

- Units: millimetres; Z-up.
- Origin/orientation: the STEP coordinate system is preserved without scaling, rotation, centring, or relocation.
- Dimensions: 25.9 × 30.9 × 34.3 mm.
- Bounds: X `-12.95` to `12.95` mm; Y `-15.45` to `15.45` mm; Z `-27.25` to `7.05` mm.

## 2. Provenance and conversion limits

The STEP identifies `NL4MPXX-4`, Creo Parametric, and millimetres. OpenCascade reads one valid solid with 1,108 analytic B-rep faces. Because the source contains no STEP colour/presentation records, the DAE adds one dark graphite housing material rather than inferred part colours.

Source STEP SHA-256:

```text
AA7DDF218941F2284EE6E9C9E7E2591CA32B3B0ED0E6CA1A27EAEDB660CD6748
```

The converter uses `0.35 mm` linear and `0.65 rad` angular deflection. The result contains 18,262 triangles, 17,428 face-local vertices, and no degenerate triangles. Periodic CAD seams remain coincident mesh seams; the source B-rep passes OpenCascade validity.

## 3. Generator and dependency

[generate_neutrik_nl4mpxx.py](../../../src/3d_models/Neutrik_NL4MPXX/generate_neutrik_nl4mpxx.py) reads the retained STEP path above. Conversion additionally requires:

```console
python -m pip install cadquery-ocp-novtk
```

The shared preview renderer reads the generated DAE directly, so OpenCascade is needed only for STEP conversion.
