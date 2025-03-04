from datetime import datetime

expenses = {}

def add_expense():
    try:
        email = input("Enter customer email: ")
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: OMR"))
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if email not in expenses:
            expenses[email] = []
        
        expenses[email].append({"description": description, "amount": amount, "timestamp": timestamp})
        print(f"Expense added for {email}: {description} - OMR{amount} at {timestamp}")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def view_expenses(email=None):
    if not expenses:
        print("No expenses recorded.")
        return False
    
    if not email:
        email = input("Enter customer email to view expenses: ")
    
    if email in expenses and expenses[email]:
        print(f"\nExpenses for {email}:")
        for index, expense in enumerate(expenses[email], start=1):
            print(f"{index}. {expense['description']} - OMR{expense['amount']} (Added on: {expense['timestamp']})")
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
        print(f"\nExpense Dates for {email}:")
        for index, expense in enumerate(expenses[email], start=1):
            print(f"{index}. {expense['timestamp']}")
    else:
        print("No expenses found for this email.")

def update_expense():
    email = input("Enter customer email to update expense: ")
    if not view_expenses(email):
        return
    
    try:
        index = int(input("Enter expense number to update: ")) - 1
        if 0 <= index < len(expenses[email]):
            print(f"Updating: {expenses[email][index]['description']} - OMR{expenses[email][index]['amount']}")
            description = input("Enter new description (leave blank to keep unchanged): ") or expenses[email][index]['description']
            amount_input = input("Enter new amount (leave blank to keep unchanged): OMR ")
            amount = float(amount_input) if amount_input else expenses[email][index]['amount']
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            expenses[email][index] = {"description": description, "amount": amount, "timestamp": timestamp}
            print("Expense updated successfully.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def delete_expense():
    email = input("Enter customer email to delete expense: ")
    if not view_expenses(email):
        return
    
    try:
        index = int(input("Enter expense number to delete: ")) - 1
        if 0 <= index < len(expenses[email]):
            confirm = input(f"Are you sure you want to delete '{expenses[email][index]['description']}'? (y/n): ")
            if confirm.lower() == 'y':
                removed = expenses[email].pop(index)
                print(f"Deleted expense: {removed['description']} - OMR{removed['amount']} (Added on: {removed['timestamp']})")
                if not expenses[email]:
                    del expenses[email]  
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid selection. Please enter a valid expense number.")
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
