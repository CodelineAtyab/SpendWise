import base64            # For base64 encoding of the ciphertext.
import os                # For generating random bytes (IV and key).
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes  # For AES encryption.
from cryptography.hazmat.primitives import padding  # To pad the email content to block size.
from cryptography.hazmat.backends import default_backend

def generate_secret_key():
    # Generate a secure random 32-byte key for AES-256.
    return os.urandom(32)

def encrypt_email(email_content, secret_key):
    # Use the generated 32-byte key directly.
    key = secret_key

    # Generate a random 16-byte IV for AES CBC mode.
    iv = os.urandom(16)

    # Create an AES cipher object in CBC mode.
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Create a PKCS7 padder to pad the email content to the AES block size (128 bits).
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(email_content.encode()) + padder.finalize()

    # Encrypt the padded email content.
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Prepend the IV to the ciphertext; the IV is needed for decryption.
    combined = iv + ciphertext

    # Base64 encode the combined IV and ciphertext so it can be saved as text.
    encoded = base64.b64encode(combined)
    return encoded.decode()  # Return as a string.

def save_encrypted_email(encoded_ciphertext, filepath):
    # Save the encoded ciphertext to a file, overwriting any previous value.
    with open(filepath, 'w') as f:
        f.write(encoded_ciphertext)
    print(f"Encrypted email saved to {filepath}")

if __name__ == '__main__':
    # Get the email message input from the user.
    email_message = input("Enter the email content to encrypt: ")

    # Generate a secure random secret key.
    secret_key = generate_secret_key()
    
    # Display the generated key (base64 encoded) for reference.
    print("Generated secret key (base64 encoded):", base64.b64encode(secret_key).decode())
    
    # Encrypt the email message.
    encoded = encrypt_email(email_message, secret_key)
    
    # Define the output secure storage file.
    output_path = 'encrypted_email.txt'
    save_encrypted_email(encoded, output_path)