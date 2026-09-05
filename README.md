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
- The SU-V570 reference fixture has passed topology, construction, resistance,
  four-polarity DC clamp, ground-path, interconnect, and proportionate AC gates.
  It is released for controlled UMC202HD bench use under the documented startup
  and stop rules. The UMC202HD rear outputs are mechanically TRS but
  electrically TS; the source adaptor, straight-through cable, and breakout
  cable are mapped.
- The first UMC202HD full-dual checkout passed the powered no-signal check and
  reached a clean `1.00 V RMS` at the woofer, but recurring source-stream mutes
  block its sweeps on the desktop. The interface plays continuously on a
  Windows 11 laptop, and substituting the UMC22's known-good cable did not alter
  the desktop fault. A live-Linux boot is the next useful discriminator. See
  [`rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md`](rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md).
- A risk-accepted UMC22 fallback is now the FRD critical path. Normal predicted
  reference level is `0.09892 V RMS`, about `19.9 dB` below its published
  `+2 dBu` instrument-input maximum, but fault-level survival is not guaranteed.
  Direct internal inspection establishes that both UMC22 rear outputs also use
  separate mechanical TRS contacts with ring and sleeve/shield joined on the
  same PCB copper fill; they are two-node, unbalanced, TS-equivalent outputs.
  The unpowered `INST 2` contact map passes: tip is isolated, while ring,
  sleeve, and USB shell are a sub-ohm common. Gate B phantom isolation also
  passes: all on/off readings remained at or below approximately `0.0020 V DC`
  and settled to zero. Gate C now confirms `9125 ohm` from amplifier positive
  to input tip and `10127 ohm` to every mapped return, proving there is no R1
  bypass; its `0.290-0.311 ohm` complete return paths are also explained and
  stable. Gates A-C therefore pass. Gate D's amplifier-disconnected no-signal
  check also passes: `0.0015 V DC` settled to zero with no clipping or abnormal
  behaviour. REW device enumeration also passes using Java exclusive-mode UMC22
  input/output, independent L/R channels, `48 kHz`, and calibration `None`.
  The no-excitation channel/timing UI assignment initially used measurement L,
  reference input R, and reference output R, with loopback calibration/timing,
  IR merge, and zero offset. The user has also
  confirmed unity input scaling, the UMC22-specific measurement name, and the
  `20-20000 Hz` first-checkout range. The bounded amplifier-disconnected
  `1 kHz` check also passes at `0.0207 V RMS`, with only `0.0205-0.0210 V RMS`
  slow movement and no clipping, dropout, or abnormality. Live REW reference
  capture was initially held because `Ref In` remained at approximately
  `-93.72 dBFS` across the full `GAIN 2`
  range despite the external tone. The cause was the accidentally selected
  non-exclusive input endpoint; choosing the `EXCL:` variant immediately
  restored linear gain response. Input 2 now reads a stable `-20.88 dBFS` at
  `0.0218 V RMS`. Input 1 also responds normally to its gain control and nearby
  sound without clipping. The controlled headphone-to-microphone setup also
  passes at `-19.5 dBFS` main and `-20.84 dBFS` reference, with a stable
  `0.0230 V RMS` external reference and no clipping, dropout, or abnormality.
  The first amplifier-disconnected `1M` full-duplex sweep then completed with
  no warning, error, clipping, audible discontinuity, or abnormality; its
  impulse has one clear dominant arrival. This is the first verified dropout-
  free UMC22 REW full-duplex sweep, but its timing is invalid: the stored timing
  index is `N/A` and System Delay is unavailable because reference output R was
  physically unconnected while the fixture sensed measurement output L. The
  second sweep corrected both output selectors to L and also ran without
  clipping or dropout at a confirmed `0.0222 V AC`, but it stored reference
  input L rather than R. Its almost-flat SPL/phase trace is consequently an
  invalid self-reference and its timing index is still `N/A`. The exact routing
  is measurement/reference outputs L, measurement input L, and reference input
  R. Selecting that reference input then caused REW V5.40 beta 133 to throw
  `Index 1 out of bounds for length 1`. A restart restored a visually coherent
  exact-`EXCL:`, `48 kHz`, L/L/L/R configuration. The retry with Java `Stereo
  only` then completed without the exception and stored the intended reference
  output L/input R, but still produced no timing index or System Delay. Its
  `0.5100 ms` peak and `0.4792 ms` IR start are physically plausible but do not
  close timing validity. A proposed read-only inspection of retained measurement
  and reference captures has been withdrawn: the current REW Scope is a live
  two-channel instrument and offers no route to a preceding measurement's raw
  captures. The next proportionate discriminator was one short, amplifier-
  disconnected `256k` sweep using loopback as timing reference only, with the
  established L/L/L/R routing and all physical settings unchanged. That sweep
  has now passed without warning, clipping, dropout, or exception. REW stored
  timing-reference index `47970.52`, System Delay `0.6141 ms`, IR start
  `0.5208 ms`, output L, and reference input R. Gate D therefore passes for the
  UMC22 hardware, two-channel stream, routing, and ordinary loopback timing; the
  failure is confined to the combined mode's IR-merge treatment in the present
  beta-133 setup. The final unchanged `256k` low-voltage check
  has also established the UMC22/electrical-reference magnitude-calibration
  route. `Make calibration data from loopback response` produced `Soundcard:
  Loopback cal`, reference index
  `47975.52`, and System Delay `0.5100 ms`, with no warning or abnormality. Use
  that treatment for the UMC22 and exclude IR merging. Gate D and its calibration
  route are complete. Gate E's switched-off full-dual assembly also passes:
  woofer and fixture are in
  parallel at B-left with correct polarity, the breakout is restrained and
  insulated, and headphone, Output 2, and AUX right are empty. Its subsequent
  UMC22-only USB/phantom no-signal observation also passes: the phantom
  indicator illuminated, neither channel clipped, and there was no unexpected
  sound, instability, smell, heating, or other abnormality. The subsequent
  minimum-volume SU-V570 no-signal power-up also passes after approximately one
  minute: the woofer remained silent, neither UMC22 channel clipped, and there
  was no transient or persistent hum/buzz, instability, heating, smell, smoke,
  or other abnormality. The controlled woofer level now passes with
  `1.0000 V AC` indicated on the Agilent U1282A at the SU-V570's `-38 dB`
  volume-scale mark. The gross protected-reference voltage also passes at a
  stable `98.53 mV AC`, giving a measured transfer of `0.09853`
  (`-20.129 dB`), only `-0.39%` from prediction. Generator was stopped, neither
  channel clipped, and there was no dropout, instability, or other abnormality.
  The breakout has now been removed, the fixture is connected directly to
  `INST 2`, the U1282A is back across the woofer, and the powered final
  connection shows no abnormality. Reference-input `GAIN 2` now passes at a
  stable `-20.87 dBFS` (`+/-0.01 dB`) with `GAIN 2` approximately 2 o'clock,
  the woofer at `1.0003 V AC`, at least `6 dB` peak headroom, and no clipping,
  dropout, or anomaly. The supplied
  `calibration/ECM8000_calibration_data.csv` is a generic `0-degree` response,
  not a serial-number-specific calibration and not an absolute-sensitivity
  calibration. Its orientation matches the present microphone aimed at the
  cabinet. The CSV has now been made directly REW-compatible by adding the
  documented required whitespace after its commas without changing any numeric
  value; the redundant pre-consolidation `.cal` copy has been removed at the
  user's request. Apply the CSV only to microphone input L; reference input R
  must remain without microphone calibration. The reported acoustic geometry
  is `1000 mm` capsule-to-baffle,
  on the woofer axis, with a fixed microphone and a secured 10-degree rotation
  jig. The earlier derived file loaded without warning and persisted on L only,
  with R showing `None`; because the retained canonical filename is now the
  CSV, reselecting that CSV and reconfirming the same assignment is the next
  no-signal step. Its unquantified unit-to-unit error keeps resulting acoustic
  magnitude and phase provisional. See
  [`rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md`](rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md).

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
| [AGENTS.md](AGENTS.md) | Standing collaboration instructions, including proportionate testing and commissioning, agent delegation, same-turn Markdown maintenance, conservative ignore policy, and completion checks. |
| [DOCUMENTATION_REVIEW.md](DOCUMENTATION_REVIEW.md) | Reusable comprehensive documentation-review and handover procedure. |
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
| [rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md](rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md) | Completed interconnect preflight, low-voltage observations, and proportionate AC release decision. |
| [rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md](rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md) | Conditional UMC22 fallback: risk boundary, level calculations, minimum connector/phantom/ground/full-duplex gates, and release state. |
| [rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md](rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md) | Single authority for the desktop UMC202HD dropout evidence, closed causes, remaining boundary, and live-Linux next test. |

