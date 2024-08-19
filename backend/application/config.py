from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Auth0 Configuration
    auth0_domain: str
    auth0_api_audience: str
    auth0_issuer: str
    auth0_algorithms: str

    # Database Configuration
    database_env: str = "local"  # Default to 'local', can be 'production'
    local_database_url: str
    rds_database_url: str

    class Config:
        env_file = ".env"

    def get_database_url(self) -> str:
        """Return the appropriate database URL based on the environment."""
        if self.database_env == "production":
            return self.rds_database_url
        return self.local_database_url


@lru_cache()
def get_settings() -> Settings:
    return Settings()
