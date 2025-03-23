import os
import shutil
import tarfile
import logging
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException

# Use a log file in the current working directory instead of /var/log
log_file = os.path.join(os.getcwd(), "auto_cleanup.log")
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Auto cleanup API started.")

# Define Directories and File Extensions
SCAN_DIR = '/home/user/downloads'   # Directory to scan for files
ARCHIVE_DIR = '/home/user/archives'   # Directory to store archived files
RETENTION_DAYS = 30  # Archives older than 30 days will be deleted
ARCHIVE_OLDER_THAN_DAYS = 7  # Files older than 7 days will be archived

def organize_files_by_extension(scan_dir):
    """
    Organize files in 'scan_dir' into subdirectories based on file extension.
    """
    file_extensions = ['pdf', 'txt', 'jpg', 'py', 'mp3']  # Extend this list as needed
    for ext in file_extensions:
        subdir = os.path.join(scan_dir, ext)
        if not os.path.exists(subdir):
            os.makedirs(subdir)
            logging.info(f"Created directory {subdir}")
        for filename in os.listdir(scan_dir):
            file_path = os.path.join(scan_dir, filename)
            # Skip directories
            if os.path.isdir(file_path):
                continue
            # Move files based on their extension (case-insensitive)
            if filename.lower().endswith(f".{ext}"):
                destination = os.path.join(subdir, filename)
                try:
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

# Create FastAPI app
app = FastAPI()

@app.get("/organize")
def api_organize():
    """
    Endpoint to organize files by their extension.
    """
    try:
        organize_files_by_extension(SCAN_DIR)
        return {"message": "Files organized by extension."}
    except Exception as e:
        logging.error(f"Error in organize: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/archive")
def api_archive():
    """
    Endpoint to archive old files.
    """
    try:
        archive_old_files(SCAN_DIR, ARCHIVE_DIR)
        return {"message": "Old files archived."}
    except Exception as e:
        logging.error(f"Error in archive: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/delete")
def api_delete():
    """
    Endpoint to delete old archive files.
    """
    try:
        delete_old_archives(ARCHIVE_DIR)
        return {"message": "Old archives deleted."}
    except Exception as e:
        logging.error(f"Error in delete: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/auto_cleanup")
def auto_cleanup():
    """
    Combined endpoint to organize files, archive old files, and delete old archives.
    """
    try:
        organize_files_by_extension(SCAN_DIR)
        archive_old_files(SCAN_DIR, ARCHIVE_DIR)
        delete_old_archives(ARCHIVE_DIR)
        logging.info("Auto cleanup completed successfully via API.")
        return {"message": "Auto cleanup script completed successfully."}
    except Exception as e:
        logging.error(f"Error in auto_cleanup: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
