import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware  # Import the CORS middleware

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # Allow requests from all origins
  allow_credentials=True,
  allow_methods=["*"],  # Allow all methods
  allow_headers=["*"],  # Allow all headers
)

data = []

@app.get("/vowels", response_class=JSONResponse)
def get_vowels_count(request: Request):
  vowel_count = 0

  for char in request.query_params.get("sentence"):
    if char.lower() in ["a", "e", "i", "o", "u"]:
      vowel_count += 1

  return {"vowel_count": vowel_count, "status": "success"}

@app.post("/vowels", response_class=JSONResponse)
def save_vowel_count():
  data.append("a")
  return {"msg": "successfully saved!"}


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)