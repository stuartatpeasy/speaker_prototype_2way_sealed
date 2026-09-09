import base64
import io
import json
import math
import struct
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from src import measurement_analysis as analysis
from src import measurement_summary


def encoded(*values):
    return base64.b64encode(struct.pack(f">{len(values)}f", *values)).decode("ascii")


class ParseAndInspectTests(unittest.TestCase):
    def test_parses_rew_zma_and_reports_provenance_without_rows(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "load.zma"
            path.write_text(
                "* Measurement: synthetic\n"
                "* Freq(Hz) Z(Ohms) Phase(degrees)\n"
                "10 8 0\n20 4 -30\n40 6 20\n",
                encoding="utf-8",
            )
            curve = analysis.parse_curve(path)
            summary = analysis.summarize_curve(curve, band=(15, 40))
        self.assertEqual(curve.kind, "impedance")
        self.assertEqual(summary["validation"]["sourceSampleCount"], 3)
        self.assertEqual(summary["validation"]["selectedFiniteSampleCount"], 2)
        self.assertEqual(summary["analysis"]["magnitude"]["minimum"]["value"], 4)
        self.assertEqual(len(summary["source"]["sha256"]), 64)
        self.assertNotIn("rows", json.dumps(summary).lower())

    def test_parses_rew_extracted_frequency_csv(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "frequency-response.csv"
            path.write_text(
                "frequency_hz,magnitude,phase_degrees\n100,70,179\n200,71,-179\n",
                encoding="utf-8",
            )
            curve = analysis.parse_curve(path)
        self.assertEqual(curve.frequencies_hz, (100.0, 200.0))
        self.assertEqual(curve.phases_degrees, (179.0, -179.0))

    def test_inspect_reports_duplicates_nonfinite_and_missing_phase(self):
        curve = analysis.curve_from_rows([(10, 1), (10, float("nan"))])
        summary = analysis.summarize_curve(curve)
        warnings = " ".join(summary["validation"]["warnings"])
        self.assertIn("duplicate", warnings)
        self.assertIn("non-finite", warnings)
        self.assertIn("phase is absent", warnings)

    def test_decodes_rew_payload_without_csv(self):
        curve = analysis.curve_from_rew_payload({
            "startFreq": 100,
            "ppo": 1,
            "unit": "SPL",
            "magnitude": encoded(70, 71, 72),
            "phase": encoded(0, 10, 20),
        })
        self.assertEqual(curve.frequencies_hz, (100.0, 200.0, 400.0))
        self.assertEqual(curve.unit, "SPL")


class PointAndImpedanceTests(unittest.TestCase):
    def test_circular_phase_interpolation_crosses_wrap(self):
        curve = analysis.curve_from_rows([(100, 1, 170), (200, 3, -170)])
        result = analysis.query_points(curve, [150], method="interpolate")
        self.assertAlmostEqual(abs(result["result"][0]["phaseDegrees"]), 180)
        self.assertEqual(result["result"][0]["magnitude"], 2)

    def test_impedance_reports_rectangular_components_and_epdr(self):
        curve = analysis.curve_from_rows(
            [(1000, 5, 0), (1942, 4.905, -25.113), (3000, 6, 30)],
            kind="impedance", unit="ohm",
        )
        result = analysis.summarize_impedance(curve, band=(1000, 3000))["result"]
        self.assertAlmostEqual(result["realOhm"]["minimum"]["value"],
                               4.905 * math.cos(math.radians(25.113)), places=6)
        self.assertAlmostEqual(result["idealClassBEpdrOhm"]["minimum"]["value"],
                               2.563, places=3)
        self.assertEqual(result["magnitudeOhm"]["minimum"]["frequencyHz"], 1942)

    def test_explicit_threshold_resonance_q(self):
        curve = analysis.curve_from_rows(
            [(50, 4, 0), (75, 7, 0), (100, 10, 0), (125, 7, 0), (150, 4, 0)],
            kind="impedance",
        )
        q = analysis.summarize_impedance(
            curve, band=(50, 150), q_band=(50, 150), q_threshold_ohm=7
        )["result"]["singleResonanceQ"]
        self.assertEqual(q["lowerCrossingHz"], 75)
        self.assertEqual(q["upperCrossingHz"], 125)
        self.assertEqual(q["q"], 2)

    def test_missing_q_crossing_is_explicit(self):
        curve = analysis.curve_from_rows([(50, 8, 0), (100, 10, 0), (150, 8, 0)],
                                         kind="impedance")
        result = analysis.summarize_impedance(curve, band=(50, 150), q_band=(50, 150))
        self.assertIsNone(result["result"]["singleResonanceQ"]["q"])
        self.assertIn("both threshold crossings", result["warnings"][-1])


class CurveComparisonTests(unittest.TestCase):
    def test_exact_grid_gain_and_circular_phase(self):
        a = analysis.curve_from_rows([(100, 72, 179), (200, 73, -179), (300, 74, -170)])
        b = analysis.curve_from_rows([(100, 70, -179), (200, 71, 179), (300, 72, -172)])
        result = analysis.compare_curves(a, b, band=(100, 300), grid="exact", fit_gain=True)
        self.assertEqual(result["result"]["magnitude"]["mean"], 2)
        self.assertEqual(result["result"]["gainFit"]["residual"]["rms"], 0)
        self.assertEqual(result["result"]["phaseDegrees"]["maximumAbsolute"]["absolute"], 2)

    def test_exact_grid_rejects_mismatch(self):
        a = analysis.curve_from_rows([(100, 1, 0), (200, 2, 0)])
        b = analysis.curve_from_rows([(100, 1, 0), (250, 2, 0)])
        with self.assertRaisesRegex(ValueError, "identical"):
            analysis.compare_curves(a, b, band=(100, 300), grid="exact")

    def test_explicit_interpolation_uses_a_grid(self):
        a = analysis.curve_from_rows([(100, 2, 0), (200, 4, 0), (300, 6, 0)])
        b = analysis.curve_from_rows([(100, 1, 0), (300, 3, 0)])
        result = analysis.compare_curves(a, b, band=(100, 300), grid="interpolate")
        self.assertEqual(result["result"]["sampleCount"], 3)
        self.assertEqual(result["result"]["magnitude"]["mean"], 2)

    def test_delay_fit_recovers_correction_sign(self):
        # A-B slopes down 0.0036 degree/Hz, so +10 us removes the slope.
        a = analysis.curve_from_rows([(1000, 0, -3.6), (2000, 0, -7.2), (3000, 0, -10.8)])
        b = analysis.curve_from_rows([(1000, 0, 0), (2000, 0, 0), (3000, 0, 0)])
        fit = analysis.compare_curves(a, b, band=(1000, 3000), grid="exact",
                                      fit_delay=True)["result"]["delayFit"]
        self.assertAlmostEqual(fit["microsecondsToAddInCorrection"], 10)
        self.assertAlmostEqual(fit["correctedPhaseDegrees"]["rms"], 0, places=10)

    def test_polar_reports_signed_excess_and_selected_frequency(self):
        reference = analysis.curve_from_rows([(100, 10, 0), (200, 10, 0), (300, 10, 0)])
        off_axis = analysis.curve_from_rows([(100, 9, 0), (200, 11, 0), (300, 8, 0)])
        result = analysis.compare_polar(reference, {"20deg": off_axis}, band=(100, 300),
                                        grid="exact", frequencies=(200,))["result"]["20deg"]
        self.assertEqual(result["maximumOffAxisExcess"], {"value": 1.0, "frequencyHz": 200.0})
        self.assertEqual(result["selectedFrequencies"][0]["offAxisMinusReference"], 1)


class ImpulseTests(unittest.TestCase):
    def test_rew_json_payload_and_gain_comparison(self):
        a = analysis.impulse_from_rew_payload({
            "startTime": 0, "sampleInterval": 0.001, "data": [0, 1, 2, 1, 0]
        })
        b = analysis.impulse_from_rew_payload({
            "startTime": 0, "sampleInterval": 0.001, "data": [0, 0.5, 1, 0.5, 0]
        })
        result = analysis.compare_impulses(a, b, window=(0, 0.004), sample_rate_hz=1000,
                                           grid="exact", fit_gain=True)
        self.assertEqual(result["result"]["gainToMultiplyB"], 2)
        self.assertEqual(result["result"]["residualRms"], 0)
        self.assertAlmostEqual(result["result"]["correlation"], 1)

    def test_impulse_csv_validates_explicit_sample_rate(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "ir.csv"
            path.write_text("time_s,amplitude\n0,0\n0.001,1\n0.002,0\n", encoding="utf-8")
            impulse = analysis.parse_impulse(path, sample_rate_hz=1000)
            self.assertEqual(impulse.sample_rate_hz, 1000)
            with self.assertRaisesRegex(ValueError, "not requested"):
                analysis.parse_impulse(path, sample_rate_hz=48000)

    def test_delay_fit_is_bounded_by_requested_lag(self):
        a = analysis.impulse_from_rows([(i / 1000, value) for i, value in enumerate([0, 1, 0, 0, 0])])
        b = analysis.impulse_from_rows([(i / 1000, value) for i, value in enumerate([0, 0, 1, 0, 0])])
        result = analysis.compare_impulses(a, b, window=(0, 0.004), grid="exact",
                                           max_lag_s=0.002)
        self.assertEqual(result["result"]["delayFit"]["lagSamplesOfBRelativeToA"], 1)
        self.assertEqual(result["result"]["delayFit"]["lagSecondsOfBRelativeToA"], 0.001)


class CliTests(unittest.TestCase):
    def test_cli_outputs_json_and_errors_are_concise(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "x.frd"
            path.write_text("100 1 0\n200 2 10\n", encoding="utf-8")
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                code = measurement_summary.main(["points", str(path), "-f", "150", "--method", "interpolate"])
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(stdout.getvalue())["operation"], "points")
            stderr = io.StringIO()
            with redirect_stderr(stderr):
                code = measurement_summary.main(["inspect", str(path), "--band", "200", "100"])
            self.assertEqual(code, 2)
            self.assertIn("ordered low < high", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
