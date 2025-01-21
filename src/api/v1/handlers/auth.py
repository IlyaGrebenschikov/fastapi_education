from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.api.common.providers import Stub
from src.services.security import BcryptHasher, TokenJWT
from src.services import ServiceGateway
from src.common.dto import UserInDBSchema, Token


class AuthHandler:
    def __init__(
        self,
        gateway: Annotated[ServiceGateway, Depends(Stub(ServiceGateway))],
        hasher: Annotated[BcryptHasher, Depends(Stub(BcryptHasher))],
        jwt: Annotated[TokenJWT, Depends(Stub(TokenJWT))]
    ) -> None:
        self._gateway = gateway
        self._hasher = hasher
        self._jwt = jwt
    
    async def execute(self, current_user: UserInDBSchema, query: OAuth2PasswordRequestForm) -> Token:
        return await self._gateway.auth(self._hasher, self._jwt).generate_token(current_user, query)
