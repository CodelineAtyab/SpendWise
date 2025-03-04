"""
This is where we keep all of the data in RAM
TODO: We are going to implement the logic in this module
TODO: To save everything in a persistent storage like DB
"""
_expense_data_list = {}

def add(email, amount_list):
    if email in _expense_data_list:
        print(f"\nRecord for {email} already exists. Updating the record.")
        existing_amount = _expense_data_list[email][0]
        new_amount = existing_amount + amount_list[0]
        number_of_loans = _expense_data_list[email][3] + 1
        _expense_data_list[email] = [new_amount, amount_list[1], amount_list[2], number_of_loans]
    else:
        amount_list.append(1)  # Initialize the number of loans to 1
        _expense_data_list[email] = amount_list
    return True

def delete(item_key):
    if item_key in _expense_data_list:
        del _expense_data_list[item_key]
        return True
    return False

def get_all():
    return _expense_data_list

def update(email, amount_list):
    _expense_data_list[email] = amount_list
    return True
