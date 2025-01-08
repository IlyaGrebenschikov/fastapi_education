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
    def get_url_obj(self) -> URL:
        return URL.create(
            'postgresql+asyncpg',
            username=self.USER,
            password=self.PASSWORD,
            database=self.DB,
            host=self.HOST,
            port=self.PORT
        )

    @property
    def get_url_str(self) -> str:
        return (
            f'postgresql+asyncpg://'
            f'{self.USER}:'
            f'{self.PASSWORD}@'
            f'{self.HOST}:'
            f'{self.PORT}/'
            f'{self.DB}'
        )
        
        
def database_settings() -> DatabaseSettings:
    return DatabaseSettings()
