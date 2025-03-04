import expense_utils
def view_expenses():
    expenses = expense_utils.get_all()
    if expenses:
      print("\n".join(f"{i}. Amount: {expense['amount']} {expense['currency']}, Email: {expense['email']}, Date: {expense['datetime']}" 
          for i, expense in enumerate(expenses, 1)))
      
    else:
      print("No expenses recorded.")

def update_expense():
    expenses = expense_utils.get_all()
    if expenses:
      print("\n".join(f"{i}. Amount: {expense['amount']} {expense['currency']}, Date: {expense['datetime']}" 
          for i, expense in enumerate(expenses, 1)))
      
    else:
      print("No expenses recorded.")
      
import expense_utils

def delete_expense(email):
    if expense_utils.remove(email):
        print("Expense deleted successfully!")
    else:
        print("Failed to delete the expense. The email was not found.")


       
        
    
