
#Python

#Budget
from budgets.schemas import BudgetCreate, BudgetUpdate

#Database
from sqlalchemy.orm import Session
from database import models

def insert_budget(db: Session, 
                 budget:BudgetCreate):

    db_budget = models.Budget(**budget.dict())
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)

    return db_budget

def select_budget_by_id(db: Session, id: int):

    db_budget= db.query(models.Budget)\
                .filter(models.Budget.id == id)\
                .first()
                
    return db_budget

def select_all_budgets(db:Session):

    db_budgets= db.query(models.Budget).all()
    return db_budgets

def update_budget_in_db(db: Session, id: int, 
                        budget:BudgetUpdate):

    db_budget = select_budget_by_id(db, id)

    db_budget.name=budget.name
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)

    return db_budget

def delete_budget_in_db(db: Session, id: int):
    
    db_user = select_budget_by_id(db, id)

    db.delete(db_user)
    db.commit()