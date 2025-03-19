import os
import shutil
import tarfile
import time
import logging
from datetime import datetime, timedelta

# Set up logging to log activity
logging.basicConfig(filename='/var/log/auto_cleanup/activity.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Auto cleanup script started.")

#Define Directories and File Extensions
SCAN_DIR = '/home/user/downloads'  # Directory to scan for files
ARCHIVE_DIR = '/home/user/archives'  # Directory to store archived files
RETENTION_DAYS = 30  # Files older than 30 days will be deleted after archiving
ARCHIVE_OLDER_THAN_DAYS = 7  # Files older than 7 days will be archived

def organize_files_by_extension(scan_dir):
    file_extensions = ['pdf', 'txt', 'jpg', 'py', 'mp3']  # You can expand this list as needed

    for ext in file_extensions:
        subdir = os.path.join(scan_dir, ext)
        if not os.path.exists(subdir):
            os.makedirs(subdir)

        for filename in os.listdir(scan_dir):
            file_path = os.path.join(scan_dir, filename)

            # Skip directories
            if os.path.isdir(file_path):
                continue

            # Move files into subdirectories based on their extension
            if filename.endswith(f".{ext}"):
                destination = os.path.join(subdir, filename)
                shutil.move(file_path, destination)
                logging.info(f"Moved {filename} to {subdir}")

def archive_old_files(scan_dir, archive_dir, retention_days=ARCHIVE_OLDER_THAN_DAYS):
    today = datetime.today()
    archive_name = os.path.join(archive_dir, f"archived_{today.strftime('%Y%m%d')}.tar.gz")
    
    with tarfile.open(archive_name, "w:gz") as archive:
        for filename in os.listdir(scan_dir):
            file_path = os.path.join(scan_dir, filename)
            if os.path.isdir(file_path):
                continue

            # Get the last modified time of the file
            file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            if today - file_mtime > timedelta(days=retention_days):
                archive.add(file_path, arcname=filename)
                os.remove(file_path)  # Remove the file after archiving
                logging.info(f"Archived and removed {filename}")

    logging.info(f"Archived files into {archive_name}")

def delete_old_archives(archive_dir, retention_days=RETENTION_DAYS):
    today = datetime.today()

    for filename in os.listdir(archive_dir):
        file_path = os.path.join(archive_dir, filename)
        
        if os.path.isdir(file_path):
            continue
        
        # Get the last modified time of the archive
        file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
        if today - file_mtime > timedelta(days=retention_days):
            os.remove(file_path)  # Remove the archive file
            logging.info(f"Deleted old archive {filename}")


if __name__ == "__main__":
    try:
        # Organize files by extension
        organize_files_by_extension(SCAN_DIR)
        
        # Archive files older than 7 days
        archive_old_files(SCAN_DIR, ARCHIVE_DIR)

        # Delete archives older than 30 days
        delete_old_archives(ARCHIVE_DIR)

        logging.info("Auto cleanup script completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
