from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from application.config import get_settings

# Fetch all the database settings from the config file
settings = get_settings()

# Base class for models
Base = declarative_base()

# Create the engine using the appropriate database URL
engine = create_engine(settings.get_database_url())

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency for FastAPI to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Script to create all the tables based on the models defined
def create_all_tables():
    Base.metadata.create_all(bind=engine)
