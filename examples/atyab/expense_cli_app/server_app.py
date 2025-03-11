import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
origins = ["*"]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,  # Allows all origins
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Serve the index.html file located in the current directory
@app.get("/home")
def home():
  return FileResponse("index.html")

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=80)
