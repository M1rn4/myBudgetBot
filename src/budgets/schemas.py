
from pydantic import BaseModel

class BudgetCreate(BaseModel):
    name:str

class BudgetRead(BaseModel):
    id:int
    name:str

    class Config:
        from_attributes = True

class BudgetUpdate(BaseModel):
    name:str