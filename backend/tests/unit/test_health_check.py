import pytest
from fastapi.testclient import TestClient

from application.main import app


@pytest.fixture(scope="module")
def client(get_auth0_access_token):
    """Fixture to provide a TestClient with the Auth0 token in the header."""
    client = TestClient(app)
    client.headers.update({"Authorization": f"Bearer {get_auth0_access_token}"})
    return client


def test_unauthenticated_health_check(client):
    response = client.get("/v1/api/autoM8/unauth")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "data": {
            "message": "From unauth health check route, autoM8 is up and running!",
            "author": "Aryan Khurana",
            "github_url": "https://github.com/AryanK1511/autoM8",
            "version": "0.0.1",
            "hostname": "Aryans-MacBook-Pro.local",
        },
    }


def test_authenticated_health_check(client):
    response = client.get("/v1/api/autoM8/auth")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "data": {
            "message": "From auth health check route, autoM8 is up and running!",
            "author": "Aryan Khurana",
            "github_url": "https://github.com/AryanK1511/autoM8",
            "version": "0.0.1",
            "hostname": "Aryans-MacBook-Pro.local",
        },
    }
