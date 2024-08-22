import os

import httpx
import pytest
from dotenv import load_dotenv

load_dotenv()

"""
    This fixture is used to obtain an access token from Auth0. The token is used to authenticate requests to the API.
"""


@pytest.fixture(scope="session", autouse=True)
def get_auth0_access_token():
    url = f"{os.getenv('AUTH0_ISSUER')}oauth/token"
    payload = {
        "client_id": os.getenv("AUTH0_CLIENT_ID"),
        "client_secret": os.getenv("AUTH0_CLIENT_SECRET"),
        "audience": os.getenv("AUTH0_API_AUDIENCE"),
        "grant_type": "client_credentials",
    }
    headers = {"Content-Type": "application/json"}
    response = httpx.post(url, json=payload, headers=headers)
    response.raise_for_status()

    token = response.json().get("access_token")

    if not token:
        raise RuntimeError("Failed to obtain access token from Auth0")

    return token
