from abc import ABC, abstractmethod


class AbstractHasher(ABC):
    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        raise NotImplemented
    
    @abstractmethod
    def hash_password(self, password: str) -> str:
        raise NotImplemented
