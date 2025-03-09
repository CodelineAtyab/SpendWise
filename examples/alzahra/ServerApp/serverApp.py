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

#@app.get("/add-amount")
#def my_func():
 #   return {"message":add_amount(15)}

@app.get("/view-amount")
def view_amount():
    try:
        transactions = read_transactions()
        return {"transactions": transactions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/add-amount")
def add_amount_query(amount: float):
    """Adds an amount via a URL query parameter."""
    try:
        result = add_amount(amount)  
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
