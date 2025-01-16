from passlib.context import CryptContext
  
from src.common.interfaces import AbstractHasher


class BcryptHasher(AbstractHasher):
    def __init__(self, hasher: CryptContext) -> None:
        self._hasher = hasher
        
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self._hasher.verify(plain_password, hashed_password)
    
    def hash_password(self, password: str) -> str:
        return self._hasher.hash(password)
