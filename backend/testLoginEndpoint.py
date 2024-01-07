from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from api import API  # Ensure this is the correct import for your FastAPI app instance

client = TestClient(API().app)

@patch('api.Connection', return_value=MagicMock(bind=MagicMock(return_value=True)))
@patch('api.Server')
def test_login_success(mock_server, mock_conn):
    response = client.post("/login", json={"username": "valid_user", "password": "valid_password"})
    assert response.status_code == 200
    assert "access_token" in response.json()

@patch('api.Connection', return_value=MagicMock(bind=MagicMock(return_value=False)))
@patch('api.Server')
def test_login_failure(mock_server, mock_conn):
    response = client.post("/login", json={"username": "invalid_user", "password": "invalid_password"})
    assert response.status_code == 401
