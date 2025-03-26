import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Function to derive a secret key from a password using PBKDF2
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Function to encrypt email content
def encrypt_email_content(email_content: str, password: str, output_file: str):
    # Generate a random salt and IV
    salt = os.urandom(16)  # 16 bytes salt for key derivation
    iv = os.urandom(16)    # 16 bytes IV for AES encryption

    # Derive the AES key from the password
    key = derive_key(password, salt)

    # Create AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the email content to ensure it's a multiple of the block size (AES block size = 128 bits = 16 bytes)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(email_content.encode()) + padder.finalize()

    # Encrypt the data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Base64 encode the ciphertext, salt, and IV
    encrypted_data = {
        "salt": base64.b64encode(salt).decode('utf-8'),
        "iv": base64.b64encode(iv).decode('utf-8'),
        "ciphertext": base64.b64encode(ciphertext).decode('utf-8')
    }

    # Save the encrypted data to the output file
    with open(output_file, 'w') as f:
        f.write(str(encrypted_data))

    print(f"Email content encrypted and saved to {output_file}")

# Example usage
if __name__ == "__main__":
    email_content = input("Enter the email content: ")
    password = input("Enter the password (used to generate the encryption key): ")
    output_file = "encrypted_email.txt"
    
    encrypt_email_content(email_content, password, output_file)
