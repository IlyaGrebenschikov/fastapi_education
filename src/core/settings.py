from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


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
        

class UvicornServerSettings:
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_prefix='UVICORN_SERVER_',
        extra='ignore'
    )
    
    HOST: Optional[str] = '0.0.0.0'
    PORT: Optional[int] = 8080


class Settings(BaseSettings):
    database: DatabaseSettings
    uvicorn_server: UvicornServerSettings       


def load_settings(
    database: Optional[DatabaseSettings] = None,
    uvicorn_server: Optional[UvicornServerSettings] = None,
    ) -> Settings:
    return Settings(
        database=database or DatabaseSettings(),
        uvicorn_server=uvicorn_server or UvicornServerSettings()
    )

