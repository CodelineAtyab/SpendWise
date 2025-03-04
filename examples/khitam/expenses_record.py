expenses = []
def create_expense(description, amount):
    expense = {'description': description, 'amount': amount}
    expenses.append(expense)

def read_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        print(expenses)

def update_expense(index, new_description, new_amount):
    if 0 <= index < len(expenses):
        expenses[index]['description'] = new_description
        expenses[index]['amount'] = new_amount

def delete_expense(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)
        
create_expense("Lunch", 15)
create_expense("Coffee", 5)
read_expenses()
update_expense(0, "Lunch", 12)
delete_expense(1)
read_expenses()