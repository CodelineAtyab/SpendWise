import os
import subprocess
import hashlib
import base64

def generate_keys():
    # Generate private key 
    if not os.path.exists("privateKey.pem"):
        subprocess.run(["openssl", "genrsa", "-out", "privateKey.pem", "2048"], check=True)
    # Generate public key
    if not os.path.exists("publicKey.pem"):
        subprocess.run(["openssl", "rsa", "-in", "privateKey.pem", "-pubout", "-out", "publicKey.pem"], check=True)

def save_email(content, filename="email.txt"):
    with open(filename, "w") as f:
        f.write(content)

def compute_hash(content):
    sha256 = hashlib.sha256()
    sha256.update(content.encode())
    return sha256.hexdigest()

def sign_hash(hash_value):
    # Write hash to a temporary file
    with open("hash.txt", "w") as f:
        f.write(hash_value)
    # Sign the hash using the private key
    subprocess.run([
        "openssl", "rsautl", "-sign", "-inkey", "privateKey.pem","-in", "hash.txt", "-out", "signature.bin"
    ], check=True)
    # Base64 encode the signature
    with open("signature.bin", "rb") as f:
        sig_data = f.read()
    sig_b64 = base64.b64encode(sig_data).decode()
    with open("signature.b64", "w") as f:
        f.write(sig_b64)
    # Clean up temporary file
    os.remove("hash.txt")

def verify_email(content):
    # Compute the current hash of the email content
    current_hash = compute_hash(content)
    # Decode the saved base64 signature back to binary form
    with open("signature.b64", "r") as f:
        b64_data = f.read()
    sig_data = base64.b64decode(b64_data)
    with open("signature_decoded.bin", "wb") as f:
        f.write(sig_data)
    # Decrypt (verify) the signature using the public key to retrieve the original hash
    subprocess.run([
        "openssl", "rsautl", "-verify", "-pubin", "-inkey", "publicKey.pem","-in", "signature_decoded.bin", "-out", "decrypted_hash.txt"
    ], check=True)
    with open("decrypted_hash.txt", "r") as f:
        decrypted_hash = f.read().strip()
    # Clean up temporary files
    os.remove("signature_decoded.bin")
    os.remove("decrypted_hash.txt")
    # Compare the decrypted hash with the current hash
    return current_hash == decrypted_hash

if __name__ == "__main__":
    # Sample email content
    email_content = "Dear Raiya, this is a sample email content. Regards,"
    # 1. Generate keys (only once if they do not exist)
    generate_keys()
    # 2. Save email content to a file
    save_email(email_content)
    # 3. Compute the SHA-256 hash of the email content and sign it
    content_hash = compute_hash(email_content)
    sign_hash(content_hash)
    # 4. Verify the integrity of the email content
    if verify_email(email_content):
        print("Email integrity valid: True")
    else:
        print("Email integrity valid: False")

