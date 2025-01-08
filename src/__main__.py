from src.api.v1 import init_app
from src.core import run_uvicorn_server


def main() -> None:
    app = init_app()
    
    run_uvicorn_server(app)


if __name__ == '__main__':
    main()
