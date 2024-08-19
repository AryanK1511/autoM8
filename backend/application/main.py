from fastapi import FastAPI
from routes import get
from data.database import create_all_tables
from .logging_config import setup_logging

# Import all database models
from data.models.automation import Automation

# Creates app instance
app = FastAPI()

# Initialize logging
setup_logging()

# Initialize the FastAPI router
app.include_router(get.router)

# Create all the PostgreSQL tables
create_all_tables()
