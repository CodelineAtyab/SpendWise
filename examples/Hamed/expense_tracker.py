class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, email, description, amount):

        if "@" not in email or "." not in email:
            print("Invalid email address. Please enter a valid email.")
            return

        if amount < 0:
            print("Expense amount cannot be negative.")
            return

        if email not in self.expenses:
            self.expenses[email] = []

        self.expenses[email].append({"description": description, "amount": round(amount, 2)})
        print(f" Expense '{description} - ${amount:.2f}' added successfully for {email}!")

    def view_expenses(self, email):
        
        if email not in self.expenses or not self.expenses[email]:
            print(f"No expenses found for {email}.")
            return

        print(f"\n**Expenses for {email}:**")
        print("=" * 40)
        for idx, expense in enumerate(self.expenses[email], 1):
            print(f"{idx}. {expense['description']} - ${expense['amount']:.2f}")
        print("=" * 40)

    def update_expense(self, email, index, new_description, new_amount):
        
        if email not in self.expenses or index < 1 or index > len(self.expenses[email]):
            print("Invalid email or index. Please check and try again.")
            return

        if new_amount < 0:
            print("Expense amount cannot be negative.")
            return

        self.expenses[email][index - 1] = {"description": new_description, "amount": round(new_amount, 2)}
        print(f"Expense updated: '{new_description} - ${new_amount:.2f}' for {email}.")

    def delete_expense(self, email, index):
     
        if email not in self.expenses or index < 1 or index > len(self.expenses[email]):
            print("Invalid email or index. Please check and try again.")
            return

        removed_expense = self.expenses[email].pop(index - 1)
        print(f"Expense '{removed_expense['description']} - ${removed_expense['amount']:.2f}' deleted for {email}.")

        if not self.expenses[email]:
            del self.expenses[email]
