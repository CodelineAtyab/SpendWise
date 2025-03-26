#!/usr/bin/env python3

import os
import shutil
import tarfile
import time
import argparse
import logging
from datetime import datetime

def setup_logging():
    """Configures logging to a user-friendly location."""
    log_dir = os.path.expanduser("~/auto_cleanup_logs")
    os.makedirs(log_dir, exist_ok=True)  # Ensure the log directory exists
    log_file = os.path.join(log_dir, "activity.log")
    
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Logging initialized.")

def ensure_directories(base_dir):
    """Ensures required subdirectories exist within the target directory."""
    folders = {
        "documents": ['pdf', 'txt', 'docx'],
        "images": ['jpg', 'png', 'jpeg'],
        "scripts": ['py', 'sh', 'js'],
        "archives": []
    }
    paths = {}
    
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        paths[folder] = folder_path
    
    return paths

def organize_files(base_dir, paths):
    """Moves files into categorized folders based on their extensions."""
    logging.info("Organizing files in: %s", base_dir)
    moved_count = 0
    
    for file_name in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file_name)
        
        if os.path.isfile(file_path):
            ext = file_name.split('.')[-1].lower()
            target_dir = None
            
            for folder, extensions in paths.items():
                if ext in extensions:
                    target_dir = paths[folder]
                    break
            
            if target_dir:
                try:
                    shutil.move(file_path, os.path.join(target_dir, file_name))
                    moved_count += 1
                    logging.info("Moved: %s -> %s", file_name, target_dir)
                except Exception as e:
                    logging.error("Failed to move %s: %s", file_name, str(e))
    
    logging.info("Finished organizing. Files moved: %d", moved_count)
    return moved_count

def archive_old_files(base_dir, archives_dir):
    """Archives files older than 7 days into a compressed archive."""
    logging.info("Archiving files older than 7 days in: %s", base_dir)
    now = time.time()
    files_to_archive = []
    
    for root, _, files in os.walk(base_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_age = now - os.path.getmtime(file_path)
            
            if file_age > 7 * 24 * 60 * 60:  # Older than 7 days
                files_to_archive.append(file_path)
    
    if files_to_archive:
        archive_name = f"archived_{datetime.now().strftime('%Y%m%d')}.tar.gz"
        archive_path = os.path.join(archives_dir, archive_name)
        
        try:
            with tarfile.open(archive_path, "w:gz") as tar:
                for file_path in files_to_archive:
                    tar.add(file_path, arcname=os.path.basename(file_path))
                    os.remove(file_path)
                    logging.info("Archived and removed: %s", file_path)
            return len(files_to_archive)
        except Exception as e:
            logging.error("Error creating archive: %s", str(e))
    
    logging.info("No files were archived.")
    return 0

def delete_old_archives(archives_dir):
    """Removes archive files older than 30 days."""
    logging.info("Deleting archives older than 30 days in: %s", archives_dir)
    now = time.time()
    deleted_count = 0
    
    for file_name in os.listdir(archives_dir):
        file_path = os.path.join(archives_dir, file_name)
        file_age = now - os.path.getmtime(file_path)
        
        if file_age > 30 * 24 * 60 * 60:  # Older than 30 days
            try:
                os.remove(file_path)
                deleted_count += 1
                logging.info("Deleted archive: %s", file_path)
            except Exception as e:
                logging.error("Failed to delete archive %s: %s", file_path, str(e))
    
    return deleted_count

def main():
    parser = argparse.ArgumentParser(description="Automated file organizer and cleaner.")
    parser.add_argument("directory", help="Target directory to process.")
    args = parser.parse_args()
    
    base_dir = os.path.abspath(args.directory)
    
    if not os.path.isdir(base_dir):
        logging.error("Invalid directory: %s", base_dir)
        print("Error: The specified directory does not exist.")
        return
    
    setup_logging()
    paths = ensure_directories(base_dir)
    
    moved_count = organize_files(base_dir, paths)
    archived_count = archive_old_files(base_dir, paths["archives"])
    deleted_count = delete_old_archives(paths["archives"])
    
    logging.info("Process completed. Moved: %d, Archived: %d, Deleted: %d", moved_count, archived_count, deleted_count)

if __name__ == "__main__":
    main()


