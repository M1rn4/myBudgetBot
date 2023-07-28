
from sqlalchemy import Column, Integer,String
from database.database import Base


class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(50))
    

class Suscription(Base):
    __tablename__="suscriptions"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(50))


class Income(Base):
    __tablename__="incomes"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(50))


class Expense(Base):
    __tablename__="expenses"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(50))


class Budget(Base):
    __tablename__="budgets"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(50))