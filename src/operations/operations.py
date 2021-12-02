from math import pi, sqrt, sin, cos, tan, factorial, log, e
from fractions import Fraction
π = pi


class Operations:
    def __init__(self, equation, fraction_decimal_view, round_view):
        self._equ = equation
        self._fraction_decimal = fraction_decimal_view
        self._round_view = round_view
        self._expression = ""
        self._round = 1
        self._form = "decimal"

    def press(self, symbol):
        self._expression = self._expression + str(symbol)
        self._equ.set(self._expression)

    def equal(self):
        if self._form == "decimal":
            value = self.calculate_decimal()
        if self._form == "fraction":
            value = self.calculate_fraction()
        if value == "error":
            self._equ.set("????error????")
        else:
            self._equ.set(f"{self._expression} = {value}")
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
        global π
        try:
            value = str(round(eval(self._expression), self._round))
            return value
        except ValueError:
            return "error"

    def calculate_fraction(self):
        global π
        try:
            value = Fraction(eval(self._expression)).limit_denominator()
            return value
        except ValueError:
            return "error"

    def increase_round(self):
        self._round += 1
        self._round_view.set(str(self._round))

    def default_round(self):
        self._round = 1
        self._round_view.set(str(self._round))

    def switch_fraction_decimal(self):
        if self._form == "decimal":
            self._form = "fraction"
            self._fraction_decimal.set("fraction")
        else:
            self._form = "decimal"
            self._fraction_decimal.set("decimal")


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
