
#Python

#Suscription
from suscriptions.schemas import SuscriptionCreate, SuscriptionUpdate

#Database
from sqlalchemy.orm import Session
from database import models

def insert_suscription(db: Session, 
                 suscription:SuscriptionCreate):

    db_suscription = models.Suscription(**suscription.dict())
    db.add(db_suscription)
    db.commit()
    db.refresh(db_suscription)

    return db_suscription

def select_suscription_by_id(db: Session, id: int):

    db_suscription= db.query(models.Suscription)\
                .filter(models.Suscription.id == id)\
                .first()
                
    return db_suscription

def select_all_suscriptions(db:Session):

    db_suscriptions= db.query(models.Suscription).all()
    return db_suscriptions

def update_suscription_in_db(db: Session, id: int, 
                        suscription:SuscriptionUpdate):

    db_suscription = select_suscription_by_id(db, id)

    db_suscription.name=suscription.name
    db.add(db_suscription)
    db.commit()
    db.refresh(db_suscription)

    return db_suscription

def delete_suscription_in_db(db: Session, id: int):
    
    db_user = select_suscription_by_id(db, id)

    db.delete(db_user)
    db.commit()