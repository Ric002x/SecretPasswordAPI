from fastapi import FastAPI

from .config import cors_middleware, get_settings
from .routers import router


def create_api():
    settings = get_settings()
    api = FastAPI(debug=settings.DEBUG)
    api.include_router(router)
    cors_middleware(api)
    return api
