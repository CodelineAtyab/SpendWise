import hashlib
import os

TRANSACTIONS_FILE = 'transactions.csv'
HASH_FILE = 'transactions.hash'

def compute_sha256(file_path):
    """Compute the SHA-256 hash of the specified file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b''):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def save_hash(hash_value, hash_file):
    """Save the hash value to the specified hash file."""
    with open(hash_file, 'w') as f:
        f.write(hash_value)

def load_hash(hash_file):
    """Load the hash value from the specified hash file."""
    if not os.path.exists(hash_file):
        return None
    with open(hash_file, 'r') as f:
        return f.read().strip()

def verify_file_integrity():
    """Verify the integrity of the transactions file by comparing hashes."""
    if not os.path.exists(TRANSACTIONS_FILE):
        print("Transactions file does not exist. Skipping integrity check.")
        return

    current_hash = compute_sha256(TRANSACTIONS_FILE)
    saved_hash = load_hash(HASH_FILE)
    if saved_hash is None:
        print("No saved hash found. Saving current hash.")
        save_hash(current_hash, HASH_FILE)
    elif current_hash != saved_hash:
        print("File integrity check failed! The transactions file has been tampered with.")
    else:
        print("File integrity check passed. The transactions file is intact.")

def update_transactions(new_transaction):
    """Update the transactions file with a new transaction and save the new hash."""
    with open(TRANSACTIONS_FILE, 'a') as f:
        f.write(new_transaction + '\n')
    new_hash = compute_sha256(TRANSACTIONS_FILE)
    save_hash(new_hash, HASH_FILE)
    print("Transaction added and hash updated.")

if __name__ == "__main__":
    # Verify file integrity on startup
    verify_file_integrity()

    # Example usage: Add a new transaction
    new_transaction = "2025-03-25,Item A,10.00"
    update_transactions(new_transaction)

