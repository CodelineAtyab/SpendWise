from store_expense import add_expense
from read_expenses import view_expenses
import datetime

_expense_data_dict = {} 
expense_counter = 1  # A counter to generate unique IDs automatically
 

def modify_expense():
  try:
    index = input("Enter the ID of the expense to modify: ")
    if index not in _expense_data_dict:
        print( "Expense not found. Please enter a valid ID.")
        return

    new_expense = float(input("Enter an update expense amount: "))
    _expense_data_dict [index] = new_expense  

    print(f"Expense at index {index} updated to {new_expense}.")

  except ValueError:
        print("Invalid input. Please enter a valid number.")


def delete_expense():
   index = int(input("Enter the index of the expense to delete: "))
   if index >= 0 and index < len(_expense_data_dict):
      del _expense_data_dict[index]
      print(f"item in index {index}is deleted")

def main():
    print("SpendWise CLI")
    print("=============")
    
    while True:  # Infinite loop until exit option is chosen
        print("\n1. Add an expense")
        print("2. View expenses")
        print("3. Modify an expense")
        print("4. Delete an expense")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                given_amount = float(input("Enter expense amount: "))
                input_description=  input("Enter expense description: ")
                _expense_data_dict[description] = given_amount
                add_expense(given_amount , description)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            modify_expense()
            print("Updated expense data list:", _expense_data_dict)

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            print("Exiting CLI ...")
            break  # Break the loop to exit the program

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

