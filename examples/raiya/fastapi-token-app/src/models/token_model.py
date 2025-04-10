from pydantic import BaseModel

# This class is used to obtaining a token
class TokenRequest(BaseModel):
    username: str

# This class represents the response that will be returned
class TokenResponse(BaseModel):
    token: str

#This class for validating a token.
class TokenValidationResponse(BaseModel):
    valid: bool
    username: str = None