from pydantic import BaseModel, EmailStr
from typing import Optional


class UserIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    username: str


class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr
    status: bool


class UserUpdate(BaseModel):
    password: Optional[str] = None


class UserRemove(BaseModel):
    username: str

