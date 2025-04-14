import hashlib
import base64
import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Step 1: Compute SHA-256 Hash of the Email Content
def compute_sha256_hash(content: str) -> bytes:
    sha256_hash = hashlib.sha256()
    sha256_hash.update(content.encode('utf-8'))
    return sha256_hash.digest()

# Step 2: Encrypt (Sign) the SHA-256 Hash Using the Private Key
def sign_hash_with_private_key(hash_value: bytes, private_key_path: str) -> str:
    with open(private_key_path, 'rb') as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

    encrypted_hash = private_key.sign(
        hash_value,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return base64.b64encode(encrypted_hash).decode('utf-8')

# Step 3: Encrypt the Hash Using AES-256
def encrypt_hash_with_aes(hash_value: bytes, aes_key: bytes) -> str:
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_hash = encryptor.update(hash_value) + encryptor.finalize()
    return base64.b64encode(iv + encrypted_hash).decode()

# Save email content to a file
def save_email_content_to_file(content: str, filename: str):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Email content saved to {filename}")

# Verify integrity using RSA public key
def verify_signature(encrypted_hash: str, email_content: str, public_key_path: str) -> bool:
    with open(public_key_path, 'rb') as f:
        public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())

    hash_value = compute_sha256_hash(email_content)
    encrypted_hash_bytes = base64.b64decode(encrypted_hash)

    try:
        public_key.verify(
            encrypted_hash_bytes,
            hash_value,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        print("RSA: Signature verified. The email content is authentic.")
        return True
    except Exception as e:
        print(f"RSA: Signature verification failed: {e}")
        return False

# Verify integrity using AES
def verify_aes_integrity(email_content: str, encrypted_hash_b64: str, aes_key: bytes) -> bool:
    hash_value = compute_sha256_hash(email_content)
    encrypted_data = base64.b64decode(encrypted_hash_b64)
    iv = encrypted_data[:16]
    encrypted_hash = encrypted_data[16:]

    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_hash = decryptor.update(encrypted_hash) + decryptor.finalize()

    if decrypted_hash == hash_value:
        print("AES: Integrity verified. The email content has not been altered.")
        return True
    else:
        print("AES: Integrity check failed. The email content has been altered.")
        return False

# Main function
def main():
    # Input
    email_content = input("Enter the email content: ")
    password = input("Enter a password to derive AES key: ").encode()

    # File paths
    email_file = "email_content.txt"
    rsa_encrypted_hash_file = "rsa_encrypted_hash.txt"
    aes_encrypted_hash_file = "aes_encrypted_hash.txt"

    # Save email content
    save_email_content_to_file(email_content, email_file)

    # Compute SHA-256 hash
    hash_value = compute_sha256_hash(email_content)

    # Derive AES-256 key from password
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    aes_key = kdf.derive(password)

    # Encrypt hash with AES and save
    aes_encrypted_hash = encrypt_hash_with_aes(hash_value, aes_key)
    with open(aes_encrypted_hash_file, 'w') as f:
        f.write(base64.b64encode(salt).decode() + ":" + aes_encrypted_hash)
    print("AES-encrypted hash saved to aes_encrypted_hash.txt")

    # Sign hash with RSA and save
    private_key_path = "private_key.pem"
    rsa_signature = sign_hash_with_private_key(hash_value, private_key_path)
    with open(rsa_encrypted_hash_file, 'w') as f:
        f.write(rsa_signature)
    print("RSA signature saved to rsa_encrypted_hash.txt")

    # === Verification ===
    # AES Verification
    with open(aes_encrypted_hash_file, 'r') as f:
        salt_b64, aes_encrypted = f.read().split(":")
        derived_key = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=base64.b64decode(salt_b64),
            iterations=100000,
            backend=default_backend()
        ).derive(password)
        verify_aes_integrity(email_content, aes_encrypted, derived_key)

    # RSA Verification
    public_key_path = "public_key.pem"
    verify_signature(rsa_signature, email_content, public_key_path)

if __name__ == "__main__":
    main()
