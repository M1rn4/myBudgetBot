
#Python

#Expense
from expenses.schemas import ExpenseCreate, ExpenseUpdate

#Database
from sqlalchemy.orm import Session
from database import models

def insert_expense(db: Session, 
                 expense:ExpenseCreate):

    db_expense = models.Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)

    return db_expense

def select_expense_by_id(db: Session, id: int):

    db_expense= db.query(models.Expense)\
                .filter(models.Expense.id == id)\
                .first()
                
    return db_expense

def select_all_expenses(db:Session):

    db_expenses= db.query(models.Expense).all()
    return db_expenses

def update_expense_in_db(db: Session, id: int, 
                        expense:ExpenseUpdate):

    db_expense = select_expense_by_id(db, id)

    db_expense.name=expense.name
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)

    return db_expense

def delete_expense_in_db(db: Session, id: int):
    
    db_user = select_expense_by_id(db, id)

    db.delete(db_user)
    db.commit()