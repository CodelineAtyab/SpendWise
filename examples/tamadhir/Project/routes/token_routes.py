from fastapi import APIRouter, HTTPException
from models.token_models import TokenRequest, TokenResponse, ValidationResponse
from app_utils.token_helper import generate_token, validate_token

router = APIRouter()

@router.post("/token/generate", response_model=TokenResponse)
def generate_token_endpoint(request: TokenRequest):
    """
    Generate a token for the given username.
    """
    token = generate_token(request.username)
    return {"token": token}

@router.get("/token/validate", response_model=ValidationResponse)
def validate_token_endpoint(token: str):
    """
    Validate the provided token.
    """
    is_valid = validate_token(token)
    if not is_valid:
        # Log the invalid token for debugging purposes
        print(f"Invalid token received: {token}")
        raise HTTPException(status_code=400, detail="Invalid token")
    return {"is_valid": True}