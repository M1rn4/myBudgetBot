
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Import routs

from myBudgetBot.router import myBudgetBot_routes
from users.router import users_routes
from suscriptions.router import suscriptions_routes
from incomes.router import incomes_routes
from expenses.router import expenses_routes
from budgets.router import budgets_routes


app = FastAPI(title="Mybudgetbot API",
              description="A powerful API for Mybudgetbot project",
              version="1.0.0")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# Include routs

app.include_router(myBudgetBot_routes)
app.include_router(users_routes)
app.include_router(suscriptions_routes)
app.include_router(incomes_routes)
app.include_router(expenses_routes)
app.include_router(budgets_routes)
