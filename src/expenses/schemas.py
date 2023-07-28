
from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    name:str

class ExpenseRead(BaseModel):
    id:int
    name:str

    class Config:
        from_attributes = True

class ExpenseUpdate(BaseModel):
    name:str