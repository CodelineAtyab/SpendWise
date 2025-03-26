import hashlib
import os

def compute_sha256(file_path):
    """Compute the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:  # Open the file in binary mode
        # Read the file in chunks to avoid memory overload with large files
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)  # Update the hash with the file's data
    return sha256_hash.hexdigest()  # Return the computed hash as a hexadecimal string

def save_hash_to_file(hash_value, hash_file_path):
    """Save the computed hash value to a file."""
    with open(hash_file_path, "w") as f:
        f.write(hash_value)  # Write the hash to the file
    print(f"Hash saved to {hash_file_path}")

def verify_file_integrity(csv_file_path, hash_file_path):
    """Verify the integrity of the CSV file by comparing the computed hash with the saved hash."""
    # Compute the current hash of the CSV file
    current_hash = compute_sha256(csv_file_path)

    # Read the saved hash from the hash file
    try:
        with open(hash_file_path, "r") as f:
            saved_hash = f.read().strip()  # Remove any extra spaces/newlines
    except FileNotFoundError:
        print(f"Error: {hash_file_path} not found. Integrity check cannot be performed.")
        return

    # Compare the computed hash with the saved hash
    if current_hash == saved_hash:
        print("File integrity verified: The CSV file is unchanged.")
    else:
        print("Warning: File integrity compromised! The CSV file has been tampered with.")

def update_hash_if_modified(csv_file_path, hash_file_path):
    """Check if the CSV file has been modified and update the hash if necessary."""
    # First, check if the hash file exists
    try:
        with open(hash_file_path, "r") as f:
            saved_hash = f.read().strip()  # Read the current saved hash
    except FileNotFoundError:
        saved_hash = None  # If hash file doesn't exist, there's no previous hash

    # Compute the current hash of the CSV file
    current_hash = compute_sha256(csv_file_path)

    # If the hash file doesn't exist or the hash has changed, update it
    if saved_hash is None or current_hash != saved_hash:
        save_hash_to_file(current_hash, hash_file_path)  # Save the new hash
    else:
        print("No changes detected in the CSV file. Hash remains the same.")

def add_transaction(csv_file_path, transaction_data):
    """Add a new transaction to the CSV file."""
    with open(csv_file_path, 'a') as f:
        f.write(transaction_data + '\n')
    print("Transaction added.")

def main():
    # Paths to the CSV and hash files
    csv_file_path = "transactions.csv"
    hash_file_path = "transactions_hash.txt"

    # Check file integrity on startup
    print("Verifying file integrity on startup...")
    verify_file_integrity(csv_file_path, hash_file_path)

    # Simulate adding a new transaction (You can replace this with actual user input or transaction handling)
    new_transaction = "5,2025-03-05,250.00,Purchase at Store E"  # Example new transaction data
    add_transaction(csv_file_path, new_transaction)

    # After modifying the CSV, update the hash
    update_hash_if_modified(csv_file_path, hash_file_path)

    # Optionally, verify file integrity after modification (this is not necessary in the main loop, but for testing)
    print("\nVerifying file integrity after modification...")
    verify_file_integrity(csv_file_path, hash_file_path)

if __name__ == "__main__":
    main()
