import hashlib
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os
from cryptography.hazmat.primitives import hashes  # Ensure this import is present

# Function to save email content to a file
def save_email_content(email_content, email_file):
    """Save email content to a plain text file."""
    with open(email_file, "w") as file:
        file.write(email_content)

# Function to compute SHA-256 hash of the email content
def compute_sha256_hash(email_content):
    """Compute the SHA-256 hash of the email content."""
    return hashlib.sha256(email_content.encode()).digest()

# Function to encrypt the hash using AES-256
def encrypt_hash(hash_value, aes_key):
    """Encrypt the SHA-256 hash using AES-256."""
    iv = os.urandom(16)  # Generate a random initialization vector (IV)
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_hash = encryptor.update(hash_value) + encryptor.finalize()
    return base64.b64encode(iv + encrypted_hash).decode()  # Combine IV and encrypted hash

# Function to save the encrypted hash to a file
def save_encrypted_hash(encrypted_hash, hash_file):
    """Save the encrypted hash to a file."""
    with open(hash_file, "w") as file:
        file.write(encrypted_hash)

# Function to verify the integrity of the email content
def verify_email_integrity(email_file, hash_file, aes_key):
    """Verify the integrity of the email content."""
    # Load email content
    with open(email_file, "r") as file:
        email_content = file.read()

    # Compute the current hash
    current_hash = compute_sha256_hash(email_content)

    # Load the encrypted hash
    with open(hash_file, "r") as file:
        encrypted_data = base64.b64decode(file.read())

    # Extract IV and encrypted hash
    iv = encrypted_data[:16]
    encrypted_hash = encrypted_data[16:]

    # Decrypt the hash
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_hash = decryptor.update(encrypted_hash) + decryptor.finalize()

    # Compare the hashes
    if current_hash == decrypted_hash:
        print("Integrity verified: The email content has not been altered.")
    else:
        print("Integrity check failed: The email content has been altered.")

# Example usage
if __name__ == "__main__":
    # User inputs the email content
    email_content = input("Enter the email content: ")

    # File paths
    email_file = "email.txt"
    hash_file = "email_hash.txt"

    # AES key (must be 32 bytes for AES-256)
    password = input("Enter a password to generate the AES key: ").encode()
    salt = os.urandom(16)  # Generate a random salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),  # Corrected here
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    aes_key = kdf.derive(password)

    # Save email content
    save_email_content(email_content, email_file)

    # Compute and encrypt hash
    hash_value = compute_sha256_hash(email_content)
    encrypted_hash = encrypt_hash(hash_value, aes_key)

    # Save encrypted hash
    save_encrypted_hash(encrypted_hash, hash_file)

    # Verify integrity
    verify_email_integrity(email_file, hash_file, aes_key)