from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

# File to store the encrypted email content
ENCRYPTED_FILE = "encrypted_email.txt"

def pad_message(message):
    """Pads the message to make its length a multiple of 16 bytes (block size for AES)."""
    block_size = AES.block_size
    padding_length = block_size - len(message) % block_size
    return message + chr(padding_length) * padding_length

def unpad_message(padded_message):
    """Removes padding from the message."""
    padding_length = ord(padded_message[-1])
    return padded_message[:-padding_length]

def encrypt_email_content(email_content, secret_key):
    """
    Encrypts the email content using AES-256 encryption.
    :param email_content: The email content to encrypt.
    :param secret_key: A 32-byte secret key for AES-256 encryption.
    :return: Base64-encoded ciphertext and the initialization vector (IV).
    """
    cipher = AES.new(secret_key, AES.MODE_CBC)
    iv = cipher.iv
    padded_message = pad_message(email_content)
    ciphertext = cipher.encrypt(padded_message.encode('utf-8'))
    encoded_ciphertext = base64.b64encode(iv + ciphertext).decode('utf-8')
    return encoded_ciphertext

def save_encrypted_content(encoded_ciphertext, file_path):
    """
    Saves the Base64-encoded ciphertext to a file.
    :param encoded_ciphertext: The Base64-encoded ciphertext.
    :param file_path: The file path to save the ciphertext.
    """
    with open(file_path, "w") as f:
        f.write(encoded_ciphertext)

def generate_secret_key():
    """
    Generates a secure 32-byte secret key for AES-256 encryption.
    :return: A 32-byte secret key.
    """
    return get_random_bytes(32)

def main():
    # Prompt the user for the email content
    email_content = input("Enter the email content to encrypt: ")

    # Generate or prompt for a secret key
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as key_file:
            secret_key = key_file.read()
        print("Using existing secret key.")
    else:
        secret_key = generate_secret_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(secret_key)
        print("Generated and saved a new secret key.")

    # Encrypt the email content
    encoded_ciphertext = encrypt_email_content(email_content, secret_key)

    # Save the encrypted content to a file
    save_encrypted_content(encoded_ciphertext, ENCRYPTED_FILE)
    print(f"Encrypted email content saved to {ENCRYPTED_FILE}.")

if __name__ == "__main__":
    main()

key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_CBC)
print("AES cipher initialized successfully.")