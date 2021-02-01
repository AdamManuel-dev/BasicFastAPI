from fastapi import Depends, FastAPI
from typing import Optional

from .dependencies import get_query_token, get_token_header
from .routes import items, users, customers

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router, prefix="/user", tags=["user"])
app.include_router(items.router, prefix="/item", tags=["item"])
app.include_router(customers.router, prefix="/customers", tags=["customer"])
