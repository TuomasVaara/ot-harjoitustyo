from math import pi, sqrt, sin, cos, tan, factorial, log, e
from fractions import Fraction
π = pi

class OperationsTest:
    def __init__(self):
        self._expression = ""
        self._round = 1
        self._form = "Decimal"

    def press(self, symbol):
        if self._expression == ("error") or "=" in self._expression:
            self._expression = ""
        self._expression = self._expression + str(symbol)

    def set_round(self, num):
        self._round = num

    def set_form(self, name):
        self._form = name

    def equal(self):
        if self._form == "Decimal":
            value = self.calculate_decimal()
        if self._form == "Fraction":
            value = self.calculate_fraction()
        self._expression = f"={str(value)}"
            

    def clear_expression(self):
        self._expression = ""

    def brackets(self):
        left = self._expression.count("(")
        right = self._expression.count(")")
        if left == right:
            self._expression = self._expression + "("
        else:
            self._expression = self._expression + ")"

    def calculate_decimal(self):
        global π
        try:
            if self._expression == "":
                return 0
            value = str(round(eval(self._expression), self._round))
            return value
        except (SyntaxError,ZeroDivisionError):
            return "error"

    def calculate_fraction(self):
        global π
        try:
            if self._expression == "":
                return 0
            value = Fraction(eval(self._expression)).limit_denominator()
            return value
        except (SyntaxError,ZeroDivisionError):
            return "error"