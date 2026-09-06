# M4 × 10 mm Type E Non-Flanged Threaded Insert

[Collection import, regeneration, and retention instructions](../README.md)

## 1. Model and placement

The SketchUp model is [M4x10_Type_E_NonFlanged_Threaded_Insert.dae](../../../3d_models/M4x10_Type_E_NonFlanged_Threaded_Insert/M4x10_Type_E_NonFlanged_Threaded_Insert.dae).

- Units: millimetres; Z-up.
- Origin: centre of the upper drive face.
- Orientation: insert extends exactly 10 mm along negative Z.
- The unheaded body can be installed below the wood surface.

## 2. Controlling dimensions

| Feature | Dimension |
| --- | ---: |
| Internal thread | M4 × 0.7 |
| Overall length | 10.0 mm |
| Maximum external-thread diameter | 8.5 mm |
| External-thread root diameter | 5.5 mm |
| Hex drive | 4.0 mm across flats |
| Suggested pilot hole | 5.6–6.0 mm |

## 3. Provenance and limitations

Dimensions and the non-flanged form come from [The Insert Company Type E record](https://www.theinsertcompany.com/type_e_threaded_insert_for_wood.php). External-thread pitch and crest form, bottom runout, hex depth, drive-to-bore transition, and four-lobed upper contour details are inferred from supplier imagery. The hidden M4 female helix is represented by a smooth 3.24 mm minor-diameter bore.

The model is a closed, outward-wound manifold containing 936 vertices and 1,872 triangles. Its 24-sided maximum-diameter approximation preserves the exact 8.5 mm X/Y envelope with approximately 0.036 mm maximum chord error.

## 4. Generator

[generate_m4_type_e_insert.py](../../../src/3d_models/M4x10_Type_E_NonFlanged_Threaded_Insert/generate_m4_type_e_insert.py)
