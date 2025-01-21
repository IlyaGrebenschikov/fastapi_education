from fastapi.security import OAuth2PasswordRequestForm

from src.services.security.bcrypt_hasher import BcryptHasher
from src.services.security.token_jwt import TokenJWT
from src.common.exceptions import UnAuthorizedException
from src.common.dto import UserInDBSchema, Token, TokenSubject


class AuthService:
    def __init__(
            self,
            hasher: BcryptHasher,
            jwt: TokenJWT,
    ) -> None:
        self._hasher = hasher
        self._jwt = jwt

    async def generate_token(self, current_user: UserInDBSchema, query: OAuth2PasswordRequestForm) -> Token:
        if not self._hasher.verify_password(query.password, current_user.password):
            raise UnAuthorizedException('Incorrect password')

        token_data = TokenSubject(sub=current_user.id, scopes=query.scopes)
        token = self._jwt.create_jwt_token(token_data.model_dump())

        return Token(access_token=token, token_type='Bearer')
