import crud_utils

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
            email = input("Enter customer email: ")
            description = input("Enter expense description: ")
            amount_input = input("Enter expense amount: OMR ")
            if amount_input.replace('.', '', 1).isdigit() and amount_input.count('.') <= 1:
                amount = float(amount_input)
                print(crud_utils.add_expense(email, description, amount))
            else:
                print("Invalid amount.")
        
        elif choice == '2':
            email = input("Enter customer email to view expenses: ")
            expenses = crud_utils.view_expenses(email)
            if expenses:
                print("\nExpenses for " + email + ":")
                for exp in expenses:
                    print(str(exp[0]) + ". " + exp[1] + " - OMR" + str(exp[2]) + " (Added on: " + exp[3] + ")")
            else:
                print("No expenses found for this email.")
        
        elif choice == '3':
            email = input("Enter customer email to update expense: ")
            expenses = crud_utils.view_expenses(email)
            if not expenses:
                print("No expenses found.")
                continue
            for exp in expenses:
                print(str(exp[0]) + ". " + exp[1] + " - OMR" + str(exp[2]) + " (Added on: " + exp[3] + ")")
            index_input = input("Enter expense number to update: ")
            if index_input.isdigit():
                index = int(index_input) - 1
                description = input("Enter new description (leave blank to keep unchanged): ")
                amount_input = input("Enter new amount (leave blank to keep unchanged): OMR ")
                amount = float(amount_input) if amount_input else None
                print(crud_utils.update_expense(email, index, description, amount))
            else:
                print("Invalid input.")
        
        elif choice == '4':
            email = input("Enter customer email to delete expense: ")
            expenses = crud_utils.view_expenses(email)
            if not expenses:
                print("No expenses found.")
                continue
            for exp in expenses:
                print(str(exp[0]) + ". " + exp[1] + " - OMR" + str(exp[2]) + " (Added on: " + exp[3] + ")")
            index_input = input("Enter expense number to delete: ")
            if index_input.isdigit():
                index = int(index_input) - 1
                confirm = input("Are you sure? (y/n): ")
                if confirm.lower() == 'y':
                    print(crud_utils.delete_expense(email, index))
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid input.")
        
        elif choice == '5':
            print("Exiting CLI ...")
            break
        else:
            print("Invalid choice, please try again.")

main()
