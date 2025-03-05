import sys
import traceback

FILE_PATH = "./data/data_store.txt"

if len(sys.argv) < 2:
    print("Usage: python main_app.py <action> <amount:(Optional in case of read)>")
    sys.exit(1)

# Read the data from the file
list_of_transactions: list[str] = []

# Techinal Debt
try:
  with open(FILE_PATH, "r") as data_store_file:
    list_of_transactions = [float(x.strip()) for x in data_store_file.readlines()]
except Exception:
   print(traceback.format_exc())

# Action handler for action add-amount
if sys.argv[1] == "add-amount":
    try:
      with open(FILE_PATH, "a") as data_store_file:
        list_of_transactions.append(float(sys.argv[2]))
        data_store_file.write(sys.argv[2] + "\n")
        print("Amount added successfully!")
    except Exception:
      print(traceback.format_exc())
    
elif sys.argv[1] == "view-amount":
    print(list_of_transactions)
