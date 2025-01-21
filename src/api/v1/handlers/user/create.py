from typing import Annotated

from fastapi import Depends

from src.api.common.providers import Stub
from src.common.dto import UserSchema, UserResponseSchema
from src.services.security import BcryptHasher
from src.services import ServiceGateway


class CreateUserHandler:
    def __init__(
            self,
            hasher: Annotated[BcryptHasher, Depends(Stub(BcryptHasher))],
            gateway: Annotated[ServiceGateway, Depends(Stub(ServiceGateway))]
    ) -> None:
        self._gateway = gateway
        self._hasher = hasher

    async def execute(self, query: UserSchema) -> UserResponseSchema:
        async with self._gateway:
            await self._gateway.database.manager.create_transaction()
            
            return await self._gateway.user_db().create(query, self._hasher)
