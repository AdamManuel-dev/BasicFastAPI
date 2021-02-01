# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import Dict, List, Optional
from pydantic import BaseModel, Schema


class BasicItem(BaseModel):
    """
    New User Record Model
    """
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class Item(BaseModel):
    """
    New User Record Model
    """
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
