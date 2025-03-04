"""
This is where we keep all of the data in RAM
TODO: We are going to implement the logic in this module
TODO: To save everything in a persistent storage like DB
"""
_expense_data_list = []

def add(item):
  _expense_data_list.append(item)
  return True

def remove(item_id):
  return True 

def get_all():
  return _expense_data_list