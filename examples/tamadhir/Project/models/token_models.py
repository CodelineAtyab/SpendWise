from pydantic import BaseModel

class TokenRequest(BaseModel):
    username: str

class TokenResponse(BaseModel):
    token: str

class ValidationResponse(BaseModel):
    is_valid: bool