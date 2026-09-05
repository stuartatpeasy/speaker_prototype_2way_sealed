# SB Acoustics SB26STWGC-4 SketchUp model

The model file is `SB_Acoustics_SB26STWGC-4.dae`. COLLADA retains the model's
material colours and imports natively into SketchUp.

## 1. Import And Placement

- In SketchUp, use **File > Import > COLLADA (`*.dae`)**.
- Units are declared as millimetres.
- The origin is the acoustic axis on the **rear mounting face of the
  waveguide**.
- The front/waveguide projects along positive Z.
- The motor and rear chamber extend along negative Z.
- Placing Z = 0 on the baffle surface puts the rear limit at exactly
  Z = -42.1 mm.

## 2. Manufacturer-Published Dimensions Used Unchanged

| Feature | Dimension |
|---|---:|
| Waveguide/faceplate outside diameter | 103.8 mm |
| Mounting-hole pitch circle | 92.0 mm |
| Mounting recesses | 4 x 8.0 mm diameter |
| Through holes | 4 x 4.2 mm diameter |
| Rear/terminal envelope diameter | 82.8 mm |
| Motor diameter | 70.0 mm |
| Faceplate thickness | 6.0 mm |
| Mounting depth | 42.1 mm |
| Overall depth | 48.1 mm |
| Voice-coil diameter | 25.4 mm |
| Voice-coil winding height | 1.3 mm |

Sources:

- Manufacturer product page:
  <https://sbacoustics.com/product/sb26stwgc-4-fabric/>
- Manufacturer datasheet:
  <https://sbacoustics.com/wp-content/uploads/2020/05/SB26STWGC-4.pdf>
- Public multi-angle product imagery:
  <https://www.soundimports.eu/en/sb-acoustics-sb26stwgc-4.html>

## 3. Model Scope And Inferred Details

The waveguide curvature, dome/surround profiles, central adapter-boss shape,
motor plate thicknesses, rear chamber, pole vent, terminal construction and
labels were estimated from manufacturer and public product photographs. A
user-supplied side sketch of a physical production unit clarified that the
waveguide has a flat rear annulus blending into an approximately Ø64 mm
central boss with a 3.0 mm concave root fillet. The Ø70 motor overhangs this
boss and the opposed terminals define the larger Ø82.8 rear envelope. These
inferred details are visually representative rather than manufacturing
drawings. None changes a dimension published in the datasheet.

The stepped mounting-hole sizes and pitch circle are represented accurately
as coloured recess/void reference surfaces. To keep the mesh moderate, they
are not boolean-cut through the aluminium waveguide.

This is a visual/layout assembly containing overlapping parts and reference
surfaces; it is not intended as a watertight 3D-printing solid.

The main 103.8 mm circumference uses 64 sides, with a maximum
chord-to-true-circle deviation of approximately 0.062 mm. Less prominent
motor and inner surfaces use lower radial resolutions to control polygon
count. The 3 mm quarter-circle fillet uses four profile subdivisions, with a
maximum profile chord error of approximately 0.058 mm. The finished DAE
contains 5,714 triangles and the generator reports no degenerate triangles.

From the project root, regenerate the model and preview with:

```console
python src/3d_models/SB_Acoustics_SB26STWGC-4/generate_sb26stwgc_4.py
python src/3d_models/render_preview.py SB_Acoustics_SB26STWGC-4
```
