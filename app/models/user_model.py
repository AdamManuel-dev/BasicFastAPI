# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import Dict, List, Optional
from pydantic import BaseModel, Schema


class UserIn(BaseModel):
    """
    New User Record Model
    """
    username: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    phone: Optional[int] = None


class UserOut(BaseModel):
    """
    Existing User Record Model
    """
    id: str
    username: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    phone: Optional[int] = None
