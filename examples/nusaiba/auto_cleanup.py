import os
import shutil
import tarfile
import time
import logging
from datetime import datetime

source_dir = '/home/user/downloads'
archive_dir = '/home/user/archives'
log_file = '/var/log/auto_cleanup/activity.log'

os.makedirs(archive_dir, exist_ok=True)
os.makedirs(os.path.dirname(log_file), exist_ok=True)

file_extensions = {
    '.pdf': 'PDFs',
    '.txt': 'TextFiles',
    '.jpg': 'Images',
    '.png': 'Images',
    '.py': 'PythonScripts',
}

def get_current_date():
    return datetime.now().strftime('%Y%m%d')

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def organize_files():
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file_name)
        ext = ext.lower()

        if ext in file_extensions:
            subdir = file_extensions[ext]
            subdir_path = os.path.join(source_dir, subdir)

            os.makedirs(subdir_path, exist_ok=True)

            new_file_path = os.path.join(subdir_path, file_name)
            shutil.move(file_path, new_file_path)
            logging.info(f"Moved {file_name} to {subdir_path}")

# Archive the files
def archive_old_files(days_threshold=7):
    current_time = time.time()
    archive_file_name = f"archived_{get_current_date()}.tar.gz"
    archive_file_path = os.path.join(archive_dir, archive_file_name)

    with tarfile.open(archive_file_path, "w:gz") as archive:
        for file_name in os.listdir(source_dir):
            file_path = os.path.join(source_dir, file_name)

            if os.path.isdir(file_path):
                continue

            file_mod_time = os.path.getmtime(file_path)
            if (current_time - file_mod_time) > (days_threshold * 86400):
                archive.add(file_path, arcname=file_name)
                os.remove(file_path)
                logging.info(f"Archived and removed {file_name}")

    logging.info(f"Archived files into {archive_file_name}")

# Delete the files
def delete_old_archives(days_threshold=30):
    current_time = time.time()

    for archive_file_name in os.listdir(archive_dir):
        archive_file_path = os.path.join(archive_dir, archive_file_name)

        if os.path.isdir(archive_file_path):
            continue

        file_mod_time = os.path.getmtime(archive_file_path)
        if (current_time - file_mod_time) > (days_threshold * 86400):
            os.remove(archive_file_path)
            logging.info(f"Deleted old archive {archive_file_name}")

# Main function
def main():
    logging.info("Starting auto cleanup process")
    organize_files()
    archive_old_files()
    delete_old_archives()
    logging.info("Auto cleanup process completed")

if __name__ == "__main__":
    main()