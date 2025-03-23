import os
import shutil
import tarfile
import logging
from datetime import datetime, timedelta

# Configuration
BASE_DIR = "/home/TAMADHIR/Downloads"  # Base directory to organize
ARCHIVE_DIR = os.path.join(BASE_DIR, "archives")  # Directory to store archives
LOG_FILE = os.path.expanduser("~/auto_clearup/activity.log")  # Log file path
FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt", ".csv"],
    "scripts": [".py", ".sh", ".js"],
    "videos": [".mp4", ".mkv", ".avi"],
}
DAYS_TO_ARCHIVE = 7  # Files older than this will be archived
DAYS_TO_DELETE_ARCHIVE = 30  # Archives older than this will be deleted

# Ensure required directories exist
os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(ARCHIVE_DIR, exist_ok=True)
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Set up logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def organize_files_by_extension():
    """Organize files into directories based on their extensions."""
    files_moved = 0
    for category, extensions in FILE_CATEGORIES.items():
        category_dir = os.path.join(BASE_DIR, category)
        os.makedirs(category_dir, exist_ok=True)

    uncategorized_dir = os.path.join(BASE_DIR, "others")
    os.makedirs(uncategorized_dir, exist_ok=True)

    for filename in os.listdir(BASE_DIR):
        file_path = os.path.join(BASE_DIR, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            target_dir = next((key for key, exts in FILE_CATEGORIES.items() if file_ext in exts), "others")
            target_path = os.path.join(BASE_DIR, target_dir)
            shutil.move(file_path, os.path.join(target_path, filename))
            files_moved += 1

    logging.info(f"Files organized: {files_moved} moved.")
    return files_moved

    

def archive_old_files():
    """Archive files older than DAYS_TO_ARCHIVE days."""
    cutoff_date = datetime.now() - timedelta(days=DAYS_TO_ARCHIVE)
    archive_name = os.path.join(ARCHIVE_DIR, f"archived_{datetime.now().strftime('%Y%m%d')}.tar.gz")
    archived_files = 0

    with tarfile.open(archive_name, "w:gz") as archive:
        for root, _, files in os.walk(BASE_DIR):
            if root.startswith(ARCHIVE_DIR):
                continue
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.exists(file_path) and os.path.getmtime(file_path) < cutoff_date.timestamp():
                    archive.add(file_path, arcname=os.path.relpath(file_path, BASE_DIR))
                    os.remove(file_path)
                    archived_files += 1

    logging.info(f"Files archived: {archived_files} into {archive_name}.")
    return archived_files

def delete_old_archives():
    """Delete archives older than DAYS_TO_DELETE_ARCHIVE days."""
    cutoff_date = datetime.now() - timedelta(days=DAYS_TO_DELETE_ARCHIVE)
    deleted_archives = 0

    for filename in os.listdir(ARCHIVE_DIR):
        file_path = os.path.join(ARCHIVE_DIR, filename)
        if os.path.getmtime(file_path) < cutoff_date.timestamp():
            os.remove(file_path)
            deleted_archives += 1

    logging.info(f"Old archives deleted: {deleted_archives}.")
    return deleted_archives
    
   
if __name__ == "__main__":
    files_moved = organize_files_by_extension()
    archived_files = archive_old_files()
    deleted_archives = delete_old_archives()
    print(f"[Summary] Files organized: {files_moved}, archived: {archived_files}, deleted: {deleted_archives}.")