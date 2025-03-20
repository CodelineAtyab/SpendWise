import os
import shutil

# Configuration
BASE_DIR = "/home/TAMADHIR/Downloads"  # Base directory to organize
FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt", ".csv"],
    "scripts": [".py", ".sh", ".js"],
    "videos": [".mp4", ".mkv", ".avi"],
}

def organize_files_by_extension():
    """Organize files into directories based on their extensions."""
    if not os.path.exists(BASE_DIR):
        print(f"Error: Directory does not exist: {BASE_DIR}")
        return

    # Create directories for each category
    for category, extensions in FILE_CATEGORIES.items():
        category_dir = os.path.join(BASE_DIR, category)
        os.makedirs(category_dir, exist_ok=True)

    # Create a directory for uncategorized files
    
    uncategorized_dir = os.path.join(BASE_DIR, "others")
    os.makedirs(uncategorized_dir, exist_ok=True)

    # Move files into their respective directories
    files_moved = 0
    for filename in os.listdir(BASE_DIR):
        if filename.startswith("."):
            continue  # Skip hidden files
        file_path = os.path.join(BASE_DIR, filename)
        if os.path.isfile(file_path):
            print(f"Detected file: {filename}")  # Debugging line
            file_ext = os.path.splitext(filename)[1].lower()
            # Find the category for the file extension
            target_dir = next((key for key, exts in FILE_CATEGORIES.items() if file_ext in exts), "others")
            target_path = os.path.join(BASE_DIR, target_dir)
            shutil.move(file_path, os.path.join(target_path, filename))
            files_moved += 1

    print(f"Files organized: {files_moved} moved.")

if __name__ == "__main__":
    organize_files_by_extension()