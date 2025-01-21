from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.api.common.providers import Stub
from src.services import ServiceGateway
from src.common.dto import UserInDBSchema


class GetUserFromLoginHandler:
    def __init__(
            self,
            gateway: Annotated[ServiceGateway, Depends(Stub(ServiceGateway))],
    ) -> None:
        self._gateway = gateway

    async def execute(self, query: OAuth2PasswordRequestForm) -> UserInDBSchema:
        async with self._gateway:
            fetched_user = await self._gateway.user_db().get(login=query.username)

        return fetched_user
    