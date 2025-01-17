from typing import Optional, Any
from datetime import datetime, timedelta, timezone

import jwt

from src.core import JWTSettings
from src.common.exceptions import UnAuthorizedException


class TokenJWT:
    def __init__(self, settings: JWTSettings) -> None:
        self._settings = settings

    def create_jwt_token(self, data: dict) -> str:
        expiration = datetime.now(timezone.utc) + timedelta(minutes=self._settings.jwt_expiration)
        data.update({"exp": expiration})
        token = jwt.encode(data, self._settings.private_key, algorithm=self._settings.algorithm)
        
        return token

    def verify_jwt_token(self, token: str) -> Optional[Any]:
        try:
            decoded_data = jwt.decode(
                token,
                self._settings.public_key,
                algorithms=[self._settings.algorithm]
            )
            return decoded_data

        except jwt.PyJWTError:
            raise UnAuthorizedException('Token is invalid or expired')
