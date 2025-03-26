import os
import shutil
import tarfile
import logging
from datetime import datetime, timedelta
 
# Use a log file in the current working directory instead of /var/log
log_file = os.path.join(os.getcwd(), "auto_cleanup.log")
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Auto cleanup API started.")
 

# Define Directories and File Extensions
SCAN_DIR = '/home/zainabghaithi/Downloads' 
ARCHIVE_DIR = '/home/zainabghaithi/Downloads/archives'   
# Directory to store archived files
RETENTION_DAYS = 30  # Archives older than 30 days will be deleted
ARCHIVE_OLDER_THAN_DAYS = 7  # Files older than 7 days will be archived

def organize_files_by_extension(scan_dir):
    """
    Organize files in 'scan_dir' into subdirectories based on file extension.
    """
    file_extensions = ['pdf', 'txt', 'jpg', 'py', 'mp3','html','png']  # Extend this list as needed
    for ext in file_extensions:
        # Ensure the subdirectory for each extension is created
        subdir = os.path.join(scan_dir, ext)
        
        # Create the directory if it doesn't exist
        if not os.path.exists(subdir): 
            os.makedirs(subdir)
            logging.info(f"Created directory {subdir}")
        
        # Loop through all files in the scan directory
        for filename in os.listdir(scan_dir):
            file_path = os.path.join(scan_dir, filename)
            
            # Skip directories (only move files)
            if os.path.isdir(file_path):
                continue

             # Log the filename and extension being processed
            logging.info(f"Processing file: {filename} with extension: {ext}")
            
            # Check the file extension and move the file accordingly
            # We use lower() to handle case-insensitivity
            if filename.lower().endswith(f".{ext}"):
                destination = os.path.join(subdir, filename)
                try:
                    # Move the file to the respective subdirectory
                    shutil.move(file_path, destination)
                    logging.info(f"Moved {filename} to {subdir}")
                except Exception as e:
                    logging.error(f"Error moving {filename}: {e}")


def archive_old_files(scan_dir, archive_dir, retention_days=ARCHIVE_OLDER_THAN_DAYS):
    """
    Archive files in 'scan_dir' that are older than 'retention_days'.
    The archived files are stored in 'archive_dir' as a tar.gz file.
    Files are removed after being archived.
    """
    today = datetime.today()
    archive_name = os.path.join(archive_dir, f"archived_{today.strftime('%Y%m%d')}.tar.gz")

    try:
        with tarfile.open(archive_name, "w:gz") as archive:
            for filename in os.listdir(scan_dir):
                file_path = os.path.join(scan_dir, filename)
                # Skip directories
                if os.path.isdir(file_path):
                    continue

                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                if today - file_mtime > timedelta(days=retention_days):
                    archive.add(file_path, arcname=filename)
                    os.remove(file_path)
                    logging.info(f"Archived and removed {filename}")
        logging.info(f"Archived files into {archive_name}")
    except Exception as e:
        logging.error(f"Error during archiving: {e}")
        raise

def delete_old_archives(archive_dir, retention_days=RETENTION_DAYS):
    """
    Delete archive files in 'archive_dir' that are older than 'retention_days'.
    """
    today = datetime.today()
    for filename in os.listdir(archive_dir):
        file_path = os.path.join(archive_dir, filename)
        if os.path.isdir(file_path):
            continue
        file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
        if today - file_mtime > timedelta(days=retention_days):
            try:
                os.remove(file_path)
                logging.info(f"Deleted old archive {filename}")
            except Exception as e:
                logging.error(f"Error deleting archive {filename}: {e}")

if __name__ == "__main__":
    organize_files_by_extension(SCAN_DIR)
