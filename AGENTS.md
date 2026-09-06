# Project Working Instructions

These instructions apply to the entire project tree. A direct user instruction
for a particular task takes precedence.

## 1. Project orientation and authority

1. Begin project work by reading [README.md](README.md), then follow exactly one
   task-oriented reading route unless the task genuinely spans several topics.
2. Treat `README.md` as the high-level project source of truth and entry point.
   Treat each indexed topic file as the detailed authority for its subject.
3. Before driver, enclosure-alignment, crossover, simulation, or
   driver-procurement work, read [doc/DRIVER_ANALYSIS.md](doc/DRIVER_ANALYSIS.md).
   For measurement operation, read it only when the task depends on driver
   baselines or conclusions; otherwise use the measurement route in `README.md`.
4. Keep verified measurements, derivations, inferences, provisional decisions,
   and open items explicitly distinguished. Do not silently promote an estimate
   or exploratory result into a settled design decision.
5. Preserve user work and unrelated changes. Do not initialise Git, commit,
   delete artefacts, or untrack files unless the user asks.
6. Treat `CURRENT PROCEDURE` and current topic authorities as normal context.
   Load `QUALIFICATION` records only to audit a gate, change qualified hardware,
   or diagnose a failure. Load `HISTORY` only for provenance or a superseded
   decision. Do not routinely ingest history merely because it is linked.

## 2. Technical communication

Regarding technical topics: teach the user technical mathematics in small,
sequential chunks. Anchor abstractions in circuit or physical intuition, derive
important results rather than merely stating them, and follow each new idea with
a worked example and a manageable exercise. Pause while the user shows their
working, then give direct and frank correctness feedback, identifying the
precise point of any error. Use dimensional and physical sanity checks.

Assume a rusty EE-undergraduate mathematical foundation: the user's conceptual
and engineering reasoning is sound, but calculus recall and algebraic fluency
need rebuilding. Do not over-simplify the engineering ideas, but avoid
unexplained mathematical jumps. If a concept does not settle immediately, park
it and revisit it from another direction later.

## 3. Proportionate project process and safety

1. Keep every proposed test procedure, measurement, safety verification, and
   other commissioning step proportionate to, and justified by, the nature and
   intended use of this project.
2. The objective is not laboratory-grade assurance or a product proven against
   every potentially applicable safety standard. It is a system that works
   well, can be reproduced at very limited scale, and has basic electrical and
   mechanical safety.
3. Before proposing any activity or process step, consider its likely practical
   value, the uncertainty or credible risk it addresses, and its cost in time,
   effort, complexity, and enjoyment. Do not add work merely because a more
   exhaustive or more precise process is possible.
4. Preserve checks that address credible electrical, mechanical, equipment, or
   personal-safety hazards, but distinguish those checks explicitly from
   optional characterisation, optimisation, or marginal confidence-building.
5. Treat this as a pleasant and absorbing hobby intended to produce work to a
   good standard. Do not turn it into tedious unpaid work by pursuing immaterial
   improvements or the last hundredth of a percent without a project-relevant
   justification.

## 4. Agent delegation

1. Use agents when independent or parallel work would materially reduce the
   wall-clock time needed to complete a task.
2. Select each agent's model and effort level deliberately to match the
   complexity, uncertainty, and consequence of its assigned work.
3. Do not delegate when coordination and review overhead would outweigh the
   likely time saving. The primary agent remains responsible for integrating
   and checking delegated results.

## 5. Keep Markdown current in the same turn

1. For every project task, identify whether the work changes any documented
   fact, measurement baseline, calculation, decision, procedure, filename,
   dependency, reconstruction route, status, priority, or open item.
2. If it does, update every affected Markdown file before completing that same
   task. Do not knowingly leave a document stale or defer an obvious update to a
   future turn.
3. Do not rewrite unrelated documents merely to create activity. “Keep current”
   means correcting documents affected by the work, not introducing churn.
4. When adding, renaming, moving, or deleting a durable Markdown file, update
   the nearest subtree dispatcher and any affected task-oriented reading route
   in [README.md](README.md). Add detailed qualification or history files to the
   root map only through their dispatcher. Search the whole project for stale
   filename and link references.
5. Keep the root and topic-document section/subsection hierarchy numbered.
6. Preserve dated history and superseded conclusions where they explain the
   engineering process. Label the new conclusion and why it supersedes the old
   one rather than rewriting history. When a measurement baseline is explicitly
   replaced, update every current conclusion and source reference that depends
   on it.
7. Maintain evidence labels and current driver conclusions in
   [doc/DRIVER_ANALYSIS.md](doc/DRIVER_ANALYSIS.md). Add to that record whenever
   conditioning, electrical/acoustic measurements, calculations, simulations,
   crossover tuning, pair matching, procurement decisions, or superseding
   conclusions materially change the driver picture. Put detailed chronology
   in its history record and non-driver measurement evidence in the relevant
   REW qualification or history authority.
