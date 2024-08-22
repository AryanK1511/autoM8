import logging
from functools import lru_cache

from pydantic_settings import BaseSettings

from .logging_config import setup_logging


class Settings(BaseSettings):
    # Setup logging
    setup_logging()

    # Auth0 Configuration
    auth0_domain: str
    auth0_api_audience: str
    auth0_issuer: str
    auth0_algorithms: str
    auth0_client_id: str
    auth0_client_secret: str

    # Database Configuration
    database_env: str = "local"  # Default to 'local', can be 'production'
    local_database_url: str
    rds_database_url: str

    class Config:
        env_file = ".env"

    def get_database_url(self) -> str:
        """Return the appropriate database URL based on the environment."""
        if self.database_env == "production":
            logging.info("Using RDS database URL")
            return self.rds_database_url
        logging.info("Using local database URL")
        return self.local_database_url


@lru_cache()
def get_settings() -> Settings:
    return Settings()
