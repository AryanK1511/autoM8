from fastapi import FastAPI
from routes import get

# Creates app instance
app = FastAPI()

app.include_router(get.router)
