from store_expense import add_expense
from read_expenses import view_expenses
import expense_utils

def main():
    print("SpendWise CLI")
    print("=============")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Update an expense")
    print("4. Delete an expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expense_amount = float(input("Enter expense amount: "))
        expense_description = input("Enter expense description: ")
        add_expense(expense_description, expense_amount)  # Pass both description and amount to add_expense

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        expense_id = int(input("Enter expense ID to update: "))
        new_description = input("Enter new description: ")
        new_amount = float(input("Enter new amount: "))
        if expense_utils.update(expense_id, new_description, new_amount):
            print("Expense updated successfully!")
        else:
            print("Expense not found.")

    elif choice == "4":
        expense_id = int(input("Enter expense ID to delete: "))
        if expense_utils.remove(expense_id):
            print("Expense deleted successfully!")
        else:
            print("Expense not found.")

    elif choice == "5":
        return

    else:
        print("Invalid choice. Please try again.")

    main()  # Loop the menu again for the user

if __name__ == "__main__":
    main()
    print("Exiting CLI ...")


