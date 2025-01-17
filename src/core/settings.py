import logging
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


def get_root_dir_path() -> Path:
    return Path(__file__).resolve().parent.parent.parent
    

class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_prefix='POSTGRES_',
        extra='ignore'
    )
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    DB: str

    @property
    def url_obj(self) -> URL:
        return URL.create(
            'postgresql+asyncpg',
            username=self.USER,
            password=self.PASSWORD,
            database=self.DB,
            host=self.HOST,
            port=self.PORT
        )

    @property
    def url_str(self) -> str:
        return (
            f'postgresql+asyncpg://'
            f'{self.USER}:'
            f'{self.PASSWORD}@'
            f'{self.HOST}:'
            f'{self.PORT}/'
            f'{self.DB}'
        )
        

class UvicornServerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_prefix='UVICORN_SERVER_',
        extra='ignore'
    )
    
    HOST: Optional[str] = '0.0.0.0'
    PORT: Optional[int] = 8080
    

class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_prefix='APP_',
        extra='ignore',
    )
    
    TITLE: Optional[str] = 'FastApi'
    VERSION: Optional[str] = '0.1.0'
    DOCS_URL: Optional[str] = '/docs'
    REDOC_URL: Optional[str] = '/redoc'
    
    
class JWTSettings:
    private_key: str = (get_root_dir_path() / ".certs" / "jwt-private.pem").read_text()
    public_key: str = (get_root_dir_path() / ".certs" / "jwt-public.pem").read_text()
    algorithm: str = 'RS256'
    jwt_expiration: int = 30
    

class LoggerSettings:
    name = 'base'
    level = logging.DEBUG
    dir_path = (get_root_dir_path() / 'logs')
    formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s\n')


class Settings(BaseSettings):
    app: AppSettings
    database: DatabaseSettings
    uvicorn_server: UvicornServerSettings       
    jwt: JWTSettings


def load_settings(
    app: Optional[AppSettings] = None,
    database: Optional[DatabaseSettings] = None,
    uvicorn_server: Optional[UvicornServerSettings] = None,
    jwt: Optional[JWTSettings] = None,
    ) -> Settings:
    return Settings(
        app=app or AppSettings(),
        database=database or DatabaseSettings(),
        uvicorn_server=uvicorn_server or UvicornServerSettings(),
        jwt=jwt or JWTSettings(),
    )


def load_logger_settings() -> LoggerSettings:
    return LoggerSettings()
