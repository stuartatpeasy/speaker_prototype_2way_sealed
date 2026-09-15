# 3D Model Collection

| State | Value |
| --- | --- |
| Lifecycle | **CURRENT COLLECTION HUB** |
| Owns | Model catalogue, shared SketchUp import, regeneration, output, retention, and verification instructions |
| Does not own | Component-specific dimensions, provenance, inferred geometry, or limitations |
| Source tree | [`src/3d_models/`](../../src/3d_models/) |
| Artefact tree | [`3d_models/`](../../3d_models/) |

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

Canonical cabinet and room assemblies, fabrication STLs, and printer jobs also live under [`3d_models/`](../../3d_models/), but they are not members of this scripted component catalogue.

## 2. Shared layout and SketchUp import

Generated/importable component artefacts use:

```text
3d_models/<Model_Name>/
```

Python geometry sources use matching folders under:

```text
src/3d_models/<Model_Name>/
```

Each generator writes a same-named COLLADA `.dae` to its artefact folder. In SketchUp, use **File > Import > COLLADA (`*.dae`)**. The generated DAE files declare millimetres and Z-up coordinates. Preserve the model-specific origin and orientation stated in its component record, and make repeated objects SketchUp components.

STL generation has been retired from the component generators because the coloured DAE files import reliably. Existing legacy or fabrication STL files remain retained where the current generators cannot recreate them.

## 3. Runtime bootstrap

The reference Windows environment uses Python 3.12.10; the validated WSL2 environment uses Ubuntu 24.04 Python 3.12.3. Preview dependencies are pinned in [`requirements.txt`](../../requirements.txt). Windows and WSL require separate disposable environments.

### 3.1 Windows PowerShell

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\Activate.ps1
```

### 3.2 WSL2

```bash
python3 -m venv .venv-wsl
.venv-wsl/bin/python -m pip install -r requirements.txt
source .venv-wsl/bin/activate
```

Do not share a virtual environment between operating systems. Keep the repository in its Windows location and access the same files from WSL at `/mnt/c/Users/swallace/Projects/Speaker prototype`; moving it would also require updating and verifying Windows-application paths elsewhere in the project.

The Neutrik STEP converter additionally requires `cadquery-ocp-novtk`; its
[component record](Neutrik_NL4MPXX/README.md) identifies the retained STEP
input. The exact converter-package version used for the present DAE was not
recorded, so that one conversion environment is not byte-for-byte
reconstructible. The retained STEP, converter settings, and geometry checks
support semantic regeneration; pin the OpenCascade package before changing or
re-qualifying that converter.

## 4. Regeneration and preview

From the project root, run the generator linked in the selected component record:

```console
python src/3d_models/<Model_Name>/generate_<model>.py
```

Then render the standard preview:

```console
python src/3d_models/render_preview.py <Model_Name>
```

[`render_preview.py`](../../src/3d_models/render_preview.py) loads the model generator, calls its mesh-building interface, and applies any `PREVIEW_CONFIG`. Rasterisation, materials, lighting, labels, layout, and output paths are shared.

Generated DAE metadata includes a timestamp, so semantic geometry equivalence—not a byte-identical hash—is the target. The component record states expected bounds, dimensions, mesh checks, or other model-specific verification evidence.

## 5. Verification

For ordinary regeneration:

1. compile the selected generator and shared source modules;
2. run the generator and require its geometry checks to pass;
3. confirm the expected DAE exists and is non-empty;
4. render the preview and confirm the PNG exists and is non-empty; and
5. compare reported dimensions, bounds, triangle count, and degeneracy/manifold checks with the component record where specified.

For a migration or toolchain change, perform those steps in a temporary copy of the required source/input/artefact layout so canonical committed inputs are not modified merely to test the environment.

## 6. Printer machine code

G-code is machine- and toolchain-specific and intentionally ignored. Printable STL files remain committed. [`3d_models/PRINT_SETTINGS.json`](../../3d_models/PRINT_SETTINGS.json) preserves the Cura 5.13.0 / Creality CR-20 Pro profile identity, per-job overrides, instance counts, ArcWelder state, and reference output bounds, time, and filament use.

Re-slice the named STL using that manifest. For historical jobs whose original
STL was renamed and changed, use the recorded `sourceRevisionAtCapture` and
`sourceStlAtCapture`; do not assume the related current STL is equivalent.
Functional equivalence is the target; timestamps, object ordering, placement,
and slicer line ordering may differ. Regenerated machine code must be checked
for the printer and material actually in use.

## 7. Retention boundary

The collection-specific `.gitignore` rules exclude only generated DAE and
preview PNG files in model folders with matching retained generators. The
separate project `outputs/` rule covers disposable inspection and REW-API
exports whose authorities and reconstruction commands are retained elsewhere.
Canonical assembly/room DAE files, imported STEP sources, legacy and
fabrication STLs, measurements, PDFs, spreadsheets, and reference images remain
retained because no complete reconstruction path covers all of them.

Do not delete a retained source because a derivative is regenerable, and do not extend the ignore pattern to a new model until its inputs, generator, dependencies, command, and expected verification result are documented.
