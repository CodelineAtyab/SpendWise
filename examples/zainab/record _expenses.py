from store_expense import add_expense
from read_expenses import view_expenses
import time

_expense_data_list = []
 

def modify_expense():
  try:
    index = int(input("Enter the index of the expense to modify: "))


    if index < 0 or index >= len(_expense_data_list):
            print("Invalid index. Please try again.")
            return

    new_expense = float(input("Enter an update expense amount: "))

    _expense_data_list [index] = new_expense  

    print(f"Expense at index {index} updated to {new_expense}.")

  except ValueError:
        print("Invalid input. Please enter a valid number.")

modify_expense()
print("Updated expense data list:", _expense_data_list)
 
  
   
def delete_expense():
   index = int(input("Enter the index of the expense to delete: "))
   if index >= 0 and index < len(_expense_data_list):
      del _expense_data_list[index]
      print(f"item in index {index}is deleted")
   


def main():
  print("SpendWise CLI")
  print("=============")
  print("1. Add an expense")
  print("2. View expenses")
  print("3. Modify an expense")
  print("4. Delete an expense")
  print("5. Exit")

  choice = input("Enter your choice: ")
  if choice == "1":
    expense_amount = float(input("Enter expense amount: "))
    add_expense(expense_amount)
  elif choice == "2":
    view_expenses()
  elif choice == "3":
    modify_expense( )
  elif choice == "4":
    delete_expense( )
  elif choice == "5":
    return
  else:
    print("Invalid choice. Please try again.")
  
    main()


if __name__ == "__main__":
  main()
  print("Exiting CLI ...")
