from fastapi import FastAPI

from .config import cors_middleware
from .routers import router


def create_api():
    api = FastAPI()
    api.include_router(router)
    cors_middleware(api)
    return api
