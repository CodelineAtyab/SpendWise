from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64
import os

def encrypt_email_content(email_content, secret_key=None):
    # AES-256 requires a 32-byte key
    if secret_key:
        key = secret_key.encode('utf-8')
        if len(key) != 32:
            raise ValueError("Secret key must be 32 bytes for AES-256 encryption.")
    else:
        # Generate a secure 32-byte key if not provided
        key = get_random_bytes(32)
        print(f"Generated random key: {base64.b64encode(key).decode('utf-8')}")

    # Ensure that the email content is in bytes
    email_bytes = email_content.encode('utf-8')

    # Generate a random IV for AES encryption
    iv = get_random_bytes(AES.block_size)

    # Set up AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the email content to be AES block size aligned
    padded_email = pad(email_bytes, AES.block_size)

    # Encrypt the email content
    ciphertext = cipher.encrypt(padded_email)

    # Combine the IV with the ciphertext to store in the file
    encrypted_data = iv + ciphertext

    # Encode the encrypted data using base64
    encrypted_base64 = base64.b64encode(encrypted_data).decode('utf-8')

    return encrypted_base64, key

def save_encrypted_content_to_file(encrypted_base64, filename):
    with open(filename, 'w') as file:
        file.write(encrypted_base64)
    print(f"Encrypted content saved to {filename}")

def main():
    # Get email content from the user
    email_content = input("Enter the email content to encrypt: ")

    # Get secret key from the user or leave it blank to generate a key
    secret_key = input("Enter a 32-byte secret key (leave empty to generate a key): ")

    # Encrypt the email content
    encrypted_base64, encryption_key = encrypt_email_content(email_content, secret_key)

    # Save the encrypted content to a file
    save_encrypted_content_to_file(encrypted_base64, "encrypted_email.txt")

    # Optionally, print the secret key used (if generated) and the base64 encoded ciphertext
    print(f"Encryption completed with key: {base64.b64encode(encryption_key).decode('utf-8')}")
    print("Encrypted base64 content:")
    print(encrypted_base64)

if __name__ == "__main__":
    main()

