from fastapi import FastAPI

from src.core import Settings, log
from src.database.core import create_engine, create_async_session_maker, TransactionManager
from src.database import create_database_factory, DBGateway


def setup_dependencies(app: FastAPI, settings: Settings) -> None:
    log.debug('Initialize API dependencies')
    
    engine = create_engine(settings.database.url_obj)
    session = create_async_session_maker(engine)
    db_factory = create_database_factory(TransactionManager, session)
    
    app.dependency_overrides[DBGateway] = db_factory
