
from pydantic import BaseModel

class SuscriptionCreate(BaseModel):
    name:str

class SuscriptionRead(BaseModel):
    id:int
    name:str

    class Config:
        from_attributes = True

class SuscriptionUpdate(BaseModel):
    name:str