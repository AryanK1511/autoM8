"""
A successful response looks like:
{
    "status": "ok",
    ...
}
"""


def create_success_response(data):
    return {"status": "ok", **data}


"""
An error response looks like:
{
    "status": "error",
    "error": {
        "code": 400,
        "message": "invalid request, missing ...",
    }
}
"""


def create_error_response(code, message):
    return {"status": "error", "error": {"code": code, "message": message}}
