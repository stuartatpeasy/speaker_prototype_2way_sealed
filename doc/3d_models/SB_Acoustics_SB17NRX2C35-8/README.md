# SB Acoustics SB17NRX2C35-8 SketchUp Model

[Collection import, regeneration, and retention instructions](../README.md)

## 1. Model and placement

The primary model is [SB_Acoustics_SB17NRX2C35-8.dae](../../../3d_models/SB_Acoustics_SB17NRX2C35-8/SB_Acoustics_SB17NRX2C35-8.dae). The [STL](../../../3d_models/SB_Acoustics_SB17NRX2C35-8/SB_Acoustics_SB17NRX2C35-8.stl) is an uncoloured legacy fallback, not a watertight printing solid.

- Units: millimetres.
- Origin: acoustic axis on the rear mounting face of the flange.
- Orientation: cone/front along positive Z; motor along negative Z.
- Rear limit with the mounting plane at Z = 0: exactly `-75 mm`.

## 2. Manufacturer-published dimensions

| Feature | Dimension |
| --- | ---: |
| Frame outside diameter | 171.0 mm |
| Mounting-hole pitch circle | 159.0 mm |
| Mounting recesses / through holes | 4 × 8.5 mm / 4 × 4.3 mm |
| Rear basket envelope | 144.9 mm diameter |
| Magnet outside diameter | 100.0 mm |
| Front flange thickness | 6.5 mm |
| Mounting / overall depth | 75.0 mm / 85.9 mm |
| Front projection | 10.9 mm |
| Voice-coil diameter / winding height | 35.5 mm / 16.0 mm |

Sources: [manufacturer product page](https://sbacoustics.com/product/6in-sb17nrx2c35-8-norex/) and [datasheet](https://sbacoustics.com/wp-content/uploads/2020/02/6in-SB17NRX2C35-8.pdf).

## 3. Inferred geometry and limitations

Basket/spokes, cone and surround profiles, spider, motor plates, pole vent, terminals, tinsel leads, and labels are visually representative estimates from manufacturer and public product imagery. They do not override published dimensions.

Stepped mounting holes and pitch circle are accurate coloured reference surfaces but are not boolean-cut through the flange. The visual/layout assembly contains overlapping closed parts. Its 64-sided 171 mm circumference has approximately 0.103 mm maximum chord error; less visible parts use lower radial resolution. The generated model contains 8,068 triangles.

## 4. Generator

[generate_sb17nrx2c35_8.py](../../../src/3d_models/SB_Acoustics_SB17NRX2C35-8/generate_sb17nrx2c35_8.py) produces the correctly named `.dae` above; it does not recreate the legacy STL.
