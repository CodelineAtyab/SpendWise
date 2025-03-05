import expense_utils
    
def view_expenses():
    expenses = expense_utils.get_all() 
    
    print("Type of expenses:", type(expenses))  
    print("Contents of expenses:", expenses)    
   
    if expenses:
        if isinstance(expenses, list) and isinstance(expenses[0], dict):
            print("\n".join(f"{i}. Amount: {expense['amount']} {expense['currency']}, Email: {expense['email']}, Date: {expense['datetime']}" 
                            for i, expense in enumerate(expenses, 1)))
        else:
            print("")
    else:
        print("No expenses recorded.")
