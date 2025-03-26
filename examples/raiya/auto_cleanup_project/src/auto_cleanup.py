import os
import shutil
import tarfile
import time
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(filename='cleanup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            ext = filename.split('.')[-1]
            ext_dir = os.path.join(directory, ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            shutil.move(os.path.join(directory, filename), os.path.join(ext_dir, filename))
            logging.info(f'Moved file {filename} to {ext_dir}')

def archive_old_files(directory):
    now = time.time()
    archive_dir = os.path.join(directory, 'archives')
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and (now - os.path.getmtime(file_path)) > 7 * 86400:
            archive_path = os.path.join(archive_dir, f'{filename}.tar.gz')
            with tarfile.open(archive_path, 'w:gz') as tar:
                tar.add(file_path, arcname=filename)
            os.remove(file_path)
            logging.info(f'Archived file {filename} to {archive_path}')

def delete_old_archives(directory):
    now = time.time()
    archive_dir = os.path.join(directory, 'archives')

    for filename in os.listdir(archive_dir):
        file_path = os.path.join(archive_dir, filename)
        if os.path.isfile(file_path) and (now - os.path.getmtime(file_path)) > 30 * 86400:
            os.remove(file_path)
            logging.info(f'Deleted old archive {filename}')

def main():
    target_directory = '/home/raiya/Downloads'  
    organize_files(target_directory)
    archive_old_files(target_directory)
    delete_old_archives(target_directory)

if __name__ == '__main__':
    main()
