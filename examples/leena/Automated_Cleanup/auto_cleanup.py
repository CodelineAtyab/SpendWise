import os
import shutil
import time
import tarfile
from datetime import datetime
import logging

# Set up logging configuration
log_file = '/var/log/auto_cleanup/activity.log'
logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format='[%(asctime)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Directories
directory = '/home/user/downloads'
archives_directory = '/home/user/downloads/Archives'
subdirectories = ['Documents', 'Images', 'Script', 'Text', 'Others']

# Organize files into subdirectories function
def organize_files():
    files_moved = 0
    # Create subdirectories if they don't exist
    for subdirectory in subdirectories:
        if not os.path.exists(directory + '/' + subdirectory):
            os.makedirs(directory + '/' + subdirectory)
    
    for file in os.listdir(directory):
        try:
            if file.endswith('.pdf') or file.endswith('.doc') or file.endswith('.docx') or file.endswith('.txt'):
                shutil.move(directory + '/' + file, directory + '/Documents')
                files_moved += 1
            elif file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                shutil.move(directory + '/' + file, directory + '/Images')
                files_moved += 1
            elif file.endswith('.py') or file.endswith('.sh') or file.endswith('.js'):
                shutil.move(directory + '/' + file, directory + '/Script')
                files_moved += 1
            elif file.endswith('.txt'):
                shutil.move(directory + '/' + file, directory + '/Text')
                files_moved += 1
            else:
                shutil.move(directory + '/' + file, directory + '/Others')
                files_moved += 1
        except Exception as e:
            logging.error(f"Error organizing file {file}: {e}")

    return files_moved

# Automatically archives old files older than 7 days function
def automatically_archives_old_files():
    archived_files = 0
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
                        archived_files += 1
        return archived_files
    except Exception as e:
        logging.error(f"Error archiving files: {e}")
        return archived_files

# Automatically deletes archives older than 30 days function
def automatically_deletes_old_archives():
    deleted_files = 0
    cutoff_time = time.time() - 30 * 86400  # 30 days in seconds

    try:
        for file in os.listdir(archives_directory):
            if file.endswith('.tar.gz') and os.path.getmtime(archives_directory + '/' + file) < cutoff_time:
                os.remove(archives_directory + '/' + file)
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
    
