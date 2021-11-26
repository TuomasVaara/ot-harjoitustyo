from Operations.expression import Expression


class Operations:
    def __init__(self):
        None

    def add(self, x, y):
        if type(x) == float or type(y) == float:
            return round((x+y), 2)
        return x + y

    def Subtract(self, x, y):
        return x - y

    def Multiply(self, x, y):
        return x * y

    def Divide(self, x, y):
        if y == 0 or x == 0:
            return 0
        return round((x / y), 2)

    def Power(self, number, power): None

    def Square(self, number): None

    def __str__(self):
        return f"4 operations"


if __name__ == "__main__":
    calculator = Operations()
