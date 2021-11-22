from Operations.operations import Operations
from Operations.insert import Insert
class Calculator:

    def __init__(self):
        self.operations = Operations()
        self.insert = Insert()

    def calculate(self):
        print(f"Pick operation. 1.Add, 2.Subtract, 3.Multiply, 4.Divide, 0.Exit")

        while True:
            problem = int(input("Operation: "))
            if problem == 0:
                break

            number_1 = int(input("First number: "))
            number_2 = int(input("Second number: "))

            if problem == 1:
                print(self.insert.expression((number_1, number_2), "+"),"=", self.operations.Add(number_1,number_2) )
            
            if problem == 2: 
                print()
            
            if problem == 3:
                print()
            
            if problem == 4:
                print()
            

if __name__ == "__main__":
    Calculator.calculate()
