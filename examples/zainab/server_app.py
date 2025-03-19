import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
import pycountry

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

@app.get("/country_origin")
def country_origin(name: str):
    response = requests.get("https://api.nationalize.io", params={"name": name})
    data = response.json()
    for country in data.get("country", []):
        country_id = country.get("country_id")
        country_obj = pycountry.countries.get(alpha_2=country_id)
        country["country_name"] = country_obj.name if country_obj else country_id
    return data

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=80)