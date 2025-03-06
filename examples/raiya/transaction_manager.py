import sys
import traceback

FILE_PATH = "./data_store.txt"

if len(sys.argv) < 2:
    print("Usage: python ransaction_manager.py <action> <amount:(Optional in case of read)>")
    sys.exit(1)

# Read the data from the file
list_of_transactions: list[str] = []

# Techinal Debt
try:
  with open(FILE_PATH, "r") as data_store_file:
    list_of_transactions = [float(x.strip()) for x in data_store_file.readlines()]
except Exception:
   print(traceback.format_exc())


def add_amount(amount: float):
    try:
      with open(FILE_PATH, "a") as data_store_file:
        list_of_transactions.append(float(amount))
        data_store_file.write(str(amount) + "\n")
        print("Amount added successfully!")
    except Exception:
      print(traceback.format_exc())

def view_amount():
    print(list_of_transactions)

    

