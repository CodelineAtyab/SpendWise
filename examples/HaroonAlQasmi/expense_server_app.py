import uvicorn

from fastapi import FastAPI

from datetime import datetime

expenses_dictionary = {}
app = FastAPI()

@app.get("/add_expense")
def add_expense(expense,customer_name,customer_contact):
    global expenses_dictionary
    current_datetime = datetime.now()
    expenses_dictionary[customer_contact] = [customer_name, expense, current_datetime]
    return (f"Expense added with ID: {customer_contact}")

@app.get("/view_expenses")
def view_expenses():
    for key, value in expenses_dictionary.items(): # this for loop is used to extract the data from the dictionary
        customer_name = value[0]
        amount = value[1]
        date_time = value[2].strftime("%#m/%#d/%Y %H:%M")
    return (f"Contact Info: {key}, Customer Name: {customer_name}, Amount: {amount} OMR, Date-Time: {date_time}") # this is used to print a humanly readable string

@app.get("/update_expense")
def update_expense(expense_index,updated_expense,updated_customer_name):
    current_datetime = datetime.now()
    expenses_dictionary[expense_index] = [updated_customer_name, updated_expense, current_datetime]
    return("Expense updated.")

@app.get("/remove_expense")   
def remove_expense(expense_index):
    global expenses_dictionary
    if expense_index in expenses_dictionary:
        del expenses_dictionary[expense_index]
        return ("Deletion successful.")
    else:
        return ("Expense ID not found.")

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8888)