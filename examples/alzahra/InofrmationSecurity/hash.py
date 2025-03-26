import hashlib
import os

CSV_FILE_PATH = 'transactions.csv'
HASH_FILE_PATH = 'transactions_hash.txt'

def compute_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b''):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def save_hash(hash_value, hash_file_path):
    with open(hash_file_path, 'w') as f:
        f.write(hash_value)

def load_hash(hash_file_path):
    if not os.path.exists(hash_file_path):
        return None
    with open(hash_file_path, 'r') as f:
        return f.read().strip()

def verify_file_integrity():
    current_hash = compute_sha256(CSV_FILE_PATH)
    saved_hash = load_hash(HASH_FILE_PATH)
    if saved_hash is None:
        print("No saved hash found. Saving current hash.")
        save_hash(current_hash, HASH_FILE_PATH)
    elif current_hash != saved_hash:
        print("File integrity check failed! The file has been tampered with.")
    else:
        print("File integrity check passed. The file is intact.")

def update_transactions(new_transaction):
    with open(CSV_FILE_PATH, 'a') as f:
        f.write(new_transaction + '\n')
    new_hash = compute_sha256(CSV_FILE_PATH)
    save_hash(new_hash, HASH_FILE_PATH)
    print("Transaction added and hash updated.")

if __name__ == "__main__":
    verify_file_integrity()
    # Example usage: update_transactions("2025-03-25,ItemX,100")
    update_transactions("2025-03-25,ItemX,100")
