from store_expense import add_expense
from read_expenses import view_expenses

def main():
  print("SpendWise CLI")
  print("=============")
  print("1. Add an expense")
  print("2. View expenses")
  print("3. Exit")

  choice = input("Enter your choice: ")
  if choice == "1":
    expense_amount = float(input("Enter expense amount: "))
    add_expense(expense_amount)
  elif choice == "2":
    view_expenses()
  elif choice == "3":
    return
  else:
    print("Invalid choice. Please try again.")
  
  main()


if __name__ == "__main__":
  main()
  print("Exiting CLI ...")
