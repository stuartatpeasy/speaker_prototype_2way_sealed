# 3D model source layout

## 1. Source and artefact layout

Generated/importable artifacts live under:

```text
3d_models/<Model_Name>/
```

Python geometry sources live in matching folders under:

```text
src/3d_models/<Model_Name>/
```

Each generator writes a same-named COLLADA file back to its artifact folder.
STL generation has been retired because the coloured DAE files import
reliably into SketchUp.

Legacy and fabrication STL files remain committed. They are not covered by the
generated-artifact ignore rules because the current generators do not recreate
all of them.

## 2. Recreating generated model artefacts

Use Python 3.12.10 and the pinned preview dependencies in the project-root
`requirements.txt`:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Run the appropriate `generate_*.py` file under `src/3d_models/<Model_Name>/`
to recreate the ignored same-named DAE. Each model's committed README gives
its exact command and records its geometry/provenance.

All models use the shared preview renderer:

```powershell
.venv\Scripts\python.exe src/3d_models/render_preview.py <Model_Name>
```

The renderer loads the model generator, calls its mesh-building function, and
uses its optional `PREVIEW_CONFIG`. Camera-independent rasterisation,
materials, lighting, layout, labels, and artifact paths are centralised in
the shared script. A new model therefore needs only a generator and a small
preview configuration rather than a copied rendering implementation.

The generated DAE metadata includes a generation timestamp, so semantic model
equivalence—not a byte-identical file hash—is the reproducibility target.

## 3. Recreating 3D-printer machine code

G-code is machine- and toolchain-specific and is intentionally ignored. The
printable STL files remain committed. `3d_models/PRINT_SETTINGS.json` preserves
the Cura 5.13.0 / Creality CR-20 Pro profile identity, per-job overrides,
instance counts, ArcWelder state, and reference output bounds, time, and
filament consumption extracted from the previous G-code files.

Re-slice the named STL using that manifest. Functional equivalence is the
target; timestamps, object ordering, automatic placement, and slicer-generated
line ordering may prevent byte-for-byte identity. Machine code should in any
case be regenerated and checked for the printer/material currently in use.

## 4. Retention boundary

The project `.gitignore` excludes only the generated DAE and preview PNG files
in model folders that already have matching committed generators. Canonical
assembly/room DAE files, imported STEP sources, legacy and fabrication STLs,
measurements, PDFs, spreadsheets, and reference images remain versioned because
there is no complete documented reconstruction path for all of them.
