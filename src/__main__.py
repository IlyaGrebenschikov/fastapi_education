from src.api.v1 import init_app, setup_dependencies
from src.core import run_uvicorn_server, load_settings
from src.api.v1.endpoints import setup_routers


def main() -> None:
    settings = load_settings()
    app = init_app(settings.app)

    setup_routers(app)   
    setup_dependencies(app, settings)
    run_uvicorn_server(app, settings.uvicorn_server)


if __name__ == '__main__':
    main()
