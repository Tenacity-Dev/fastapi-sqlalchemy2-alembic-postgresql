from fastapi import FastAPI
from core.config import Settings
from starlette.middleware.cors import CORSMiddleware

from core.database import Base, engine

from user.routes.user_router import user_router

Base.metadata.create_all(bind=engine)

settings = Settings()
app = FastAPI()

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(user_router, prefix='/api')


@app.get("/")
def read_root():
    return {"Hello": "World"}

