# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import Dict, List, Optional
from pydantic import BaseModel, Schema


class Address(BaseModel):
    """
    New User Record Model
    """
    street: str
    city: str
    state: str
    zipCode: str


class CreditCard(BaseModel):
    """
    New User Record Model
    """
    network: str
    number: str


class Customer(BaseModel):
    """
    New User Record Model
    """
    firstName: str
    lastName: str
    address: Optional[Address] = None
    telephone: str
    creditCard: Optional[CreditCard] = None
    ref_id: str


class NewCustomer(BaseModel):
    """
    New User Record Model
    """
    firstName: str
    lastName: str
    address: Optional[Address] = None
    telephone: str
    creditCard: Optional[CreditCard] = None
