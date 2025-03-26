import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
# a pip installation done "pycryptodome"

def generate_key():
    return get_random_bytes(32)  # Generates a 32-byte AES key

def encrypt_email_content(email_content, key):
    iv = get_random_bytes(16)  # AES block size is 16 bytes
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_bytes = cipher.encrypt(pad(email_content.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_bytes).decode()

def save_encrypted_content(filename, encrypted_content):
    with open(filename, 'w') as file:
        file.write(encrypted_content)

def main():
    email_content = input("Enter the email content: ")
    use_existing_key = input("Do you have an existing key? (yes/no): ").strip().lower()

    if use_existing_key == 'yes':
        key_input = input("Enter the 32-byte key (base64 encoded): ")
        
        key = base64.b64decode(key_input)

        if len(key) != 32:
            print("Invalid key length! The key must be 32 bytes.")
            return
    else:
        key = generate_key()
        print("Generated key (save this for decryption):", base64.b64encode(key).decode())

    encrypted_content = encrypt_email_content(email_content, key)
    save_encrypted_content("encrypted_email.txt", encrypted_content)
    print("Encryption successful! The encrypted content is saved")

if __name__ == "__main__":
    main()