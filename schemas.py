from pydantic import BaseModel, EmailStr

# This is a schema for creating a user
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# This is a schema for creating a post (moved from main.py)
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class User_response(BaseModel):
    email : EmailStr
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostCreate(PostBase):
    pass

class Post(PostBase):
    pass
