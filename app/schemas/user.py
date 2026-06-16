from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime
from enum import Enum


class User(BaseModel):
    id: int
    first_name: str = Field(
        min_length=2,
        max_length=50,
    )
    last_name: str = Field(min_length=2, max_length=50)
    role: Literal["user", "admin"]
    state: Literal["Active", "Inactive"]
    created_at: datetime
    created_by: str


class UserCreate(BaseModel):
    first_name: str = Field(
        min_length=2,
        max_length=50,
    )
    last_name: str = Field(min_length=2, max_length=50)
    role: Literal["user", "admin"]


class StateFilter(str, Enum):
    active = "active"
    inactive = "inactive"
    all = "all"
