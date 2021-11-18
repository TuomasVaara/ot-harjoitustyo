from repositories.expenses_repository import expenses_repository
from repositories.Income_repository import income_repository

class BudjetOperations:
    def __init__(self):
        self.exrepositary = expenses_repository()
        self.inrepository = income_repository()

    def add_expenses(self, expense:str, amount:int): 
        self.exrepositary.add_expenses(expense, amount)

    def add_income(self, income, amount): None

    def show_summary(self): None

