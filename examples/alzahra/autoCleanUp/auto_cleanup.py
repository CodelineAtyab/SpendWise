import os
import shutil
import tarfile
import time
import logging
from datetime import datetime, timedelta

# Configuration
download_dir = r"C:\Users\Codeline\downloads"
archive_dir = os.path.join(download_dir, "archives")
log_file = "/var/log/auto_cleanup/activity.log"
extension_dirs = {
    ".jpg": "images",
    ".png": "images",
    ".pdf": "documents",
    ".txt": "documents",
    ".py": "scripts",
    ".sh": "scripts",
}

# Setup logging
logging.basicConfig(filename=log_file, level=logging.INFO, format='[%(asctime)s] %(message)s')

def organize_files():
    files_moved = 0
    for filename in os.listdir(download_dir):
        file_path = os.path.join(download_dir, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            if ext in extension_dirs:
                target_dir = os.path.join(download_dir, extension_dirs[ext])
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(target_dir, filename))
                files_moved += 1
    return files_moved

def archive_old_files():
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    cutoff_date = datetime.now() - timedelta(days=7)
    archive_name = f"archived_{datetime.now().strftime('%Y%m%d')}.tar.gz"
    archive_path = os.path.join(archive_dir, archive_name)
    
    with tarfile.open(archive_path, "w:gz") as tar:
        files_archived = 0
        for root, _, files in os.walk(download_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path) and datetime.fromtimestamp(os.path.getmtime(file_path)) < cutoff_date:
                    tar.add(file_path, arcname=file)
                    os.remove(file_path)
                    files_archived += 1
    return files_archived

def delete_old_archives():
    cutoff_date = datetime.now() - timedelta(days=30)
    archives_deleted = 0
    for filename in os.listdir(archive_dir):
        archive_path = os.path.join(archive_dir, filename)
        if os.path.isfile(archive_path) and datetime.fromtimestamp(os.path.getmtime(archive_path)) < cutoff_date:
            os.remove(archive_path)
            archives_deleted += 1
    return archives_deleted

def set_permissions():
    os.system(f"chmod -R 750 {download_dir}")
    os.system(f"chmod -R 750 {archive_dir}")
    os.system(f"chmod 640 {log_file}")

def main():
    files_moved = organize_files()
    files_archived = archive_old_files()
    archives_deleted = delete_old_archives()
    set_permissions()
    
    logging.info(f"Files organized: {files_moved} moved, {files_archived} archived, {archives_deleted} deleted.")
    print("Cleanup complete. Check logs for details.")

if __name__ == "__main__":
    main()