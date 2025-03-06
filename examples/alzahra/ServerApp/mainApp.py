
FILE_PATH = "amounts.txt"

def read_transactions():
    """Reads transactions from the file."""
    try:
        with open(FILE_PATH, "r") as data_store_file:
            list_of_transactions = [float(x.strip()) for x in data_store_file.readlines()]
        return list_of_transactions
    except FileNotFoundError:
        return []  # If file does not exist, return an empty list
    except Exception as e:
        raise Exception(f"Error reading the file: {str(e)}")

def add_amount(amount: float):
    """Adds an amount to the transaction file."""
    try:
        with open(FILE_PATH, "a") as data_store_file:
            data_store_file.write(f"{amount}\n")
        return "Amount added successfully!"
    except Exception as e:
        raise Exception(f"Error writing to the file: {str(e)}")
