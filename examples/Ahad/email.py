import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os

# a pip installation done "pycryptodome"

def generate_key():
    return get_random_bytes(32)  # Generates a 32-byte AES key

def encrypt_email_content(email_content, key):
    iv = get_random_bytes(16)  # AES block size is 16 bytes
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_bytes = cipher.encrypt(pad(email_content.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_bytes).decode()

def save_encrypted_content(filename, encrypted_content):
    # Save the encrypted content to the file
    with open(filename, 'w') as file:
        file.write(encrypted_content)

    # Save the hash of the encrypted content to ensure integrity
    hash_value = hashlib.sha256(encrypted_content.encode()).hexdigest()
    with open(filename + '.hash', 'w') as hash_file:
        hash_file.write(hash_value)

def verify_integrity(filename):
    # Verify if the file exists
    if not os.path.exists(filename):
        print(f"Error: {filename} does not exist.")
        return False

    # Read the encrypted content from the file
    with open(filename, 'r') as file:
        encrypted_content = file.read()

    # Read the saved hash from the .hash file
    hash_filename = filename + '.hash'
    if not os.path.exists(hash_filename):
        print(f"Error: {hash_filename} does not exist.")
        return False

    with open(hash_filename, 'r') as hash_file:
        saved_hash = hash_file.read().strip()

    # Calculate the current hash of the encrypted content
    current_hash = hashlib.sha256(encrypted_content.encode()).hexdigest()

    # Compare hashes
    if current_hash == saved_hash:
        print("Content integrity verified successfully.")
        return True
    else:
        print("Warning: The content has been tampered with!")
        return False

def main():
    email_content = input("Enter the email content: ")
    use_existing_key = input("Do you have an existing key? (yes/no): ").strip().lower()

    if use_existing_key == 'yes':
        key_input = input("Enter the 32-byte key (base64 encoded): ")
        key = base64.b64decode(key_input)

        if len(key) != 32:
            print("Invalid key length! The key must be 32 bytes.")
            return
    else:
        key = generate_key()
        print("Generated key (save this for decryption):", base64.b64encode(key).decode())

    encrypted_content = encrypt_email_content(email_content, key)
    save_encrypted_content("encrypted_email.txt", encrypted_content)
    print("Encryption successful! The encrypted content is saved")

    # Verify the integrity after saving
    print("\nVerifying file integrity...")
    if verify_integrity("encrypted_email.txt"):
        print("The encrypted content is intact and hasn't been tampered with.")
    else:
        print("Content integrity verification failed!")

if __name__ == "__main__":
    main()