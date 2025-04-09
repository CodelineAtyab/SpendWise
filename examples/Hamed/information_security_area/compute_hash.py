import os
import hashlib
import csv
from datetime import datetime

# ✅ Fixed file paths using raw strings to avoid escape sequence issues
TRANSACTIONS_FILE = r"C:\Users\codel\OneDrive\Desktop\git22\SpendWise\examples\Hamed\information_security_area\transactions.csv"
HASH_FILE = r"C:\Users\codel\OneDrive\Desktop\git22\SpendWise\examples\Hamed\information_security_area\transactions_hash.txt"

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
        hash_dir = os.path.dirname(HASH_FILE)
        if hash_dir and not os.path.exists(hash_dir):
            os.makedirs(hash_dir)
        
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
        # Ensure the CSV file exists with headers
        if not os.path.exists(TRANSACTIONS_FILE):
            with open(TRANSACTIONS_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Customer", "Transaction Type", "Amount"])

        # Append the new transaction
        with open(TRANSACTIONS_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([timestamp] + data)
        print("✅ Transaction added successfully.")

        # Update the hash
        new_hash = compute_sha256(TRANSACTIONS_FILE)
        if new_hash:
            save_hash(new_hash)

    except Exception as e:
        print(f"❌ Error writing transaction: {e}")

# ✅ Perform integrity check
verify_integrity()

# ✅ Add example transaction
new_transaction = ["Customer123", "Purchase", "50.00"]
update_csv_with_hash(new_transaction)
