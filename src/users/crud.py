
#Python

#User
from users.schemas import UserCreate, UserUpdate

#Database
from sqlalchemy.orm import Session
from database import models

def insert_user(db: Session, 
                 user:UserCreate):

    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def select_user_by_id(db: Session, id: int):

    db_user= db.query(models.User)\
                .filter(models.User.id == id)\
                .first()
                
    return db_user

def select_all_users(db:Session):

    db_users= db.query(models.User).all()
    return db_users

def update_user_in_db(db: Session, id: int, 
                        user:UserUpdate):

    db_user = select_user_by_id(db, id)

    db_user.name=user.name
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def delete_user_in_db(db: Session, id: int):
    
    db_user = select_user_by_id(db, id)

    db.delete(db_user)
    db.commit()