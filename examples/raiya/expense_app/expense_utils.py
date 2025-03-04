# This is where we keep all of the data in RAM
# TODO: We are going to implement the logic in this module
# TODO: To save everything in a persistent storage like DB

_expense_data_dict = {}

def add(given_amount, currency, email, current_datetime):
    expense = {
        "amount": given_amount,
        "currency": currency,
        "datetime": current_datetime
    }
    if email in _expense_data_dict:
        _expense_data_dict[email].append(expense)
    else:
        _expense_data_dict[email] = [expense]
    return True

def update(email, new_amount, new_currency, current_datetime):
    if email in _expense_data_dict:
        for expense in _expense_data_dict[email]:
            expense["amount"] = new_amount if new_amount is not None else expense["amount"]
            expense["currency"] = new_currency if new_currency else expense["currency"]
            expense["datetime"] = current_datetime if current_datetime else expense["datetime"]
        return True
    return False

def remove(email):
    if email in _expense_data_dict:
        del _expense_data_dict[email] 
        return True
    return False

def get_all():
    return _expense_data_dict

def get_info_of_customer_transaction(email):
    return _expense_data_dict.get(email, [])
