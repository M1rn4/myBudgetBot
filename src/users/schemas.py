
from pydantic import BaseModel
from pydantic import EmailStr

class UserCreate(BaseModel):
    first_name:str
    last_name:str
    username:str
    email:EmailStr
    password:str

class UserRead(BaseModel):
    id:int
    first_name:str
    last_name:str
    username:str
    email:str

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name:str