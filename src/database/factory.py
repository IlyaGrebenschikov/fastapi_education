from typing import Callable, Type

from src.database.core import TransactionManager
from src.database.gateway import DBGateway
from src.database.core.connection import SessionFactoryType


def create_database_factory(
    manager: Type[TransactionManager], session_factory: SessionFactoryType
) -> Callable[[], DBGateway]:
    def _create() -> DBGateway:
        return DBGateway(manager(session_factory()))

    return _create
