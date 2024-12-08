import os
import pathlib
from functools import lru_cache

from fastapi.middleware.cors import CORSMiddleware


def cors_middleware(api):
    api.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5500",  # BackEnd
                       "http://127.0.0.1:5500"],  # FrontEnd
        allow_credentials=True,
    )


class BaseConfig:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent

    DATABASE_URL: str = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3")
    DATABASE_CONNECT_DICT: dict = {}


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class TestingConfig(BaseConfig):
    DEBUG = True
    DATABASE_URL: str = os.environ.get(
        "DATABASE_URL_TESTS", f"sqlite:///{BaseConfig.BASE_DIR}/db.sqlite3")


@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig
    }

    config_name = os.environ.get("FASTAPI_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls


settings = get_settings()
