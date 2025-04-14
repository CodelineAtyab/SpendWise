import re
import os
import base64
from cryptography.hazmat.primitives import hashes, padding, serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding

# Email format validation regex
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def generate_key():
    return os.urandom(32)  # AES-256 requires a 32-byte key

def encrypt_email_content(email_content, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(email_content.encode()) + padder.finalize()

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return iv + ciphertext

def save_encrypted_content(filename, encrypted_content):
    try:
        encoded_content = base64.b64encode(encrypted_content)
        with open(filename, 'wb') as file:
            file.write(encoded_content)
        print(f"✅ Email content encrypted and saved to: {filename}")
    except Exception as e:
        print(f"❌ Error saving encrypted content: {e}")

def validate_email(email):
    if re.match(EMAIL_REGEX, email):
        return True
    print("❌ Invalid email format. Please enter a valid email like user@domain.com.")
    return False

def get_valid_secret_key():
    while True:
        secret_key = input("3. Enter a 32-byte secret key (or press Enter to generate a new one): ")

        if not secret_key:
            secret_key = generate_key()
            print(f"Generated secret key: {base64.b64encode(secret_key).decode()}")
            return secret_key

        secret_key = secret_key.encode()
        if len(secret_key) == 32:
            return secret_key
        print("❌ The key must be exactly 32 bytes. Please try again.")

def sign_hash_with_private_key(private_key, hash_bytes):
    return private_key.sign(
        hash_bytes,
        asymmetric_padding.PKCS1v15(),
        hashes.SHA256()
    )

def save_signature_to_file(filename, signature):
    try:
        with open(filename, 'wb') as file:
            file.write(signature)
        print(f"✅ Signature saved to: {filename}")
    except Exception as e:
        print(f"❌ Error saving signature: {e}")

def save_hash_to_file(filename, hash_bytes):
    try:
        # Write the hash to a file in hexadecimal format for readability
        with open(filename, 'w') as file:
            file.write(hash_bytes.hex())
        print(f"✅ Hash saved to: {filename}")
    except Exception as e:
        print(f"❌ Error saving hash: {e}")

def verify_signature_with_public_key(public_key, hash_bytes, signature):
    try:
        public_key.verify(
            signature,
            hash_bytes,
            asymmetric_padding.PKCS1v15(),
            hashes.SHA256()
        )
        print("✅ Signature verification successful. Content integrity is intact.")
    except Exception as e:
        print(f"❌ Signature verification failed: {e}")

def main():
    print("================================")
    print("**** Secure Email Encryption ****")
    print("================================")

    email_content = input("1. Enter the email content to encrypt: ")
    email_address = input("2. Enter the email address to validate: ")

    if not validate_email(email_address):
        return

    secret_key = get_valid_secret_key()
    encrypted_content = encrypt_email_content(email_content, secret_key)

    encrypted_file_path = r"C:\Users\codel\OneDrive\Desktop\git22\SpendWise\examples\Hamed\Encrypted Email Hash\Encrypted_email.txt"
    save_encrypted_content(encrypted_file_path, encrypted_content)

    # Compute SHA-256 hash of the email content
    hasher = hashes.Hash(hashes.SHA256(), backend=default_backend())
    hasher.update(email_content.encode())
    hash_bytes = hasher.finalize()

    # Save the hash to a file (in hexadecimal format)
    hash_file_path = r"C:\Users\codel\OneDrive\Desktop\git22\SpendWise\examples\Hamed\Encrypted Email Hash\email_hash.txt"
    save_hash_to_file(hash_file_path, hash_bytes)

    # Load the private key (fix path to private_key.pem)
    private_key_path = r"C:\Users\codel\private_key.pem"  # Updated path
    with open(private_key_path, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=b'hamed',  # Update if different PEM passphrase
            backend=default_backend()
        )

    # Sign and save the hash
    signature = sign_hash_with_private_key(private_key, hash_bytes)
    signature_file_path = r"C:\Users\codel\OneDrive\Desktop\git22\SpendWise\examples\Hamed\Encrypted Email Hash\signature.txt"
    save_signature_to_file(signature_file_path, signature)

    # Provide an option to verify the content later
    verify_choice = input("Do you want to verify the email integrity now? (yes/no): ").lower()
    if verify_choice == 'yes':
        verify_integrity()

def verify_integrity():
    # Load the public key
    public_key_path = r"C:\Users\codel\OneDrive\Desktop\git22\SpendWise\examples\Hamed\Encrypted Email Hash\public_key.pem"
    with open(public_key_path, 'rb') as key_file:
        public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())

    # Load the stored signature
    signature_file_path = r"C:\Users\codel\OneDrive\Desktop\git22\SpendWise\examples\Hamed\Encrypted Email Hash\signature.txt"
    with open(signature_file_path, 'rb') as file:
        signature = file.read()

    # Load the email content file (decode base64 to get the original content)
    email_file_path = r"C:\Users\codel\OneDrive\Desktop\git22\SpendWise\examples\Hamed\Encrypted Email Hash\Encrypted_email.txt"
    with open(email_file_path, 'rb') as file:  # Read as binary
        encrypted_content = base64.b64decode(file.read())  # Decode the base64 content

    # Decrypt the email content (using the AES key here, omitted in this part)
    # You can add decryption logic if needed

    # Compute the hash of the email content
    hasher = hashes.Hash(hashes.SHA256(), backend=default_backend())
    hasher.update(encrypted_content)  # Update with the decrypted content, if needed
    hash_bytes = hasher.finalize()

    # Verify the signature with the public key
    verify_signature_with_public_key(public_key, hash_bytes, signature)

if __name__ == "__main__":
    main()
