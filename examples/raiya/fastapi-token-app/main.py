from fastapi import FastAPI
from src.routes.token_routes import router as token_router

app = FastAPI()

app.include_router(token_router)

@app.get("/home")
def read_root():
    return {"message": "Welcome to the Token Service!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)