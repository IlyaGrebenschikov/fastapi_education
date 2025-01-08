import uvicorn
from fastapi import FastAPI


def run_uvicorn_server(app: FastAPI, host: str = '0.0.0.0', port: int = 8080):
    uvicorn.run(app, host=host, port=port)
