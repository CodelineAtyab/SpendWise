import uvicorn
from transaction_manager import add_amount, view_amount

from fastapi import FastAPI

app = FastAPI()

@app.get("/add-amount")
def add_amount(amount: float):
    add_amount(amount)
    return {"message": "Amount added successfully!"}

@app.get("/view-amount")
def view_amount():
    return {"transactions": view_amount()}

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8888)
