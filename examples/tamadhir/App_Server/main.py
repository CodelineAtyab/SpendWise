import sys
import traceback

FILE_PATH = "./data/amounts.txt"

# if len(sys.argv) < 2:
#     print("Usage: python main_app.py <action> <amount:(Optional in case of read)>")
#     sys.exit(1)

# Read the data from the file
list_of_transactions: list[str] = []

# Techinal Debt
try:
  with open(FILE_PATH, "r") as data_store_file:
    list_of_transactions = [float(x.strip()) for x in data_store_file.readlines()]
except Exception:
   print(traceback.format_exc())

def add_amount(amount):
    """Adds the given amount to the transaction list and saves it to a file."""
    try:
        with open(FILE_PATH, "a") as data_store_file:
            list_of_transactions.append(float(amount))
            data_store_file.write(str(amount) + "\n")
        print("Amount added successfully!")
    except Exception:
        print(traceback.format_exc())

def view_amount():
    """Displays all stored transactions."""
    print(list_of_transactions)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        action = sys.argv[1]
        
        if action == "add-amount" and len(sys.argv) > 2:
            add_amount(sys.argv[2])
        elif action == "view-amount":
            view_amount()
        else:
            print("Invalid command or missing amount.")
    else:
        print("Usage: python script.py [add-amount <value> | view-amount]")