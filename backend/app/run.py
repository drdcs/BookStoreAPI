import os
import logging
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from .configs.config import Settings, get_settings
from .utils import tasks
from .utils.db_objects import get_db_connection

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
    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))
    return app

app = get_application()
