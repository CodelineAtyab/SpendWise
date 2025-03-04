from store_expense import add_expense
from read_expenses import view_expenses 
from store_expense import update_expense
from delete_expense import delete_expense
import datetime

def main():
  print("SpendWise CLI")
  print("====================")
  print("1. Add an expense")
  print("2. View expenses")
  print("3. Update Expense")
  print("4. Delete Expense")
  print("5. Exit")

  choice = input("Enter your choice: ")
  if choice == "1":
    expense_amount = float(input("Enter expense amount: "))
    currency = input("Enter the currency:")
    email = input("Enter your email:")
    current_datetime = datetime.datetime.now()
    add_expense(expense_amount, currency, email, current_datetime)
    
  elif choice == "2":
    view_expenses()

  elif choice == "3":
    print("Update Expense")
    email = input("Enter the email of the expense you want to update: ")
    new_amount = float(input("Enter the new expense amount: "))
    new_currency = input("Enter the new currency:")
    current_datetime = datetime.datetime.now()
    update_expense( new_amount, new_currency, email, current_datetime)

  elif choice == "4":
    print("Delete Expense")
    email = input("Enter the email of the expense you want to delete: ")
    delete_expense(email)
 
  elif choice == "5":
    return
  else:
    print("Invalid choice. Please try again.")

    

  main()

if __name__ == "__main__":
  main()
  print("Exiting CLI ...")
