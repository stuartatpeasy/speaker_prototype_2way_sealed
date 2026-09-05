import base64
import io
import json
import struct
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock
from urllib import error

from src import rew_api_extract as rew


def encoded(*values):
    return base64.b64encode(struct.pack(f">{len(values)}f", *values)).decode("ascii")


class FloatAndAxisTests(unittest.TestCase):
    def test_decodes_big_endian_float32(self):
        self.assertEqual(rew.decode_float32_be(encoded(0.125, 0.25, 0.375, 0.5)),
                         [0.125, 0.25, 0.375, 0.5])

    def test_rejects_malformed_or_misaligned_base64(self):
        with self.assertRaisesRegex(rew.RewApiError, "valid Base64"):
            rew.decode_float32_be("not base64!")
        with self.assertRaisesRegex(rew.RewApiError, "multiple of 4"):
            rew.decode_float32_be(base64.b64encode(b"abc").decode("ascii"))

    def test_builds_logarithmic_frequency_axis(self):
        self.assertEqual(rew.frequency_axis({"startFreq": 10, "ppo": 1}, 4),
                         [10.0, 20.0, 40.0, 80.0])

    def test_builds_linear_frequency_axis(self):
        self.assertEqual(rew.frequency_axis({"startFreq": 0, "freqStep": 2.5}, 3),
                         [0.0, 2.5, 5.0])

    def test_frequency_response_length_mismatch_is_rejected(self):
        with self.assertRaisesRegex(rew.RewApiError, "Phase array"):
            rew.frequency_rows({
                "startFreq": 20,
                "ppo": 12,
                "magnitude": encoded(1, 2),
                "phase": encoded(3),
            })


class SelectionAndPathTests(unittest.TestCase):
    def test_translates_wsl_windows_path(self):
        source = Path("/mnt/c/Users/example/measurement.mdat")
        self.assertEqual(rew.path_for_rew(source), "C:/Users/example/measurement.mdat")

    def test_selects_only_new_measurement_ids_by_default(self):
        before = {"1": {}}
        after = {"1": {}, "3": {}, "2": {}}
        self.assertEqual(rew.select_measurements(before, after, None), ["2", "3"])

    def test_selects_measurement_by_uuid(self):
        after = {"4": {"uuid": "abc"}, "5": {"uuid": "def"}}
        self.assertEqual(rew.select_measurements({}, after, ["def"]), ["5"])

    def test_uuid_selection_ignores_an_older_copy(self):
        before = {"4": {"uuid": "same"}}
        after = {"4": {"uuid": "same"}, "5": {"uuid": "same"}}
        self.assertEqual(rew.select_measurements(before, after, ["same"]), ["5"])

    def test_waits_for_quiet_period_after_last_new_measurement(self):
        class LoadingApi:
            responses = [
                {"1": {}, "2": {}},
                {"1": {}, "2": {}},
                {"1": {}, "2": {}, "3": {}},
                {"1": {}, "2": {}, "3": {}},
                {"1": {}, "2": {}, "3": {}},
                {"1": {}, "2": {}, "3": {}},
            ]

            def measurements(self):
                return self.responses.pop(0)

        clock = [0.0]

        def advance(seconds):
            clock[0] += seconds

        with mock.patch.object(rew.time, "monotonic", side_effect=lambda: clock[0]), \
                mock.patch.object(rew.time, "sleep", side_effect=advance):
            loaded = rew.wait_for_loaded_measurements(
                LoadingApi(), {"1": {}}, timeout=5, poll_interval=0.2, settle_time=0.5
            )
        self.assertEqual(set(loaded), {"1", "2", "3"})

    def test_slug_is_stable_and_bounded(self):
        self.assertEqual(rew.safe_slug("Woofer / left @ 0 deg"), "woofer-left-0-deg")
        self.assertLessEqual(len(rew.safe_slug("x" * 200)), 80)


