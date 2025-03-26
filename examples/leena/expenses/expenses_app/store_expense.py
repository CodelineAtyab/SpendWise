import expense_utils

def add_expense(email, amount_list):
    expense_utils.add(email, amount_list)
    print("")
    print("Expense added successfully!")
    print("")