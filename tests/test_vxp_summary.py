import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from src import vxp_summary as vxp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
VXP_DIR = PROJECT_ROOT / "vituixcad"
BASELINE = VXP_DIR / "Prototype loudspeaker measured baseline verified 2026-09-07.vxp"
NOMINAL = VXP_DIR / "Prototype loudspeaker crossover Seed A sparse polar verified 2026-09-07.vxp"
PRACTICAL = VXP_DIR / "Prototype loudspeaker crossover Seed A practical measured 2026-09-08.vxp"


def synthetic_vxp(*, component_value="1.4", layout_x="10", impedance="rew/test.zma"):
    return f'''<?xml version="1.0" encoding="utf-8"?>
<SPEAKER>
  <Description>Synthetic</Description>
  <ReferenceAngle>0</ReferenceAngle>
  <IncludeHor>True</IncludeHor>
  <DRIVER di="0">
    <Model>Test Driver</Model><SPL>80</SPL><Z>8</Z><ExtendedData>False</ExtendedData>
    <ResponseDirectory>rew/frd/Test Driver</ResponseDirectory>
    <ResponseScale>2</ResponseScale><ResponseDelay>0.125</ResponseDelay>
    <ResponseInvert>False</ResponseInvert><ResponseMute>False</ResponseMute>
    <MinimumPhase>False</MinimumPhase><ResponseSmooth>None</ResponseSmooth>
    <ImpedanceFile>{impedance}</ImpedanceFile><ImpedanceScale>1</ImpedanceScale>
    <RESPONSE ri="0"><FileName>000.frd</FileName><Hor>0</Hor><Ver>0</Ver></RESPONSE>
  </DRIVER>
  <CROSSOVER><DSP>Analog</DSP><SampleRate>96000</SampleRate>
    <PART xi="0"><Type>Resistor</Type><CenX>{layout_x}</CenX><PartID>R1</PartID>
      <PARAM pi="0"><Name>R</Name><Value>{component_value}</Value><Unit>ohm</Unit><Optimize>False</Optimize><Min>0.1</Min><Max>10</Max></PARAM>
      <PARAM pi="1"><Name>Pow</Name><Value>5</Value><Unit>W</Unit><Optimize>False</Optimize></PARAM>
    </PART>
  </CROSSOVER>
</SPEAKER>'''


class RealProjectTests(unittest.TestCase):
    def test_practical_project_summary(self):
        summary = vxp.parse_vxp(PRACTICAL)
        self.assertEqual(summary["kind"], "vituixcadProjectSummary")
        self.assertEqual(summary["counts"]["drivers"], 2)
        self.assertEqual(summary["counts"]["electricalComponents"], 8)
        self.assertEqual(summary["sourceAudit"]["missingCount"], 0)

        woofer, tweeter = summary["drivers"]
        self.assertEqual(woofer["model"], "SB17NRX2C35-8")
        self.assertEqual(len(woofer["responses"]), 4)
        self.assertTrue(woofer["impedanceFile"]["exists"])
        self.assertEqual(
            woofer["impedanceFile"]["projectRelative"],
            "rew/SB17NRX2C35-8 installed.zma",
        )
        self.assertAlmostEqual(tweeter["responseScaleDb"], 11.14, places=3)
        self.assertEqual(
            [response["horizontalDegrees"] for response in tweeter["responses"]],
            [0, 20, 40, 60],
        )

        components = {component["id"]: component for component in summary["components"]}
        l1_parameters = {item["name"]: item for item in components["L1"]["parameters"]}
        self.assertEqual(l1_parameters["L"]["value"], 0.724)
        self.assertEqual(l1_parameters["DCR"]["value"], 0.292)
        self.assertEqual(l1_parameters["Wire"]["value"], 1.8)

    def test_all_retained_projects_parse_and_sources_exist(self):
        for path in (BASELINE, NOMINAL, PRACTICAL):
            with self.subTest(path=path.name):
                summary = vxp.parse_vxp(path)
                self.assertEqual(summary["counts"]["drivers"], 2)
                self.assertEqual(summary["sourceAudit"]["missingCount"], 0)
        self.assertEqual(vxp.parse_vxp(BASELINE)["counts"]["electricalComponents"], 0)

    def test_nominal_to_practical_diff_is_semantic_and_bounded(self):
        left = vxp.parse_vxp(NOMINAL)
        right = vxp.parse_vxp(PRACTICAL)
        diff = vxp.semantic_diff(left, right, max_differences=3)
        self.assertFalse(diff["equal"])
        self.assertGreater(diff["differenceCount"], 3)
        self.assertEqual(diff["reportedDifferenceCount"], 3)
        self.assertTrue(diff["differencesTruncated"])
        paths = [item["path"] for item in diff["differences"]]
        self.assertTrue(any(path.startswith("components.") for path in paths))


