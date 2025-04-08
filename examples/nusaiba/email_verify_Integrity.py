import os
import base64
import hashlib
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.backends import default_backend

EMAIL_FILE = 'email.txt'
HASH_FILE = 'email.hash'

def save_email_content(email_content):
    """Save email content to a plain text file."""
    with open(EMAIL_FILE, 'w') as f:
        f.write(email_content)
    print(f"Email content saved to {EMAIL_FILE}.")

def compute_sha256(content):
    """Compute the SHA-256 hash of the given content."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(content.encode('utf-8'))
    return sha256_hash.digest()

def encrypt_hash_with_private_key(hash_value, private_key_path):
    """Encrypt the SHA-256 hash using the private key."""
    with open(private_key_path, 'rb') as key_file:
        private_key = load_pem_private_key(key_file.read(), password=None, backend=default_backend())
    encrypted_hash = private_key.sign(
        hash_value,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return base64.b64encode(encrypted_hash).decode('utf-8')

def save_encrypted_hash(encrypted_hash):
    """Save the encrypted hash to a file."""
    with open(HASH_FILE, 'w') as f:
        f.write(encrypted_hash)
    print(f"Encrypted hash saved to {HASH_FILE}.")

def verify_email_integrity(public_key_path):
    """Verify the integrity of the email content."""
    if not os.path.exists(EMAIL_FILE) or not os.path.exists(HASH_FILE):
        print("Email file or hash file is missing.")
        return

    # Load email content
    with open(EMAIL_FILE, 'r') as f:
        email_content = f.read()

    # Compute the current hash
    current_hash = compute_sha256(email_content)

    # Load the encrypted hash
    with open(HASH_FILE, 'r') as f:
        encrypted_hash = base64.b64decode(f.read())

    # Load the public key
    with open(public_key_path, 'rb') as key_file:
        public_key = load_pem_public_key(key_file.read(), backend=default_backend())

    # Verify the hash
    try:
        public_key.verify(
            encrypted_hash,
            current_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Email integrity verified. No changes detected.")
    except Exception as e:
        print("Email integrity verification failed! The email content has been altered.")
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    private_key_path = 'private_key.pem'  # Path to your private key
    public_key_path = 'public_key.pem'   # Path to your public key

    # Prompt the user to enter email content
    email_content = input("Enter the email content:\n")

    # Save email content
    save_email_content(email_content)

    # Compute hash and encrypt it with the private key
    email_hash = compute_sha256(email_content)
    encrypted_hash = encrypt_hash_with_private_key(email_hash, private_key_path)
    save_encrypted_hash(encrypted_hash)

    # Verify email integrity
    verify_email_integrity(public_key_path)

