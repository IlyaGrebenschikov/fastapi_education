from src.api.v1 import init_app, setup_dependencies
from src.core import run_uvicorn_server, load_settings


def main() -> None:
    app = init_app()
    settings = load_settings()
    
    setup_dependencies(app, settings)
    run_uvicorn_server(app, settings.uvicorn_server)


if __name__ == '__main__':
    main()
