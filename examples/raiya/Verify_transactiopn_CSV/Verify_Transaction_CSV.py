import hashlib
import os

# File paths (adjust as needed)
csv_file_path = r'./transactions.csv'
hash_file_path = r'./transactions_csv.hash'

def compute_sha256(file_path):
    """Compute the SHA-256 hash of the file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    return sha256.hexdigest()

def read_saved_hash(file_path):
    """Read the saved hash from file."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read().strip()
    return None

def save_hash(file_path, hash_value):
    """Save the computed hash to the file (overwrite)."""
    with open(file_path, 'w') as f:
        f.write(hash_value)

def verify_file_integrity():
    current_hash = compute_sha256(csv_file_path)
    if current_hash is None:
        return
    
    saved_hash = read_saved_hash(hash_file_path)
    
    if saved_hash:
        if current_hash != saved_hash:
            print("Alert: Discrepancy detected! The CSV file has been modified manually or is corrupt.")
        else:
            print("File integrity verified. No discrepancies found.")
    else:
        print("No previously saved hash found. Creating one now.")

    # Save or update the hash file with the current hash
    save_hash(hash_file_path, current_hash)
    print("SHA-256 hash saved/updated.")

if __name__ == '__main__':
    verify_file_integrity()
   
   