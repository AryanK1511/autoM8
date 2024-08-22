import os

import httpx
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def get_auth0_access_token():
    # Define the URL and payload for the Auth0 token request
    url = f"{os.getenv('AUTH0_ISSUER')}oauth/token"
    payload = {
        "client_id": os.getenv("AUTH0_CLIENT_ID"),
        "client_secret": os.getenv("AUTH0_CLIENT_SECRET"),
        "audience": os.getenv("AUTH0_API_AUDIENCE"),
        "grant_type": "client_credentials",
    }
    headers = {"Content-Type": "application/json"}

    # Make the request to Auth0
    response = httpx.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Ensure we raise an error for bad responses

    # Extract the access token from the response
    token = response.json().get("access_token")

    if not token:
        raise RuntimeError("Failed to obtain access token from Auth0")

    # Store the token in a global fixture
    return token
