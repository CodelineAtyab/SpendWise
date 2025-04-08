import hashlib
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Step 1: Compute SHA-256 Hash of the Email Content
def compute_sha256_hash(content: str) -> str:
    sha256_hash = hashlib.sha256()
    sha256_hash.update(content.encode('utf-8'))
    return sha256_hash.hexdigest()

# Step 2: Encrypt (Sign) the SHA-256 Hash Using the Private Key
def encrypt_hash_with_private_key(hash_value: str, private_key_path: str) -> str:
    with open(private_key_path, 'rb') as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())
    
    # Convert the hash string to bytes
    hash_bytes = hash_value.encode('utf-8')

    # Encrypt (sign) the hash using the private key
    encrypted_hash = private_key.sign(
        hash_bytes,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

    # Return the encrypted hash as a Base64 encoded string
    return base64.b64encode(encrypted_hash).decode('utf-8')

# Step 3: Save Email Content to a File
def save_email_content_to_file(content: str, filename: str):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Email content saved to {filename}")

# Step 4: Verify Email Content Integrity Using the Public Key
def verify_integrity(encrypted_hash: str, email_content: str, public_key_path: str) -> bool:
    # Load the public key
    with open(public_key_path, 'rb') as f:
        public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())

    # Recompute the SHA-256 hash of the email content
    recomputed_hash = compute_sha256_hash(email_content)
    hash_bytes = recomputed_hash.encode('utf-8')

    # Decode the encrypted hash from Base64
    encrypted_hash_bytes = base64.b64decode(encrypted_hash)

    try:
        # Decrypt the encrypted hash using the public key
        decrypted_hash = public_key.verify(
            encrypted_hash_bytes,
            hash_bytes,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        print("The email content has not been tampered with.")
        return True
    except Exception as e:
        print(f"Integrity check failed: {e}")
        return False

# Main function
def main():
    # Sample email content
    email_content = "This is a sample email content."

    # Save email content to a file
    save_email_content_to_file(email_content, "email_content.txt")

    # Compute SHA-256 hash of the email content
    email_hash = compute_sha256_hash(email_content)
    
    # Encrypt the hash using the private key
    private_key_path = "private_key.pem"  # Ensure the path is correct
    encrypted_hash = encrypt_hash_with_private_key(email_hash, private_key_path)

    # Save the encrypted hash to a file
    with open("encrypted_hash.txt", 'w') as f:
        f.write(encrypted_hash)
    print("Encrypted hash saved to encrypted_hash.txt")

    # Now let's verify the integrity (e.g., later)
    public_key_path = "public_key.pem"  # Ensure the path is correct
    is_intact = verify_integrity(encrypted_hash, email_content, public_key_path)

    if is_intact:
        print("The email content is intact.")
    else:
        print("The email content has been tampered with.")

if __name__ == "__main__":
    main()
