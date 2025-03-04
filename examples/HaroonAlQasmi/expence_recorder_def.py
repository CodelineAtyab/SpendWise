from datetime import datetime
expenses_dictionary = {}
item_id = 1
def add_expense():
    global expenses_dictionary, item_id
    expense = input("Enter amount: ")
    customer_name = input("Enter customer name: ")
    current_datetime = datetime.now()
    expenses_dictionary[item_id] = [customer_name, expense, current_datetime]
    print(f"Expense added with ID: {item_id}")
    item_id += 1
def view_expenses():
    print(expenses_dictionary)
def update_expense():
    global expenses_dictionary
    expense_index = int(input("Enter index number 'the number on the left': "))
    updated_expense = input("Enter the updated amount: ")
    updated_customer_name = input("Enter updated customer name: ")
    current_datetime = datetime.now()
    expenses_dictionary[expense_index] = [updated_customer_name, updated_expense, current_datetime]
    print("Expense updated.")
def remove_expense():
    global expenses_dictionary
    expense_index = int(input("Enter index number 'the number on the left': "))
    if expense_index in expenses_dictionary:
        del expenses_dictionary[expense_index]
        print("Deletion successful.")
    else:
        print("Expense ID not found.")
