from datetime import datetime

expenses = []

def add_expense():
    try:
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: OMR"))
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expenses.append({"description": description, "amount": amount, "timestamp": timestamp})
        print(f"Expense added: {description} - OMR{amount} at {timestamp}")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nExpense List:")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['description']} - OMR{expense['amount']} (Added on: {expense['timestamp']})")

def display_expense_dates():
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nExpense Dates:")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['timestamp']}")

def update_expense():
    view_expenses()
    if not expenses:
        return
    try:
        index = int(input("Enter expense number to update: ")) - 1
        if 0 <= index < len(expenses):
            description = input("Enter new description: ")
            amount = float(input("Enter new amount: OMR "))
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            expenses[index] = {"description": description, "amount": amount, "timestamp": timestamp}
            print("Expense updated successfully.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def delete_expense():
    view_expenses()
    if not expenses:
        return
    try:
        index = int(input("Enter expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            confirm = input(f"Are you sure you want to delete '{expenses[index]['description']}'? (y/n): ")
            if confirm.lower() == 'y':
                removed = expenses.pop(index)
                print(f"Deleted expense: {removed['description']} - OMR{removed['amount']} (Added on: {removed['timestamp']})")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

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

if __name__ == "__main__":
    main()
