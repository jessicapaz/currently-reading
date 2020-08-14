from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError, HTTPException

from app.books import routes

app = FastAPI()


@app.exception_handler(Exception)
async def http_exception_handler(request, exc):
    """Handler to normalize exception error responses"""
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='Internal server error'
    )


def build_api():
    app.include_router(routes.router)
    return app
