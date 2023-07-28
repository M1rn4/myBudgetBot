
from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db

from expenses.schemas import ExpenseCreate
from expenses.schemas import ExpenseRead
from expenses.schemas import ExpenseUpdate

from expenses.crud import insert_expense,select_expense_by_id
from expenses.crud import select_all_expenses,update_expense_in_db
from expenses.crud import delete_expense_in_db

expenses_routes= APIRouter(prefix="/api/v1/expenses")


@expenses_routes.post(path="/create/",
                     tags=["Expenses"],
                     response_model=ExpenseRead,
                     status_code=status.HTTP_201_CREATED)
async def create_expense(expense_data:ExpenseCreate,
                        db:Session=Depends(get_db)):

    return insert_expense(db,expense_data)

@expenses_routes.get(path="/get/all/",
                    tags=["Expenses"],
                    response_model=List[ExpenseRead],
                    status_code=status.HTTP_200_OK)
async def get_all_expenses(db:Session=Depends(get_db)):

    db_expenses=select_all_expenses(db)
    if not db_expenses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="expenses not found")
    
    return db_expenses

@expenses_routes.get(path="/get/{id}/",
                    tags=["Expenses"],
                    response_model=ExpenseRead,
                    status_code=status.HTTP_200_OK)
async def get_expense(id:int,db:Session=Depends(get_db)):

    db_expense=select_expense_by_id(db,id)
    if not db_expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="expense not found")
    return db_expense

@expenses_routes.put(path="/update/{id}/",
                tags=["Expenses"],
                response_model=ExpenseRead,
                status_code=status.HTTP_200_OK)
async def update_expense(id:int,
                        expense_data:ExpenseUpdate,
                        db:Session=Depends(get_db)):

    return update_expense_in_db(db,id,expense_data)

@expenses_routes.delete(path="/delete/{id}/",
                    tags=["Expenses"],
                    status_code=status.HTTP_200_OK)
async def delete_expense(id:int,db:Session=Depends(get_db)):

    delete_expense_in_db(db,id)

    return JSONResponse(content={"detail":"expense deleted"},
                        status_code=status.HTTP_200_OK)
