import json
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import requests
import pycountry
import os  # Add os module for path handling

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

# Mount static directory to serve files of any size
# Files will be available at /static/{filename}
# Define base directory and static directory paths
base_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(base_dir, "static")

# Mount static directory using absolute path
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Serve the index.html file using the absolute path
@app.get("/home")
def home():
  index_path = os.path.join(static_dir, "index.html")
  return FileResponse(index_path)

@app.get("/country_origin")
def country_origin(name: str = "abdullah"):
    # Call external API with the provided name
    # response = requests.get("https://api.nationalize.io", params={"name": name})
    data = json.loads('{"count":201453,"name":"abdullah","country":[{"country_id":"MY","probability":0.1345583001474345},{"country_id":"SA","probability":0.050729740052967064},{"country_id":"KW","probability":0.04006473303096316},{"country_id":"PK","probability":0.039340773722441685},{"country_id":"BN","probability":0.034211567583257135}]}')
    # Replace country_id with full country name using pycountry
    for country in data.get("country", []):
        cid = country.get("country_id")
        if cid:
            cdata = pycountry.countries.get(alpha_2=cid)
            country["country_name"] = cdata.name if cdata else cid
    return data

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8080)
