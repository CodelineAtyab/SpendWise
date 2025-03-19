import os #module provides a way of using operating system dependent functionality
import shutil #module provides functions to copy, move, and delete files and directories
import tarfile #module makes it possible to read and write tar archives, including those using gzip, bz2 and lzma compression
import logging #module defines functions and classes which implement a flexible event logging system for applications and libraries
from datetime import datetime, timedelta #module supplies classes for manipulating dates and times

# Configuration
BASE_DIR = r"C:/home/user/downloads"
ARCHIVE_DIR = os.path.join(BASE_DIR, "archives")
LOG_FILE = "activity.log"
DAYS_TO_ARCHIVE = 7
DAYS_TO_DELETE_ARCHIVE = 30

# File type categories
FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt", ".csv"],
    "scripts": [".py", ".sh", ".js"],
}

# Set up logging
log_dir = os.path.dirname(LOG_FILE)
if log_dir and not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def organize_files():
    """Sort files into subdirectories based on extensions."""
    if not os.path.exists(BASE_DIR):
        logging.error(f"Directory does not exist: {BASE_DIR}")
        return "Directory does not exist", 400
    
    try:
        files_moved = 0
        for filename in os.listdir(BASE_DIR):
            file_path = os.path.join(BASE_DIR, filename)
            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1].lower()
                target_dir = next((key for key, exts in FILE_CATEGORIES.items() if file_ext in exts), "others")
                target_path = os.path.join(BASE_DIR, target_dir)
                os.makedirs(target_path, exist_ok=True)
                shutil.move(file_path, os.path.join(target_path, filename))
                files_moved += 1
        logging.info(f"{files_moved} files organized.")
        return f"{files_moved} files organized.", 200
    except Exception as e:
        logging.error(f"Error in organize_files: {e}")
        return f"Error: {e}", 500

def archive_old_files():
    """Compress files older than DAYS_TO_ARCHIVE days."""
    if not os.path.exists(BASE_DIR):
        return "Base directory does not exist", 400

    try:
        cutoff_date = datetime.now() - timedelta(days=DAYS_TO_ARCHIVE)
        os.makedirs(ARCHIVE_DIR, exist_ok=True)
        
        archive_name = os.path.join(ARCHIVE_DIR, f"archived_{datetime.now().strftime('%Y%m%d')}.tar.gz")
        with tarfile.open(archive_name, "w:gz") as archive:
            archived_files = 0
            for root, _, files in os.walk(BASE_DIR):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.getmtime(file_path) < cutoff_date.timestamp():
                        archive.add(file_path, arcname=os.path.relpath(file_path, BASE_DIR))
                        os.remove(file_path)
                        archived_files += 1
        
        if archived_files > 0:
            logging.info(f"Archived {archived_files} files into {archive_name}.")
            return f"Archived {archived_files} files into {archive_name}.", 200
        else:
            os.remove(archive_name)
            return "No files to archive.", 200
    except Exception as e:
        logging.error(f"Error in archive_old_files: {e}")
        return f"Error: {e}", 500

def delete_old_archives():
    """Delete archives older than DAYS_TO_DELETE_ARCHIVE days."""
    if not os.path.exists(ARCHIVE_DIR):
        return "Archive directory does not exist", 400

    try:
        cutoff_date = datetime.now() - timedelta(days=DAYS_TO_DELETE_ARCHIVE)
        deleted_archives = 0
        
        for filename in os.listdir(ARCHIVE_DIR):
            file_path = os.path.join(ARCHIVE_DIR, filename)
            if os.path.getmtime(file_path) < cutoff_date.timestamp():
                os.remove(file_path)
                deleted_archives += 1
        
        logging.info(f"Deleted {deleted_archives} old archives.")
        return f"Deleted {deleted_archives} old archives.", 200
    except Exception as e:
        logging.error(f"Error in delete_old_archives: {e}")
        return f"Error: {e}", 500