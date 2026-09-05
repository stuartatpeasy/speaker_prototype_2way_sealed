# M4 x 10 mm Type D flanged threaded insert

For an enclosure containing many instances, use
`M4x10_Type_D_Flanged_Threaded_Insert_SketchUp_LowPoly.dae`.  It retains the
published dimensions, flange, hex drive, through bore, and visible helical
external thread in approximately 1,900 triangles.  The original
`M4x10_Type_D_Flanged_Threaded_Insert.dae` retains the modelled internal M4
thread and is intended for close-up rendering.  Matching `.stl` files are
included as fallbacks for SketchUp installations with the STL importer enabled.

## 1. Placement And Units

- Units: millimetres (`.dae` declares millimetres explicitly; `.stl` units are
  implicit but its coordinates are in millimetres).
- Origin: centre of the upper flange face.
- Orientation: the flange face lies in the XY plane and the insert extends
  10 mm along negative Z.
- SketchUp import: **File > Import**, select **COLLADA File (`*.dae`)**, and
  leave **Merge Coplanar Faces** enabled if that option is offered.
- After import, make the object a SketchUp component before copying it to all
  mounting positions; component instances keep the enclosure model lighter.

## 2. Modelled Dimensions

| Feature | Dimension |
|---|---:|
| Overall length, L | 10.0 mm |
| Flange / maximum diameter, D1 | 8.5 mm |
| Body root diameter, D2 | 5.5 mm |
| Internal machine thread | M4 x 0.7 |
| Hex drive, K | 4.0 mm across flats |
| Suggested pilot hole (reference only) | 5.6-6.0 mm |

The envelope dimensions are from The Insert Company (UK) headed zinc
hex-drive / Type D table.  That table does not specify flange thickness, hex
recess depth, or the exact die-cast external tooth form, so those small details
are representative rather than tied to a particular production batch.  For a
machining template, confirm the actual insert in hand and size the pilot hole
to the MDF/plywood and installation tests.

Source: <https://www.theinsertcompany.com/type_d_threaded_insert_for_wood.php>

Both versions are closed, manifold triangle meshes.  The low-poly version uses
a smooth 3.24 mm M4 minor-diameter bore instead of modelling the normally
invisible internal helix.  Its 24-sided flange has the exact 8.5 mm X/Y envelope
and a maximum chord-to-true-circle deviation of 0.036 mm.

The Python generators now produce COLLADA only; the existing STL files are
legacy fallbacks. From the project root, regenerate the models with:

```console
python src/3d_models/M4x10_Type_D_Flanged_Threaded_Insert/generate_m4_type_d_insert.py
python src/3d_models/M4x10_Type_D_Flanged_Threaded_Insert_LowPoly/generate_m4_type_d_insert_low_poly.py
```

The common preview entry point accepts either model-folder name:

```console
python src/3d_models/render_preview.py M4x10_Type_D_Flanged_Threaded_Insert
python src/3d_models/render_preview.py M4x10_Type_D_Flanged_Threaded_Insert_LowPoly
```
