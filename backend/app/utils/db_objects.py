import os
from fastapi import Depends, FastAPI
from databases import Database
from ..configs.config import Settings
import logging

logger = logging.getLogger(__name__)

settings = Settings()

async def connect_to_db(app: FastAPI) -> None:
    if os.getenv("TESTING") == 1:
        db_url=settings.database_uri_test
    else:
        db_url=settings.database_uri_prod
    database = Database(db_url, min_size=2, max_size=10)  # these can be configured in config as well

    try:
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warn("--- DB CONNECTION ERROR ---")
        logger.warn(e)
        logger.warn("--- DB CONNECTION ERROR ---")


async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("--- DB DISCONNECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DB DISCONNECT ERROR ---")


async def get_db_connection():
    if os.getenv("TESTING") == 1:
        db_url=settings.database_uri_test
        db = Database(db_url)
        return db
    else:
        db_url=settings.database_uri_prod
        db = Database(db_url)
        return db