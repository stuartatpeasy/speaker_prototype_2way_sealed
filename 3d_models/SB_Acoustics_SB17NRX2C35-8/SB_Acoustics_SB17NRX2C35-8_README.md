# SB Acoustics SB17NRX2C35-8 SketchUp model

The primary file is `SB_Acoustics_SB17NRX2C35-8_SketchUp.dae`. COLLADA retains
the model's material colours and imports natively into SketchUp. An uncoloured
binary STL is included as a fallback.

## Import and placement

- In SketchUp, use **File > Import > COLLADA (`*.dae`)**.
- Units are declared as millimetres.
- The origin is the acoustic axis on the **rear mounting face of the flange**.
- The cone/front projects along positive Z.
- The motor extends along negative Z.
- With the component placed on a front-baffle mounting plane, its rear limit is
  exactly Z = -75 mm.

## Manufacturer-published dimensions used unchanged

| Feature | Dimension |
|---|---:|
| Frame outside diameter | 171.0 mm |
| Mounting-hole pitch circle | 159.0 mm |
| Mounting recesses | 4 x 8.5 mm diameter |
| Through holes | 4 x 4.3 mm diameter |
| Rear basket envelope | 144.9 mm diameter |
| Magnet outside diameter | 100.0 mm |
| Front flange thickness | 6.5 mm |
| Mounting depth | 75.0 mm |
| Overall depth | 85.9 mm |
| Front projection relative to mounting plane | 10.9 mm |
| Voice-coil diameter | 35.5 mm |
| Voice-coil winding height | 16.0 mm |

Sources:

- Manufacturer product page:
  <https://sbacoustics.com/product/6in-sb17nrx2c35-8-norex/>
- Manufacturer datasheet:
  <https://sbacoustics.com/wp-content/uploads/2020/02/6in-SB17NRX2C35-8.pdf>

## Model scope and inferred details

The cast basket, eight spokes, cone/surround profiles, spider, motor plate
thicknesses, pole vent, terminals, tinsel leads and label details were
estimated from the manufacturer imagery and publicly available product-angle
photographs. They are visually representative rather than manufacturing
drawings. None of these estimates changes a dimension published in the
datasheet.

The stepped mounting-hole sizes and their pitch circle are represented
accurately as coloured recess/void surfaces for layout and snapping. To keep
the mesh moderate, they are not boolean-cut through the cast flange.

This is a visual/layout assembly containing overlapping closed parts; the STL
is not intended as a single watertight 3D-printing solid.

The main 171 mm circumference uses 64 sides (maximum chord-to-true-circle
deviation approximately 0.103 mm). Less visible diaphragm, spider and motor
surfaces use lower radial resolutions to control polygon count. The generated
model contains 8,068 triangles.

The Python generator now produces the `.dae` only; the existing STL is a
legacy fallback. From the project root, regenerate the model and preview with:

```powershell
python src/3d_models/SB_Acoustics_SB17NRX2C35-8/generate_sb17nrx2c35_8.py
python src/3d_models/render_preview.py SB_Acoustics_SB17NRX2C35-8
```
