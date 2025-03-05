import expense_utils

def delete_expense(item_key,loan_index):
    if expense_utils.delete(item_key,loan_index):
        print("")
        print("Expense deleted successfully!")
        print("")
    else:
        print("Expense not found!")


