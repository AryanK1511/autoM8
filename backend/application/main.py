from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from data.database import create_all_tables
from routes import get, health_check

from .response import create_error_response

# Import all database models

# Creates app instance
app = FastAPI()


"""
    Custom exception handler for HTTPException.
    This handler intercepts all HTTPExceptions raised in the application and 
    returns a response in your custom error format.
"""


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    # Use your custom error response structure
    error_response = create_error_response(exc.status_code, exc.detail)
    return JSONResponse(status_code=exc.status_code, content=error_response)


"""
    Middleware that wraps around every HTTP request to catch and handle any 
    uncaught exceptions that might occur during request processing.
"""


@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception:
        # Generic exception handling for unexpected errors
        error_response = create_error_response(
            status_code=500, message="Internal Server Error"
        )
        return JSONResponse(status_code=500, content=error_response)


# Initialize the FastAPI router
app.include_router(get.router)
app.include_router(health_check.router)


# Create all the PostgreSQL tables
create_all_tables()
