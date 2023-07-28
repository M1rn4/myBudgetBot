
from fastapi import APIRouter,Depends
from fastapi.responses import RedirectResponse
from myBudgetBot.settings import MybudgetbotSettings,get_myBudgetBot_settings

myBudgetBot_routes= APIRouter()

@myBudgetBot_routes.get(path="/",
                   include_in_schema=False)
def documentation(myBudgetBot_settings:MybudgetbotSettings=Depends(get_myBudgetBot_settings)):
    return RedirectResponse(url=myBudgetBot_settings.BACKEND_HOST +"/docs/")