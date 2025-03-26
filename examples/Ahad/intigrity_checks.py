import hashlib
import os
import csv

csv_file = "T_Hask.csv"  
hash_file = "hash.text"

# Compute SHA-256 hash of the file
def compute_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            byte_block = f.read(4096)  
            if not byte_block:
                break
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Save hash to file
def save_hash(hash_value):
    with open(hash_file, 'w') as f:
        f.write(hash_value)

# Load the saved hash from hash.text
def load_saved_hash():
    if os.path.exists(hash_file):
        with open(hash_file, 'r') as f:
            return f.read().strip()
    return None

# Check file integrity
def check_file_integrity():
    if not os.path.exists(csv_file):
        print(f" Error: {csv_file} does not exist. Creating a new file...")
        create_csv_file()
        return
    
    current_hash = compute_sha256(csv_file)
    saved_hash = load_saved_hash()
    
    if saved_hash is None:
        print(" No previous hash found. Saving initial hash...")
        save_hash(current_hash)
    elif saved_hash != current_hash:
        print("  Alert: File integrity compromised! The CSV file has been tampered with.")
    else:
        print(" File integrity verified successfully.")

# Function to create a CSV file if it doesn't exist
def create_csv_file():
    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Transaction_ID", "Amount", "Description"])  # Adding header
        print(f" Created {csv_file} with headers.")

# Function to add a new transaction
def modify_transaction():
    # Ask user for transaction details
    date = input("Enter transaction date (YYYY-MM-DD): ")
    transaction_id = input("Enter transaction ID: ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    new_transaction = [date, transaction_id, amount, description]

    # Check if the CSV file exists, create it if not
    create_csv_file()

    # Append the new transaction to the CSV file
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_transaction)

    # Compute and update the new hash
    new_hash = compute_sha256(csv_file)
    save_hash(new_hash)
    
    print(" Transaction added and hash updated.")


print("\n Checking file integrity on startup...")
check_file_integrity()

print("\n Adding a new transaction...")
modify_transaction()

print("\n Checking file integrity after modification...")
check_file_integrity()


























pvt_massage = "This is a private message" 
hashlib.sha256(pvt_massage.encode("utf-8"))
hashobject=hashlib.sha256(pvt_massage.encode("utf-8"))
hashoutput=hashobject.hexdigest()
print(hashoutput)

