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

The reference Windows environment uses Python 3.12.10. The WSL2 bootstrap was
validated with Ubuntu 24.04's Python 3.12.3. Both use the pinned preview
dependencies in the project-root `requirements.txt`.

Do not try to share one virtual environment between Windows and WSL: its
launchers and interpreter paths are operating-system-specific. The disposable
Windows environment is `.venv`; the disposable WSL environment is
`.venv-wsl`. Both are explicitly ignored, and either can be reconstructed
from the commands below.

### 2.1 Windows PowerShell bootstrap

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\Activate.ps1
```

### 2.2 WSL2 bootstrap

```bash
python3 -m venv .venv-wsl
.venv-wsl/bin/python -m pip install -r requirements.txt
source .venv-wsl/bin/activate
```

After activation, the shell-neutral `python` commands in each model's
committed README use the selected environment. Keep the repository in its
Windows location and access it in WSL at
`/mnt/c/Users/swallace/Projects/Speaker prototype`: the modest mounted-drive
I/O penalty is preferable here to breaking the absolute Windows paths used by
VituixCAD and the Windows measurement/CAD toolchain.

### 2.3 Regeneration and verification

Run the appropriate `generate_*.py` file under `src/3d_models/<Model_Name>/`
to recreate the ignored same-named DAE. Each model's committed README gives
its exact command and records its geometry/provenance.

All models use the shared preview renderer:

```console
python src/3d_models/render_preview.py <Model_Name>
```

The renderer loads the model generator, calls its mesh-building function, and
uses its optional `PREVIEW_CONFIG`. Camera-independent rasterisation,
materials, lighting, layout, labels, and artifact paths are centralised in
the shared script. A new model therefore needs only a generator and a small
preview configuration rather than a copied rendering implementation.

The generated DAE metadata includes a generation timestamp, so semantic model
equivalence—not a byte-identical file hash—is the reproducibility target.
For a migration check, compile all Python sources, regenerate one representative
model in a temporary copy of the source/artifact layout, and render its preview.
Success means the generator's geometry checks pass and the renderer writes a
non-empty PNG without modifying canonical committed inputs.

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
