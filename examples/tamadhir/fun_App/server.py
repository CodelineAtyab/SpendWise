import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import requests
import pycountry

# Initialize FastAPI app
app = FastAPI()

# Mount the "img" directory to serve images
app.mount("/img", StaticFiles(directory="img"), name="img")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the index.html file
@app.get("/home")
def home():
    return FileResponse("index.html")

# Country origin API
@app.get("/country_origin")
def country_origin(name: str = "abdullah"):
    response = requests.get("https://api.nationalize.io", params={"name": name})
    data = response.json()

    # Replace country_id with full country name
    for country in data.get("country", []):
        cid = country.get("country_id")
        if cid:
            cdata = pycountry.countries.get(alpha_2=cid)
            country["country_name"] = cdata.name if cdata else cid
    return data

# Gender API endpoint
@app.get("/gender")
def get_gender(name: str):
    response = requests.get("https://api.genderize.io", params={"name": name})
    data = response.json()

    # Check if gender exists
    return {"gender": data.get("gender", "unknown")}

# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
