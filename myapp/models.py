from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    id: int
    address_1: str
    address_2: str
    city: str
    state: str
    zip: str
    country: str

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    mail: str
    password: str
    addresses: List[Address]
