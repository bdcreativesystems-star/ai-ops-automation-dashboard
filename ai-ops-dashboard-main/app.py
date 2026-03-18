from flask import Flask, render_template, request
from automations.file_organizer import organize_files
from automations.system_report import generate_report
import os
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def dashboard():
    message = ""
    message_type = ""
    report_content = ""
    organizer_result = ""
    folder_value = ""

    if request.method == "POST":
        action = request.form.get("action", "").strip()

        if action == "organize":
            folder = request.form.get("folder", "").strip()
            folder_value = folder

            if not folder:
                message = "Please enter a folder path before running the organizer."
                message_type = "error"
            else:
                try:
                    moved_files = organize_files(folder)
                    if moved_files:
                        message = f"File organizer completed successfully for: {folder}"
                        message_type = "success"
                        organizer_result = json.dumps(
                            {
                                "folder": folder,
                                "moved_count": len(moved_files),
                                "moved_files": moved_files,
                            },
                            indent=2,
                        )
                    else:
                        message = f"No loose files were found to organize in: {folder}"
                        message_type = "success"
                        organizer_result = json.dumps(
                            {
                                "folder": folder,
                                "moved_count": 0,
                                "message": "All files are already organized.",
                            },
                            indent=2,
                        )
                except (FileNotFoundError, ValueError) as exc:
                    message = str(exc)
                    message_type = "error"
                except Exception as exc:
                    message = f"File organizer failed: {exc}"
                    message_type = "error"

        elif action == "report":
            try:
                report = generate_report()
                if isinstance(report, dict):
                    report_content = json.dumps(report, indent=2)
                else:
                    report_content = str(report)

                message = "System report generated successfully."
                message_type = "success"
            except Exception as exc:
                message = f"System report failed: {exc}"
                message_type = "error"

    return render_template(
        "dashboard.html",
        message=message,
        message_type=message_type,
        report_content=report_content,
        organizer_result=organizer_result,
        folder_value=folder_value
    )


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
