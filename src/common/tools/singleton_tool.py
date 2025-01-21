from typing import TypeVar, Callable


DependencyType = TypeVar("DependencyType")


def singleton(value: DependencyType) -> Callable[[], DependencyType]:
    def singleton_factory() -> DependencyType:
        return value

    return singleton_factory
