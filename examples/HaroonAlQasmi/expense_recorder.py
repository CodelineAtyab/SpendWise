from expence_recorder_def import remove_expense, update_expense, view_expenses, add_expense

app_is_on = True
while app_is_on:
    print("SpendWise CLI")
    print("=============")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Update expense")
    print("4. Remove expense")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        update_expense()
    elif choice == "4":
        remove_expense()
    elif choice == "5":
        app_is_on = False
    else:
        print("Invalid choice. Please try again.")
