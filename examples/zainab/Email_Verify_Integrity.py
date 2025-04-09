import os
import hashlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Function to generate SHA-256 hash of the email content
def generate_hash(email_content):
    return hashlib.sha256(email_content.encode()).hexdigest()

# Function to sign the hash with the RSA private key (using PKCS#1 v1.5)
def sign_hash(hash_value, private_key_path):
    # Load private key
    with open(private_key_path, 'rb') as private_file:
        private_key = RSA.import_key(private_file.read())
    # Create SHA256 hash object from the hash value
    h = SHA256.new(hash_value.encode())
    signature = pkcs1_15.new(private_key).sign(h)
    return base64.b64encode(signature).decode()

# Function to save email content to a file
def save_email_content(email_content, email_file_path):
    with open(email_file_path, 'w') as email_file:
        email_file.write(email_content)

# Function to save the signature to a file
def save_signature(signature, sig_file_path):
    with open(sig_file_path, 'w') as sig_file:
        sig_file.write(signature)

# Function to verify the signature with the RSA public key
def verify_signature(hash_value, signature, public_key_path):
    # Load public key
    with open(public_key_path, 'rb') as public_file:
        public_key = RSA.import_key(public_file.read())
    h = SHA256.new(hash_value.encode())
    signature_bytes = base64.b64decode(signature)
    try:
        pkcs1_15.new(public_key).verify(h, signature_bytes)
        return True
    except (ValueError, TypeError):
        return False

# Function to verify the email content integrity
def verify_email_integrity(email_content, email_file_path, sig_file_path, public_key_path):
    # Generate SHA-256 hash of the current email content
    current_hash = generate_hash(email_content)
    
    # Read the signature from the file
    with open(sig_file_path, 'r') as sig_file:
        signature = sig_file.read()
    
    # Verify the signature using the public key
    if verify_signature(current_hash, signature, public_key_path):
        print("Email content is intact.")
    else:
        print("Email content has been modified!")

# Main functionality
if __name__ == '__main__':
    # Example Email Content
    email_content = "Hello, this Email from Zainab."
    
    # Paths to files
    email_file_path = 'email_content.txt'
    sig_file_path = 'email_signature.txt'
    private_key_path = 'private_key.pem'
    public_key_path = 'public_key.pem'

    # Step 1: Save the email content to a text file
    save_email_content(email_content, email_file_path)
    
    # Step 2: Generate SHA-256 hash of the email content
    email_hash = generate_hash(email_content)
    
    # Step 3: Sign the hash with the RSA private key
    signature = sign_hash(email_hash, private_key_path)
    
    # Step 4: Save the signature to a file
    save_signature(signature, sig_file_path)
    
    # Step 5: Verify the email content integrity by verifying the signature
    print("\nVerifying email content integrity:")
    verify_email_integrity(email_content, email_file_path, sig_file_path, public_key_path)