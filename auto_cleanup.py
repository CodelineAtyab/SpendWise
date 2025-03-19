import os
import shutil
import tarfile
import time
import logging
from datetime import datetime, timedelta

# Set up logging
logging.basicConfig(filename='/var/log/auto_cleanup/activity.log', 
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Directories
DOWNLOADS_DIR = '/home/user/downloads'
ARCHIVES_DIR = os.path.join(DOWNLOADS_DIR, 'archives')
EXTENSION_DIRS = {
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'documents': ['.pdf', '.txt', '.docx'],
    'scripts': ['.py', '.js', '.sh']
}

# Ensure necessary directories exist
os.makedirs(ARCHIVES_DIR, exist_ok=True)

def organize_files():
    """Organize files based on extension into subdirectories."""
    files_moved = 0
    for file_name in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, file_name)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file_name)[1].lower()
            
            for category, extensions in EXTENSION_DIRS.items():
                if file_ext in extensions:
                    category_dir = os.path.join(DOWNLOADS_DIR, category)
                    os.makedirs(category_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_dir, file_name))
                    files_moved += 1
                    break
    return files_moved

def archive_old_files():
    """Archive files older than 7 days into a tar.gz file."""
    archived_files = 0
    now = time.time()
    archive_name = os.path.join(ARCHIVES_DIR, f"archived_{datetime.now().strftime('%Y%m%d')}.tar.gz")
    
    with tarfile.open(archive_name, "w:gz") as archive:
        for file_name in os.listdir(DOWNLOADS_DIR):
            file_path = os.path.join(DOWNLOADS_DIR, file_name)
            if os.path.isfile(file_path) and now - os.path.getmtime(file_path) > 7 * 86400:
                archive.add(file_path, arcname=file_name)
                archived_files += 1
                os.remove(file_path)
    
    return archived_files

def delete_old_archives():
    """Delete archives older than 30 days."""
    deleted_files = 0
    now = time.time()
    
    for file_name in os.listdir(ARCHIVES_DIR):
        file_path = os.path.join(ARCHIVES_DIR, file_name)
        if os.path.isfile(file_path) and now - os.path.getmtime(file_path) > 30 * 86400:
            os.remove(file_path)
            deleted_files += 1
    
    return deleted_files

def main():
    """Main cleanup process."""
    try:
        files_moved = organize_files()
        archived_files = archive_old_files()
        deleted_files = delete_old_archives()

        logging.info(f"Files organized: {files_moved} moved, {archived_files} archived, {deleted_files} deleted.")
    except Exception as e:
        logging.error(f"Error during auto cleanup: {str(e)}")

if __name__ == "__main__":
    main()

