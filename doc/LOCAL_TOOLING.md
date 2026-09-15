# Local Tooling Environment

**Lifecycle:** CURRENT SUPPORTING REFERENCE

**Owns:** repository paths, local Python environments, REW API runtime boundary,
Git authentication notes, and project documentation checks

**Does not own:** engineering state, measurement procedures, or generated-model
reconstruction details

**Read when:** maintaining local tooling, moving the checkout, or diagnosing a
repository/runtime problem

**Last reviewed:** 2026-09-15

## 1. Repository Paths

- Windows applications such as REW, VituixCAD, SketchUp, and Cura use
  `C:\Users\swallace\Projects\Speaker prototype`.
- WSL2 automation uses the same files through
  `/mnt/c/Users/swallace/Projects/Speaker prototype`.
- Keep the repository on the Windows drive unless a deliberate migration also
  updates the absolute source paths in the retained VituixCAD projects and
  verifies every Windows application.

## 2. Python And Application Boundary

- The reconstructed Windows Python environment is `.venv`.
- The separate WSL environment is `.venv-wsl`.
- Neither environment is committed; 3D dependency and reconstruction details
  belong in [3D regeneration and retention](3d_models/REGENERATION_AND_RETENTION.md).
- `%USERPROFILE%\.wslconfig` now selects WSL mirrored networking. After the
  required WSL restart, ordinary WSL and host-permitted Codex commands can reach
  REW's Windows-local API at `127.0.0.1:4735`.
- Start REW with its API enabled on `127.0.0.1:4735` and leave it open. REW
  session-state capture, `.mdat` inspection, and repeatable CSV extraction use
  either Windows `.venv` or standard-library Python in WSL. WSL mirrored
  networking permits ordinary WSL and host-permitted Codex access to the
  Windows-local API; the default inner sandbox still blocks localhost and
  Windows interoperability, so live Codex calls require host access. Use
  [REW API client](REW_API_CLIENT.md) for `status`/snapshot and its linked
  [MDAT extraction procedure](rew/procedures/REW_MDAT_EXTRACTION.md) for any
  workspace-mutating `.mdat` work.
- The committed FRD/ZMA/impulse summariser, REW `.mdat` compact mode, and VXP
  auditor use only the Python standard library. They run under either environment
  and are documented together in
  [Measurement data tooling](MEASUREMENT_DATA_TOOLING.md).

## 3. Documentation and changed-file checks

The standard-library [`src/project_docs.py`](../src/project_docs.py) checks
local Markdown links and heading anchors offline, including URL-encoded paths:

```text
python3 src/project_docs.py links
python3 src/project_docs.py links --file doc/LOCAL_TOOLING.md
python3 src/project_docs.py routes --task "Documentation review"
```

`links` checks tracked Markdown and new, untracked files under `doc/` by default and reports only broken local
targets with source file and line. It skips remote links; technical external
authorities still need proportionate human spot-checks. `routes` checks whether
all project Markdown in scope is reachable from `README.md` or `AGENTS.md` and reports
the files and word cost in each `README.md` task route. The optional `--task`
limits route output; an unfiltered report is useful for a comprehensive review.
The checker cannot judge whether an engineering statement is current or true.

[`src/project_checks.py`](../src/project_checks.py) runs a compact changed-file
pass:

```text
python3 src/project_checks.py
```

It checks all tracked Markdown links and routes when project Markdown changes;
compiles changed project Python and runs the unit suite when Python changes;
and always checks both staged and unstaged Git diff whitespace. Its JSON report includes check counts and
failure details only when needed. It summarizes unrelated changed files without
reading or modifying them. This is a convenience check, not a replacement for
reviewing the actual diff or for the documentation procedure's evidence and
interpretation checks. Both commands write normal results only to stdout, so
no new ignored output class is needed.

## 4. GitHub Authentication In WSL

GitHub CLI authentication and Git-over-SSH authentication are separate. A Codex
GitHub connection does not authenticate the WSL `gh` command.

Git-over-SSH uses the user-level `codex-ssh-agent.service` and the stable socket
`~/.ssh/agent.sock`; the relevant host entry selects it with `IdentityAgent`.
After a complete WSL shutdown or service restart, the new agent may be empty and
the encrypted GitHub key must be loaded once. Keep private-key names and contents
out of project documentation.

## 5. Verification

After changing checkout paths or environments, verify the specific affected
workflow rather than assuming Windows and WSL state transfer automatically.
Repository maintenance must preserve unrelated work and follow [AGENTS.md](../AGENTS.md).

For the current REW bridge, the proportionate checks are `cmd.exe /c ver`, an
HTTP GET of `http://127.0.0.1:4735/measurements`, and
`python3 src/rew_api_extract.py status`. In a Codex task these checks must use
host access; failure in the default inner sandbox does not show that ordinary
WSL or REW is unavailable.
