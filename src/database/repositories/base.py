import abc
from typing import Generic, Type, TypeVar, Protocol

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.base import ModelType
from src.database.repositories.crud import CRUDRepository


RepositoryType = TypeVar("RepositoryType", bound="Repository")


class Repository(Protocol):
    def __init__(self, session: AsyncSession) -> None: ...


class BaseRepository(Repository, Generic[ModelType]):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._crud = CRUDRepository(session, self.model)

    @property
    @abc.abstractmethod
    def model(self) -> Type[ModelType]:
        raise NotImplementedError
    