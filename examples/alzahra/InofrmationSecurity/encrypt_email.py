import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# File to store the encrypted content
ENCRYPTED_FILE_PATH = 'encrypted_email.txt'

def generate_key():
    """
    Generate a secure 32-byte key for AES-256 encryption.
    """
    return get_random_bytes(32)

def encrypt_email_content(email_content, key):
    """
    Encrypt the email content using AES-256 encryption and return the Base64-encoded ciphertext.
    """
    cipher = AES.new(key, AES.MODE_CBC)  # Use AES in CBC mode
    iv = cipher.iv  # Initialization vector
    ciphertext = cipher.encrypt(pad(email_content.encode('utf-8'), AES.block_size))  # Encrypt with padding
    return base64.b64encode(iv + ciphertext).decode('utf-8')  # Encode IV + ciphertext in Base64

def save_encrypted_content(encrypted_content, file_path):
    """
    Save the Base64-encoded ciphertext to a file.
    """
    with open(file_path, 'w') as f:
        f.write(encrypted_content)

def main():
    # Prompt the user for the email content
    email_content = input("Enter the email content to encrypt: ")

    # Generate or provide a secret key
    key = generate_key()
    print(f"Generated encryption key (keep this safe!): {base64.b64encode(key).decode('utf-8')}")

    # Encrypt the email content
    encrypted_content = encrypt_email_content(email_content, key)

    # Save the encrypted content to a file
    save_encrypted_content(encrypted_content, ENCRYPTED_FILE_PATH)
    print(f"Encrypted email content saved to {ENCRYPTED_FILE_PATH}")

if __name__ == "__main__":
    main()