import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/my_func")
def my_func():
  return {"message": "Hello,This is comming from Alzahra, Team Abtal A-Digital!!!"}

@app.get("/sum")
def sum(num1, num2):
  return {"result": int(num1) + int(num2)}

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8888)
