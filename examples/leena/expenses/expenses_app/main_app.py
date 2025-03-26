from store_expense import add_expense
from read_expenses import view_expenses
from update_expense import update_expense
from delete_expense import delete_expense
from datetime import datetime

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
        e_mail = input("Enter your Email: ")
        amount_list = []
        amount_list.append(int(input("Enter the amount: ")))
        amount_list.append(input("Enter the currency: "))
        current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        amount_list.append(current_date)
        add_expense(e_mail, amount_list)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        e_mail = input("Enter the email of the expense to update: ")
        loan_index = int(input("Enter the loan index to update: "))
        amount_list = []
        amount_list.append(int(input("Enter the amount: ")))
        amount_list.append(input("Enter the currency: "))
        current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        amount_list.append(current_date)
        update_expense(e_mail, loan_index, amount_list)
    elif choice == "4":
        e_mail = input("Enter the email of the expense to delete: ")
        loan_index = int(input("Enter the loan index to delete: "))
        delete_expense(e_mail, loan_index)
    elif choice == "5":
        return
    else:
        print("Invalid choice. Please try again.")
    
    main()
    
if __name__ == "__main__":
    main()
    print("Exiting CLI ...")