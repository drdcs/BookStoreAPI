import os
import logging
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from .configs.config import Settings
from .utils import core

log = logging.getLogger("uvicorn")


def get_application():
    settings = Settings()
    app = FastAPI(title=settings.title, 
                  description="Backend for the BookStore",
                  version=settings.version)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_event_handler("startup", core.create_start_app_handler(app))
    app.add_event_handler("shutdown", core.create_stop_app_handler(app))
    return app

app = get_application()
