from datetime import datetime

expenses_dictionary = {}


def add_expense():
    global expenses_dictionary
    expense = input("Enter amount: ")
    customer_name = input("Enter customer name: ")
    customer_contact = input("Enter customer contact info:")
    current_datetime = datetime.now()
    expenses_dictionary[customer_contact] = [customer_name, expense, current_datetime]
    print(f"Expense added with ID: {customer_contact}")


def view_expenses():
    for key, value in expenses_dictionary.items(): # this for loop is used to extract the data from the dictionary
        customer_name = value[0]
        amount = value[1]
        date_time = value[2].strftime("%#m/%#d/%Y %H:%M")
    print(f"Contact Info: {key}, Customer Name: {customer_name}, Amount: {amount} OMR, Date-Time: {date_time}") # this is used to print a humanly readable string


def update_expense():
    expense_index = int(input("Enter Contact info: "))
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
