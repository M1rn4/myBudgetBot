
from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db

from budgets.schemas import BudgetCreate
from budgets.schemas import BudgetRead
from budgets.schemas import BudgetUpdate

from budgets.crud import insert_budget,select_budget_by_id
from budgets.crud import select_all_budgets,update_budget_in_db
from budgets.crud import delete_budget_in_db

budgets_routes= APIRouter(prefix="/api/v1/budgets")


@budgets_routes.post(path="/create/",
                     tags=["Budgets"],
                     response_model=BudgetRead,
                     status_code=status.HTTP_201_CREATED)
async def create_budget(budget_data:BudgetCreate,
                        db:Session=Depends(get_db)):

    return insert_budget(db,budget_data)

@budgets_routes.get(path="/get/all/",
                    tags=["Budgets"],
                    response_model=List[BudgetRead],
                    status_code=status.HTTP_200_OK)
async def get_all_budgets(db:Session=Depends(get_db)):

    db_budgets=select_all_budgets(db)
    if not db_budgets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="budgets not found")
    
    return db_budgets

@budgets_routes.get(path="/get/{id}/",
                    tags=["Budgets"],
                    response_model=BudgetRead,
                    status_code=status.HTTP_200_OK)
async def get_budget(id:int,db:Session=Depends(get_db)):

    db_budget=select_budget_by_id(db,id)
    if not db_budget:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="budget not found")
    return db_budget

@budgets_routes.put(path="/update/{id}/",
                tags=["Budgets"],
                response_model=BudgetRead,
                status_code=status.HTTP_200_OK)
async def update_budget(id:int,
                        budget_data:BudgetUpdate,
                        db:Session=Depends(get_db)):

    return update_budget_in_db(db,id,budget_data)

@budgets_routes.delete(path="/delete/{id}/",
                    tags=["Budgets"],
                    status_code=status.HTTP_200_OK)
async def delete_budget(id:int,db:Session=Depends(get_db)):

    delete_budget_in_db(db,id)

    return JSONResponse(content={"detail":"budget deleted"},
                        status_code=status.HTTP_200_OK)
