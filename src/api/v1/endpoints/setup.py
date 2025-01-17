from fastapi import FastAPI

from src.core import log
from src.api.v1.endpoints.user import user_router


def setup_routers(app: FastAPI) -> None:
    log.debug('Initialize API endpoints')
    
    app.include_router(user_router)
    