class SyntheticTests(unittest.TestCase):
    def make_project(self, directory: Path, xml: str) -> Path:
        (directory / "README.md").write_text("test", encoding="utf-8")
        (directory / "vituixcad").mkdir()
        (directory / "rew" / "frd" / "Test Driver").mkdir(parents=True)
        (directory / "rew" / "test.zma").write_text("data", encoding="utf-8")
        (directory / "rew" / "frd" / "Test Driver" / "000.frd").write_text(
            "data", encoding="utf-8"
        )
        path = directory / "vituixcad" / "test.vxp"
        path.write_bytes(b"\xef\xbb\xbf" + xml.encode("utf-8"))
        return path

    def test_bom_and_project_relative_paths(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.make_project(root, synthetic_vxp())
            summary = vxp.parse_vxp(path)
            driver = summary["drivers"][0]
            self.assertEqual(driver["responseScale"], 2)
            self.assertAlmostEqual(driver["responseScaleDb"], 6.020599913, places=8)
            self.assertEqual(summary["sourceAudit"]["missingCount"], 0)
            self.assertEqual(driver["responses"][0]["source"]["projectRelative"],
                             "rew/frd/Test Driver/000.frd")

    def test_windows_path_maps_from_checkout_name(self):
        with tempfile.TemporaryDirectory(prefix="Speaker prototype-") as temporary:
            root = Path(temporary) / "Speaker prototype"
            root.mkdir()
            windows_path = r"C:\Users\elsewhere\Speaker prototype\rew\test.zma"
            path = self.make_project(root, synthetic_vxp(impedance=windows_path))
            summary = vxp.parse_vxp(path)
            record = summary["drivers"][0]["impedanceFile"]
            self.assertTrue(record["exists"])
            self.assertEqual(record["projectRelative"], "rew/test.zma")

    def test_layout_only_changes_do_not_affect_semantic_diff(self):
        with tempfile.TemporaryDirectory() as left_temp, tempfile.TemporaryDirectory() as right_temp:
            left = vxp.parse_vxp(self.make_project(Path(left_temp), synthetic_vxp(layout_x="10")))
            right = vxp.parse_vxp(self.make_project(Path(right_temp), synthetic_vxp(layout_x="99")))
            diff = vxp.semantic_diff(left, right, max_differences=10)
            self.assertTrue(diff["equal"])
            self.assertEqual(diff["differenceCount"], 0)

    def test_component_value_change_is_reported(self):
        with tempfile.TemporaryDirectory() as left_temp, tempfile.TemporaryDirectory() as right_temp:
            left = vxp.parse_vxp(self.make_project(Path(left_temp), synthetic_vxp(component_value="1.4")))
            right = vxp.parse_vxp(self.make_project(Path(right_temp), synthetic_vxp(component_value="1.401")))
            diff = vxp.semantic_diff(left, right, max_differences=10)
            self.assertEqual(diff["differenceCount"], 1)
            self.assertEqual(diff["differences"][0]["path"], "components.R1.parameters.R.value")

    def test_missing_source_and_malformed_xml_are_safe_errors(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = self.make_project(root, synthetic_vxp(impedance="rew/missing.zma"))
            summary = vxp.parse_vxp(path)
            self.assertEqual(summary["sourceAudit"]["missingCount"], 1)

            malformed = root / "vituixcad" / "bad.vxp"
            malformed.write_text("<SPEAKER>", encoding="utf-8")
            with self.assertRaises(vxp.VxpError):
                vxp.parse_vxp(malformed)

    def test_cli_writes_one_line_json_and_structured_error(self):
        output = io.StringIO()
        with redirect_stdout(output):
            result = vxp.main(["summary", str(BASELINE)])
        self.assertEqual(result, 0)
        self.assertEqual(len(output.getvalue().splitlines()), 1)
        self.assertEqual(json.loads(output.getvalue())["kind"], "vituixcadProjectSummary")

        error_output = io.StringIO()
        with redirect_stderr(error_output):
            result = vxp.main(["summary", str(VXP_DIR / "missing.vxp")])
        self.assertEqual(result, 2)
        self.assertIn("error", json.loads(error_output.getvalue()))


if __name__ == "__main__":
    unittest.main()
