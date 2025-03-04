import expense_utils

def delete_expense(email):
    if expense_utils.remove(email):
        print("Expense deleted successfully!")
    else:
        print("Failed to delete the expense. The email was not found.")


       
        
    
