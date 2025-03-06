import expense_utils
 
def add_expense(expense_amount, currency, email, current_datetime):
    expense_utils.add(expense_amount, currency, email, current_datetime)
    print("Expense details have been successfully added!")
    print("")

def update_expense(email,new_amount, new_currency, current_datetime):
    if expense_utils.update(email, new_amount, new_currency, current_datetime):
        print("Expense updated successfully!")
    else:
        print("Failed to update the expense. The email was not found.")
    print("")