# Local Tooling Environment

**Lifecycle:** CURRENT SUPPORTING REFERENCE

**Owns:** repository paths, local Python environments, REW API runtime boundary,
and Git authentication notes

**Does not own:** engineering state, measurement procedures, or generated-model
reconstruction details

**Read when:** maintaining local tooling, moving the checkout, or diagnosing a
repository/runtime problem

**Last reviewed:** 2026-09-06

## 1. Repository Paths

- Windows applications such as REW, VituixCAD, SketchUp, and Cura use
  `C:\Users\swallace\Projects\Speaker prototype`.
- WSL2 automation uses the same files through
  `/mnt/c/Users/swallace/Projects/Speaker prototype`.
- Keep the repository on the Windows drive unless a deliberate migration also
  updates the absolute impedance-file paths in
  `vituixcad/Prototype loudspeaker.vxp` and verifies every Windows application.

## 2. Python And Application Boundary

- The reconstructed Windows Python environment is `.venv`.
- The separate WSL environment is `.venv-wsl`.
- Neither environment is committed; dependency and reconstruction details for
  3D models belong in [3D model documentation](3d_models/README.md).
- REW session-state capture, `.mdat` inspection, and repeatable CSV extraction
  use Windows Python because REW's API listener is on Windows localhost. See
  [REW API Client](REW_API_CLIENT.md).

## 3. GitHub Authentication In WSL

GitHub CLI authentication and Git-over-SSH authentication are separate. A Codex
GitHub connection does not authenticate the WSL `gh` command.

Git-over-SSH uses the user-level `codex-ssh-agent.service` and the stable socket
`~/.ssh/agent.sock`; the relevant host entry selects it with `IdentityAgent`.
After a complete WSL shutdown or service restart, the new agent may be empty and
the encrypted GitHub key must be loaded once. Keep private-key names and contents
out of project documentation.

## 4. Verification

After changing checkout paths or environments, verify the specific affected
workflow rather than assuming Windows and WSL state transfer automatically.
Repository maintenance must preserve unrelated work and follow [AGENTS.md](../AGENTS.md).
