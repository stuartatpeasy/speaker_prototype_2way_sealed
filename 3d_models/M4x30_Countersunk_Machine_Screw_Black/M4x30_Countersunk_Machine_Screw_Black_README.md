# M4 x 30 mm black countersunk machine screw

The SketchUp import file is
`M4x30_Countersunk_Machine_Screw_Black.dae`. It is a low-polygon model of the
common black M4 x 30 mm DIN 965-style Pozidriv countersunk machine screw.

## Import and placement

- In SketchUp, use **File > Import > COLLADA (`*.dae`)**.
- The DAE declares millimetres and Z-up coordinates.
- The origin is the centre of the flat upper head face.
- The screw extends exactly 30.0 mm along negative Z.
- Countersunk-screw length includes the head.
- Make the imported object a SketchUp component before placing multiple
  instances.

## Controlling dimensions

| Feature | Dimension |
|---|---:|
| Thread | M4 x 0.7, right hand |
| Overall length | 30.0 mm |
| Head diameter | 7.5 mm |
| Head height | 2.2 mm |
| Countersink angle | 90 degrees |
| Drive | PZ2 |
| Modelled thread-root diameter | 3.14 mm |

The product dimensions and black finish are taken from Accu's M4 x 30 mm
black Pozi countersunk screw listing. The 7.5 mm head diameter and 2.2 mm head
height also match the published DIN 965 M4 dimensions.

Sources:

- Accu, black M4 x 30 mm Pozi countersunk screw:
  <https://www.accu.co.uk/pozi-countersunk-screws/988564-SPK-M4-30-CS-BL>
- Westfield Fasteners, M4 DIN 965 dimensions:
  <https://www.westfieldfasteners.co.uk/Bolts-Screws-Metric/Machine-Screw-Phillips-Countersunk-M4x75-A2-Stainless.html>

## Model scope and polygon budget

The 24-sided head retains the exact 7.5 mm X/Y envelope. The right-hand
external thread is a continuous geometric helix with a flat, lightly
chamfered machine-screw end. The Pozidriv recess is modelled as a real cavity,
although its detailed wing shape and the 3.14 mm thread-root diameter are
representative because the product drawing does not fully dimension them.

The closed manifold mesh contains 1,562 vertices and 3,120 triangles. This is
deliberately much lighter than a manufacturing-detail fastener model while
retaining a readable thread and drive at enclosure-design scale.

From the project root, regenerate the DAE and preview with:

```console
python src/3d_models/M4x30_Countersunk_Machine_Screw_Black/generate_m4x30_countersunk_machine_screw.py
python src/3d_models/render_preview.py M4x30_Countersunk_Machine_Screw_Black
```
