import os
from fastapi import FastAPI
from sqlmodel import SQLModel
from starlette.middleware.cors import CORSMiddleware
from api.api import api_router
from database.database import engine

SQLModel.metadata.create_all(engine)

def create_app() -> FastAPI:
    app_title = os.environ["APP_TITLE"]
    app_version = os.environ["APP_VERSION"]

    app = FastAPI(title=app_title, version=app_version)

    # CORS
    app.add_middleware(
        CORSMiddleware
    )

    app.include_router(api_router, prefix="/api")

    return app

app = create_app()