# DIY Near-Wall Two-Way Loudspeaker

This is the high-level source of truth and entry point for the sealed passive two-way prototype. Detailed engineering evidence is divided by topic so a future reader can load only the files needed for the task.

## 1. Current project status

- One acoustically representative sealed prototype cabinet has been built and both selected drivers have been installed.
- The accepted cabinet body is approximately **280 × 430 × 300 mm**, with approximately **21.7 L geometric net volume** before damping.
- The woofer is undergoing controlled installed-cabinet conditioning. A matched 48 kHz comparison shows a clear reduction in sealed-system resonance, but the latest post-run trace contained residual series resistance and requires a fully cooled confirmation before replacing the crossover impedance baseline.
- The tweeter's installed impedance agrees closely with its published parameters. No dedicated tweeter run-in is presently justified.
- Both drivers remain provisionally retained.
- The passive crossover remains exploratory. Installed-baffle acoustic magnitude, common timing/phase, directivity, and distortion measurements are still required before topology or component values can be frozen.
- The intended acoustic crossover region remains approximately **2.2–2.4 kHz**, probably using fourth-order Linkwitz–Riley-like acoustic slopes, subject to measurement.
- The amplifier-reference fixture has passed every topology, construction, DC,
  and ground-path gate. AC commissioning is the sole remaining electrical gate;
  full-dual amplifier use is not yet approved.

## 2. Project goal and engineering principles

Design and build a pair of accurate, measurement-led passive loudspeakers as an enthusiastic-novice project.

Priorities:

- neutral tonal balance, smooth on-axis response, and controlled off-axis behaviour;
- low distortion and clear separation of vocals and instruments, including dense electronic material;
- engineering-led decisions without unsupported audiophile claims;
- a practical prototype whose components are not so expensive that iteration becomes financially painful;
- explicit separation of verified measurements, derivations, inferences, provisional decisions, and open items;
- measured installed behaviour takes precedence over nominal impedance, textbook crossover values, or the expectation that a sample must reproduce every datasheet parameter.

## 3. Locked architecture

- passive **two-way** loudspeaker;
- **SB Acoustics SB17NRX2C35-8** woofer/midwoofer;
- **SB Acoustics SB26STWGC-4** waveguide tweeter;
- sealed enclosure;
- near-wall shelf/stand placement;
- nominally amplifier-friendly complete load, to be established by final measurement rather than driver labels;
- passive crossover designed from measurements of the installed drivers in the actual prototype;
- external development crossover through a four-pole speakON connection before any final internal installation.

Three-way, open-baffle, transmission-line, horn, and reflex alternatives are outside this first version. DSP may be used experimentally before the passive crossover is finalised.

## 4. Documentation index

| File | Authority and when to read it |
|---|---|
| [README.md](README.md) | High-level project state, locked architecture, document map, and open decisions. Start here. |
| [AGENTS.md](AGENTS.md) | Standing collaboration instructions, including same-turn Markdown maintenance, conservative ignore policy, and completion checks. |
| [.gitignore](.gitignore) | Current committed/generated boundary for caches, machine outputs, scripted exports, and irreplaceable project artefacts. |
| [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md) | Living driver evidence record: published data, valid impedance baselines, alignment calculations, conditioning results, and driver-retention gates. |
| [DRIVER_RUNIN.md](DRIVER_RUNIN.md) | Controlled installed-cabinet woofer stabilisation, cooldown gates, REW settings, repeat/stop rule, and the no-dedicated-tweeter-run-in decision. |
| [CABINET_DESIGN.md](CABINET_DESIGN.md) | Enclosure alignment, dimensions, materials, driver mounting, rear panel, bracing, damping, connector mechanics, and open fabrication items. |
| [CROSSOVER_DESIGN.md](CROSSOVER_DESIGN.md) | Provisional acoustic direction, external-development interface, capacitor/inductor/resistor engineering, power philosophy, and validation gates. |
| [MEASUREMENT_WORKFLOW.md](MEASUREMENT_WORKFLOW.md) | Project-wide measurement sequence, calibration/file conventions, evidence handling, and links to specialised procedures. |
| [ROOM_DETAILS.md](ROOM_DETAILS.md) | Current room geometry, canonical DAE interpretation, intended placement, coupled spaces, and reversible placement trials. |
| [src/3d_models/README.md](src/3d_models/README.md) | Source/generated boundary and reconstruction procedure for scripted 3D models, previews, and printer machine code. |
| [rew/FRD_MEASUREMENT_SETUP_TEST.md](rew/FRD_MEASUREMENT_SETUP_TEST.md) | Detailed installed acoustic-response and common-timing setup. |
| [rew/SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md](rew/SU-V570_OUTPUT_TOPOLOGY_AND_LOOPBACK_VERIFICATION.md) | SU-V570 schematic assessment, unpowered common-ground test, and amplifier-suitability gate. |
| [rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md](rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md) | Current cable-to-TRS fixture authority: rationale, construction, calculations, qualification summary, and release gate. |
| [rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md](rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md) | Completed phantom, resistance, DC clamp, construction, ground-path, and UMC202HD output-topology evidence. Read for audit/history, not the next procedure. |
| [rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md](rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md) | Live interconnect preflight and matched AC transfer/noise procedure; this is the exact signal-path-testing resume point. |

