# module imports
import os        
import hashlib   

# Defines the file paths
TRANSACTIONS_FILE = 'transactions.csv'  
HASH_FILE = 'transactions.csv.hash'     


# Function for computing the hash of a file
def compute_file_hash(file_path, chunk_size=8192):         
    transactions_sha256 = hashlib.sha256()             # Creates a new SHA‑256 hash object
    # Reads the file and updates the hash
    try:                                  
        with open(file_path, 'rb') as file:   
            while chunk := file.read(chunk_size):
                transactions_sha256.update(chunk)
        return transactions_sha256.hexdigest()   
    # Handles file not found error  
    except FileNotFoundError:             
        print(f"Transactions file '{file_path}' not found.")  
        return None                     
    return sha256.hexdigest()     

# Function for saving the hash to a file
def save_hash(hash_value, file_path):  
    with open(file_path, 'w') as f:       
        f.write(hash_value)               

# Function for verifying the file integrity
def verify_file_integrity():              
    # Computes the hash of the transactions file
    current_hash = compute_file_hash(TRANSACTIONS_FILE)  
    if current_hash is None:              
        return                          
    if os.path.exists(HASH_FILE):         
        with open(HASH_FILE, 'r') as f:   
            saved_hash = f.read().strip() 
        if current_hash != saved_hash:  
            # Prints an alert if the hashes do not match  
            print("Warning: The transactions file may have been modified!")  
        else:   
            # Prints a success message if the hashes match
            print("The transactions file is secure and unchanged.")
    else:
        # Prints a message if the hash file is not found                                 
        print("No hash file found. Creating a new hash file.") 
        save_hash(current_hash, HASH_FILE)  

# Function for adding a transaction
def add_transaction(transaction_data):   
    # Appends the transaction data to the transactions file
    with open(TRANSACTIONS_FILE, 'a') as f:
        f.write(transaction_data + '\n') 
    new_hash = compute_file_hash(TRANSACTIONS_FILE)
    # Updates the hash if the transaction is added successfully
    if new_hash:                          
        save_hash(new_hash, HASH_FILE) 
        print("Transaction added and hash updated.")

if __name__ == '__main__':               
    verify_file_integrity()      
    # add_transaction("2025-03-26,Sale,100.00") 
    # add_transaction("2025-03-27,Purchase,50.00")
    # add_transaction("2025-03-28,Refund,25.00")
    # add_transaction("2025-03-29,Sale,200.00")
    # add_transaction("2025-03-30,Purchase,75.00")


