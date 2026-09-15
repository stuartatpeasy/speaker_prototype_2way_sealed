#!/usr/bin/env python3
"""Run proportionate checks for changed project files and return a short report."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    from .project_docs import check_links, project_root, route_report, tracked_markdown
except ImportError:
    from project_docs import check_links, project_root, route_report, tracked_markdown


def command(root: Path, args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=root, capture_output=True, text=True)


def changed_files(root: Path) -> list[str]:
    names = set()
    for args in (["git", "diff", "--name-only", "-z"],
                 ["git", "diff", "--cached", "--name-only", "-z"],
                 ["git", "ls-files", "--others", "--exclude-standard", "-z"]):
        result = subprocess.run(args, cwd=root, capture_output=True, check=True)
        names.update(name.decode() for name in result.stdout.split(b"\0") if name)
    return sorted(names)


def check(root: Path) -> dict:
    all_changed = changed_files(root)
    changed = [name for name in all_changed if name.startswith(("src/", "tests/", "doc/"))
               or name in ("README.md", "AGENTS.md", ".gitignore")]
    markdown = [name for name in changed if name.endswith(".md") and (root / name).is_file()]
    python_changed = [name for name in changed if name.endswith(".py") and
                      name.startswith(("src/", "tests/"))]
    python = [name for name in python_changed if (root / name).is_file()]
    checks = []
    if markdown:
        links = check_links(root, tracked_markdown(root) +
                            [root / name for name in markdown if root / name not in tracked_markdown(root)])
        checks.append({"name": "markdownLinks", "passed": links["problemCount"] == 0,
                       "checked": links["localLinks"], "details": links["problems"]})
        routes = route_report(root)
        checks.append({"name": "documentationRoutes", "passed": not routes["unreachable"],
                       "checked": routes["markdownFiles"], "details": routes["unreachable"]})
    if python_changed:
        if python:
            compiled = command(root, [sys.executable, "-m", "py_compile", *python])
            checks.append({"name": "pythonCompile", "passed": compiled.returncode == 0,
                           "checked": len(python), "details": compiled.stderr[-2000:] if compiled.returncode else []})
        tested = command(root, [sys.executable, "-m", "unittest", "discover", "-s", "tests"])
        count = re.search(r"Ran (\d+) tests?", tested.stderr)
        checks.append({"name": "unitTests", "passed": tested.returncode == 0,
                       "checked": int(count.group(1)) if count else None,
                       "details": tested.stderr[-3000:] if tested.returncode else []})
    unstaged = command(root, ["git", "diff", "--check"])
    staged = command(root, ["git", "diff", "--cached", "--check"])
    checks.append({"name": "diffWhitespace",
                   "passed": unstaged.returncode == 0 and staged.returncode == 0,
                   "details": (unstaged.stdout + staged.stdout)[-2000:]
                   if unstaged.returncode or staged.returncode else []})
    failed = [item for item in checks if not item["passed"]]
    return {"kind": "changedProjectChecks", "changedFileCount": len(changed),
            "otherChangedFileCount": len(all_changed) - len(changed),
            "changedFiles": changed, "passed": not failed,
            "checks": [{key: value for key, value in item.items() if key != "details"}
                       for item in checks], "failures": failed}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    try:
        result = check(project_root())
    except (OSError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"kind": "changedProjectChecks", "passed": False, "error": str(exc)}))
        return 2
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
