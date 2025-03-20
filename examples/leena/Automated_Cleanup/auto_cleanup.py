# Automated Cleanup and Archival Script
import os
import shutil
import time
import tarfile
from datetime import datetime
import logging

# Set up logging configuration
log_dir = '/home/leena/Downloads/Auto_cleanup'
log_file = os.path.join(log_dir, 'activity.log')

# Create log directory if it doesn't exist
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format='[%(asctime)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Directories
directory = '/home/leena/Downloads'
archives_directory = '/home/leena/Downloads/Archives'
subdirectories = ['documents', 'Images', 'Script', 'Text']

# Organize files into subdirectories function
def organize_files():
    files_moved = 0
    logging.info("Starting file organization")
    # Create subdirectories if they don't exist
    for subdirectory in subdirectories:
        subdirectory_path = os.path.join(directory, subdirectory)
        if not os.path.exists(subdirectory_path):
            os.makedirs(subdirectory_path)
            logging.info(f"Created subdirectory: {subdirectory_path}")

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        try:
            if file.endswith('.pdf') or file.endswith('.doc') or file.endswith('.docx'):
                shutil.move(file_path, os.path.join(directory, 'documents'))
                logging.info(f"Moved file {file} to documents")
                files_moved += 1
            elif file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                shutil.move(file_path, os.path.join(directory, 'Images'))
                logging.info(f"Moved file {file} to Images")
                files_moved += 1
            elif file.endswith('.py') or file.endswith('.sh') or file.endswith('.js'):
                shutil.move(file_path, os.path.join(directory, 'Script'))
                logging.info(f"Moved file {file} to Script")
                files_moved += 1
            elif file.endswith('.txt'):
                shutil.move(file_path, os.path.join(directory, 'Text'))
                logging.info(f"Moved file {file} to Text")
                files_moved += 1
        except Exception as e:
            logging.error(f"Error organizing file {file}: {e}")

    return files_moved

# Automatically archives old files older than 7 days function
def automatically_archives_old_files():
    archived_files = 0
    logging.info("Starting archiving of old files")
    archive_name = f"archived_{datetime.now().strftime('%Y%m%d')}.tar.gz"
    archive_path = os.path.join(archives_directory, archive_name)
    cutoff_time = time.time() - 7 * 86400  # 7 days in seconds

    try:
        with tarfile.open(archive_path, "w:gz") as tar:
            for subdir, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(subdir, file)
                    if os.path.isfile(file_path) and os.path.getmtime(file_path) < cutoff_time:
                        tar.add(file_path, arcname=os.path.relpath(file_path, directory))
                        os.remove(file_path)
                        logging.info(f"Archived and removed file: {file_path}")
                        archived_files += 1
        logging.info(f"Created archive: {archive_path}")
        return archived_files
    except Exception as e:
        logging.error(f"Error archiving files: {e}")
        return archived_files

# Automatically deletes archives older than 30 days function
def automatically_deletes_old_archives():
    deleted_files = 0
    logging.info("Starting deletion of old archives")
    cutoff_time = time.time() - 30 * 86400  # 30 days in seconds

    try:
        for file in os.listdir(archives_directory):
            file_path = os.path.join(archives_directory, file)
            if file.endswith('.tar.gz') and os.path.getmtime(file_path) < cutoff_time:
                os.remove(file_path)
                logging.info(f"Deleted old archive: {file_path}")
                deleted_files += 1
        return deleted_files
    except Exception as e:
        logging.error(f"Error deleting old archives: {e}")
        return deleted_files

if __name__ == "__main__":
    # Perform cleanup tasks
    files_moved = organize_files()
    archived_files = automatically_archives_old_files()
    deleted_files = automatically_deletes_old_archives()

    # Log the consolidated message
    logging.info(f"Files organized: {files_moved} moved, {archived_files} archived, {deleted_files} deleted.")