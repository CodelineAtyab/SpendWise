import os
import sys
import hashlib
import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa  # Added rsa
from cryptography.hazmat.backends import default_backend
from pathlib import Path

EMAIL_FILE = 'email.txt'
HASH_FILE = 'email_hash.sig'
PRIVATE_KEY_FILE = 'private_key.pem'
PUBLIC_KEY_FILE = 'public_key.pem'

def save_email(content: str):
    with open(EMAIL_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"$ Email saved to {EMAIL_FILE}")

def hash_email_content() -> bytes:
    with open(EMAIL_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    sha256_hash = hashlib.sha256(content.encode()).digest()
    return sha256_hash

def generate_rsa_key_pair():
    # Generate a new 2048-bit RSA key pair.
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    
    # Save the private key.
    with open(PRIVATE_KEY_FILE, 'wb') as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))
    
    # Save the public key.
    with open(PUBLIC_KEY_FILE, 'wb') as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    print("$ RSA key pair generated and saved.")

def load_private_key():
    with open(PRIVATE_KEY_FILE, 'rb') as f:
        return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

def load_public_key():
    with open(PUBLIC_KEY_FILE, 'rb') as f:
        return serialization.load_pem_public_key(f.read(), backend=default_backend())

def sign_hash():
    # If keys don't exist, generate them.
    if not os.path.exists(PRIVATE_KEY_FILE) or not os.path.exists(PUBLIC_KEY_FILE):
        print("RSA keys not found, generating new keys...")
        generate_rsa_key_pair()
    private_key = load_private_key()
    hash_digest = hash_email_content()
    signature = private_key.sign(
        hash_digest,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    with open(HASH_FILE, 'wb') as f:
        f.write(base64.b64encode(signature))
    print(f"$ Hash signed and saved to {HASH_FILE}")

def verify_integrity():
    public_key = load_public_key()
    current_hash = hash_email_content()
    with open(HASH_FILE, 'rb') as f:
        signature = base64.b64decode(f.read())
    try:
        public_key.verify(
            signature,
            current_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Email integrity verified. No changes detected.")
    except Exception as e:
        print("WARNING: Email content has been altered or signature is invalid!")

# Example usage
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python Encrypt_Email_2.py [save|sign|verify]")
        sys.exit(1)
    command = sys.argv[1].lower()
    if command == 'save':
        email_text = input("Enter your email content:\n")
        save_email(email_text)
    elif command == 'sign':
        sign_hash()
    elif command == 'verify':
        verify_integrity()
    else:
        print("Invalid command. Use: python Encrypt_Email_2.py save | sign | verify")