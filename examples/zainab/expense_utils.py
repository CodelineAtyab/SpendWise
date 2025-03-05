import store_expense
"""
This is where we keep all of the data in RAM
TODO: We are going to implement the logic in this module
TODO: To save everything in a persistent storage like DB

"""
_expense_data_dict = {}


def add():
    global expense_counter  # Access the global expense_counter variable
    
    # Automatically generate an ID based on the current value of expense_counter
    expense_id = f"{expense_counter}"
    
    description = input("Enter the description of the expense: ")
    try:
        amount = float(input("Enter the amount of the expense: "))
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")
        return
    
    _expense_data_dict[expense_id] = {
        "description": description,
        "amount": amount
    }
    print(f"Expense '{description}' with ID '{expense_id}' added successfully.")
    expense_counter += 1  # Increment the counter for the next expense


def add(item, key):
    _expense_data_dict[key] = item
    return True

def get_all():
    return _expense_data_dict
