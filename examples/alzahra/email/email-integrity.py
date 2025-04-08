import os
import base64
import hashlib
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

# File paths
EMAIL_FILE_PATH = 'email_content.txt'
HASH_FILE_PATH = 'encrypted_hash.txt'
PRIVATE_KEY_PATH = 'private_key.pem'
PUBLIC_KEY_PATH = 'public_key.pem'

def save_email_content(email_content):
    """
    Save the email content to a plain text file.
    """
    with open(EMAIL_FILE_PATH, 'w') as f:
        f.write(email_content)
    print(f"Email content saved to {EMAIL_FILE_PATH}")

def compute_sha256_hash(content):
    """
    Compute the SHA-256 hash of the given content.
    """
    sha256_hash = hashlib.sha256(content.encode('utf-8')).digest()
    return sha256_hash

def encrypt_hash_with_private_key(hash_value, private_key_path):
    """
    Encrypt the SHA-256 hash using the private key.
    """
    with open(private_key_path, 'rb') as key_file:
        private_key = load_pem_private_key(key_file.read(), password=None)
    encrypted_hash = private_key.sign(
        hash_value,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return base64.b64encode(encrypted_hash).decode('utf-8')

def save_encrypted_hash(encrypted_hash):
    """
    Save the encrypted hash to a file.
    """
    with open(HASH_FILE_PATH, 'w') as f:
        f.write(encrypted_hash)
    print(f"Encrypted hash saved to {HASH_FILE_PATH}")

def verify_email_integrity(public_key_path):
    """
    Verify the integrity of the email content by decrypting the hash and comparing it.
    """
    # Load the email content
    with open(EMAIL_FILE_PATH, 'r') as f:
        email_content = f.read()

    # Compute the current hash of the email content
    current_hash = compute_sha256_hash(email_content)

    # Load the encrypted hash
    with open(HASH_FILE_PATH, 'r') as f:
        encrypted_hash = base64.b64decode(f.read())

    # Load the public key
    with open(public_key_path, 'rb') as key_file:
        public_key = load_pem_public_key(key_file.read())

    # Decrypt the hash using the public key
    try:
        public_key.verify(
            encrypted_hash,
            current_hash,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        print("Email integrity verified: The content has not been altered.")
    except Exception as e:
        print("Email integrity check failed: The content has been altered.")

def main():
    # Prompt the user for email content
    email_content = input("Enter the email content: ")

    # Save the email content to a file
    save_email_content(email_content)

    # Compute the SHA-256 hash of the email content
    hash_value = compute_sha256_hash(email_content)

    # Encrypt the hash using the private key
    encrypted_hash = encrypt_hash_with_private_key(hash_value, PRIVATE_KEY_PATH)

    # Save the encrypted hash to a file
    save_encrypted_hash(encrypted_hash)

    # Verify the integrity of the email content
    verify_email_integrity(PUBLIC_KEY_PATH)

if __name__ == "__main__":
    main()