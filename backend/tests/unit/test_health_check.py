import pytest
from fastapi.testclient import TestClient

from application.main import app

"""
    Fixture to provide a TestClient with the Auth0 token in the header.
"""


@pytest.fixture(scope="module")
def client(get_auth0_access_token):
    client = TestClient(app)
    client.headers.update({"Authorization": f"Bearer {get_auth0_access_token}"})
    return client


"""
    Tests the health check route that does not require authentication.
"""


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


"""
    Tests the health check route that requires authentication.
"""


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


"""
    Tests the health check route that requires authentication but an invalid token is provided.
"""


def test_authenticated_health_check_invalid_token(client):
    client.headers.update({"Authorization": "Bearer invalid_token"})
    response = client.get("/v1/api/autoM8/auth")
    assert response.status_code == 403
    assert response.json() == {
        "status": "error",
        "error": {"code": 403, "message": "Not enough segments"},
    }


"""
    Tests the health check route that requires authentication but an invalid token format is provided.
"""


def test_authenticated_health_check_invalid_token_format(client):
    client.headers.update(
        {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJfcTVhcEZNUV84eXVmdk5Yci1zNCJ9.eyJpc3MiOiJodHRwczovL2Rldi11emY1cHVrMmJzeHNiZXVqLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnVGR5dVpzZVhSUUpDRTV0ZWxKbWdxQ2p1dkZUdjYxSkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9hdXRvTTgtYmFja2VuZC5jb20iLCJpYXQiOjE3MjQyODk4NTYsImV4cCI6MTcyNDM3NjI1NiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwiYXpwIjoiZ1RkeXVac2VYUlFKQ0U1dGVsSm1ncUNqdXZGVHY2MUoifQ.fSwF9cwb03yZaD4v_-qaINBN27GFnz_o04CGxpXP4ZyBbNc551fGm7hGRGTtFntQIubbe3-ARqW_bgCdwZOVocEgJa-zsKyCJEoQP9UWUOnmuhslrMtUx3hhCpdUW-F5D3OYrAtGu0XwnNbJ6O-wDuegsHOmV1AKPvSrF7fowfpQfHeMcTOLRFO5r6ShKTiXwLQPyuVa6hAwpq_GqZObJLGK-pVpQ_5QbKZmc8GN8cH2mQfrvkItI6mwcJanmOeNpzFq93gMk9DcnqQF5DitUnr7W4obhH2fRcn6OP-obgsZHKysK3mjlZLXYbbyYIxRq-Jmp7a0haeIeUs8LOug7Q"
        }
    )
    response = client.get("/v1/api/autoM8/auth")
    assert response.status_code == 403
    assert response.json() == {
        "status": "error",
        "error": {"code": 403, "message": "Signature verification failed"},
    }


"""
    Tests the health check route that requires authentication but no token in provided.
"""


def test_authenticated_health_check_no_token(client):
    client.headers.pop("Authorization")
    response = client.get("/v1/api/autoM8/auth")
    assert response.status_code == 403
    assert response.json() == {
        "status": "error",
        "error": {
            "code": 403,
            "message": "Not authenticated",
        },
    }
