import os
import hashlib


def compute_sha256(file_path, chunk_size=8192):
  """Compute SHA-256 hash of a file by reading it in chunks."""
  try:
    hash_obj = hashlib.sha256()
    with open(file_path, 'rb') as file:
      while chunk := file.read(chunk_size):
        hash_obj.update(chunk)
    return hash_obj.hexdigest()
  except FileNotFoundError:
    print(f"File not found: {file_path}")
  except Exception as e:
    print(f"Error computing SHA-256 hash: {e}")
  
  return

file_path = "./LICENSE_EXAMPLE.txt"
hash_hex_str_output = compute_sha256(file_path)

print(f"SHA-256 hash of {file_path} is:"
      f"{hash_hex_str_output} and length is {len(hash_hex_str_output)}")
