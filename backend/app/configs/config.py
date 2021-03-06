import logging
import os
from functools import lru_cache
from pydantic import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: int = os.getenv("TESTING", 0)
    title: str = os.getenv("TITLE")
    version: str = os.getenv("VERSION")
    database_uri_test: str = os.getenv("DATABASE_URI_TEST")
    database_uri_prod: str = os.getenv("DATABASE_URI_PROD")
    
@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()