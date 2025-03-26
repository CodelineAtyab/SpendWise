import os
import hashlib

def compute_sha256(file_path, chunk_size=8192):
    """Compute SHA-256 hash of a file by reading it in chunks."""
    try:
        hash_obj = hashlib.sha256()
        with open(file_path, 'rb') as file:
            while chunk := file.read(chunk_size):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error computing SHA-256 hash: {e}")
    return None

def save_hash_to_file(hash_value, hash_file_path):
    """Save the computed hash value to a file."""
    with open(hash_file_path, 'w') as f:
        f.write(hash_value)
        print(f"Hash saved to {hash_file_path}")

def verify_file_integrity(csv_file_path, hash_file_path):
    """Verify the integrity of the CSV file by comparing hashes."""
    current_hash = compute_sha256(csv_file_path)
    
    # Check if current hash matches the saved hash
    if current_hash is None:
        print("Failed to compute hash for the CSV file.")
        return
    
    # Check if the hash file exists and read the saved hash
    if os.path.exists(hash_file_path):
        with open(hash_file_path, 'r') as f:
            saved_hash = f.read().strip()
        
        if current_hash == saved_hash:
            print("File integrity is intact. No tampering detected.")
        else:
            print("Alert: File integrity compromised! Hash mismatch detected.")
    else:
        print("Hash file not found. This might be the first time the application is running.")

def update_transaction(csv_file_path, transaction_data, hash_file_path):
    """Simulate adding a transaction and updating the hash."""
    # Append the new transaction to the CSV file
    with open(csv_file_path, 'a') as file:
        file.write(transaction_data + "\n")
    print(f"Appended transaction: {transaction_data}")
    
    # Compute the new SHA-256 hash
    new_hash = compute_sha256(csv_file_path)
    print(f"New computed hash: {new_hash}")
    
    if new_hash:
        save_hash_to_file(new_hash, hash_file_path)
    else:
        print("Failed to update hash after transactions update.")

def main():
    # Paths
    csv_file_path = "transactions.csv"
    hash_file_path = "transactions_hash.txt"

    # Example of adding a new transaction
    new_transaction = "2025-03-26,  ,bed, A  56.8"  # Example transaction data
    update_transaction(csv_file_path, new_transaction, hash_file_path)

    # On app startup, verify file integrity
    verify_file_integrity(csv_file_path, hash_file_path)

if __name__ == "__main__":
    main()

