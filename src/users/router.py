
from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db

from users.schemas import UserCreate
from users.schemas import UserRead
from users.schemas import UserUpdate

from users.crud import insert_user,select_user_by_id
from users.crud import select_all_users,update_user_in_db
from users.crud import delete_user_in_db,select_user_by_email
from myBudgetBot.exceptions import registered_user_exception

users_routes= APIRouter(prefix="/api/v1/users")


@users_routes.post(path="/create/",
                     tags=["Users"],
                     response_model=UserRead,
                     status_code=status.HTTP_201_CREATED)
async def create_user(user_data:UserCreate,
                        db:Session=Depends(get_db)):
    user_db = select_user_by_email(db,user_data.email)
    if user_db:
        raise registered_user_exception
    
    return insert_user(db,user_data)

@users_routes.get(path="/get/all/",
                    tags=["Users"],
                    response_model=List[UserRead],
                    status_code=status.HTTP_200_OK)
async def get_all_users(db:Session=Depends(get_db)):

    db_users=select_all_users(db)
    if not db_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="users not found")
    
    return db_users

@users_routes.get(path="/get/{id}/",
                    tags=["Users"],
                    response_model=UserRead,
                    status_code=status.HTTP_200_OK)
async def get_user(id:int,db:Session=Depends(get_db)):

    db_user=select_user_by_id(db,id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="user not found")
    return db_user

@users_routes.put(path="/update/{id}/",
                tags=["Users"],
                response_model=UserRead,
                status_code=status.HTTP_200_OK)
async def update_user(id:int,
                        user_data:UserUpdate,
                        db:Session=Depends(get_db)):

    return update_user_in_db(db,id,user_data)

@users_routes.delete(path="/delete/{id}/",
                    tags=["Users"],
                    status_code=status.HTTP_200_OK)
async def delete_user(id:int,db:Session=Depends(get_db)):

    delete_user_in_db(db,id)

    return JSONResponse(content={"detail":"user deleted"},
                        status_code=status.HTTP_200_OK)
