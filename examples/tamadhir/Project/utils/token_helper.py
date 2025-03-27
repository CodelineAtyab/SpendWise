import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"  # Replace with a secure key
ALGORITHM = "HS256"

def generate_token(username: str) -> str:
    """
    Generate a JWT token for the given username.
    """
    expiration = datetime.utcnow() + timedelta(hours=1)  # Token valid for 1 hour
    payload = {"sub": username, "exp": expiration}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def validate_token(token: str) -> bool:
    """
    Validate the provided JWT token.
    """
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False