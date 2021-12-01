from math import pi, sqrt, sin, cos, tan, factorial, log, e

class Operations:
    def __init__(self, equation):
        self._equ = equation
        self._expression = ""
        self._round = 1

    def press(self, symbol):
        self._expression = self._expression + str(symbol)
        self._equ.set(self._expression)

    def equal(self):
        value = self.calculate(self._expression)
        if value == "error":
            self._equ.set("????error????")
        else:
            self._equ.set(f"{self._expression}={value}")
        self._expression = ""

    def clear_expression(self):
        self._expression = ""
        self._equ.set(str(self._expression))

    def brackets(self):
        left = self._expression.count("(")
        right = self._expression.count(")")
        if left == right:
            self._expression = self._expression + "("
        if left > right:
            self._expression = self._expression + ")"
        self._equ.set(self._expression)

    def calculate(self, expression):
        π = pi
        try:
            if expression == "" or expression == "()":
                return 0
            value = str(round(eval(self._expression), self._round))
            return value
        except ValueError:
            return "error"

    def specify_round(self):
        if self._round == 4:
            self._round = 0
        self._round += 1


class OperationsTest:
    def __init__(self):
        self._expression = ""

    def press(self, symbol):
        if self._expression == ("????error????") or "=" in self._expression:
            self._expression = ""
        self._expression = self._expression + str(symbol)

    def equal(self):
        π = pi
        try:
            if self._expression == "":
                self._expression = "=0"
            else:
                self._expression = f"={str(eval(self._expression))}"

        except:
            self._expression = "????error????"

    def clear_expression(self):
        self._expression = ""

    def brackets(self):
        left = self._expression.count("(")
        right = self._expression.count(")")
        if left == right:
            self._expression = self._expression + "("
        else:
            self._expression = self._expression + ")"
