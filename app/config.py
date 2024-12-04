from fastapi.middleware.cors import CORSMiddleware


def cors_middleware(api):
    api.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5500",  # BackEnd
                       "http://127.0.0.1:5500"],  # FrontEnd
        allow_credentials=True,
    )
