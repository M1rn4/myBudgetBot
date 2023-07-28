
#Python

#Income
from incomes.schemas import IncomeCreate, IncomeUpdate

#Database
from sqlalchemy.orm import Session
from database import models

def insert_income(db: Session, 
                 income:IncomeCreate):

    db_income = models.Income(**income.dict())
    db.add(db_income)
    db.commit()
    db.refresh(db_income)

    return db_income

def select_income_by_id(db: Session, id: int):

    db_income= db.query(models.Income)\
                .filter(models.Income.id == id)\
                .first()
                
    return db_income

def select_all_incomes(db:Session):

    db_incomes= db.query(models.Income).all()
    return db_incomes

def update_income_in_db(db: Session, id: int, 
                        income:IncomeUpdate):

    db_income = select_income_by_id(db, id)

    db_income.name=income.name
    db.add(db_income)
    db.commit()
    db.refresh(db_income)

    return db_income

def delete_income_in_db(db: Session, id: int):
    
    db_user = select_income_by_id(db, id)

    db.delete(db_user)
    db.commit()