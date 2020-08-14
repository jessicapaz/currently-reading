from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from app.books.currently_reading import get_currently_reading
from app import exceptions

router = APIRouter()


@router.get("/users/{user_id}/books")
def currently_reading(user_id: str):
    try:
        return get_currently_reading(user_id)
    except exceptions.GoodreadsException as err:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(err)
        )
