import socket

from fastapi import APIRouter, Security

from application.response import create_success_response
from application.utils import VerifyToken

router = APIRouter()
auth = VerifyToken()

"""
Health Check Route - Unauthenticated
"""


@router.get("/v1/api/autoM8/unauth")
def unauthenticated_health_check():
    return create_success_response(
        {
            "data": {
                "message": "From unauth health check route, autoM8 is up and running!",
                "author": "Aryan Khurana",
                "github_url": "https://github.com/AryanK1511/autoM8",
                "version": "0.0.1",
                "hostname": socket.gethostname(),
            }
        }
    )


"""
Health Check Route - Authenticated
"""


@router.get("/v1/api/autoM8/auth")
def authenticated_health_check(auth_result: str = Security(auth.verify)):
    return create_success_response(
        {
            "data": {
                "message": "From auth health check route, autoM8 is up and running!",
                "author": "Aryan Khurana",
                "github_url": "https://github.com/AryanK1511/autoM8",
                "version": "0.0.1",
                "hostname": socket.gethostname(),
            }
        }
    )
