from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config:
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUserBase(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True

class ShowUser(ShowUserBase):
    blogs: List[Blog]


class ShowBlogBase(BaseModel):
    title: str
    body: str

class ShowBlog(ShowBlogBase):
    creator: ShowUserBase
    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
