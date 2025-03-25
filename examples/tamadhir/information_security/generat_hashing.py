import hashlib
import os

# File paths
CSV_FILE = "./transactions.csv"  
HASH_FILE = "./transactions.hash"  

def compute_sha256(file_path):
    """Compute the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def save_hash(hash_value, hash_file):
    """Save the hash value to a file."""
    with open(hash_file, "w") as f:
        f.write(hash_value)

def load_saved_hash(hash_file):
    """Load the saved hash value from the hash file."""
    try:
        with open(hash_file, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def verify_file_integrity():
    """Verify the integrity of the CSV file by comparing hashes."""
    current_hash = compute_sha256(CSV_FILE)
    saved_hash = load_saved_hash(HASH_FILE)

    if saved_hash is None:
        print("No saved hash found. Assuming file is intact.")
        if current_hash:
            save_hash(current_hash, HASH_FILE)
    elif current_hash != saved_hash:
        print("WARNING: File integrity check failed! The file may have been tampered with.")
    else:
        print("File integrity verified. No issues detected.")

def update_hash_after_modification():
    """Update the hash file after modifying the CSV file."""
    current_hash = compute_sha256(CSV_FILE)
    if current_hash:
        save_hash(current_hash, HASH_FILE)
        print("Hash updated successfully.")

# Example usage
if __name__ == "__main__":
    # On application startup, verify file integrity
    verify_file_integrity()

    # Simulate a transaction update (modify the CSV file here)
    # After modification, update the hash
    # update_hash_after_modification()


