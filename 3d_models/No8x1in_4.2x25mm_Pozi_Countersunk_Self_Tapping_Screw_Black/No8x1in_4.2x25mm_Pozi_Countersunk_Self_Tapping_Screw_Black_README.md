# No. 8 x 1 in (4.2 x 25 mm) black countersunk self-tapping screw

The SketchUp import file is
`No8x1in_4.2x25mm_Pozi_Countersunk_Self_Tapping_Screw_Black.dae`. It is a
low-polygon model of a black DIN 7982 C Z-style Pozidriv countersunk
self-tapping screw.

## Import and placement

- In SketchUp, use **File > Import > COLLADA (`*.dae`)**.
- The DAE declares millimetres and Z-up coordinates.
- The origin is the centre of the flat upper head face.
- The screw extends exactly 25.0 mm along negative Z, including its head.
- The trade size is 1 inch; the requested metric nominal length of 25 mm is
  used as the controlling model dimension.
- Make the imported object a SketchUp component before placing multiple
  instances.

## Controlling dimensions

| Feature | Dimension |
|---|---:|
| Thread | ST4.2 x 1.4, right hand |
| Overall length | 25.0 mm |
| Head diameter | 8.1 mm |
| Head height | 2.5 mm |
| Countersink angle | 80 degrees |
| Drive | PZ2 |
| Point length | 3.7 mm |
| Modelled thread-root diameter | 3.10 mm |

The exact black No. 8 x 1 in product listing supplies the 4.2 x 25 mm size,
PZ2 drive, 8.1 mm head diameter, 2.5 mm head height, and DIN 7982 designation.
The standards table supplies the 1.4 mm pitch and 3.7 mm maximum Type C point
length.

Sources:

- Bolt World, No. 8 x 1 in black passivated Pozi countersunk self-tapper:
  <https://boltworld.co.uk/products/no-8-x-1-4-2-x-25mm-pozi-countersunk-self-tapping-screws-black-passivated-zinc-plated-din-7982/>
- Accu, black No. 8 x 1 in Pozi countersunk self-tapping screw:
  <https://www.accu.co.uk/self-tapping-pozi-countersunk-screws/163584-SPKT-No-8-1-A2-BL>
- Westfield Fasteners, DIN 7982 / ISO 7050 dimensions:
  <https://www.westfieldfasteners.co.uk/Standards/TappingScrew-PoziCsk.html>

## Model scope and polygon budget

The 24-sided head retains the exact 8.1 mm X/Y envelope. The right-hand coarse
thread is a continuous geometric helix and blends into a Type C/AB-style
tapered point. The Pozidriv recess is modelled as a real cavity. Its detailed
wing form and the 3.10 mm thread-root diameter are representative because
those features are not fully dimensioned in the cited product drawings.

The closed manifold mesh contains 890 vertices and 1,776 triangles. It is
intended to remain responsive when used repeatedly in a SketchUp assembly.

From the project root, regenerate the DAE and preview with:

```powershell
python src/3d_models/No8x1in_4.2x25mm_Pozi_Countersunk_Self_Tapping_Screw_Black/generate_no8x1in_pozi_countersunk_self_tapping_screw.py
python src/3d_models/render_preview.py No8x1in_4.2x25mm_Pozi_Countersunk_Self_Tapping_Screw_Black
```
