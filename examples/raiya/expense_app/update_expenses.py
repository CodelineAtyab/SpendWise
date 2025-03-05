import expense_utils

def update_expense():
    expenses = expense_utils.get_all()
    if expenses:
      print("\n".join(f"{i}. Amount: {expense['amount']} {expense['currency']}, Date: {expense['datetime']}" 
          for i, expense in enumerate(expenses, 1)))
      
    else:
      print("No expenses recorded.")
      
        
    
