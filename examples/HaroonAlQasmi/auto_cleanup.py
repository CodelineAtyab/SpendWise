#!/usr/bin/env python3
import os
import shutil
import tarfile
import logging
import datetime
import time


#-------------------------------------------------------------------------------------------------------------------------------------------------------
#The way this script works is by taking and input of a folders path and then it will organize it
#In my linux machine I made it run in a folder called testing in my desktop you can check how it works by inserting files in it and waiting for a minute 
#-------------------------------------------------------------------------------------------------------------------------------------------------------


def setup_logging():
    log_file = "/var/log/auto_cleanup/activity.log"
    # Ensure the log directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging initialized.")

def organize_files(directory):
    logging.info("Starting to organize files in directory: %s", directory)
    # List items in the top-level directory
    for entry in os.listdir(directory):
        entry_path = os.path.join(directory, entry)
        # Only process files (skip directories)
        if os.path.isfile(entry_path):
            # Skip archive files
            if entry.startswith("archived_") and entry.endswith(".tar.gz"):
                continue
            # Get file extension (if no extension, use 'no_extension')
            ext = os.path.splitext(entry)[1].lower()
            ext_folder = ext.lstrip('.') if ext else "no_extension"
            target_folder = os.path.join(directory, ext_folder)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
                logging.info("Created folder: %s", target_folder)
            try:
                shutil.move(entry_path, os.path.join(target_folder, entry))
                logging.info("Moved file '%s' to folder '%s'", entry, ext_folder)
            except Exception as e:
                logging.error("Error moving file '%s': %s", entry, str(e))
    logging.info("Finished organizing files.")

def archive_old_files(directory):
    logging.info("Starting to archive files older than 7 days in: %s", directory)
    files_to_archive = []
    # Determine the cutoff time (7 days ago)
    cutoff = time.time() - 7 * 24 * 60 * 60  
    # Walk the directory tree (excluding archive files)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith("archived_") and file.endswith(".tar.gz"):
                continue
            file_path = os.path.join(root, file)
            try:
                mod_time = os.path.getmtime(file_path)
            except Exception as e:
                logging.error("Error getting modification time for '%s': %s", file_path, str(e))
                continue
            if mod_time < cutoff:
                files_to_archive.append(file_path)
    if files_to_archive:
        archive_name = "archived_" + datetime.datetime.now().strftime("%Y%m%d") + ".tar.gz"
        archive_path = os.path.join(directory, archive_name)
        try:
            with tarfile.open(archive_path, "w:gz") as tar:
                for file_path in files_to_archive:
                    # Save the file path relative to the base directory in the archive
                    rel_path = os.path.relpath(file_path, directory)
                    tar.add(file_path, arcname=rel_path)
                    logging.info("Added file '%s' to archive '%s'", file_path, archive_name)
            # After archiving, delete the old files
            for file_path in files_to_archive:
                try:
                    os.remove(file_path)
                    logging.info("Deleted archived file: %s", file_path)
                except Exception as e:
                    logging.error("Error deleting file '%s': %s", file_path, str(e))
        except Exception as e:
            logging.error("Error creating archive '%s': %s", archive_path, str(e))
    else:
        logging.info("No files older than 7 days found for archiving.")

def delete_old_archives(directory):
    logging.info("Checking for archive files older than 30 days in: %s", directory)
    # Determine the cutoff time (30 days ago)
    archive_cutoff = time.time() - 30 * 24 * 60 * 60  
    # Only check the top-level directory for archives
    for entry in os.listdir(directory):
        if entry.startswith("archived_") and entry.endswith(".tar.gz"):
            archive_path = os.path.join(directory, entry)
            try:
                mod_time = os.path.getmtime(archive_path)
                if mod_time < archive_cutoff:
                    os.remove(archive_path)
                    logging.info("Deleted old archive file: %s", archive_path)
            except Exception as e:
                logging.error("Error processing archive file '%s': %s", archive_path, str(e))

def main():
    setup_logging()
    directory = input("Enter the path to the directory: ").strip()
    if not os.path.isdir(directory):
        logging.error("Provided path is not a valid directory: %s", directory)
        print("Invalid directory.")
        return
    # Convert to absolute path
    directory = os.path.abspath(directory)
    logging.info("Script started for directory: %s", directory)
    
    organize_files(directory)
    archive_old_files(directory)
    delete_old_archives(directory)
    
    logging.info("Script completed successfully.")

if __name__ == '__main__':
    main()
