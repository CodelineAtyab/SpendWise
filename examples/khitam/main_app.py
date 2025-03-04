import datetime

expenses = {}

def add_expense():
    email = input("Please enter the customer's email: ")
    description = input("Please enter the expense description: ")
    amount_input = input("Please enter the expense amount: OMR ")
    if not amount_input.replace('.', '', 1).isdigit() or amount_input.count('.') > 1:
        print("Invalid amount. Please enter a valid numeric value.")
        return
    
    amount = float(amount_input)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if email not in expenses:
        expenses[email] = []

    expenses[email].append({"description": description, "amount": amount, "timestamp": timestamp})
    print("Expense added for " + email + ": " + description + " - OMR" + str(amount) + " at " + timestamp)

def view_expenses(email=None):
    if not expenses:
        print("No expenses recorded.")
        return False
    
    if not email:
        email = input("Please enter the customer's email to view expenses: ")

    if email in expenses and expenses[email]:
        print("Expenses for " + email + ":")
        for index, expense in enumerate(expenses[email], start=1):
            print(str(index) + ". " + expense['description'] + " - OMR" + str(expense['amount']) + " (Added on: " + expense['timestamp'] + ")")
        return True
    else:
        print("No expenses found for this email.")
        return False

def display_expense_dates():
    if not expenses:
        print("No expenses recorded.")
        return
    email = input("Enter customer email to view expense dates: ")
    if email in expenses and expenses[email]:
        print("Expense Dates for " + email + ":")
        for index, expense in enumerate(expenses[email], start=1):
            print(str(index) + ". " + expense['timestamp'])
    else:
        print("No expenses found for this email.")

def update_expense():
    email = input("Enter customer email to update their expense: ")
    if not view_expenses(email):
        return

    index_input = input("Enter the expense number to update: ")
    if not index_input.isdigit():
        print("Invalid input. Please enter a valid number.")
        return

    index = int(index_input) - 1
    if 0 <= index < len(expenses[email]):
        print("Updating: " + expenses[email][index]['description'] + " - OMR" + str(expenses[email][index]['amount']))
        description = input("Enter new description (leave blank to keep unchanged): ") or expenses[email][index]['description']
        amount_input = input("Enter new amount (leave blank to keep unchanged): OMR ")
        if amount_input and (not amount_input.replace('.', '', 1).isdigit() or amount_input.count('.') > 1):
            print("Invalid amount. Please enter a valid numeric value.")
            return

        amount = float(amount_input) if amount_input else expenses[email][index]['amount']
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        expenses[email][index] = {"description": description, "amount": amount, "timestamp": timestamp}
        print("Expense updated successfully.")
    else:
        print("Invalid selection.")

def delete_expense():
    email = input("Enter customer email to delete their expense: ")
    if not view_expenses(email):
        return

    index_input = input("Enter the expense number to delete: ")
    if not index_input.isdigit():
        print("Invalid input. Please enter a valid number.")
        return

    index = int(index_input) - 1
    if 0 <= index < len(expenses[email]):
        confirm = input("Are you sure you want to delete '" + expenses[email][index]['description'] + "'? (y/n): ")
        if confirm.lower() == 'y':
            removed = expenses[email].pop(index)
            print("Deleted expense: " + removed['description'] + " - OMR" + str(removed['amount']) + " (Added on: " + removed['timestamp'] + ")")
            if not expenses[email]:
                del expenses[email]
        else:
            print("Deletion cancelled.")
    else:
        print("Invalid selection. Please enter a valid expense number.")

def main():
    while True:
        print("\nSpendWise CLI")
        print("=============")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Expense Dates")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            display_expense_dates()
        elif choice == '4':
            update_expense()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            print("Exiting CLI ...")
            break
        else:
            print("Invalid choice, please try again.")
main()