class OutputTests(unittest.TestCase):
    def test_nonempty_output_requires_overwrite(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            (directory / "existing.txt").write_text("keep", encoding="utf-8")
            with self.assertRaisesRegex(rew.RewApiError, "--overwrite"):
                rew.prepare_output_dir(directory, overwrite=False)
            rew.prepare_output_dir(directory, overwrite=True)
            self.assertEqual((directory / "existing.txt").read_text(encoding="utf-8"), "keep")

    def test_csv_has_one_row_per_response_sample(self):
        payload = {
            "startFreq": 10,
            "ppo": 1,
            "magnitude": encoded(70, 71, 72),
            "phase": encoded(0, -10, -20),
        }
        rows, metadata = rew.frequency_rows(payload)
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "frequency.csv"
            rew.write_csv(path, ("frequency_hz", "magnitude", "phase_degrees"), rows)
            self.assertEqual(len(path.read_text(encoding="utf-8").splitlines()), 4)
        self.assertEqual(metadata["sampleCount"], 3)

    def test_end_to_end_extract_with_fake_rew(self):
        class FakeApi:
            base_url = rew.DEFAULT_API
            frequency_query = None

            def __init__(self, *_args, **_kwargs):
                self.measurement_calls = 0

            def get(self, path, *, query=None):
                if path.endswith("/frequency-response"):
                    type(self).frequency_query = query
                    return {
                        "unit": query.get("unit", "SPL") if query else "SPL",
                        "smoothing": query.get("smoothing", "None") if query else "None",
                        "startFreq": 20,
                        "ppo": query.get("ppo", 1) if query else 1,
                        "magnitude": encoded(70, 71),
                        "phase": encoded(0, -10),
                    }
                if path.endswith("/ir-windows"):
                    return {"leftWindowType": "Tukey", "leftWindowWidthms": 125}
                if path.endswith("/impulse-response"):
                    self.assert_ir_query = query
                    return {
                        "unit": "Percent",
                        "startTime": -0.001,
                        "sampleInterval": 0.0005,
                        "data": encoded(0.25, 0.5),
                    }
                raise AssertionError(path)

            def measurements(self):
                self.measurement_calls += 1
                if self.measurement_calls == 1:
                    return {}
                return {"1": {
                    "title": "Test response",
                    "uuid": "uuid-1",
                    "sampleRate": 48000,
                    "rewVersion": "5.40 beta 133",
                }}

            def load(self, path):
                self.loaded_path = path
                return {"message": "loaded"}

        with tempfile.TemporaryDirectory() as temporary:
            temporary_path = Path(temporary)
            source = temporary_path / "source.mdat"
            source.write_bytes(b"test mdat")
            output = temporary_path / "extract"
            with mock.patch.object(rew, "RewApi", FakeApi), \
                    mock.patch.object(rew, "path_for_rew", return_value="C:/source.mdat"), \
                    mock.patch.object(rew.time, "sleep"):
                with redirect_stdout(io.StringIO()):
                    result = rew.main([
                        "extract", str(source), "--output-dir", str(output), "--include-ir",
                        "--settle-time", "0", "--frequency-unit", "ohm",
                        "--smoothing", "None", "--ppo", "1",
                    ])
            self.assertEqual(result, 0)
            manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["api"]["measurementRewVersions"], ["5.40 beta 133"])
            self.assertEqual(manifest["measurements"][0]["summary"]["uuid"], "uuid-1")
            self.assertEqual(
                manifest["measurements"][0]["requests"]["frequencyResponse"],
                {"unit": "ohm", "smoothing": "None", "ppo": 1},
            )
            self.assertEqual(FakeApi.frequency_query,
                             {"unit": "ohm", "smoothing": "None", "ppo": 1})
            measurement_dir = output / manifest["measurements"][0]["directory"]
            self.assertEqual(
                len((measurement_dir / "frequency-response.csv").read_text(encoding="utf-8").splitlines()),
                3,
            )
            self.assertEqual(
                len((measurement_dir / "impulse-response.csv").read_text(encoding="utf-8").splitlines()),
                3,
            )

    def test_omitted_frequency_settings_preserve_api_defaults(self):
        self.assertEqual(
            rew.validate_frequency_response_settings({}, {"unit": "SPL"}), []
        )

    def test_frequency_unit_and_ppo_mismatch_are_fatal(self):
        with self.assertRaisesRegex(rew.RewApiError, "not requested unit"):
            rew.validate_frequency_response_settings({"unit": "ohm"}, {"unit": "SPL"})
        with self.assertRaisesRegex(rew.RewApiError, "points-per-octave"):
            rew.validate_frequency_response_settings({"ppo": 96}, {"ppo": 48})

    def test_smoothing_mismatch_is_a_warning(self):
        warnings = rew.validate_frequency_response_settings(
            {"smoothing": "None"}, {"smoothing": "1/48"}
        )
        self.assertEqual(len(warnings), 1)
        self.assertIn("anti-alias smoothing", warnings[0])

    def test_nonpositive_ppo_is_rejected(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            rew.main(["extract", "unused.mdat", "--ppo", "0"])


class SnapshotTests(unittest.TestCase):
    def test_snapshot_is_get_only_partial_and_redacts_paths(self):
        class FakeApi:
            base_url = rew.DEFAULT_API

            def __init__(self):
                self.paths = []

            def measurements(self):
                return {"1": {
                    "title": "loaded",
                    "uuid": "u1",
                    "notes": r"from \\server\share\private\capture.wav",
                }}

            def get(self, path, *, query=None):
                self.paths.append(path)
                if path == "/audio/driver":
                    return "Java"
                if path == "/measure/timing/reference":
                    return "Acoustic"
                if path == "/audio/input-cal":
                    return {"calDataAllInputs": {"calFilePath": r"C:\\Users\\me\\mic.cal"}}
                if path == "/application/last-error":
                    return {"details": r"failed at C:\\Users\\me\\secret.txt"}
                if path == "/generator/signal/configuration":
                    raise rew.RewApiError("not available", status=404)
                return {"value": "ok"}

            def post(self, *_args, **_kwargs):
                raise AssertionError("snapshot must not POST")

        api = FakeApi()
        snapshot = rew.build_snapshot(api)
        self.assertFalse(snapshot["complete"])
        self.assertIn("/generator/signal/configuration", snapshot["failedEndpoints"])
        self.assertIn("/audio/java/input", api.paths)
        self.assertNotIn("/audio/asio/input", api.paths)
        self.assertIn("/measure/timing/reference/acoustic/trim", api.paths)
        input_cal = snapshot["state"]["audio"]["inputCalibration"]["value"]
        self.assertEqual(input_cal["calDataAllInputs"]["calFilePath"], "mic.cal")
        error_details = snapshot["state"]["application"]["lastError"]["value"]["details"]
        self.assertNotIn("Users", error_details)
        self.assertEqual(snapshot["measurements"]["1"]["notes"], "from <absolute-path>")

    def test_driver_kind_selects_asio_case_insensitively(self):
        self.assertEqual(rew._driver_kind({"value": "ASIO"}), "asio")
        self.assertEqual(rew._driver_kind("java"), "java")

    def test_snapshot_output_requires_overwrite(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "snapshot.json"
            output.write_text("keep", encoding="utf-8")
            args = mock.Mock(api=rew.DEFAULT_API, timeout=1, output=output, overwrite=False)
            with mock.patch.object(rew, "RewApi"):
                with self.assertRaisesRegex(rew.RewApiError, "--overwrite"):
                    rew.run_snapshot(args)


class HttpTests(unittest.TestCase):
    def test_status_accepts_json_api_response(self):
        responses = [
            mock.MagicMock(__enter__=lambda value: value,
                           __exit__=mock.Mock(return_value=False),
                           read=mock.Mock(return_value=(
                               b'{"1":{"title":"test","uuid":"u1",'
                               b'"rewVersion":"5.40 beta 133"}}'
                           ))),
        ]
        output = io.StringIO()
        with mock.patch("urllib.request.urlopen", side_effect=responses):
            with redirect_stdout(output):
                result = rew.main(["status"])
        self.assertEqual(result, 0)
        status = json.loads(output.getvalue())
        self.assertTrue(status["reachable"])
        self.assertEqual(status["measurementCount"], 1)
        self.assertEqual(status["measurementRewVersions"], ["5.40 beta 133"])

    def test_http_error_is_reported_without_traceback(self):
        http_error = error.HTTPError(
            "http://127.0.0.1:4735/measurements", 500, "failure", {}, io.BytesIO(b"bad")
        )
        stderr = io.StringIO()
        with mock.patch("urllib.request.urlopen", side_effect=http_error):
            with redirect_stderr(stderr):
                result = rew.main(["status"])
        self.assertEqual(result, 2)
        self.assertIn("HTTP 500", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())

    def test_connection_failure_has_startup_hint(self):
        stderr = io.StringIO()
        with mock.patch("urllib.request.urlopen", side_effect=error.URLError("refused")):
            with redirect_stderr(stderr):
                result = rew.main(["status"])
        self.assertEqual(result, 2)
        self.assertIn("start REW V5.40", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
