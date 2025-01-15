from fastapi import FastAPI

from src.core import AppSettings, log


def init_app(settings: AppSettings):
    log.debug('Initialize API')
    
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOC_URL
    )
    
    return app
