import os
from fastapi import Depends, FastAPI
from databases import Database
from ..configs.config import Settings, get_settings
import logging

logger = logging.getLogger(__name__)


async def connect_to_db(app: FastAPI) -> None:
    if os.getenv("TESTING") == 1:
        db_url=os.environ.get("DATABASE_URI_TEST")
    else:
        db_url=os.environ.get("DATABASE_URI_PROD")
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
        db_url=os.environ.get("DATABASE_URI_TEST")
        db = Database(db_url)
        return db
    else:
        db_url=os.environ.get("DATABASE_URI_PROD")
        db = Database(db_url)
        return db