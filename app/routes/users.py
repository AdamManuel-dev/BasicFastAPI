from fastapi import APIRouter
from ..models.user_model import UserIn, UserOut

router = APIRouter()


@router.get("/", tags=["user"])
async def read_users():
    """
    Lists all of the customer records in FaunaDB 
    """
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me", tags=["user"])
async def read_user_me():
    """
    Lists all of the customer records in FaunaDB 
    """
    return {"username": "fakecurrentuser"}


@router.get("/{username}", tags=["user"])
async def read_user(username: str):
    """
    Lists all of the customer records in FaunaDB 
    """
    return {"username": username}


@router.post("/", tags=["user"], response_model=UserOut)
async def create_user(user: UserIn):
    """
    Lists all of the customer records in FaunaDB 
    """
    return {"id": "UUID", **user.dict()}
