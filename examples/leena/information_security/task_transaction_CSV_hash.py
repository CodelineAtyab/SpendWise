import os        # 1
import hashlib   # 2

TRANSACTIONS_FILE = 'transactions.csv'  # 3
HASH_FILE = 'transactions.csv.hash'     # 4

def compute_file_hash(file_path):         # 5
    """Compute the SHA-256 hash of a file."""  
    sha256 = hashlib.sha256()             # 6
    try:                                  # 7
        with open(file_path, 'rb') as f:   # 8
            for chunk in iter(lambda: f.read(4096), b""):  # 9
                sha256.update(chunk)      # 10
    except FileNotFoundError:             # 11
        print(f"Transactions file '{file_path}' not found.")  # 12
        return None                     # 13
    return sha256.hexdigest()             # 14

def save_hash(hash_value, file_path):     # 15
    """Save the computed hash to a file (overwrites previous value)."""
    with open(file_path, 'w') as f:       # 16
        f.write(hash_value)               # 17

def verify_file_integrity():              # 18
    """Compare the current hash of the transactions file to the saved hash."""
    current_hash = compute_file_hash(TRANSACTIONS_FILE)  # 19
    if current_hash is None:              # 20
        return                          # 21
    if os.path.exists(HASH_FILE):         # 22
        with open(HASH_FILE, 'r') as f:   # 23
            saved_hash = f.read().strip() # 24
        if current_hash != saved_hash:    # 25
            print("Alert: The transactions CSV file has been tampered with!")  # 26
        else:                             # 27
            print("File integrity verified.")  # 28
    else:                                 # 29
        print("No hash file found. Creating a new hash file.")  # 30
        save_hash(current_hash, HASH_FILE)  # 31

def add_transaction(transaction_data):    # 32
    """Append a new transaction to the CSV and update the hash file."""
    with open(TRANSACTIONS_FILE, 'a') as f:  # 33
        f.write(transaction_data + '\n')   # 34
    new_hash = compute_file_hash(TRANSACTIONS_FILE)  # 35
    if new_hash:                          # 36
        save_hash(new_hash, HASH_FILE)    # 37
        print("Transaction added and hash updated.")  # 38

if __name__ == '__main__':                # 39
    # On startup, verify the CSV file's integrity.
    verify_file_integrity()               # 40
    
    # Example usage: Uncomment to add a transaction.
    # add_transaction("2025-03-26,Sale,100.00")  # 41


