from entities.budjet import Budjet
from entities.user import User 

from repositories.Expenses_repository import ExpensesRepository
from repositories.Income_repository import IncomeRepository

class BudjetOperations:
    def self __init__(self, expenses_repository, income_repository):
        self._expenses_repository = ExpensesRepository
        self._income_repository = IncomeRepository
        self._user = None

    def add_expenses(self, expense, amount): None

    def add_income(self, income, amount): None

    def show_summary(self): None