### 4.1 Minimal reading routes

- **Driver, run-in, or enclosure alignment:** this file + `DRIVER_ANALYSIS.md`; add `DRIVER_RUNIN.md` for conditioning and `CABINET_DESIGN.md` for box construction/damping.
- **Cabinet fabrication:** this file + `CABINET_DESIGN.md`.
- **Crossover development:** this file + `DRIVER_ANALYSIS.md` + `CROSSOVER_DESIGN.md` + `MEASUREMENT_WORKFLOW.md`.
- **Acoustic measurements:** this file + `MEASUREMENT_WORKFLOW.md` + the relevant procedure under `rew/`.
- **Room or placement work:** this file + `ROOM_DETAILS.md`; re-inspect the current `3d_models/Listening room.dae` after any geometry change.
- **Amplifier loopback/reference work:** this file +
  `rew/SU-V570_TO_UMC202HD_REFERENCE_FIXTURE.md`. Add the SU-V570 topology
  record or qualification record only to audit those completed gates. For the
  release rationale, add `rew/REFERENCE_FIXTURE_AC_COMMISSIONING.md`. The
  fixture gate now says `YES` for controlled bench use; add
  `rew/FRD_MEASUREMENT_SETUP_TEST.md` for the switched-off full-dual connection,
  minimum-volume startup, and practical performance checks.
  If substituting the UMC22, also read
  `rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md`; the UMC202HD release does not
  automatically qualify the UMC22 connector or phantom behaviour.
