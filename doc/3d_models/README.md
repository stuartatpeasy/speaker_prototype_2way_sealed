# 3D Model Collection

| State | Value |
| --- | --- |
| Lifecycle | **CURRENT COLLECTION HUB** |
| Owns | Model catalogue and selection routing |
| Does not own | Component-specific dimensions, provenance, inferred geometry, limitations, or regeneration detail |
| Source tree | [`src/3d_models/`](../../src/3d_models/) |
| Artefact tree | [`3d_models/`](../../3d_models/) |
| Regeneration, preview, printer, and retention | [Regeneration and retention](REGENERATION_AND_RETENTION.md) |
| Last reviewed | 2026-09-15 |

## 1. Collection catalogue

| Family | Preferred model and variants | Component record |
| --- | --- | --- |
| M4 × 10 Type D flanged insert | Low-poly DAE for repeated cabinet instances; detailed DAE for close views; legacy STL fallbacks retained | [Type D insert](M4x10_Type_D_Flanged_Threaded_Insert/README.md) |
| M4 × 10 Type E non-flanged insert | One DAE | [Type E insert](M4x10_Type_E_NonFlanged_Threaded_Insert/README.md) |
| M4 × 30 countersunk machine screw | One DAE | [M4 machine screw](M4x30_Countersunk_Machine_Screw_Black/README.md) |
| No. 4 × 3/4 in self-tapping screw | One DAE | [No. 4 screw](No4x3-4in_2.9x19mm_Pozi_Countersunk_Self_Tapping_Screw_Black_Passivated/README.md) |
| No. 8 × 1 in self-tapping screw | One DAE | [No. 8 screw](No8x1in_4.2x25mm_Pozi_Countersunk_Self_Tapping_Screw_Black/README.md) |
| Neutrik NL4MPXX | DAE converted from retained STEP | [NL4MPXX connector](Neutrik_NL4MPXX/README.md) |
| SB Acoustics SB17NRX2C35-8 | DAE; legacy STL fallback retained | [Woofer](SB_Acoustics_SB17NRX2C35-8/README.md) |
| SB Acoustics SB26STWGC-4 | One DAE | [Tweeter](SB_Acoustics_SB26STWGC-4/README.md) |
| Crossover-coil formers and brackets | Five retained SketchUp-exported fabrication STLs | [Crossover coils](Crossover_Coils/README.md) |

Canonical cabinet and room assemblies, fabrication STLs, and printer jobs also live under [`3d_models/`](../../3d_models/), but are not members of this scripted component catalogue.

## 2. Choose the next authority

For model selection, read only the relevant component record above. For scripted-model regeneration, SketchUp import, preview rendering, runtime/dependencies, G-code re-slicing, verification, or retention, read [Regeneration and retention](REGENERATION_AND_RETENTION.md) after the selected component record. Canonical assemblies and fabrication STL/printer jobs are not part of the scripted catalogue; use their named records and retained source files.
