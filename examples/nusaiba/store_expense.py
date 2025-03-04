import expense_utils

def add_expense(expense_description, expense_amount):
  expense_id = len(expense_utils.get_all()) + 1
  expense_utils.add(expense_id, expense_description, expense_amount)
  print(f"Expense added successfully with ID {expense_id}!")
