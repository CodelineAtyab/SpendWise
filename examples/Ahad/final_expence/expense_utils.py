"""
This is where we keep all of the data in RAM
TODO: We are going to implement the logic in this module
TODO: To save everything in a persistent storage like DB
"""
_expense_data_list = {}

def add(email, amount_list):
    loan_record = {
        "amount": amount_list[0],
        "currency": amount_list[1],
        "date": amount_list[2]
    }
    
    if email in _expense_data_list:
        print(f"\nRecord for {email} already exists. Adding a new loan record.")
        _expense_data_list[email].append(loan_record)
    else:
        _expense_data_list[email] = [loan_record]
    
    return True

def delete(email, loan_index):
    if email in _expense_data_list and 0 <= loan_index < len(_expense_data_list[email]):
        del _expense_data_list[email][loan_index]
        if not _expense_data_list[email]: 
            del _expense_data_list[email]
        return True
    return False

def get_all():
    return _expense_data_list

def update(email, loan_index, amount_list):
    if email in _expense_data_list and 0 <= loan_index < len(_expense_data_list[email]):
        _expense_data_list[email][loan_index] = {
            "amount": amount_list[0],
            "currency": amount_list[1],
            "date": amount_list[2]
        }
        return True
    return False