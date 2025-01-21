from typing import Type

from src.common.interfaces import BaseGateway
from src.database.core.manager import TransactionManager
from src.database.repositories import UserRepository, RepositoryType


class DBGateway(BaseGateway):
    def __init__(self, manager: TransactionManager) -> None:
        self.manager = manager
        super().__init__(manager)

    def user(self) -> UserRepository:
        return self._init_repo(UserRepository)

    def _init_repo(self, cls: Type[RepositoryType]) -> RepositoryType:
        return cls(self.manager.session)
