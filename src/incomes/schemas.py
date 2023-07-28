
from pydantic import BaseModel

class IncomeCreate(BaseModel):
    name:str

class IncomeRead(BaseModel):
    id:int
    name:str

    class Config:
        from_attributes = True

class IncomeUpdate(BaseModel):
    name:str