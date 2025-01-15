import uvicorn
from fastapi import FastAPI

from src.core.settings import UvicornServerSettings
from src.core.logger import log


def run_uvicorn_server(app: FastAPI, settings: UvicornServerSettings):
    log.info('Running API')
    
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
