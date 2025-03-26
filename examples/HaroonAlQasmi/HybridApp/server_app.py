import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
import pycountry

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the frontend HTML file at the root endpoint
@app.get("/")
def home():
    return FileResponse("index.html")

# Endpoint to fetch top five country origins for a given name
@app.get("/country_origin")
def country_origin(name: str):
    # Call the nationalize API
    response = requests.get("https://api.nationalize.io", params={"name": name})
    data = response.json()
    countries = data.get("country", [])
    # Sort countries by descending probability and select the top five
    countries.sort(key=lambda x: x.get("probability", 0), reverse=True)
    top_countries = countries[:5]
    # Replace country codes with full country names using pycountry
    for country in top_countries:
        cid = country.get("country_id")
        if cid:
            cdata = pycountry.countries.get(alpha_2=cid)
            country["country_name"] = cdata.name if cdata else cid
    return {"country": top_countries}

# Endpoint to fetch gender information for a given name
@app.get("/gender")
def get_gender(name: str):
    # Call the genderize API
    response = requests.get("https://api.genderize.io", params={"name": name})
    data = response.json()
    return {"gender": data.get("gender"), "probability": data.get("probability")}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
