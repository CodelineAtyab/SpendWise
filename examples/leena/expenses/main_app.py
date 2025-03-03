from store_expense import add_expense
from read_expenses import view_expenses
amount_list = []
def main():
  print("SpendWise CLI")
  print("=============")
  print("1. Add an expense")
  print("2. View expenses")
  print("3. Exit")

  choice = input("Enter your choice: ")
  if choice == "1":
    e_mail = (input("Enter your Email: "))
    amount_list[0] = int(input("Enter the amount: "))
    amount_list[1] = input("Enter the currency: ")
    amount_list[2] = input("Enter the date dd/mm/yyyy: ")
    add_expense(e_mail,amount_list)
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
