"""
This is where we keep all of the data in RAM
TODO: We are going to implement the logic in this module
TODO: To save everything in a persistent storage like DB
"""
_expense_data_list = []

def add(given_amount, currency, email, current_datetime):
    expense = {
        "amount": given_amount,
        "currency": currency,
        "email": email,
        "datetime": current_datetime
    }
    _expense_data_list.append(expense)
    return True

def update(email,new_amount, new_currency, current_datetime):
       for expense in _expense_data_list:
        if expense["email"] == email:
          expense["amount"] = new_amount if new_amount is not None else expense["amount"]
          expense["currency"] = new_currency if new_currency else expense["currency"]
          expense["datetime"] = current_datetime if current_datetime else expense["datetime"]

        return True
_expense_data_list = []


def remove(email):
  for expense in _expense_data_list:
      if expense["email"] == email:
        _expense_data_list.remove(expense)  
        return True  
  return False  



def get_all():
  return _expense_data_list