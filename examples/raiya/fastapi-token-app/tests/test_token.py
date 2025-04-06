import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#checks if the /token/generate endpoint correctly generates a token when a valid username is provided.
def test_generate_token():
    response = client.post("/token/generate", json={"username": "testuser"})
    assert response.status_code == 200
    assert "token" in response.json()

# This test validates a token by first generating a token and then validating it.
def test_validate_token_valid():
    response = client.post("/token/generate", json={"username": "testuser"})
    token = response.json()["token"]
    
    response = client.get("/token/validate", params={"token": token})
    assert response.status_code == 200
    assert response.json() == {"valid": True}

#This test checks the behavior of the API when an invalid token is provided.
def test_validate_token_invalid():
    response = client.get("/token/validate", params={"token": "invalidtoken"})
    assert response.status_code == 200
    assert response.json() == {"valid": False}