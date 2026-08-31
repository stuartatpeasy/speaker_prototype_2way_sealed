# Project Working Instructions

These instructions apply to the entire project tree. A direct user instruction
for a particular task takes precedence.

## 1. Project orientation and authority

1. Begin project work by reading [README.md](README.md), then load only the
   task-relevant files identified by its documentation index and minimal reading
   routes.
2. Treat `README.md` as the high-level project source of truth and entry point.
   Treat each indexed topic file as the detailed authority for its subject.
3. Before driver, enclosure-alignment, crossover, measurement, simulation, or
   driver-procurement work, read [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md).
4. Keep verified measurements, derivations, inferences, provisional decisions,
   and open items explicitly distinguished. Do not silently promote an estimate
   or exploratory result into a settled design decision.
5. Preserve user work and unrelated changes. Do not initialise Git, commit,
   delete artefacts, or untrack files unless the user asks.

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

## 3. Keep Markdown current in the same turn

1. For every project task, identify whether the work changes any documented
   fact, measurement baseline, calculation, decision, procedure, filename,
   dependency, reconstruction route, status, priority, or open item.
2. If it does, update every affected Markdown file before completing that same
   task. Do not knowingly leave a document stale or defer an obvious update to a
   future turn.
3. Do not rewrite unrelated documents merely to create activity. “Keep current”
   means correcting documents affected by the work, not introducing churn.
4. When adding, renaming, moving, or deleting a durable Markdown file, update
   the documentation index and any affected minimal reading route in
   [README.md](README.md). Search the whole project for stale filename and link
   references.
5. Keep the root and topic-document section/subsection hierarchy numbered.
6. Preserve dated history and superseded conclusions where they explain the
   engineering process. Label the new conclusion and why it supersedes the old
   one rather than rewriting history. When a measurement baseline is explicitly
   replaced, update every current conclusion and source reference that depends
   on it.
7. Maintain the evidence labels and dated change log in
   [DRIVER_ANALYSIS.md](DRIVER_ANALYSIS.md). Add to that record whenever new
   conditioning, electrical/acoustic measurements, calculations, simulations,
   crossover tuning, pair matching, procurement decisions, or superseding
   conclusions materially change the driver picture.
8. Keep specialised procedures beside their data where appropriate (`rew/` for
   REW work and `vituixcad/` for VituixCAD work), and link them from the relevant
   indexed Markdown file.
9. Whenever a generated output becomes intentionally uncommitted, document the
   complete reconstruction route: retained inputs, generator/tool, pinned or
   otherwise identified dependencies, configuration, command, and the expected
   verification result.

## 4. Keep `.gitignore` current without losing information

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

## 5. Completion checks

Before completing any task that changes project files:

1. search affected Markdown and the project index for stale facts, names, and
   links;
2. verify local Markdown link targets;
3. confirm new or changed topic documents are indexed appropriately;
4. confirm every newly ignored output has a committed and documented
   reconstruction path;
5. inspect the actual ignore result for representative retained and excluded
   files when `.gitignore` changes;
6. inspect Git status if this directory has become a valid repository, while
   preserving unrelated user changes; and
7. report material documentation and ignore-policy updates in the handoff.
