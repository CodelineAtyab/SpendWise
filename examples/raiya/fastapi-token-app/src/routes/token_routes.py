from fastapi import APIRouter, HTTPException
from src.utils.token_helper import create_access_token, verify_token 
from src.models.token_model import TokenRequest, TokenResponse, TokenValidationResponse

router = APIRouter()

#This endpoint generates an access token based on the username provided in the request. It uses the POST method.
@router.post("/token/generate", response_model=TokenResponse)
def generate_token(request: TokenRequest):
    if not request.username:
        raise HTTPException(status_code=400, detail="Username is required")
    token = create_access_token({'username': request.username})
    return TokenResponse(token=token)

#This endpoint is used to validate an access token by verifying its authenticity. It uses the GET method.
@router.get("/token/validate", response_model=TokenValidationResponse)
def validate_token_endpoint(token: str):
    valid, username =  verify_token (token)
    return TokenValidationResponse(valid=valid, username=username) if valid else TokenValidationResponse(valid=False)

