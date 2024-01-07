# test_jwt.py
from jwtHandler import create_access_token, verify_token

def test_create_access_token():
    username = "test_user"
    token = create_access_token(data={"sub": username})
    assert token is not None

def test_verify_token():
    username = "test_user"
    token = create_access_token(data={"sub": username})
    payload = verify_token(token)
    assert payload is not None
    assert payload.get("sub") == username

def test_verify_token_invalid():
    invalid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0X3VzZXIifQ.invalid_signature"
    payload = verify_token(invalid_token)
    assert payload is None
