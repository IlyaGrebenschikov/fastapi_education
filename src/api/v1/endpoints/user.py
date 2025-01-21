from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException

from src.common.dto import UserSchema, UserResponseSchema
from src.common.exceptions import ConflictException
from src.api.common.docs import ConflictError
from src.api.v1.handlers.user import CreateUserHandler


user_router = APIRouter(prefix='/api/v1/user', tags=['user'])


@user_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponseSchema,
    response_description='User resource created',
    description='Creates a User resource',
    summary='Creates a User resource',
    responses={
        status.HTTP_409_CONFLICT: {'model': ConflictError},
    },
)
async def create_user(
        body: UserSchema,
        handler: Annotated[CreateUserHandler, Depends(CreateUserHandler)],
) -> UserResponseSchema:
    try:
        return await handler.execute(body)

    except ConflictException as conflict_error:
        raise HTTPException(status.HTTP_409_CONFLICT, conflict_error.get_dict())
