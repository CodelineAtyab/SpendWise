# serverApp.py
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Import functions from mainApp.py
from mainApp import read_transactions, add_amount

app = FastAPI()

# Pydantic model for adding an amount
class Amount(BaseModel):
    amount: float

@app.get("/view-amount")
def my_func():
    return {"message": read_transactions}

@app.get("/sum")
def sum(num1, num2):
  return {"result": add_amount(int(num1) + int(num2))}

@app.get("/view-amount")
def view_amount():
    try:
        transactions = read_transactions()
        return {"transactions": transactions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/add-amount")
def add_amount_route(amount: Amount):
    try:
        result = add_amount(amount.amount)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
