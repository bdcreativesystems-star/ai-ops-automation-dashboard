import os
import shutil
from utils.logger import log


def organize_files(folder):
    if not folder:
        raise ValueError("No folder path was provided.")

    if not os.path.exists(folder):
        raise FileNotFoundError(f"Folder not found: {folder}")

    moved_files = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if not os.path.isfile(path):
            continue

        ext = file.split(".")[-1].lower() if "." in file else "no_extension"
        dest = os.path.join(folder, ext)

        os.makedirs(dest, exist_ok=True)

        destination_path = os.path.join(dest, file)
        shutil.move(path, destination_path)

        log(f"Moved {file} to {ext}/")
        moved_files.append({
            "file": file,
            "moved_to": dest
        })

    return moved_files