### 4.1 Minimal reading routes

- **Driver, run-in, or enclosure alignment:** this file + `DRIVER_ANALYSIS.md`; add `DRIVER_RUNIN.md` for conditioning and `CABINET_DESIGN.md` for box construction/damping.
- **Cabinet fabrication:** this file + `CABINET_DESIGN.md`.
- **Crossover development:** this file + `DRIVER_ANALYSIS.md` + `CROSSOVER_DESIGN.md` + `MEASUREMENT_WORKFLOW.md`.
- **Acoustic measurements:** this file + `MEASUREMENT_WORKFLOW.md` + the relevant procedure under `rew/`.
- **Room or placement work:** this file + `ROOM_DETAILS.md`; re-inspect the current `3d_models/Listening room.dae` after any geometry change.
- **Amplifier loopback/reference work:** this file +
  `rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md`. Add the SU-V570 topology
  record or qualification record only to audit those completed gates. For the
  current signal-path work, add `rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md`;
  add `rew/FRD_MEASUREMENT_SETUP_TEST.md` only after fixture release. Do not
  connect a powered amplifier output until the fixture gate says `YES`.
- **Repository or generated-artifact maintenance:** this file + `AGENTS.md` + `.gitignore`; add `src/3d_models/README.md` for model, preview, or printer-output reconstruction.

### 4.2 Local tooling environment

The supported local workflow is deliberately dual-environment:

- Windows applications such as REW, VituixCAD, SketchUp, and Cura continue to
  use the repository at
  `C:\Users\swallace\Projects\Speaker prototype`;
- WSL2 automation and command-line work use the same files through
  `/mnt/c/Users/swallace/Projects/Speaker prototype`;
- keep the repository on the Windows drive unless a deliberate migration also
  updates the absolute impedance-file paths in
  `vituixcad/Prototype loudspeaker.vxp` and verifies every Windows application;
- the reconstructed Windows Python environment is `.venv`; the separate WSL
  environment is `.venv-wsl`. Neither environment is committed;
- GitHub CLI authentication is environment-specific. Connecting the Codex
  GitHub plugin does not authenticate the separate `gh` installation in WSL;
- Git-over-SSH in WSL uses a user-level `codex-ssh-agent.service` with the
  stable socket `~/.ssh/agent.sock`. The relevant GitHub host entry in
  `~/.ssh/config` selects that socket with `IdentityAgent`. After a complete
  WSL shutdown or service restart, load the encrypted GitHub key into the new
  agent once with
  `SSH_AUTH_SOCK="$HOME/.ssh/agent.sock" ssh-add "$HOME/.ssh/<github-private-key>"`.

Use [src/3d_models/README.md](src/3d_models/README.md) for the exact
cross-platform Python bootstrap and verification procedure.

## 5. Current design summary

### 5.1 Drivers

The selected woofer is the **SB17NRX2C35-8**, nominally 8 Ω with published $F_s=36.5\ \mathrm{Hz}$, $Q_{ts}=0.42$, $V_{as}=27\ \mathrm{L}$, and $X_{max}=\pm5.5\ \mathrm{mm}$. The real sample's measured resonance remains higher than published; use the living analysis record rather than these nominal values for modelling.

The selected tweeter is the **SB26STWGC-4**, nominally 4 Ω with an integrated waveguide and substantial sensitivity headroom. It will require attenuation and must be protected by the complete validated high-pass network. Its conditional power rating must not be treated as an unfiltered rating.

### 5.2 Cabinet

- approximately **280 × 430 × 300 mm** body;
- approximately **23.65 L gross / 21.7 L geometric net** before damping;
- **18 mm plywood** body and **36 mm laminated plywood baffle**;
- approximately **25 mm baffle-edge roundovers**;
- removable gasketed prototype rear panel;
- window bracing and adjustable polyester/Dacron damping;
- separately wired drivers through a right-angle-compatible speakON NL4 interface;
- soft feet providing approximately 15 mm installed rise.

