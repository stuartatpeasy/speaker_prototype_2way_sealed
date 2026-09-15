import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src import project_docs, project_checks


class LinkTests(unittest.TestCase):
    def test_encoded_path_anchor_directory_and_code_are_checked(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "doc").mkdir()
            target = root / "doc" / "A file.md"
            target.write_text("## 3.4 Worked Example\n", encoding="utf-8")
            source = root / "README.md"
            source.write_text(
                "[file](doc/A%20file.md#34-worked-example)\n"
                "[directory](doc/)\n"
                "`[ignored](missing.md)`\n"
                "```md\n[ignored](also-missing.md)\n```\n", encoding="utf-8")
            result = project_docs.check_links(root, [source])
            self.assertEqual(result["localLinks"], 2)
            self.assertEqual(result["problemCount"], 0)

    def test_bad_anchor_and_missing_file_report_exact_lines(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "target.md").write_text("# Present\n", encoding="utf-8")
            source = root / "README.md"
            source.write_text("[bad](target.md#absent)\n[missing](none.md)\n", encoding="utf-8")
            problems = project_docs.check_links(root, [source])["problems"]
            self.assertEqual([(item["line"], item["reason"]) for item in problems],
                             [(1, "anchor missing"), (2, "target missing")])

    def test_repeated_headings_receive_distinct_slugs(self):
        found = project_docs.anchors("# Topic\n# Topic\n")
        self.assertEqual(found, {"topic", "topic-1"})


class RouteTests(unittest.TestCase):
    def test_current_project_is_reachable_and_has_task_routes(self):
        report = project_docs.route_report(project_docs.project_root())
        self.assertEqual(report["unreachable"], [])
        self.assertTrue(any(route["task"] == "Documentation review" for route in report["routes"]))

    def test_orphaned_markdown_is_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "doc").mkdir()
            (root / "README.md").write_text("# Start\n[known](doc/known.md)\n", encoding="utf-8")
            (root / "AGENTS.md").write_text("# Policy\n", encoding="utf-8")
            (root / "doc" / "known.md").write_text("# Known\n", encoding="utf-8")
            (root / "doc" / "orphan.md").write_text("# Orphan\n", encoding="utf-8")
            files = [root / "README.md", root / "AGENTS.md",
                     root / "doc" / "known.md", root / "doc" / "orphan.md"]
            with patch.object(project_docs, "tracked_markdown", return_value=files):
                report = project_docs.route_report(root)
            self.assertEqual(report["unreachable"], ["doc/orphan.md"])


class ChangedCheckTests(unittest.TestCase):
    def test_no_python_changes_run_no_test_suite_and_failures_are_bounded(self):
        root = project_docs.project_root()
        with patch.object(project_checks, "changed_files", return_value=["README.md"]), \
             patch.object(project_checks, "command") as command:
            command.return_value.returncode = 0
            command.return_value.stdout = ""
            command.return_value.stderr = ""
            report = project_checks.check(root)
        self.assertTrue(report["passed"])
        self.assertEqual([item["name"] for item in report["checks"]],
                         ["markdownLinks", "documentationRoutes", "diffWhitespace"])


if __name__ == "__main__":
    unittest.main()
