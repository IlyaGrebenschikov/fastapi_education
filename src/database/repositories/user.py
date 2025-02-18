from typing import Type, Optional

from src.database.repositories.base import BaseRepository
from src.common.dto import UserSchema
from src.database.models import UserModel


class UserRepository(BaseRepository[UserModel]):
    @property
    def model(self) -> Type[UserModel]:
        return UserModel

    async def create(self, **data: UserSchema) -> Optional[UserModel]:
        return await self._crud.insert(**data)

    async def get_one(
            self,
            user_id: Optional[int] = None,
            login: Optional[str] = None,
    ) -> Optional[UserModel]:
        clause = self.model.id == user_id if user_id else self.model.login == login

        return await self._crud.select(clause)

    async def update(self, user_id: Optional[int], **data: UserSchema) -> Optional[UserModel]:
        clause = self.model.id == user_id

        return await self._crud.update(clause, **data)

    async def delete(self, user_id: Optional[int]) -> Optional[UserModel]:
        clause = self.model.id == user_id

        return await self._crud.delete(clause)
