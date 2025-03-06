from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()


FILE_PATH = 'amounts.json'


if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'w') as f:
        json.dump([], f)

class Amount(BaseModel):
    value: float

def read_amounts() -> List[float]:
    """Read all amounts from the file."""
    with open(FILE_PATH, 'r') as f:
        return json.load(f)

def write_amounts(amounts: List[float]):
    """Write amounts to the file."""
    with open(FILE_PATH, 'w') as f:
        json.dump(amounts, f)

@app.post("/add-amount/{amount}")
async def add_amount(amount: float):
    """Add an amount to the stored list."""
    amounts = read_amounts()
    amounts.append(amount)
    write_amounts(amounts)
    return {"message": f"Amount {amount} added successfully"}

@app.get("/view-amount")
async def view_amount():
    """View all stored amounts."""
    amounts = read_amounts()
    return {"amounts": amounts}
