from fastapi import APIRouter
from app.books.currently_reading import get_currently_reading

router = APIRouter()


@router.get("/users/{user_id}/books")
def currently_reading(user_id: str):
    return get_currently_reading(user_id)
