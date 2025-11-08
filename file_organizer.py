# file_organizer.py
import os, shutil, logging
from pathlib import Path

def organize_files(folder_path):
    logging.info("Organizing files...")
    for file in Path(folder_path).iterdir():
        if file.is_file():
            ext = file.suffix[1:] or "others"
            dest_dir = Path(folder_path) / ext
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(file), str(dest_dir / file.name))
    logging.info("File organization complete.")