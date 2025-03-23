import os
import shutil
import time
import tarfile
from datetime import datetime
import logging

# Set the directory to scan for files
directory = r'/home/hamed/Desktop/codeline'  # Change this path as needed

# Ensure the logging directory exists before configuring logging
os.makedirs(directory, exist_ok=True)

# Configure logging inside the scan directory
log_file_path = '/var/log/auto_cleanup/activity.log'
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Define subdirectories for file organization
DOCUMENTS_DIR = os.path.join(directory, 'documents')
IMAGES_DIR = os.path.join(directory, 'images')
SCRIPTS_DIR = os.path.join(directory, 'scripts')
ARCHIVE_DIR = os.path.join(directory, 'archives')

# Create subdirectories if they don't exist
for dir_path in [DOCUMENTS_DIR, IMAGES_DIR, SCRIPTS_DIR, ARCHIVE_DIR]:
    os.makedirs(dir_path, exist_ok=True)

# File type categories
EXTENSIONS = {
    'documents': ['.pdf', '.txt', '.docx', '.doc'],
    'images': ['.jpg', '.png', '.gif', '.jpeg'],
    'scripts': ['.py', '.sh', '.bash', '.pl'],
}

# Time thresholds
SEVEN_DAYS = 7 * 24 * 60 * 60
THIRTY_DAYS = 30 * 24 * 60 * 60


def archive_old_files():
    """Finds and archives files older than 7 days."""
    current_time = time.time()
    files_to_archive = []

    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)

        if os.path.isfile(full_path) and os.path.getmtime(full_path) < current_time - SEVEN_DAYS:
            files_to_archive.append(full_path)

    if files_to_archive:
        archive_name = f"archived_{datetime.now().strftime('%Y%m%d')}.tar.gz"
        archive_path = os.path.join(ARCHIVE_DIR, archive_name)

        try:
            with tarfile.open(archive_path, "w:gz") as archive:
                for file_path in files_to_archive:
                    archive.add(file_path, os.path.basename(file_path))  # Add file to archive

            for file_path in files_to_archive:
                os.remove(file_path)  # Remove after successful archiving
                logging.info(f"Archived: {os.path.basename(file_path)}")

            logging.info(f"Archived {len(files_to_archive)} files to {archive_path}")
            return len(files_to_archive)

        except Exception as e:
            logging.error(f"Error archiving files: {e}")
            return 0
    return 0


def move_files():
    """Organizes files into categorized subdirectories."""
    moved_files = 0

    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)

        if os.path.isfile(full_path):
            file_extension = os.path.splitext(filename)[1].lower()
            destination_dir = None

            for category, extensions in EXTENSIONS.items():
                if file_extension in extensions:
                    destination_dir = globals()[category.upper() + '_DIR']
                    break

            if destination_dir:
                shutil.move(full_path, os.path.join(destination_dir, filename))
                moved_files += 1
                logging.info(f"Moved: {filename} to {destination_dir}")

    return moved_files


def delete_old_archived_files():
    """Deletes archived files older than 30 days."""
    current_time = time.time()
    deleted_files = 0

    for filename in os.listdir(ARCHIVE_DIR):
        full_path = os.path.join(ARCHIVE_DIR, filename)

        if os.path.isfile(full_path) and os.path.getmtime(full_path) < current_time - THIRTY_DAYS:
            try:
                os.remove(full_path)
                deleted_files += 1
                logging.info(f"Deleted old archive: {filename}")
            except Exception as e:
                logging.error(f"Failed to delete {filename}: {e}")

    return deleted_files


def list_files():
    """Lists files in the directory before processing."""
    print("\n--- Listing Files ---\n")
    logging.info("Listing files in directory...")

    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)

        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            modified_time = datetime.fromtimestamp(os.path.getmtime(full_path)).strftime('%Y-%m-%d %H:%M:%S')
            print(f"File: {filename} | Size: {size} bytes | Last Modified: {modified_time}")
            logging.info(f"File Found: {filename} | Size: {size} bytes | Last Modified: {modified_time}")


def main():
    """Executes the script in the correct order."""
    if not os.path.isdir(directory):
        logging.error("Invalid directory: %s", directory)
        print("Invalid directory.")
        return

    list_files()
    archived_files = archive_old_files()
    moved_files = move_files()
    deleted_files = delete_old_archived_files()

    print(f"Total files moved: {moved_files}")
    print(f"Total files archived: {archived_files}")
    print(f"Total files deleted from archive: {deleted_files}")

    logging.info(f"Total files moved: {moved_files}")
    logging.info(f"Total files archived: {archived_files}")
    logging.info(f"Total files deleted from archive: {deleted_files}")


if __name__ == "__main__":
    main()