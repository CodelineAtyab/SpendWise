"""
This is where we keep all of the data in RAM
TODO: We are going to implement the logic in this module
TODO: To save everything in a persistent storage like DB
"""


_expense_data_dict = {}  

def add(expense_id, expense_description, expense_amount):
   
    _expense_data_dict[expense_id] = {
        'description': expense_description,
        'amount': expense_amount
    }
    return True

def remove(expense_id):
    
    if expense_id in _expense_data_dict:
        del _expense_data_dict[expense_id]
        return True
    return False

def update(expense_id, new_description, new_amount):
    
    if expense_id in _expense_data_dict:
        _expense_data_dict[expense_id]['description'] = new_description
        _expense_data_dict[expense_id]['amount'] = new_amount
        return True
    return False

def get_all():
    
    return _expense_data_dict

