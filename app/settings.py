from functools import lru_cache
import os
import logging

from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    DATABASE_URL: str
    LOG_LEVEL: int = logging.INFO
    LOG_FILE: str = "../logs/veldict-be.log"
    GET_LOGGER: str = "catfish_manager_service"
    ORIGINS: list
    CORS_ALLOW_METHODS: list
    CORS_ALLOW_HEADERS: list

    class Config:
        env_file = os.environ.get('ENV_FILE', '.env')
        env_file_encoding = 'utf-8'

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()