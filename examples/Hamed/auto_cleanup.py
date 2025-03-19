import os
import shutil
import time
import tarfile
from datetime import datetime
import logging

# Configure logging to file with timestamps
logging.basicConfig(
    filename=r'C:\Users\codel\OneDrive\Desktop\test scan\auto_cleanup_activity.log',  # Path to the log file
    level=logging.INFO,  # Log level (INFO will log all levels of messages like INFO, WARNING, ERROR)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format to include timestamp
)

# Set the directory to scan for files
directory = r'C:\Users\codel\OneDrive\Desktop\test scan'  # Change this path to the folder you want to scan

# Define subdirectories for different file types
DOCUMENTS_DIR = os.path.join(directory, 'documents')
IMAGES_DIR = os.path.join(directory, 'images')
SCRIPTS_DIR = os.path.join(directory, 'scripts')
ARCHIVE_DIR = os.path.join(directory, 'archives')

# Create subdirectories if they don't exist
for dir_path in [DOCUMENTS_DIR, IMAGES_DIR, SCRIPTS_DIR, ARCHIVE_DIR]:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# Define file extensions for each type of file
EXTENSIONS = {
    'documents': ['.pdf', '.txt', '.docx', '.doc'],
    'images': ['.jpg', '.png', '.gif', '.jpeg'],
    'scripts': ['.py', '.sh', '.bash', '.pl'],
}

# Get the current time (for checking file age)
current_time = time.time()

# Define the number of seconds in 7 days and 30 days
SEVEN_DAYS_IN_SECONDS = 7 * 24 * 60 * 60  # 7 days in seconds
THIRTY_DAYS_IN_SECONDS = 30 * 24 * 60 * 60  # 30 days in seconds


# Function to move files based on their extension
def move_files():
    moved_files = 0
    archived_files = 0
    files_to_archive = []

    # Loop through files in the scan directory
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)

        # Skip directories, only handle files
        if os.path.isdir(full_path):
            continue

        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Determine the destination subdirectory based on file extension
        destination_dir = None
        for category, extensions in EXTENSIONS.items():
            if file_extension in extensions:
                destination_dir = globals()[category.upper() + '_DIR']
                break

        # If a matching category was found, move the file
        if destination_dir:
            destination_path = os.path.join(destination_dir, filename)
            shutil.move(full_path, destination_path)
            moved_files += 1
            logging.info(f"Moved: {filename} to {destination_dir}")

        # Archive files older than 7 days
        if os.path.getmtime(full_path) < current_time - SEVEN_DAYS_IN_SECONDS:
            files_to_archive.append(full_path)  # Collect file to archive

    # After moving files, archive all collected files
    if files_to_archive:
        archive_files(files_to_archive)
        archived_files = len(files_to_archive)

    return moved_files, archived_files


# Function to archive multiple files into one .tar.gz
def archive_files(files_to_archive):
    archive_name = f"archived_{datetime.now().strftime('%Y%m%d')}.tar.gz"
    archive_path = os.path.join(ARCHIVE_DIR, archive_name)

    with tarfile.open(archive_path, "w:gz") as archive:
        for file_path in files_to_archive:
            archive.add(file_path, os.path.basename(file_path))  # Add the file to the archive
            os.remove(file_path)  # Remove file after archiving

    logging.info(f"Archived {len(files_to_archive)} files to {archive_path}")


# Function to delete files older than 30 days in the archive folder
def delete_old_archived_files():
    deleted_files = 0
    # Loop through files in the archive folder
    for filename in os.listdir(ARCHIVE_DIR):
        full_path = os.path.join(ARCHIVE_DIR, filename)

        # Skip directories, only handle files
        if os.path.isdir(full_path):
            continue

        # Check if the file is older than 30 days
        if os.path.getmtime(full_path) < current_time - THIRTY_DAYS_IN_SECONDS:
            os.remove(full_path)  # Delete the file
            deleted_files += 1
            logging.info(f"Deleted old archive: {filename}")

    return deleted_files


# Main execution function to log details and call the methods
def main():
    # Move and archive files
    moved_files, archived_files = move_files()

    # Delete old archived files (older than 30 days)
    deleted_files = delete_old_archived_files()

    logging.info(f"Total files moved: {moved_files}")
    logging.info(f"Total files archived: {archived_files}")
    logging.info(f"Total files deleted from archive: {deleted_files}")
    print(f"Total files moved: {moved_files}")
    print(f"Total files archived: {archived_files}")
    print(f"Total files deleted and removed from archive: {deleted_files}")


# Run the script
if __name__ == "__main__":
    main()
