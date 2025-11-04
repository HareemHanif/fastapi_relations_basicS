from pydantic import BaseModel, EmailStr
from typing import Optional, List

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    owner_id: int

class Item(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True

class ProfileBase(BaseModel):
    full_name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None

class ProfileCreate(ProfileBase):
    user_id: int

class Profile(ProfileBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    items: List[Item] = []
    profile: Optional[Profile] = None
    class Config:
        orm_mode = True
