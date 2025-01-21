from typing import Type

from src.common.dto.base import DTOType
from src.database.models.base import ModelType


def from_model_to_dto(model: ModelType, dto: Type[DTOType]) -> DTOType:
    return dto(**model.as_dict())


def none_filter(data: Type[DTOType]) -> dict:
    return {k: v for k, v in data.model_dump().items() if v}
