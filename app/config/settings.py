from pydantic import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    """ Configurações globais """

    API_V1: str = "/api/v1"


    DATABASE_URL_LOCAL_TESTING: Optional[str] = os.environ.get('DATABASE_URL_LOCAL_TESTING')
    DATABASE_URL: Optional[str] = os.environ.get('DATABASE_URL')


settings = Settings()
