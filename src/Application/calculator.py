from Operations.operations import Operations
from Operations.expression import Expression


class Calculator:

    def __init__(self):
        self.operations = Operations()
        self.expression = Expression()

    def calculate(self):
        print(f"Pick operation. 1.Add, 2.Subtract, 3.Multiply, 4.Divide, 0.Exit")

        while True:
            problem = int(input("Operation: "))
            if problem == 0:
                break

            number_1 = int(input("First number: "))
            number_2 = int(input("Second number: "))

            if problem == 1:
                print(self.expression.expression((number_1, number_2), "+"),
                      "=", self.operations.Add(number_1, number_2))

            if problem == 2:
                print(self.expression.expression((number_1, number_2), "-"),
                      "=", self.operations.Subtract(number_1, number_2))

            if problem == 3:
                print(self.expression.expression((number_1, number_2), "*"),
                      "=", self.operations.Multiply(number_1, number_2))

            if problem == 4:
                print(self.expression.expression((number_1, number_2), "/"),
                      "=", self.operations.Divide(number_1, number_2))


if __name__ == "__main__":
    Calculator.calculate()
