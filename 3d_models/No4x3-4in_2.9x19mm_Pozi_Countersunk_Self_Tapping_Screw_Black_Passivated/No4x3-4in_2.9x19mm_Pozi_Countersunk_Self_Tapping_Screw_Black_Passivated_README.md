# No. 4 x 3/4 in (2.9 x 19 mm) black-passivated self-tapping screw

The SketchUp import file is
`No4x3-4in_2.9x19mm_Pozi_Countersunk_Self_Tapping_Screw_Black_Passivated.dae`.
It is a low-polygon model of the matching black-passivated DIN 7982 C Z
Pozidriv countersunk self-tapping screw.

## Import and placement

- In SketchUp, use **File > Import > COLLADA (`*.dae`)**.
- The DAE declares millimetres and Z-up coordinates.
- The origin is the centre of the flat upper head face.
- The screw extends exactly 19.0 mm along negative Z, including its head.
- The trade size is 3/4 inch; the requested 19 mm nominal length is the
  controlling model dimension.
- Make the imported object a SketchUp component before placing multiple
  instances.

## Controlling dimensions

| Feature | Dimension |
|---|---:|
| Thread | ST2.9 x 1.1, right hand |
| Overall length | 19.0 mm |
| Head diameter | 5.5 mm |
| Head height | 1.7 mm |
| Countersink angle | 80 degrees |
| Drive | PZ1 |
| Type Z recess width, m | 2.8 mm |
| Modelled recess depth | 1.60 mm |
| Type C point length | 2.6 mm |
| Modelled thread-root diameter | 2.08 mm |

Bolt World's exact matching product establishes the black-passivated zinc
finish, PZ1 drive, head dimensions and Type C (AB) point. Accu independently
confirms the 2.9 x 19 mm size, 80-degree countersink and DIN 7982 C Z form.
The standards table supplies the 1.1 mm pitch, 2.8 mm Type Z recess width,
1.48-1.73 mm recess-depth range and 2.6 mm maximum point length.

Sources:

- Bolt World, black-passivated No. 4 x 3/4 in Pozi countersunk self-tapper:
  <https://boltworld.co.uk/products/no-4-x-3-4-2-9-x-19mm-pozi-countersunk-self-tapping-screws-black-passivated-zinc-plated-din-7982/>
- Accu, No. 4 x 3/4 in DIN 7982 C Z product dimensions:
  <https://www.accu.co.uk/self-tapping-pozi-countersunk-screws/163548-SPKT-No-4-3-4-A2-BL>
- Westfield Fasteners, DIN 7982 / ISO 7050 dimensions:
  <https://www.westfieldfasteners.co.uk/Standards/TappingScrew-PoziCsk.html>

## Model scope and polygon budget

The 24-sided head retains the exact 5.5 mm X/Y envelope. The right-hand
external thread is a continuous geometric helix and blends into a Type C/AB-
style tapered point. The PZ1 recess is a real cavity rather than a surface
mark. Its detailed wing form and the 2.08 mm thread-root diameter remain
representative where the product drawings do not fully dimension the form.

The closed manifold mesh contains 890 vertices and 1,776 triangles, matching
the established No. 8 model's lightweight geometry budget.

From the project root, regenerate the DAE and preview with:

```powershell
python src/3d_models/No4x3-4in_2.9x19mm_Pozi_Countersunk_Self_Tapping_Screw_Black_Passivated/generate_no4x3_4in_pozi_countersunk_self_tapping_screw.py
python src/3d_models/render_preview.py No4x3-4in_2.9x19mm_Pozi_Countersunk_Self_Tapping_Screw_Black_Passivated
```
