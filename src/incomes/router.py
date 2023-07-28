
from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db

from incomes.schemas import IncomeCreate
from incomes.schemas import IncomeRead
from incomes.schemas import IncomeUpdate

from incomes.crud import insert_income,select_income_by_id
from incomes.crud import select_all_incomes,update_income_in_db
from incomes.crud import delete_income_in_db

incomes_routes= APIRouter(prefix="/api/v1/incomes")


@incomes_routes.post(path="/create/",
                     tags=["Incomes"],
                     response_model=IncomeRead,
                     status_code=status.HTTP_201_CREATED)
async def create_income(income_data:IncomeCreate,
                        db:Session=Depends(get_db)):

    return insert_income(db,income_data)

@incomes_routes.get(path="/get/all/",
                    tags=["Incomes"],
                    response_model=List[IncomeRead],
                    status_code=status.HTTP_200_OK)
async def get_all_incomes(db:Session=Depends(get_db)):

    db_incomes=select_all_incomes(db)
    if not db_incomes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="incomes not found")
    
    return db_incomes

@incomes_routes.get(path="/get/{id}/",
                    tags=["Incomes"],
                    response_model=IncomeRead,
                    status_code=status.HTTP_200_OK)
async def get_income(id:int,db:Session=Depends(get_db)):

    db_income=select_income_by_id(db,id)
    if not db_income:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="income not found")
    return db_income

@incomes_routes.put(path="/update/{id}/",
                tags=["Incomes"],
                response_model=IncomeRead,
                status_code=status.HTTP_200_OK)
async def update_income(id:int,
                        income_data:IncomeUpdate,
                        db:Session=Depends(get_db)):

    return update_income_in_db(db,id,income_data)

@incomes_routes.delete(path="/delete/{id}/",
                    tags=["Incomes"],
                    status_code=status.HTTP_200_OK)
async def delete_income(id:int,db:Session=Depends(get_db)):

    delete_income_in_db(db,id)

    return JSONResponse(content={"detail":"income deleted"},
                        status_code=status.HTTP_200_OK)
