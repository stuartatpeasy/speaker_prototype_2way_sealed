# 3D Model Regeneration and Retention

| State | Value |
| --- | --- |
| Lifecycle | **CURRENT SUPPORTING REFERENCE** |
| Owns | Shared layout/import, environment bootstrap, regeneration, preview, verification, G-code, and retention rules |
| Does not own | Component-specific dimensions, source provenance, inferred geometry, or limitations |
| Read when | Regenerating a scripted model, rendering a preview, re-slicing a printer job, changing the toolchain, or reviewing an ignored derivative |
| Current approved action | Select a component through the [3D-model hub](README.md), then use its record and this reconstruction route |
| Limitations | The retained Neutrik conversion is semantically, not byte-for-byte, reconstructible until its converter package is pinned |
| Last reviewed | 2026-09-15 |

## 1. Layout and import

Generated/importable artefacts use `3d_models/<Model_Name>/`; matching Python sources use `src/3d_models/<Model_Name>/`. Each generator writes a same-named COLLADA `.dae` to its artefact folder. Import it in SketchUp through **File > Import > COLLADA (`*.dae`)**. Generated DAE declares millimetres and Z-up; preserve the selected component record's origin/orientation and make repeated objects SketchUp components.

Component generators no longer create STL because coloured DAE imports reliably. Retain legacy and fabrication STLs where current generators cannot recreate them.

## 2. Environment and dependencies

The reference Windows environment is Python `3.12.10`; validated WSL2 is Ubuntu `24.04` Python `3.12.3`. Preview dependencies are pinned in [`requirements.txt`](../../requirements.txt); each OS needs a separate disposable environment.

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\Activate.ps1
```

```bash
python3 -m venv .venv-wsl
.venv-wsl/bin/python -m pip install -r requirements.txt
source .venv-wsl/bin/activate
```

Do not share the environments. Keep this checkout at its Windows location and access it from WSL at `/mnt/c/Users/swallace/Projects/Speaker prototype`; a deliberate move also needs VituixCAD absolute-path updates and application verification. The Neutrik STEP converter also needs `cadquery-ocp-novtk`; its [component record](Neutrik_NL4MPXX/README.md) identifies the retained STEP. Its exact converter version was not recorded, so retain the STEP, settings, and geometry checks as semantic reconstruction evidence, and pin the OpenCascade package before changing or re-qualifying the converter.

## 3. Regeneration and preview

From the project root, run the generator named in the selected component record, then render its standard preview:

```text
python src/3d_models/<Model_Name>/generate_<model>.py
python src/3d_models/render_preview.py <Model_Name>
```

[`render_preview.py`](../../src/3d_models/render_preview.py) loads the model generator, calls its mesh-building interface, and applies `PREVIEW_CONFIG` when present. Rasterisation, materials, lighting, labels, layout, and output paths are shared. Generated DAE metadata includes a timestamp, so compare semantic geometry, not byte-identical hashes; each component record supplies expected bounds, dimensions, mesh checks, or other evidence.

For ordinary regeneration: compile the selected generator and shared modules; run the generator and require its checks to pass; confirm non-empty DAE and preview PNG; then compare dimensions, bounds, triangle count, and degeneracy/manifold checks with the component record. For a migration or toolchain change, run these steps in a temporary source/input/artefact copy so testing does not modify canonical committed inputs.

## 4. Printer machine code

G-code is machine/toolchain specific and intentionally ignored; printable STLs remain committed. [`3d_models/PRINT_SETTINGS.json`](../../3d_models/PRINT_SETTINGS.json) records Cura `5.13.0` / Creality CR-20 Pro profile identity, per-job overrides, instance counts, ArcWelder state, and reference bounds, time, and filament use.

Re-slice the named STL using that manifest. For historical jobs whose source was renamed or changed, use `sourceRevisionAtCapture` and `sourceStlAtCapture`; do not infer equivalence from a related current STL. Functional equivalence is the target because timestamps, ordering, placement, and slicer-line ordering can differ. Check regenerated machine code for the actual printer and material.

## 5. Retention boundary

Collection `.gitignore` rules exclude only generated DAE and preview PNG in model folders with matching retained generators. The project `outputs/` rule covers disposable inspection and REW-API exports with retained authorities and reconstruction commands. Canonical assembly/room DAE, imported STEP, legacy and fabrication STL, measurements, PDFs, spreadsheets, and reference images remain retained because no complete reconstruction route covers them.

Do not delete a retained source because a derivative is regenerable. Do not add an ignore rule for a model until its inputs, generator, dependencies, command, and expected verification are documented.
