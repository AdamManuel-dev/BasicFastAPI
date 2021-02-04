from fastapi import Depends, FastAPI
from typing import Optional

from .dependencies import get_query_token, get_token_header
from .routes import customers

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(customers.router, prefix="/customers", tags=["Customer"])
