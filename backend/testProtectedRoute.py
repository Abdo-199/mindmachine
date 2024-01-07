from api import API
import pytest
from auth_utils import get_current_user
from fastapi.testclient import TestClient
from fastapi import HTTPException

app = API().app

app.dependency_overrides[get_current_user] = lambda: {"username": "test_user"}
client = TestClient(app)

def test_protected_route_authenticated():
    response = client.get("/protected_route")
    assert response.status_code == 200
    assert response.json() == {"message": "You are accessing a protected route", "user": "test_user"}

@pytest.mark.asyncio
async def test_get_current_user_unauthenticated():
    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(token="")
    assert excinfo.value.status_code == 401
