from math import pi, sqrt, sin, cos, tan, factorial, log, e
from fractions import Fraction
π = pi
ln = log
Sin = sin
Cos = cos
Tan = tan
Sqrt = sqrt
E = e
Factorial = factorial

class OperationsTest:
    def __init__(self):
        self._expression = ""
        self._answer = 0
        self._round = 5
        self._form = "Decimal"

    def set_round(self, num):
        self._round = num

    def set_form(self, name):
        self._form = name

    def error(self):
        self._answer = "error"

    def press(self, symbol):
        if "=" in self._expression or "error" in self._expression:
            self.clear_expression()
        self._expression = self._expression + str(symbol)

    def equal(self):
        if self._expression == "":
            self._expression = "0"
        if self._form == "Decimal":
            self.calculate_decimal()
        if self._form == "Fraction":
            self.calculate_fraction()
        self._expression = self._expression + f"={self._answer}"

    def clear_expression(self):
        self._expression = ""

    def brackets(self):
        left = self._expression.count("(")
        right = self._expression.count(")")
        if left == right:
            self._expression = self._expression + "("
        if left > right:
            self._expression = self._expression + ")"

    def calculate_decimal(self):
        try:
            self._answer = str(round(eval(self._expression), self._round))
        except (SyntaxError, ZeroDivisionError, OverflowError):
            self.error()

    def calculate_fraction(self):
        try:
            self._answer = Fraction(eval(self._expression)).limit_denominator()
        except (SyntaxError, ZeroDivisionError, OverflowError):
            self.error()

    def ans(self):
        self.press(self._answer)