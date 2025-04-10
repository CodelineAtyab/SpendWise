import os
import base64
import hashlib
import argparse

email_file = "email.txt"
hash_file = "hash.txt"
Private_key_path = r"C:\Windows\System32\private_key.pem" # Change this to your private key path
Public_key_path = r"C:\Windows\System32\public_key.pem" # Change this to your public key path
# Make sure the email file and hash file exist

user_inputs = argparse.ArgumentParser()
user_inputs.add_argument("--email",type=str, required=True, help="Email to verify")
user_inputs.add_argument("sign_or_verify", choices=["sign", "verify"], type=str, help="Sign or verify the email")

args = user_inputs.parse_args()
email = args.email
action = args.sign_or_verify
def sign_email(email):
    # Generate a hash of the email
    email_hash = hashlib.sha256(email.encode()).hexdigest()

    # Load the private key
    with open(Private_key_path, "rb") as key_file:
        private_key = key_file.read()

    # Sign the hash with the private key
    signature = base64.b64encode(hashlib.sha256(private_key + email_hash.encode()).digest()).decode()

    # Save the email and signature to files
    with open(email_file, "w") as f:
        f.write(email)
    with open(hash_file, "w") as f:
        f.write(signature)

    print(f"Email signed and saved to {email_file} and {hash_file}")
def verify_email(email):
    # Load the email and signature from files
    with open(email_file, "r") as f:
        saved_email = f.read()
    with open(hash_file, "r") as f:
        saved_signature = f.read()

    # Generate a hash of the email
    email_hash = hashlib.sha256(email.encode()).hexdigest()

    # Load the public key
    with open(Public_key_path, "rb") as key_file:
        public_key = key_file.read()

    # Verify the signature with the public key
    expected_signature = base64.b64encode(hashlib.sha256(public_key + email_hash.encode()).digest()).decode()

    if saved_signature == expected_signature:
        print("Email is verified and valid.")
    else:
        print("Email verification failed.")
if action == "sign":
    sign_email(email)
elif action == "verify":
    verify_email(email)
