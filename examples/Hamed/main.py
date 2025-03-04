from expense_tracker import ExpenseTracker

def main():
    tracker = ExpenseTracker()

    while True:
        print("===============================")
        print("******* Expense Tracker *******")
        print("===============================")
        print("1. Create a New Expense")
        print("2. View Expenses")
        print("3. Update an Expense")
        print("4. Delete an Expense")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter expense description: ")
            try:
                amount = float(input("Enter expense amount: "))
                tracker.add_expense(description, amount)
                print("Expense added successfully.")
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        
        elif choice == "2":
            tracker.view_expenses()
        
        elif choice == "3":
            tracker.view_expenses()
            try:
                index = int(input("Enter the index of the expense to update: "))
                new_description = input("Enter new description: ")
                new_amount = float(input("Enter new amount: "))
                tracker.update_expense(index, new_description, new_amount)
                print("Expense updated successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid index and amount.")
        
        elif choice == "4":
            tracker.view_expenses()
            try:
                index = int(input("Enter the index of the expense to delete: "))
                confirm = input(f"Are you sure you want to delete expense {index}? (y/n): ").lower()
                if confirm == 'y':
                    tracker.delete_expense(index)
                    print(f"Expense {index} deleted successfully.")
                else:
                    print("Deletion canceled.")
            except ValueError:
                print("Invalid input. Please enter a valid index.")
            except IndexError:
                print("Invalid index. Please select an existing expense.")
        
        elif choice == "5":
            print("Exiting Expense Tracker. Thank you, Goodbye!")
            return
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
