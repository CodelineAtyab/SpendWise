from fastapi.testclient import TestClient
from main import app
from utils.token_helper import generate_token
from unittest.mock import patch
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
secret_key = os.getenv("SECRET_KEY")
database_url = os.getenv("DATABASE_URL")

print(f"Secret Key: {secret_key}")
print(f"Database URL: {database_url}")

client = TestClient(app)

def test_generate_token():
    with patch("utils.token_helper.generate_token", return_value="mocked_token"):
        response = client.post("/token/generate", json={"username": "testuser"})
    assert response.status_code == 200
    assert "token" in response.json()

def test_validate_token():
    # Generate a valid token
    token = generate_token("testuser")
    response = client.get(f"/token/validate?token={token}")
    assert response.status_code == 200
    assert response.json() == {"is_valid": True}

def test_validate_invalid_token():
    response = client.get("/token/validate?token=invalidtoken")
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid token"