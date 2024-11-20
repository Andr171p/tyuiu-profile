import os
from pathlib import Path
from typing import List
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

load_dotenv(dotenv_path=BASE_DIR / ".env")


class DBSettings(BaseSettings):
    host: str = os.getenv('DB_HOST')
    port: int = os.getenv('DB_PORT')
    name: str = os.getenv('DB_NAME')
    user: str = os.getenv('DB_USER')
    password: str = os.getenv('DB_PASSWORD')


class RecSysSettings(BaseSettings):
    url: str = os.getenv('REC-SYS_API_URL')
    endpoint: str = '/rec_sys/recommend/'


class AppSettings(BaseSettings):
    name: str = "Tyuiu-user-profile"
    origins: List[str] = [""]


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    db: DBSettings = DBSettings()
    rec_sys: RecSysSettings = RecSysSettings()


settings = Settings()
