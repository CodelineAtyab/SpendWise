import re
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import os

# Regular expression for basic email format validation (generalized for more domains)
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def generate_key():
    # Generate a random 256-bit (32-byte) secret key for AES-256
    return os.urandom(32)

def encrypt_email_content(email_content, key):
    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16)
    
    # Create an AES cipher object with the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Pad the email content to be multiple of block size (16 bytes for AES)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(email_content.encode()) + padder.finalize()
    
    # Encrypt the padded email content
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return iv + ciphertext  

def save_encrypted_content(filename, encrypted_content):
    try:
        # Encode the encrypted 
        encoded_content = base64.b64encode(encrypted_content)
        
        # Save the Base64 encoded content to a file
        with open(filename, 'wb') as file:
            file.write(encoded_content)
        print(f"Encrypted content saved to {filename}")
    
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def validate_email(email):
    # Validate email format using regex
    if re.match(EMAIL_REGEX, email):
        return True
    else:
        print("Invalid email format. Please ensure the email contains '@' and '.' (e.g., user@domain.com).")
        return False

def get_valid_secret_key():
    while True:
        # Prompt for the secret key
        secret_key = input("Enter a 32-byte secret key (or press Enter to generate a new one): ")

        if not secret_key:
            # Generate a new secret key if not provided
            secret_key = generate_key()
            print(f"Generated secret key: {base64.b64encode(secret_key).decode()}")  # Print base64 encoded key for reference
            return secret_key
        
        # Ensure the provided key is exactly 32 bytes
        secret_key = secret_key.encode()
        if len(secret_key) == 32:
            return secret_key
        else:
            print("The key must be exactly 32 bytes. Please try again.")

def main():
    
    email_content = input("Enter the email content to encrypt: ")
    
    email_address = input("Enter the email address to validate: ")

    # Validate email 
    if not validate_email(email_address):
        return
    
    secret_key = get_valid_secret_key()

    encrypted_content = encrypt_email_content(email_content, secret_key)
    
    # file path f
    file_path = r"C:\Users\codel\OneDrive\Desktop\git22\SpendWise\examples\Hamed\encrypted_email.txt"
    
    # Save the encrypted 
    save_encrypted_content(file_path, encrypted_content)

if __name__ == "__main__":
    main()
