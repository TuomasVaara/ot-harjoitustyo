from math import pi, log, sin, cos, tan, sqrt, e, factorial
from fractions import Fraction
π = pi
ln = log
Sin = sin
Cos = cos
Tan = tan
Sqrt = sqrt
E = e
Factorial = factorial


class Operations:
    def __init__(self, equation, fraction_decimal_view, round_view):
        self._equ = equation
        self._fraction_decimal = fraction_decimal_view
        self._round_view = round_view
        self._expression = ""
        self._answer = 0
        self._round = 5
        self._form = "Decimal"

    def set_round(self, num):
        self._round = num

    def set_form(self, name):
        self._form = name

    def set_expression(self):
        self._equ.set(f"{self._expression} = {self._answer}")

    def error(self):
        self._expression = "error"
        self._equ.set(f"{self._expression}")

    def press(self, symbol):
        self._expression = self._expression + str(symbol)
        self._equ.set(self._expression)

    def equal(self):
        if self._form == "Decimal":
            self.calculate_decimal()
        if self._form == "Fraction":
            self.calculate_fraction()
        self.set_expression()
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
