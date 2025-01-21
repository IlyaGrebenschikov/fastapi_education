from sqlalchemy.exc import IntegrityError

from src.core import log
from src.common.dto.user import UserSchema, UserResponseSchema, UpdateUserQuerySchema, UserInDBSchema
from src.services.security import BcryptHasher
from src.database.repositories import UserRepository
from src.database import from_model_to_dto, none_filter
from src.common.exceptions import NotFoundException, ConflictException


class UserDBService:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def create(self, data: UserSchema, hasher: BcryptHasher) -> UserResponseSchema:
        data.password = hasher.hash_password(data.password)
        
        try:
            return from_model_to_dto(await self._repository.create(**data.model_dump()), UserResponseSchema)
        
        except IntegrityError as ie:
            log.error(f'IntegrityError - {ie}')
            raise ConflictException('This user already exists')

    async def update(
            self,
            data: UpdateUserQuerySchema,
            user_id: int,
            hasher: BcryptHasher,
    ) -> UserResponseSchema:
        filtered_data = none_filter(data)
        
        if filtered_data.get('password'):
            filtered_data['password'] = hasher.hash_password(filtered_data['password'])

        result = await self._repository.update(user_id, **filtered_data)
        
        return from_model_to_dto(result, UserResponseSchema)

    async def get(self, user_id: int) -> UserInDBSchema:
        result = await self._repository.get_one(user_id=user_id)

        if not result:
            raise NotFoundException('User not found')

        converted_result = from_model_to_dto(result, UserInDBSchema)

        return converted_result

    async def delete(self, user_id: int) -> UserResponseSchema:
        result = await self._repository.delete(user_id)
        
        return from_model_to_dto(result, UserResponseSchema)
