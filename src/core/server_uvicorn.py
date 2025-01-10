import uvicorn
from fastapi import FastAPI

from src.core.settings import UvicornServerSettings


def run_uvicorn_server(app: FastAPI, settings: UvicornServerSettings):
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
