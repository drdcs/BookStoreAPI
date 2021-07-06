
import os

import pytest
from starlette.testclient import TestClient
from app.configs.config import get_settings, Settings
from fastapi import FastAPI
from app.run import get_application
from databases import Database


os.environ["TESTING"] = "1"

# Create a new application for testing
@pytest.fixture
def app() -> FastAPI:
    return get_application()


# Grab a reference to our database when needed
@pytest.fixture
def db(app: FastAPI) -> Database:
    return app.state._db




