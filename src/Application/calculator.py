from Operations.operations import Operations
from Operations.insert import Insert
class Calculator:

    def __init__(self):
        self.operations = Operations()
        self.insert = Insert()

    def calculate(self):
        print("Solvable problems: Add, Subtract, Multiply, Divide, Add & Subtract.")

        problem = input("What kind of a problem you wish to solve? ")
        if problem == "Add":
            print(self.operations.Add())
        if problem == "Subtract": 
            print(self.operations.Subtract())
        if problem == "Multiply":
            print(self.operations.Multiply())
        if problem == "Divide":
            print(self.operations.Divide())
