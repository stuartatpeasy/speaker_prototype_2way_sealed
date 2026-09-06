# M4 × 10 mm Type D Flanged Threaded Insert

[Collection import, regeneration, and retention instructions](../README.md)

## 1. Preferred variant and placement

Use the [low-poly DAE](../../../3d_models/M4x10_Type_D_Flanged_Threaded_Insert_LowPoly/M4x10_Type_D_Flanged_Threaded_Insert_LowPoly.dae) for repeated cabinet instances. It retains the published envelope, flange, hex drive, through bore, and visible external helix in approximately 1,900 triangles. Use the [detailed DAE](../../../3d_models/M4x10_Type_D_Flanged_Threaded_Insert/M4x10_Type_D_Flanged_Threaded_Insert.dae) only for close views requiring the modelled internal M4 thread.

- Units: millimetres.
- Origin: centre of the upper flange face.
- Orientation: flange face in the XY plane; insert extends 10 mm along negative Z.

## 2. Controlling dimensions

| Feature | Dimension |
| --- | ---: |
| Overall length | 10.0 mm |
| Flange / maximum diameter | 8.5 mm |
| Body root diameter | 5.5 mm |
| Internal machine thread | M4 × 0.7 |
| Hex drive | 4.0 mm across flats |
| Suggested pilot hole, reference only | 5.6–6.0 mm |

## 3. Provenance and limitations

Envelope dimensions come from [The Insert Company Type D table](https://www.theinsertcompany.com/type_d_threaded_insert_for_wood.php). Flange thickness, hex depth, and die-cast external tooth form are not fully specified and are representative. Confirm the actual insert and pilot-hole behaviour in the cabinet material before fabrication.

Both variants are closed manifold meshes. The low-poly model substitutes a smooth 3.24 mm M4 minor-diameter bore for the hidden internal helix. Its 24-sided flange preserves the exact 8.5 mm X/Y envelope with approximately 0.036 mm maximum chord error. Retained [detailed STL](../../../3d_models/M4x10_Type_D_Flanged_Threaded_Insert/M4x10_Type_D_Flanged_Threaded_Insert.stl) and [low-poly STL](../../../3d_models/M4x10_Type_D_Flanged_Threaded_Insert_LowPoly/M4x10_Type_D_Flanged_Threaded_Insert_LowPoly.stl) files are legacy fallbacks.

## 4. Generators

- [Detailed generator](../../../src/3d_models/M4x10_Type_D_Flanged_Threaded_Insert/generate_m4_type_d_insert.py)
- [Low-poly generator](../../../src/3d_models/M4x10_Type_D_Flanged_Threaded_Insert_LowPoly/generate_m4_type_d_insert_low_poly.py)

Use the low-poly folder name with the shared preview renderer when verifying the preferred assembly variant.
