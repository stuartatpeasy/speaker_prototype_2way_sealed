# M4 x 10 mm Type E non-flanged threaded insert

The SketchUp import file is
`M4x10_Type_E_NonFlanged_Threaded_Insert.dae`. The model uses millimetres and
retains a visible coarse external helix, an open 4 mm hex drive, and a through
M4 bore. Unlike a Type D insert, it has no sealing flange and can therefore be
driven below the wood surface.

## 1. Import And Placement

- In SketchUp, use **File > Import > COLLADA (`*.dae`)**.
- The DAE declares millimetres and Z-up coordinates.
- The origin is the centre of the upper drive face.
- The insert extends exactly 10 mm along negative Z.
- Make the imported object a SketchUp component before placing multiple
  instances.

## 2. Manufacturer-Published Dimensions

| Feature | Dimension |
|---|---:|
| Internal thread | M4 × 0.7 |
| Overall length, L | 10.0 mm |
| Maximum external-thread diameter, D1 | 8.5 mm |
| External-thread root diameter, D2 | 5.5 mm |
| Hex drive, K | 4.0 mm across flats |
| Suggested pilot hole | 5.6–6.0 mm |

Primary source:

- The Insert Company, unheaded zinc hex-drive Type E:
  <https://www.theinsertcompany.com/type_e_threaded_insert_for_wood.php>

The supplier describes Type E as an unheaded insert without a sealing flange,
allowing it to bottom out or be installed below the material surface.

## 3. Model Scope And Polygon Budget

The external thread pitch, crest form, bottom runout, hex depth, and drive-to-
bore transition are not dimensioned in the product table. They are visually
representative estimates based on the manufacturer's product photograph and
detail drawing. The four-lobed upper contour follows the manufacturer's top
view rather than adding a Type D-style circular flange.

The normally hidden M4 female helix is represented by a smooth 3.24 mm
minor-diameter bore. This preserves the visible opening and through-bore while
avoiding most of the geometry that made the original detailed Type D model
heavy.

The model contains 936 vertices and 1,872 triangles. It is a closed manifold
mesh with outward winding. Its 24-sided D1 approximation preserves the exact
8.5 mm X/Y envelope and has a maximum chord-to-true-circle deviation of
approximately 0.036 mm.

From the project root, regenerate the DAE and preview with:

```console
python src/3d_models/M4x10_Type_E_NonFlanged_Threaded_Insert/generate_m4_type_e_insert.py
python src/3d_models/render_preview.py M4x10_Type_E_NonFlanged_Threaded_Insert
```
