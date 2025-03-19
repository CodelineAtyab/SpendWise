import os
import shutil
import tarfile
import time
from datetime import datetime
import logging

# Directory paths
downloads_dir = '/home/ubuntu/downloads'
archives_dir = os.path.join(downloads_dir, 'archives')
document_dir = os.path.join(downloads_dir, 'documents')
image_dir = os.path.join(downloads_dir, 'images')
script_dir = os.path.join(downloads_dir, 'scripts')

# Logging setup
log_file = "/var/log/auto_cleanup/activity.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")

# Create subdirectories if they don't exist
os.makedirs(document_dir, exist_ok=True)
os.makedirs(image_dir, exist_ok=True)
os.makedirs(script_dir, exist_ok=True)
os.makedirs(archives_dir, exist_ok=True)

# Function to move files based on extension
def move_files():
    moved_files = 0
    for file_name in os.listdir(downloads_dir):
        file_path = os.path.join(downloads_dir, file_name)
        if os.path.isfile(file_path):
            extension = file_name.split('.')[-1].lower()

            # Move files to the appropriate subdirectory
            if extension in ['pdf', 'txt', 'docx']:
                target_dir = document_dir
            elif extension in ['jpg', 'png', 'jpeg']:
                target_dir = image_dir
            elif extension in ['py', 'sh', 'js']:
                target_dir = script_dir
            else:
                continue  # Skip files that don't match any of these extensions

            target_path = os.path.join(target_dir, file_name)
            shutil.move(file_path, target_path)
            moved_files += 1

    return moved_files

# Function to archive files older than 7 days
def archive_old_files():
    archived_files = 0
    now = time.time()
    for file_name in os.listdir(downloads_dir):
        file_path = os.path.join(downloads_dir, file_name)

        if os.path.isfile(file_path):
            file_age = now - os.path.getmtime(file_path)
            if file_age > 7 * 24 * 60 * 60:  # Files older than 7 days
                archive_name = f"archived_{datetime.now().strftime('%Y%m%d')}.tar.gz"
                archive_path = os.path.join(archives_dir, archive_name)
                with tarfile.open(archive_path, "a:gz") as archive:
                    archive.add(file_path, arcname=file_name)  # Add file to archive
                    os.remove(file_path)  # Remove file from directory after archiving
                    archived_files += 1

    return archived_files

# Function to delete archives older than 30 days
def delete_old_archives():
    deleted_files = 0
    now = time.time()

    for file_name in os.listdir(archives_dir):
        file_path = os.path.join(archives_dir, file_name)

        if os.path.isfile(file_path):
            file_age = now - os.path.getmtime(file_path)
            if file_age > 30 * 24 * 60 * 60:  # Archives older than 30 days
                os.remove(file_path)
                deleted_files += 1

    return deleted_files

# Main execution function
def main():
    moved_files = move_files()
    archived_files = archive_old_files()
    deleted_files = delete_old_archives()

    # Log the action
    logging.info(f"Files organized: {moved_files} moved, {archived_files} archived, {deleted_files} deleted.")

if __name__ == "__main__":
    main()



