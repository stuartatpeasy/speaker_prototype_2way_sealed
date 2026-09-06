# SB Acoustics SB26STWGC-4 SketchUp Model

[Collection import, regeneration, and retention instructions](../README.md)

## 1. Model and placement

The model is [SB_Acoustics_SB26STWGC-4.dae](../../../3d_models/SB_Acoustics_SB26STWGC-4/SB_Acoustics_SB26STWGC-4.dae).

- Units: millimetres.
- Origin: acoustic axis on the rear mounting face of the waveguide.
- Orientation: waveguide/front along positive Z; motor and chamber along negative Z.
- Rear limit with the mounting plane at Z = 0: exactly `-42.1 mm`.

## 2. Manufacturer-published dimensions

| Feature | Dimension |
| --- | ---: |
| Waveguide outside diameter | 103.8 mm |
| Mounting-hole pitch circle | 92.0 mm |
| Mounting recesses / through holes | 4 × 8.0 mm / 4 × 4.2 mm |
| Rear/terminal envelope | 82.8 mm diameter |
| Motor diameter | 70.0 mm |
| Faceplate thickness | 6.0 mm |
| Mounting / overall depth | 42.1 mm / 48.1 mm |
| Voice-coil diameter / winding height | 25.4 mm / 1.3 mm |

Sources: [manufacturer product page](https://sbacoustics.com/product/sb26stwgc-4-fabric/), [datasheet](https://sbacoustics.com/wp-content/uploads/2020/05/SB26STWGC-4.pdf), and [public multi-angle imagery](https://www.soundimports.eu/en/sb-acoustics-sb26stwgc-4.html).

## 3. Inferred geometry and limitations

Waveguide and dome/surround profiles, adapter boss, motor plates, rear chamber, pole vent, terminals, and labels are visually representative estimates. A user-supplied production-unit sketch established a flat rear annulus blending into an approximately 64 mm central boss with a 3.0 mm concave root fillet; the 70 mm motor overhangs the boss and opposed terminals define the 82.8 mm envelope. These inferences do not override published dimensions.

Mounting recesses and holes are accurate coloured reference surfaces but are not boolean-cut. The visual/layout assembly is not a watertight printing solid. The 64-sided waveguide circumference has approximately 0.062 mm maximum chord error; the four-subdivision root fillet has approximately 0.058 mm maximum profile chord error. The DAE contains 5,714 triangles and the generator reports no degenerate triangles.

## 4. Generator

[generate_sb26stwgc_4.py](../../../src/3d_models/SB_Acoustics_SB26STWGC-4/generate_sb26stwgc_4.py)
