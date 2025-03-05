from store_expense import add_expense
from read_expenses import view_expenses
from update_expense import update_expense
from delete_expense import delete_expense
from datetime import datetime

def main():
    print("------SpendWise CLI---------")
    print("============================")
    print("    1. Add your expense")
    print("    2. View  an expenses")
    print("    3. Update an expense")
    print("    4. Delete an expense")
    print("    5. Exit Spendwise   CLI")

    Option = input ("Enter your selection : ")
    if Option == "1":
        e_mail = input("Enter your Email: ")
        # Initialize an empty list to store expense details
        amount_list = []
        #Get the expense amount from the user and convert it to an int before adding  to the list
        amount_list.append(int(input("Enter the amount: ")))
        amount_list.append(float(input("Enter the currency: ")))

        current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        amount_list.append(current_date)
        add_expense(e_mail, amount_list)


    elif Option == "2":
        view_expenses()
    elif Option == "3":
        e_mail = input("Enter the email expense to update: ")
        loan_index = int(input("Enter the loan index to update: "))
        amount_list = []
        amount_list.append(int(input("Enter the amount: ")))
        amount_list.append(input("Enter the currency: "))
        current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        amount_list.append(current_date)
        update_expense(e_mail, loan_index, amount_list)
    elif Option == "4":
        e_mail = input("Enter  email of expense to delete: ")
        loan_index = int(input("Enter the loan index to delete: "))
        delete_expense(e_mail, loan_index)
    elif Option == "5":
        return
    else:
        print("Invalid option. Please try again.")
    
    main()

   # abslote path to stor 
data_store_file = open(".\data_stor.txt", "a")


# Run the CLI application
if __name__ == "__main__":
    main()
    print("Exiting ...")
    data_store_file.close()