
from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db

from suscriptions.schemas import SuscriptionCreate
from suscriptions.schemas import SuscriptionRead
from suscriptions.schemas import SuscriptionUpdate

from suscriptions.crud import insert_suscription,select_suscription_by_id
from suscriptions.crud import select_all_suscriptions,update_suscription_in_db
from suscriptions.crud import delete_suscription_in_db

suscriptions_routes= APIRouter(prefix="/api/v1/suscriptions")


@suscriptions_routes.post(path="/create/",
                     tags=["Suscriptions"],
                     response_model=SuscriptionRead,
                     status_code=status.HTTP_201_CREATED)
async def create_suscription(suscription_data:SuscriptionCreate,
                        db:Session=Depends(get_db)):

    return insert_suscription(db,suscription_data)

@suscriptions_routes.get(path="/get/all/",
                    tags=["Suscriptions"],
                    response_model=List[SuscriptionRead],
                    status_code=status.HTTP_200_OK)
async def get_all_suscriptions(db:Session=Depends(get_db)):

    db_suscriptions=select_all_suscriptions(db)
    if not db_suscriptions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="suscriptions not found")
    
    return db_suscriptions

@suscriptions_routes.get(path="/get/{id}/",
                    tags=["Suscriptions"],
                    response_model=SuscriptionRead,
                    status_code=status.HTTP_200_OK)
async def get_suscription(id:int,db:Session=Depends(get_db)):

    db_suscription=select_suscription_by_id(db,id)
    if not db_suscription:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="suscription not found")
    return db_suscription

@suscriptions_routes.put(path="/update/{id}/",
                tags=["Suscriptions"],
                response_model=SuscriptionRead,
                status_code=status.HTTP_200_OK)
async def update_suscription(id:int,
                        suscription_data:SuscriptionUpdate,
                        db:Session=Depends(get_db)):

    return update_suscription_in_db(db,id,suscription_data)

@suscriptions_routes.delete(path="/delete/{id}/",
                    tags=["Suscriptions"],
                    status_code=status.HTTP_200_OK)
async def delete_suscription(id:int,db:Session=Depends(get_db)):

    delete_suscription_in_db(db,id)

    return JSONResponse(content={"detail":"suscription deleted"},
                        status_code=status.HTTP_200_OK)
