from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int = None
    name: str
    title: str
    avatar: str
    is_active: Optional[bool]

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    name: Optional[str]
    title: Optional[str]
    avatar: Optional[str]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
