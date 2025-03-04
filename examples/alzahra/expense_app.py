expenses = []

def add_expense():
    try:
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: OMR"))
        expenses.append({"description": description, "amount": amount})
        print(f"Expense added: {description} - OMR{amount}")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nExpense List:")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['description']} - OMR{expense['amount']}")

def update_expense():
    view_expenses()
    if not expenses:
        return
    try:
        index = int(input("Enter expense number to update: ")) - 1
        if 0 <= index < len(expenses):
            description = input("Enter new description: ")
            amount = float(input("Enter new amount: OMR "))
            expenses[index] = {"description": description, "amount": amount}
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
                print(f"Deleted expense: {removed['description']} - OMR{removed['amount']}")
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
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            update_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Exiting CLI ...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
