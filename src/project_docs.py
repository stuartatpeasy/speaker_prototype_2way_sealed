#!/usr/bin/env python3
"""Bounded, offline checks for project Markdown links and reading routes."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import deque
from pathlib import Path
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"(?<!!)\[[^\]]*\]\((<[^>]+>|(?:[^()]|\([^()]*\))*)\)|!\[[^\]]*\]\((<[^>]+>|(?:[^()]|\([^()]*\))*)\)")
REFERENCE = re.compile(r"^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)", re.MULTILINE)
REF_USE = re.compile(r"(?<!!)\[[^\]]+\]\[([^\]]+)\]")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
WORD = re.compile(r"\b[\w'-]+\b")


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def tracked_markdown(root: Path) -> list[Path]:
    result = subprocess.run(["git", "ls-files", "-z", "--", "*.md"], cwd=root,
                            capture_output=True, check=True)
    files = [root / name.decode() for name in result.stdout.split(b"\0") if name]
    new = subprocess.run(["git", "ls-files", "--others", "--exclude-standard", "-z",
                          "--", "doc/*.md"], cwd=root, capture_output=True, check=True)
    files.extend(root / name.decode() for name in new.stdout.split(b"\0") if name)
    return list(dict.fromkeys(files))


def strip_code(text: str) -> str:
    lines = []
    fenced = False
    marker = ""
    for line in text.splitlines(keepends=True):
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            if not fenced:
                fenced, marker = True, match.group(1)[0]
            elif match.group(1)[0] == marker:
                fenced = False
            lines.append(" " * (len(line.rstrip("\r\n"))) + line[len(line.rstrip("\r\n")):])
        elif fenced:
            lines.append(" " * (len(line.rstrip("\r\n"))) + line[len(line.rstrip("\r\n")):])
        else:
            lines.append(re.sub(r"`+[^`\n]*`+", lambda m: " " * len(m.group()), line))
    return "".join(lines)


def slug(value: str) -> str:
    value = re.sub(r"\[[^\]]+\]\([^)]*\)", "", value)
    value = re.sub(r"<[^>]+>", "", value)
    value = value.lower().strip()
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    return re.sub(r"\s+", "-", value)


def anchors(text: str) -> set[str]:
    counts: dict[str, int] = {}
    found = set(re.findall(r'<a\s+(?:name|id)=["\']([^"\']+)', text, re.I))
    for match in HEADING.finditer(strip_code(text)):
        base = slug(match.group(1))
        number = counts.get(base, 0)
        counts[base] = number + 1
        found.add(f"{base}-{number}" if number else base)
    return found


def links(path: Path) -> list[tuple[int, str]]:
    text = strip_code(path.read_text(encoding="utf-8"))
    definitions = {m.group(1).casefold(): m.group(2) for m in REFERENCE.finditer(text)}
    results = []
    for match in LINK.finditer(text):
        target = match.group(1) or match.group(2)
        if target:
            results.append((text.count("\n", 0, match.start()) + 1, target))
    for match in REF_USE.finditer(text):
        target = definitions.get(match.group(1).casefold())
        if target:
            results.append((text.count("\n", 0, match.start()) + 1, target))
    return results


def local_target(source: Path, target: str, root: Path) -> tuple[Path | None, str]:
    target = target.strip().strip("<>").split(' "', 1)[0]
    if not target or re.match(r"^[a-z][a-z\d+.-]*:", target, re.I) or target.startswith("//"):
        return None, ""
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None, ""
    name = unquote(parsed.path)
    fragment = unquote(parsed.fragment)
    destination = (root / name.lstrip("/")) if name.startswith("/") else (source.parent / name)
    if not name:
        destination = source
    return destination.resolve(), fragment


def check_links(root: Path, files: list[Path] | None = None) -> dict:
    files = files if files is not None else tracked_markdown(root)
    problems = []
    checked = 0
    anchor_cache = {}
    for source in files:
        if not source.exists():
            problems.append({"file": str(source.relative_to(root)), "line": 0, "reason": "Markdown source missing"})
            continue
        for line, target in links(source):
            destination, fragment = local_target(source, target, root)
            if destination is None:
                continue
            checked += 1
            reason = None
            if not destination.exists():
                reason = "target missing"
            elif fragment and destination.is_file() and destination.suffix.lower() == ".md":
                if destination not in anchor_cache:
                    anchor_cache[destination] = anchors(destination.read_text(encoding="utf-8"))
                if fragment not in anchor_cache[destination]:
                    reason = "anchor missing"
            if reason:
                problems.append({"file": str(source.relative_to(root)), "line": line,
                                 "target": target, "reason": reason})
    return {"kind": "markdownLinks", "files": len(files), "localLinks": checked,
            "problemCount": len(problems), "problems": problems}


def route_report(root: Path) -> dict:
    files = tracked_markdown(root)
    nodes = set(files)
    graph = {path: set() for path in files}
    for source in files:
        for _, target in links(source):
            destination, _ = local_target(source, target, root)
            if destination in nodes:
                graph[source].add(destination)
    seeds = [root / "README.md", root / "AGENTS.md"]
    queue = deque(seed for seed in seeds if seed in nodes)
    reached = set(queue)
    while queue:
        for child in graph[queue.popleft()]:
            if child not in reached:
                reached.add(child)
                queue.append(child)
    missing = sorted(str(path.relative_to(root)) for path in nodes - reached)
    readme = (root / "README.md").read_text(encoding="utf-8")
    routes = []
    for line in readme.splitlines():
        if not line.startswith("|") or line.startswith("| ---"):
            continue
        columns = [part.strip() for part in line.strip("|").split("|")]
        if len(columns) != 3 or columns[0] in {"Task", ""}:
            continue
        paths = []
        for match in LINK.finditer(columns[1]):
            target = match.group(1) or match.group(2)
            if target:
                destination, _ = local_target(root / "README.md", target, root)
                if destination and destination.suffix.lower() == ".md" and destination.exists():
                    paths.append(destination)
        if paths:
            unique = list(dict.fromkeys(paths))
            routes.append({"task": columns[0], "files": [str(path.relative_to(root)) for path in unique],
                           "words": sum(len(WORD.findall(path.read_text(encoding="utf-8"))) for path in unique)})
    return {"kind": "documentationRoutes", "markdownFiles": len(files),
            "reachable": len(reached), "unreachable": missing, "routes": routes}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("links", "routes"))
    parser.add_argument("--file", action="append", type=Path, help="Markdown file to check (links only)")
    parser.add_argument("--task", help="Return matching task routes only (routes only)")
    args = parser.parse_args(argv)
    root = project_root()
    if args.command == "links":
        selected = [(root / path).resolve() if not path.is_absolute() else path.resolve()
                    for path in args.file] if args.file else None
        if selected and any(not path.is_relative_to(root) for path in selected):
            parser.error("--file must be inside the project")
        result = check_links(root, selected)
        failure = result["problemCount"] > 0
    else:
        result = route_report(root)
        failure = bool(result["unreachable"])
        if args.task:
            result["routes"] = [route for route in result["routes"]
                                if args.task.casefold() in route["task"].casefold()]
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 1 if failure else 0


if __name__ == "__main__":
    raise SystemExit(main())
