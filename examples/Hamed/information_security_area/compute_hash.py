import os
import hashlib
import csv
from datetime import datetime

TRANSACTIONS_FILE = "transactions.csv"  # file path 
HASH_FILE = "transactions_hash.txt"  # file path

def compute_sha256(file_path, chunk_size=8192):
    if not os.path.exists(file_path):
        print(f"⚠️ File not found: {file_path}")
        return None
    
    hash_obj = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(chunk_size):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def save_hash(hash_value):
    try:
        # Check if the file path for the hash file includes a directory, and create it if necessary
        hash_dir = os.path.dirname(HASH_FILE)
        if hash_dir and not os.path.exists(hash_dir):
            os.makedirs(hash_dir)
        
        # Write the hash value to the file
        with open(HASH_FILE, "w") as file:
            file.write(hash_value)
        print(f"✅ Hash saved to {HASH_FILE}.")
    except Exception as e:
        print(f"❌ Error saving hash: {e}")

def load_saved_hash():
    if not os.path.exists(HASH_FILE):
        print("ℹ️ No previous hash found. Integrity check will be skipped.")
        return None
    
    try:
        with open(HASH_FILE, "r") as file:
            return file.read().strip()
    except Exception as e:
        print(f"❌ Error loading previous hash: {e}")
        return None

def verify_integrity():
    previous_hash = load_saved_hash()
    current_hash = compute_sha256(TRANSACTIONS_FILE)

    if previous_hash and current_hash:
        if previous_hash == current_hash:
            print("✅ File integrity verified: No unauthorized changes detected.")
        else:
            print("⚠️ WARNING: File integrity check failed! Possible unauthorized modifications.")
    elif not previous_hash:
        print("⚠️ No previous hash found. Integrity check skipped.")

def update_csv_with_hash(data):
    try:
        # Ensure the CSV file exists with headers if it's a new file
        if not os.path.exists(TRANSACTIONS_FILE):
            with open(TRANSACTIONS_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Customer", "Transaction Type", "Amount"])  # Add headers

        # Append the new transaction to the CSV
        with open(TRANSACTIONS_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([timestamp] + data)
        print("✅ Transaction added successfully.")

        # Compute and save the new hash after modifying the CSV
        new_hash = compute_sha256(TRANSACTIONS_FILE)
        if new_hash:
            save_hash(new_hash)

    except Exception as e:
        print(f"❌ Error writing transaction: {e}")

# ✅ Perform integrity check on startup
verify_integrity()

# ✅ Example: Adding a new transaction
new_transaction = ["Customer123", "Purchase", "50.00"]
update_csv_with_hash(new_transaction)
