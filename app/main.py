from fastapi import FastAPI
from app.books import router

app = FastAPI()


def build_api():
    app.include_router(router.router)
    return app
