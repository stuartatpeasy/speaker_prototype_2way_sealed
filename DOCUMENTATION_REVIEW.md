# Project Documentation Review Procedure

Use this procedure when the user requests a comprehensive documentation review,
consolidation, or handover preparation. It supplements `AGENTS.md`; direct user
instructions still take precedence.

## 1. Purpose

Minimise documentation size and context cost without losing project-relevant
evidence, provenance, safety information, decisions, or the ability to reproduce
the work. Prefer one authoritative statement of each fact and links from its
consumers.

## 2. Review Principles

1. Read `README.md` first and follow its documentation index and minimal reading
   routes.
2. Preserve verified measurements, conditions, units, dates, instruments,
   calculations, uncertainty, decisions, stop rules, and unresolved gates.
3. Keep verified measurements, derivations, published data, inferences,
   provisional decisions, and open items explicitly distinguished.
4. Preserve unique raw measurements, manually authored sources, and artefacts
   without a verified reconstruction path.
5. Remove conversational narration, repeated instructions, obsolete next
   actions, superseded UI troubleshooting, and project-irrelevant machine
   details once their decision-relevant conclusion is recorded.
6. Do not copy current status into several files. Give each subject one authority
   and link to it.
7. Separate current operating instructions from completed evidence and
   diagnostic history.
8. Do not split or merge files merely to alter their size. Change boundaries
   only when topic ownership, reading routes, or current-versus-historical use
   becomes clearer.

## 3. Parallel Review Roles

Use agents when requested or when they materially reduce review time. Assign
non-overlapping roles:

1. a session-evidence agent to identify facts, measurements, corrections,
   decisions, and open actions not yet persisted;
2. topic agents to review distinct document groups for duplication, stale
   content, scope, and reproducibility;
3. an independent validation agent to check links, index coverage,
   reconstruction routes, and contradictions; and
4. one integrating agent responsible for final edits and consistency.

Agents should normally return findings before overlapping files are edited. The
integrating agent remains responsible for checking every change.

## 4. Inventory And Scope

1. Inspect Git status before editing and identify user-owned or unrelated
   changes.
2. Inventory every tracked and untracked project file.
3. Read every tracked Markdown and other documentation-bearing text file fully.
4. For binary, CAD, measurement, and generated artefacts, establish their role,
   provenance, retention status, and reconstruction path; do not treat them as
   disposable merely because their contents cannot be text-reviewed.
5. Record which document owns each major topic and which files merely consume
   it.

## 5. Session-Evidence Capture Gate

Before deleting, moving, or consolidating text, create a temporary evidence
ledger containing:

| Item | Evidence class | Source | Intended authority | Persisted |
| --- | --- | --- | --- | --- |

Capture at least:

- new measurements and their conditions;
- corrections to previously reported facts;
- calculations and assumptions that affect a decision;
- passed, failed, waived, and still-pending gates;
- superseded conclusions and why they changed;
- current hardware/software configuration where project-relevant;
- the exact next safe action and current stop conditions; and
- privacy-sensitive raw files whose decision-relevant results must instead be
  transcribed.

Do not proceed with destructive consolidation until every relevant item has one
durable destination.

## 6. Per-File Review

For every documentation file, determine:

1. its authoritative topic and intended reader;
2. whether each section is current procedure, current conclusion, raw evidence,
   dated history, or background explanation;
3. whether another file states the same fact;
4. whether any value, status, filename, link, next action, or dependency is
   stale or contradictory;
5. whether the information is directly relevant to the project;
6. whether a concise table, equation, or link can replace repeated prose;
7. whether completed step-by-step dialogue can be reduced to results,
   conditions, and decision rationale; and
8. whether the file still contains enough information to reproduce or audit its
   work.

Prefer deleting a duplicate and linking to its authority. Do not summarise
unique numerical evidence so aggressively that test conditions or uncertainty
are lost.

## 7. Split, Merge, And Archive Decisions

Consider splitting a file when it:

- mixes current procedure with extensive completed history;
- contains more than one independent topic authority;
- is routinely loaded for a small current section but dominated by archival
  material; or
- duplicates large sections needed by different hardware or workflows.

Consider merging or removing a file when it:

- has no distinct authority;
- only repeats another document;
- describes a completed temporary gate whose raw evidence belongs in an
  existing qualification record; or
- adds another navigation step without reducing normal context.

When splitting:

1. keep current instructions and conclusions in the routinely read file;
2. move raw evidence or chronology to a clearly labelled record;
3. add reciprocal links and update `README.md`;
4. update every affected minimal reading route;
5. search the whole project for the old filename and stale section references;
   and
6. preserve Git history through ordinary committed changes rather than copying
   obsolete narrative indefinitely.

## 8. Repeatability And Reconstruction

For repeatable work, retain:

- inputs and raw source artefacts;
- equipment and relevant topology;
- software/tool and identifiable dependency versions;
- calibration and configuration;
- commands or complete manual procedure;
- units, tolerances, environmental conditions, and acceptance criteria; and
- the expected verification result.

If a generated output is intentionally uncommitted, retain and document all
inputs, generator code, dependencies, configuration, command, and verification.
Reassess `.gitignore` under the rules in `AGENTS.md`.

## 9. Validation

After edits:

1. validate every local Markdown link and anchor;
2. spot-check external links used as technical authorities;
3. confirm root and topic heading numbering is coherent;
4. confirm every durable topic file is indexed in `README.md`;
5. exercise each minimal reading route and ensure it reaches the current
   authority without requiring an archive unnecessarily;
6. search for stale filenames, old status phrases, contradictory release
   states, and obsolete next-action text;
7. compare the evidence ledger against the final files;
8. inspect the complete Git diff, preserving unrelated user changes;
9. inspect representative retained and ignored files if `.gitignore` changed;
10. check that no secrets, private host inventories, or unnecessary personal
    data entered the repository; and
11. run any available reconstruction or documentation-validation checks.

## 10. Handover And Git

The handover must state:

- the current engineering state;
- the exact next action and applicable safety gate;
- unresolved questions and deliberately closed investigations;
- files created, moved, merged, or removed;
- material information intentionally retained only in an archive;
- validation performed and any limitations; and
- Git commit and push status.

Commit or push only when the user has requested it. Before committing, inspect
the full diff and status. After pushing, verify that the intended branch and
remote commit agree.

## 11. Completion Criteria

The review is complete only when:

- every relevant session result is persisted exactly once in an appropriate
  authority or evidence record;
- current procedures contain no obsolete next actions;
- completed history does not dominate routine reading routes;
- links, indexes, and reconstruction routes work;
- no unique evidence or user work has been lost;
- the documentation remains sufficient to reproduce the work from scratch; and
- the final diff has been reviewed as a coherent whole.