8. Keep specialised procedures under the corresponding documentation subtree
   (`doc/rew/` for REW work), while retaining measurement and project artefacts
   in their existing data directories (`rew/` and `vituixcad/`). Link procedures
   from the relevant indexed Markdown file.
9. Give each durable fact one current authority. Other current documents should
   state only the consequence they consume and link to that authority. A history
   record may repeat a fact as part of dated chronology but must identify itself
   as non-current context.
10. Begin each routinely loaded topic authority or procedure with a compact
    state card where applicable: lifecycle, owns, does not own, read-when rule,
    current approved action or conclusion, next gate, limitations, and
    last-reviewed date. Keep detailed results in their owning evidence record.
11. Whenever a generated output becomes intentionally uncommitted, document the
    complete reconstruction route: retained inputs, generator/tool, pinned or
    otherwise identified dependencies, configuration, command, and the expected
    verification result.
12. Keep `README.md` as a compact dashboard and router. It may state the current
    phase, the decision-relevant consequence for each subsystem, task routes,
    and immediate priorities, but it must not accumulate test transcripts,
    detailed derivations, qualification evidence, or chronological narrative.
    Put those details in their owning topic, qualification, or history record.
13. Keep durable project Markdown under `doc/`, except for the root `README.md`
    and `AGENTS.md`. Keep measurements, CAD, source code, and generated artefacts
    in their existing data/source trees rather than moving them under `doc/`.
    Add a subtree dispatcher only when it materially shortens or clarifies the
    task routes through that subtree.
14. Do not use a current procedure as an append-only work log. When a procedure
    step is completed, move durable results into the owning current authority or
    qualification record, retain decision-relevant superseded chronology in a
    dated history record, and revise the procedure to show only its current
    prerequisites, safe next action, stop rules, and unresolved gates.

## 6. Keep `.gitignore` current without losing information

1. Reassess [`.gitignore`](.gitignore) whenever work introduces a new tool,
   dependency manager, cache, temporary workspace, build directory, generated
   file class, export pipeline, or machine-specific output.
2. Apply this priority order:
   1. preserve unique information;
   2. preserve practical reproducibility;
   3. minimise committed payload.
3. Ignore a file only when it is disposable local state or its useful content
   can be reconstructed from committed sources. If the reconstruction inputs or
   settings are incomplete, retain the file or stop and ask the user before
   ignoring it.
4. Prefer narrow, explicit project paths over broad extension rules. Broad
   rules can silently hide a future source file that happens to share an output
   extension.
5. Never globally ignore measurement/project formats such as `.zma`, `.mdat`,
   `.frd`, `.vxp`, `.xlsx`, `.pdf`, `.stl`, `.dae`, `.stp`, `.obj`, `.lib`,
   `.png`, or `.jpg`. Some current scripted DAE/preview outputs are ignored only
   by explicit directory rules because matching generators are committed.
6. Keep raw measurements, manually authored CAD, imported reference geometry,
   fabrication sources, source images, and any artefact without a verified
   reconstruction path.
7. When ignoring a dependency tree or environment, commit the smallest adequate
   manifest or lock file needed to recreate it. Update that manifest when the
   relevant dependency versions change.
8. Keep 3D-printer G-code ignored, retain the source STL or slicer project, and
   update `3d_models/PRINT_SETTINGS.json` whenever a materially different print
   job becomes part of the project. Prefer committing future `.3mf` slicer
   projects because they preserve placement and complete slicing state.
9. Do not delete a file merely because it is ignored. Remember that adding an
   ignore rule does not untrack a file already committed.
10. Keep explanatory comments in `.gitignore` accurate, especially its explicit
    retained/ignored boundary. Remove or revise an ignore rule if its generator
    or reconstruction source ceases to exist.

## 7. Completion checks

For a user-requested comprehensive documentation review or handover, follow
[`doc/DOCUMENTATION_REVIEW.md`](doc/DOCUMENTATION_REVIEW.md) in addition to this file.

Before completing any task that changes project files:

1. search affected Markdown and the project index for stale facts, names, and
   links;
2. verify local Markdown link targets;
3. confirm new or changed current documents are indexed appropriately and that
   qualification/history records are reachable through a subtree dispatcher;
4. confirm every newly ignored output has a committed and documented
   reconstruction path;
5. inspect the actual ignore result for representative retained and excluded
   files when `.gitignore` changes;
6. inspect Git status if this directory has become a valid repository, while
   preserving unrelated user changes; and
7. report material documentation and ignore-policy updates in the handoff.
