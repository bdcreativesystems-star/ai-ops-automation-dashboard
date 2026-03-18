import os
import tempfile
import unittest

from app import app


class DashboardDemoSmokeTest(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_dashboard_homepage_loads(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Operations Dashboard", response.data)

    def test_system_report_flow(self):
        response = self.client.post("/", data={"action": "report"})

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"System report generated successfully.", response.data)
        self.assertIn(b"Latest System Report", response.data)
        self.assertIn(b"&#34;python_version&#34;", response.data)
        self.assertIn(b"&#34;generated_at&#34;", response.data)

    def test_file_organizer_flow(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = os.path.join(temp_dir, "notes.txt")
            image_path = os.path.join(temp_dir, "photo.png")

            with open(report_path, "w", encoding="utf-8") as handle:
                handle.write("demo text")

            with open(image_path, "w", encoding="utf-8") as handle:
                handle.write("image bytes placeholder")

            response = self.client.post(
                "/",
                data={"action": "organize", "folder": temp_dir},
            )

            self.assertEqual(response.status_code, 200)
            self.assertIn(b"File organizer completed successfully", response.data)
            self.assertTrue(os.path.exists(os.path.join(temp_dir, "txt", "notes.txt")))
            self.assertTrue(os.path.exists(os.path.join(temp_dir, "png", "photo.png")))
            self.assertIn(b"&#34;moved_count&#34;: 2", response.data)

    def test_file_organizer_reports_when_nothing_needs_moving(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            os.makedirs(os.path.join(temp_dir, "txt"), exist_ok=True)

            with open(
                os.path.join(temp_dir, "txt", "notes.txt"),
                "w",
                encoding="utf-8",
            ) as handle:
                handle.write("already sorted")

            response = self.client.post(
                "/",
                data={"action": "organize", "folder": temp_dir},
            )

            self.assertEqual(response.status_code, 200)
            self.assertIn(b"No loose files were found to organize", response.data)
            self.assertIn(b"&#34;moved_count&#34;: 0", response.data)
            self.assertIn(b"All files are already organized.", response.data)

    def test_file_organizer_validation_message(self):
        response = self.client.post("/", data={"action": "organize", "folder": ""})

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Please enter a folder path before running the organizer.",
            response.data,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
