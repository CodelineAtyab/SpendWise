"""
This is where we keep all of the data in RAM
TODO: We are going to implement the logic in this module
TODO: To save everything in a persistent storage like DB
"""
_expense_data_list = {}

def add(email, amount_list):
    _expense_data_list[email] = amount_list
    return True

def remove(item_id):
    if item_id in _expense_data_list:
        del _expense_data_list[item_id]
        return True
    return False

def get_all():
    return _expense_data_list