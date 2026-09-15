# Crossover Coil Fabrication Models

| State | Value |
| --- | --- |
| Lifecycle | **CURRENT RETAINED FABRICATION SOURCES** |
| Owns | Identity, file-level provenance, geometry checks, print reconstruction, and retention limits for the crossover-coil formers and brackets |
| Does not own | Electrical winding targets, inductance/DCR acceptance, PCB layout, installed restraint, or manufacturing release |
| Source tree | [`3d_models/Crossover coils/`](../../../3d_models/Crossover%20coils/) |
| Current use | Candidate formers and restraint brackets for the reversible external crossover and its matched second network |
| Limitations | Only binary STL exports are retained; no editable SketchUp source or parameterised generator is present, and STL dimensions do not prove fit or mechanical adequacy |
| Last reviewed | 2026-09-15 |

## 1. Retained models

Each binary header begins `SketchUp STL tmp`, which establishes the exporter
family but not the SketchUp version, units setting, authoring history, or design
intent. File-level inspection gives:

| STL | Bytes | Triangles | Axis-aligned size, mm | SHA-256 |
| --- | ---: | ---: | --- | --- |
| `Crossover coil bracket 70mm.stl` | `36,884` | `736` | `24 x 45 x 47` | `1a1c5f53c819f191d65dd57bc6a944bdf2bd17f0ede35a2619a52653eb27129a` |
| `Crossover coil bracket B.stl` | `81,284` | `1,624` | `54 x 50 x 51` | `bb128d6cfdb267210c2d28ef907b901df0f76c888de0b029383f7d10baa7defd` |
| `Crossover coil former 50mm.stl` | `87,884` | `1,756` | `50 x 50 x 33` | `1d27ed4c79d08ac5ad17f20713781e60b5f202eba2ae47380797f6348366c287` |
| `Crossover coil former 60mm.stl` | `115,484` | `2,308` | `60 x 60 x 33` | `46a93e1c0fd671c08022aa63b22a1416570dfbe013cbe9eb493ed98c347cc9a6` |
| `Crossover coil former 70mm.stl` | `104,084` | `2,080` | `70 x 70 x 33.5` | `411bb6568155a367072750986901e53c84828467ae5ccf0e84cfa93079025e8f` |

These are retained fabrication sources because no complete reconstruction path
exists. Do not replace or ignore them merely because a slicer can consume the
exports. Verify coil fit, lead exit, separation/orientation, restraint, PCB and
cabinet clearance, material, and print quality on the actual assembly.

## 2. Print reconstruction

[`3d_models/PRINT_SETTINGS.json`](../../../3d_models/PRINT_SETTINGS.json) owns
the Cura 5.13.0 / Creality CR-20 Pro settings and reference output statistics.
G-code is intentionally ignored. Re-slice the named current STL with the
manifest settings and compare bounds, time, and filament use proportionately;
functional rather than byte-identical equivalence is expected.

The 2026-09-13 file reorganisation changed two former geometries while removing
their old names. For historical print jobs, the manifest therefore records the
source path and Git revision that existed at capture. Recover that exact input
without altering the worktree with:

```text
git show <sourceRevisionAtCapture>:3d_models/<sourceStlAtCapture>
```

Redirect that output only into a temporary workspace. A similarly named current
STL is not assumed geometrically equivalent unless the manifest says the move
was exact.

## 3. Electrical authority

Former diameter and winding space are mechanical constraints, not inductance
specifications. Use [Crossover component
development](../../CROSSOVER_COMPONENT_DEVELOPMENT.md) for the measured Seed A
inductances, DCRs, winding practice, pair matching, and thermal limitations.