- **UMC202HD desktop-dropout diagnosis:** this file +
  `rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md`; do not load the fixture
  qualification archive unless raw electrical evidence is needed.
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
- Raw LatencyMon text exports are intentionally local-only because they disclose
  private, project-irrelevant host details. Decision-relevant results are in
  `rew/UMC202HD_DESKTOP_DROPOUT_DIAGNOSIS.md`.
- Installed-baffle phase-bearing FRD, horizontal off-axis, distortion/compression, filtered-driver, reverse-null, and final-system impedance/EPDR measurements remain outstanding.
- The UMC202HD reference fixture is electrically released, but that interface
  remains blocked for measurement by the desktop dropout. The UMC22 fallback
  has passed its unpowered Input 2 contact map and otherwise-unloaded USB-
  powered phantom-isolation gate. Its Gate C amplifier-positive isolation also
  passes, and the completed return map closes Gate C. The amplifier-disconnected
  Gate D no-signal check and REW device enumeration also pass; channel/timing
  assignment and pre-excitation settings now pass as well. The controlled
  amplifier-disconnected `1 kHz` level passes at `0.0207 V RMS`; live reference
  capture also passes after selecting the exclusive input endpoint, at
  `-20.88 dBFS` for `0.0218 V RMS`. The Input 1 microphone-channel check also
  passes, as does the controlled headphone-to-microphone level setup. The first
  amplifier-disconnected `1M` full-duplex sweep completes without dropout or
  error and shows one dominant arrival, but its timing is invalid because the
  unconnected output R was selected as the reference output. A second sweep
  with both outputs L also completes cleanly, but mistakenly stores reference
  input L and therefore produces invalid self-referenced response/timing data.
  Selecting reference input R then triggered a REW beta 133 one-channel array
  exception. The post-restart settings audit passes and the `Stereo only` exact-
  routing retry completes without that exception, but timing metadata remains
  unavailable despite the stored L/R assignments. REW Scope cannot inspect the
  preceding sweep's raw captures. The subsequent amplifier-disconnected `256k`
  timing-only sweep passes with reference index `47970.52`, System Delay
  `0.6141 ms`, exact L/L/L/R routing, and no warning, clipping, dropout, or
  exception. Gate D is closed and the IR-merge treatment remains excluded. The
  final low-voltage `256k` check using `Make calibration data from loopback
  response` passes with `Soundcard:
  Loopback cal`, reference index `47975.52`, and System Delay `0.5100 ms`. Load
  the ECM8000 calibration before reusable acoustic capture; establish and review
  Gate E's complete switched-off wiring before amplifier power. That assembly
  now passes, including the woofer-only load, fixture polarity, insulation, and
  unused sockets. The UMC22-only USB/phantom no-signal observation also passes
  with normal phantom indication, no clipping, and no audible, stability,
  thermal, smell, or other abnormality. The minimum-volume SU-V570 no-signal
  power-up also passes after approximately one minute, with a silent woofer and
  no clipping or other abnormality. The controlled woofer level now passes with
  `1.0000 V AC` indicated on the U1282A at the SU-V570's `-38 dB` scale mark.
  The protected reference also measures a stable `98.53 mV AC`, only `-0.39%`
  from the resistance-derived prediction, with no clipping, dropout,
  instability, or other abnormality. Final direct connection of the fixture to
  `INST 2` now passes its powered no-signal observation. Reference-input gain
  also passes at `-20.87 dBFS` with stable `1.0003 V AC` woofer voltage and no
  clipping or dropout. The generic `0-degree` ECM8000 CSV is now REW-compatible,
  and the reported microphone orientation and `1000 mm` on-axis geometry match
  it. The pre-consolidation derived file passed loading and L-only persistence,
  but the canonical CSV must now be reselected on input L because that derived
  file was removed at the user's request. Installed-driver FRD is not yet
  approved.

## 7. Immediate development sequence

1. Qualify the risk-accepted UMC22 fallback under
   [`rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md`](rew/UMC22_RISK_ACCEPTED_FRD_FALLBACK.md),
   then complete the controlled full-dual three-repeat checkout. Continue the
   desktop-specific UMC202HD live-Linux diagnosis independently.
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
