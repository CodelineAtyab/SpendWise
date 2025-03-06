import uvicorn
from main import view_amount, add_amount
from fastapi import FastAPI

app = FastAPI()

@app.get("/view-amount")
def my_func():
  return {"message":view_amount}

@app.get("/add-amount")
def add_amount():
  return {"message":add_amount}

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8888)
