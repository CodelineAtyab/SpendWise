import expense_utils

def update_expense(email, loan_index, amount_list):
        if expense_utils.update(email, loan_index, amount_list):
            print("")
            print("Expense updated successfully!")
            print("")