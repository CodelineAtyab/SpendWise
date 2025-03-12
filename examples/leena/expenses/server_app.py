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
def country_origin(name: str = "abdullah"):
    # Call external API with the provided name
    response = requests.get("https://api.nationalize.io", params={"name": name})
    data = response.json()
    # Replace country_id with full country name using pycountry
    for country in data.get("country", []):
        cid = country.get("country_id")
        if cid:
            cdata = pycountry.countries.get(alpha_2=cid)
            country["country_name"] = cdata.name if cdata else cid
    return data

@app.get("/gender")
def gender(name: str):
    # Call external API to get gender
    response = requests.get("https://api.genderize.io", params={"name": name})
    return response.json()

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=80)
