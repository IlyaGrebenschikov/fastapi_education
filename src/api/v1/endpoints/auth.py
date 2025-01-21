from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.api.v1.handlers import AuthHandler
from src.api.v1.handlers.user import GetUserFromLoginHandler
from src.common.exceptions import NotFoundException, UnAuthorizedException
from src.common.dto import Token
from src.api.common.docs import BadRequestError, NotFoundError


auth_router = APIRouter(prefix='/api/v1/token', tags=['token'])


@auth_router.post(
    '',
    status_code=status.HTTP_200_OK,
    response_model=Token,
    response_description='JWT token resource',
    description='Retrieves a JWT token resource',
    summary='Retrieves a JWT token resource',
    responses={
        status.HTTP_400_BAD_REQUEST: {'model': BadRequestError},
        status.HTTP_401_UNAUTHORIZED: {'model': NotFoundError},
    }
)
async def token(
        query: Annotated[OAuth2PasswordRequestForm, Depends()],
        current_user_handler: Annotated[GetUserFromLoginHandler, Depends(GetUserFromLoginHandler)],
        auth_handler: Annotated[AuthHandler, Depends(AuthHandler)]
) -> Token:
    try:
        current_user = await current_user_handler.execute(query)
        return await auth_handler.execute(current_user, query)
        
    except UnAuthorizedException as un_auth_error:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, un_auth_error.get_dict(), {"WWW-Authenticate": "Bearer"})

    except NotFoundException as not_found:
        raise HTTPException(status.HTTP_404_NOT_FOUND, not_found.get_dict())