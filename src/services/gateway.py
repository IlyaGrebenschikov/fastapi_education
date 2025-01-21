from src.common.interfaces import BaseGateway
from src.database import DBGateway
from src.services.user_db import UserDBService
from src.services.security import BcryptHasher, AuthService, TokenJWT


class ServiceGateway(BaseGateway):
    def __init__(self, database: DBGateway) -> None:
        self.database = database
        super().__init__(database)

    def user_db(self) -> UserDBService:
        return UserDBService(self.database.user())
    
    def auth(self, hasher: BcryptHasher, jwt: TokenJWT):
        return AuthService(hasher, jwt)
