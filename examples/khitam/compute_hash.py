import hashlib

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

# Test the functions with the transactions.csv and transactions_hash.txt
csv_file_path = "transactions.csv"
hash_file_path = "transactions_hash.txt"

# Call this function to check and update the hash if the CSV file was modified
update_hash_if_modified(csv_file_path, hash_file_path)

# Optionally, verify file integrity after updating the hash (if desired)
verify_file_integrity(csv_file_path, hash_file_path)
