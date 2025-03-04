import expense_utils

def delete_expense(item_key):
    if expense_utils.delete(item_key):
        print("")
        print("Expense deleted successfully!")
        print("")
    else:
        print("Expense not found!")