from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from src.core import Settings, log
from src.database.core import create_engine, create_async_session_maker, TransactionManager
from src.database import create_database_factory
from src.services import create_service_gateway_factory, ServiceGateway
from src.services.security import TokenJWT, BcryptHasher, get_pwd_context
from src.common.tools import singleton


def setup_dependencies(app: FastAPI, settings: Settings) -> None:
    log.debug('Initialize API dependencies')
    
    engine = create_engine(settings.database.url_obj)
    session = create_async_session_maker(engine)
    db_factory = create_database_factory(TransactionManager, session)
    
    jwt_token = TokenJWT(settings.jwt)
    bcrypt_pwd_context = get_pwd_context(['bcrypt'])
    bcrypt_hasher = BcryptHasher(bcrypt_pwd_context)
    
    service_factory = create_service_gateway_factory(db_factory)
    
    app.dependency_overrides[TokenJWT] = singleton(jwt_token)
    app.dependency_overrides[BcryptHasher] = singleton(bcrypt_hasher)
    app.dependency_overrides[ServiceGateway] = service_factory


oauth2_scheme = OAuth2PasswordBearer('/api/v1/token')
