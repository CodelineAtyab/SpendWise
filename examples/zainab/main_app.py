from fastapi import FastAPI
from pydantic import BaseModel
import json
from typing import List
import sys
import traceback

app = FastAPI()

# File where we will save the amounts
AMOUNTS_FILE = "amounts.json"

# Function to load data from the file
def load_amounts():
    try:
        with open(AMOUNTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist yet

# Function to save data to the file
def save_amounts(amounts):
    with open(AMOUNTS_FILE, "w") as file:
        json.dump(amounts, file)

# Pydantic model for handling the expense request
class Expense(BaseModel):
    description: str
    amount: float

# Route to add a new expense
@app.post("/add-amount")
async def add_amount(expense: Expense):
    # Load existing data from file
    amounts = load_amounts()
    
    # Add the new expense to the list
    amounts.append({
        "description": expense.description,
        "amount": expense.amount
    })
    
    # Save the updated list back to the file
    save_amounts(amounts)
    
    return {"message": "Expense added successfully", "expense": expense}

# Route to view all expenses
@app.get("/view-amounts")
async def view_amounts():
    # Load the data from the file
    amounts = load_amounts()
    
    return {"amounts": amounts}

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)
