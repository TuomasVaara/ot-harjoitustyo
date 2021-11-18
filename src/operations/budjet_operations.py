from entities.budjet import Budjet
from entities.user import User 
import json

from repositories.Expenses_repository import ExpensesReporitory
from repositories.Income_reporitory import IncomeRepository

class BudjetOperations:
    def self __init__(self, expenses_repository, income_repository):
        self._expenses_repository = ExpensesRepository
        self._income_repository = IncomeRepository
        self._user = None

    def add_expenses(self, expense:str, amount:int): 
        exp = {"expense" : expense, "amount" = amount}
        with open("expenses_data.json", "w") as outfile:
            json.dump(exp, outfile)

    def add_income(self, income, amount): None

    def show_summary(self): None

if __name__ == "__main__":
    add_expenses("Rent",587)