### 5.3 Room and placement

The design is explicitly **near-wall / near-corner**, not a free-space standmount. Nominal placement leaves approximately 100 mm behind and beside each cabinet on a full-width shelf in the measured listening room. Use [ROOM_DETAILS.md](ROOM_DETAILS.md) for the complete, current geometry and reversible right-speaker/listener trials.

Consequences:

- avoid excessive bass lift or reflex-style showroom tuning;
- use partial rather than automatic full baffle-step compensation;
- include intended placement in final measurements;
- broad room effects may later be addressed with DSP, but narrow room-mode nulls should not be corrected in the passive crossover.

### 5.4 Crossover

The current 2.2–2.4 kHz LR4-like acoustic direction is a development hypothesis, not a locked circuit. Use complete measured ZMA and common-timing FRD data; include component DCR, tolerances, system impedance/phase, directivity, reverse-polarity null, distortion, and thermal limits. Textbook component tables and optimiser outputs are seeds only.

## 6. Current measurement state

- `rew/SB17NRX2C35-8 installed.zma`: controlled 48 kHz pre-conditioning woofer trace and current crossover-model baseline until a cooled replacement is validated.
- `rew/SB17NRX2C35-8 runin 30Hz 4Vrms 1h 48kHz.zma`: matched-rate post-conditioning comparison; shows lower $F_c$ but contains an approximately 0.34 Ω broadband series-resistance offset and is not yet a cold crossover baseline.
- `rew/SB26STWGC-4 installed.zma`: current tweeter impedance baseline.
- Installed-baffle phase-bearing FRD, horizontal off-axis, distortion/compression, filtered-driver, reverse-null, and final-system impedance/EPDR measurements remain outstanding.
- The protected amplifier-reference path has passed the SU-V570 common-ground,
  UMC202HD phantom-isolation, fixture resistance/DC/physical, full unpowered
  ground-path, and rear-output-topology gates. Both inspected rear output
  sockets are mechanically TRS but electrically tip plus a ring/sleeve common,
  so the mapped Output 1 TS-to-RCA playback lead is compatible and Output 2
  drives the fixture test asymmetrically.
- The direct-baseline TRS cable passes. Before any powered-amplifier connection,
  map the Output 2 source adaptor and inline TRS breakout, then complete the
  matched transfer/noise test in
  [`rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md`](rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md).
  Full-dual approval remains **NO**. Completed raw readings are retained only in
  the [qualification record](rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE_QUALIFICATION.md).

## 7. Immediate development sequence

1. Complete the source-adaptor/breakout preflight and matched transfer/noise
   release gate in
   [`rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md`](rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md).
2. Complete woofer stabilisation under [DRIVER_RUNIN.md](DRIVER_RUNIN.md) and obtain a cooled reproducible 48 kHz ZMA.
3. Retain the tweeter without dedicated run-in; confirm its installed impedance before acoustic work.
4. Acquire installed-baffle magnitude and phase for both drivers with common timing and fixed geometry.
5. Acquire horizontal off-axis and controlled distortion measurements.
6. Import current ZMA/FRD sources into VituixCAD and optimise only within realizable component and load constraints.
7. Build the external development crossover from measured parts and accessible inductor taps.
8. Verify filtered responses, normal sum, reverse-polarity null, directivity, distortion, impedance/EPDR, and thermal behaviour.
9. Iterate one controlled change at a time and update the relevant living record.

## 8. Open decisions

- final damping quantity and distribution;
- final cooled woofer impedance baseline and whether further conditioning is useful;
- exact crossover frequency, topology, acoustic polarity, and component values;
- final L(W1) development implementation: revised former or separate tapped series-trim inductor;
- inductor interlock, binding, and PCB restraint;
- final system impedance classification and amplifier headroom;
- final crossover mounting position;
- final cosmetic veneer and finish;
- final room placement among the documented reversible trials;
- whether DSP remains development-only or is used in the finished system;
- whether a future subwoofer is added;
- production-driver spread and stereo-pair matching after the prototype passes its acoustic and load gates.

## 9. One-line design summary

The accepted prototype is a **sealed, near-wall, measurement-designed passive two-way loudspeaker** using an SB17NRX2C35-8 woofer and SB26STWGC-4 waveguide tweeter in an approximately 21.7 L geometric-net, 280 × 430 × 300 mm plywood cabinet with a 36 mm rounded baffle, removable development rear panel, externally accessible crossover, and neutral low-distortion reproduction as the overriding goal.
