import os
import logging
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from .configs.config import Settings, get_settings

log = logging.getLogger("uvicorn")


def get_application(settings: Settings = Depends(get_settings)):
    app = FastAPI(title=os.getenv("TITLE"), 
                  description="Backend for the BookStore",
                  version=os.getenv("VERSION"))
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = get_application()