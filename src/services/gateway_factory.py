from typing import Callable

from src.database import DBGateway
from src.services.gateway import ServiceGateway

ServiceGatewayFactory = Callable[[], ServiceGateway]


def create_service_gateway_factory(
    database: Callable[[], DBGateway],
) -> ServiceGatewayFactory:
    def _create_instance() -> ServiceGateway:
        return ServiceGateway(database())

    return _create_instance
