from entities.expenses import Expenses
from entities.income import Income

from database_connection import get_database_connection

def get_income_by_row(row):
    return Income(row['income'], row['amount']) if row else None

def get_expenses_by_row(row):
    return Expenses(row['expenses'], row['amount']) if row else None

class IncomeExpensesRepositary:
    def __init__ (self, connection):
        self._connection = connection

    def find_incomes(self): 
        cursor = self._connection.cursor()
        cursor.execute('select * from income')
        rows = cursor.fetchall()
        return list(map(get_income_by_row, rows))

    def find_expenses(self):
        cursor = self._connection.cursor()
        cursor.execute('select * from expenses')
        rows = cursor.fetchall()
        return list(map(get_expenses_by_row, rows))

    def delete_all_incomes_expenses(self):
        cursor = self._connection.cursor()
        cursor.execute('delete from expenses')
        cursor.execute('delete from income')
        self._connection.commit()

in_ex_repositary = IncomeExpensesRepositary(get_database_connection())

