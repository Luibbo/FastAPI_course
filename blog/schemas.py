from pydantic import BaseModel, ConfigDict
from typing import List, Optional
class Blog(BaseModel):
    title: str
    body: str


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUserBase(BaseModel):
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)

class ShowUser(ShowUserBase):
    blogs: List[Blog] = []

    model_config = ConfigDict(from_attributes=True)
    
    
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[ShowUserBase]
    # class Config():
    #     orm_mode = True

    model_config = ConfigDict(from_attributes=True)
    
class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None    