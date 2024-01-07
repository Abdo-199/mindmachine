# auth_utils.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwtHandler import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    return payload
