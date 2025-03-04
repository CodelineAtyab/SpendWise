import expense_utils

def update_expense(email, amount_list):
    if expense_utils.update(email, amount_list):
        print("")
        print("Expense updated successfully!")
        print("")