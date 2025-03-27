from fastapi import FastAPI
from routes.token_routes import router as token_router
import uvicorn

app = FastAPI()

# Include token routes
app.include_router(token_router)

@app.get("/home")
def read_root():
    return {"message": "Welcome to the Token Service!"}

# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5555)
