import pytest
from fastapi.testclient import TestClient
from starlette import status
from src.session_13.main import api

@pytest.fixture(scope="session")
def client():
    return TestClient(api)

def test_api_create_Task(client):
    response = client.post("/task")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() is not None