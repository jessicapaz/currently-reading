from fastapi import FastAPI
from app.books import router

app = FastAPI()


def build_api():
    return app
