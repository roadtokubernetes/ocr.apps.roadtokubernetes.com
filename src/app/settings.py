import pathlib
from functools import lru_cache

from pydantic import BaseSettings

BASE_DIR = pathlib.Path(__file__).parent


class Settings(BaseSettings):
    secret_token: str = None
    debug: bool = False
    echo_active: bool = False
    skip_auth: bool = False

    class Config:
        env_file = str(BASE_DIR / ".env")


@lru_cache
def get_settings():
    return Settings()
