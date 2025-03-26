from expence_recorder_def import remove_expense, update_expense, view_expenses, add_expense,hash_dictionary,expenses_dictionary,compute_sha256
import os
import json
from datetime import datetime 

hash_file = "hashes.json"
expenses_file = "expenses.json"

app_is_on = True
while app_is_on:
    print("==============")
    print("SpendWise CLI")
    print("==============")
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
        if os.path.exists(hash_file):
            with open(hash_file, "r") as json_file:
                try:
                    data = json.load(json_file)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}
        data.update(hash_dictionary)
        with open(hash_file, "w") as json_file:
            json.dump(data, json_file, indent=4, default=str)
        if os.path.exists(expenses_file):
            with open(expenses_file, "r") as json_file:
                try:
                    data = json.load(json_file)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}
        data.update(expenses_dictionary)
        with open(expenses_file, "w") as json_file:
            json.dump(data, json_file, indent=4, default=str)
        app_is_on = False
    else:
        print("Invalid choice. Please try again.")
