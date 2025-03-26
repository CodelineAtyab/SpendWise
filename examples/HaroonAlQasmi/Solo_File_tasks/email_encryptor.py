import os
import base64
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

program_on = True
email_dictionary = {}
email_counter = 0
jason_file = "email_encryption.json"

while program_on:
    print("Welcome to the email encryptor!")
    print("What would you like to do?")
    print("1. Encrypt an email")
    print("2. Decrypt an email")
    print("3. Exit")
    choice = input("Enter number to select an option:")
    if choice == "1":
        email = input("Enter the email you want to encrypt: ")
        email_counter += 1
        encryption_key = input("Enter an encryption key or leave blank to generate randomly: ")
        if encryption_key == "":
            encryption_key = os.urandom(32)
            iv = os.urandom(16)
            padder = padding.PKCS7(128).padder()
            padded_email = padder.update(email.encode()) + padder.finalize()
            cipher = Cipher(algorithms.AES(encryption_key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_email) + encryptor.finalize()
            encoded_ciphertext = base64.b64encode(iv + ciphertext).decode()
            email_dictionary[email_counter] = encoded_ciphertext
            print("Email encrypted successfully!")
        else:
            encryption_key = encryption_key.encode( 'utf-8' )
            iv = os.urandom(16)
            padder = padding.PKCS7(128).padder()
            padded_email = padder.update(email.encode()) + padder.finalize()
            cipher = Cipher(algorithms.AES(encryption_key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_email) + encryptor.finalize()
            encoded_ciphertext = base64.b64encode(iv + ciphertext).decode()
            email_dictionary[email_counter] = encoded_ciphertext
            print("Email encrypted successfully!")
    elif choice == "2":
        email_id = int(input("Enter the email ID you want to decrypt: "))
        encoded_ciphertext = base64.b64decode.email_dictionary[email_id]
        iv = encoded_ciphertext[:16]
        ciphertext = encoded_ciphertext[16:]
        cipher = Cipher(algorithms.AES(encryption_key), modes.CBC(iv), backend=default_backend())
        dycreptor = cipher.decryptor()
        padded_email = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        email = unpadder.update(padded_email) + unpadder.finalize()
        print("Decrypted email: ", email.decode())
    elif choice == "3":
        with open(jason_file, "w") as file:
            json.dump(email_dictionary, file)
        program_on = False
    else:
        print("Invalid choice. Please try again.")