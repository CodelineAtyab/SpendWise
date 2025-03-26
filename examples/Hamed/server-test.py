import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

# File path where the amounts will be stored
FILE_PATH = "./data_store.txt"

# Ensure the data file exists
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as f:
        f.write("")  # Creating an empty file if it does not exist

# FastAPI instance
app = FastAPI()

# Pydantic model to handle amount input
class Amount(BaseModel):
    amount: float

@app.get("/my_func")
def my_func():
    return {"message": "Hello team, Welcome!!!"}

@app.get("/sum")
def sum_numbers(num1: int = 10, num2: int = 25):
    result = num1 + num2
    return {"result": result}

@app.post("/add-amount")
def add_amount(amount: Amount):
    try:
        # Append the new amount to the file
        with open(FILE_PATH, "a") as f:
            f.write(f"{amount.amount}\n")
        return {"message": f"Added amount: {amount.amount}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding amount: {e}")

@app.get("/view-amount")
def view_amount():
    try:
        # Read all amounts from the file
        with open(FILE_PATH, "r") as f:
            amounts = f.readlines()
        
        # If there are no amounts, return a message
        if not amounts:
            return {"message": "Enter the amounts."}
        
        # Clean up the amounts list (remove any trailing newlines and convert to floats)
        amounts = [float(amount.strip()) for amount in amounts]
        return {"amounts": amounts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error viewing amounts: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
