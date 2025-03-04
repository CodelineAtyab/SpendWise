class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        expense = {"description": description, "amount": amount}
        self.expenses.append(expense)
        print(f"Expense '{description} - ${amount}' added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses added yet.")
            return
        print("\nExpenses List:")
        for idx, expense in enumerate(self.expenses, 1):
            print(f"{idx}. {expense['description']} - ${expense['amount']}")

    def update_expense(self, index, new_description, new_amount):
        if index < 1 or index > len(self.expenses):
            print("Invalid index. Please select a valid expense.")
            return
        self.expenses[index - 1]["description"] = new_description
        self.expenses[index - 1]["amount"] = new_amount
        print(f"Expense updated: {new_description} - ${new_amount}")

    def delete_expense(self, index):
        if index < 1 or index > len(self.expenses):
            print("Invalid index. Please select a valid expense.")
            return
        removed_expense = self.expenses.pop(index - 1)
        print(f"Expense '{removed_expense['description']} - ${removed_expense['amount']}' deleted successfully!")
