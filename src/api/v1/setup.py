from fastapi import FastAPI

from src.core import AppSettings


def init_app(settings: AppSettings):
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOC_URL
    )
    
    return app
