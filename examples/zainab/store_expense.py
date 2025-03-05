import expense_utils

_expense_data_list = []
_expense_data_dict = {}

def add_expense(given_amount , description):
   expense = {
        "description": description,
        "amount": given_amount
    }
   global expense_counter
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

   expense_utils.add(given_amount, description)

   _expense_data_list.append(expense)
   print(f"Expense'{description} 'of OMR{given_amount}added successfully!")
   print("")

   


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
