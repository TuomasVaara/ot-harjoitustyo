from math import pi, sqrt, sin, cos, tan, factorial, log, e 

#Tkinter
class Operations:
    def __init__(self, equation):
        self._equ = equation
        self._expression = ""

    def press(self, symbol):
        self._expression = self._expression + str(symbol)
        self._equ.set(self._expression)

    def equal(self):
        π = pi
        try:
            if self._expression == "":
                self._equ.set(0)
            else:
                self._equ.set(
                    f"{self._expression}={str(eval(self._expression))}")
            self._expression = ""

        except:
            self._equ.set("????error????")
            self._expression = ""

    def clear_expression(self):
        self._expression = ""
        self._equ.set(str(self._expression))

    def brackets(self, symbol):
        left = self._expression.count("(")
        right = self._expression.count(")")
        if left == right:
            self._expression = self._expression + "("
        if left > right:
            self._expression = self._expression + ")"
        self._equ.set(self._expression)

#TestClass
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

    def brackets(self, symbol):
        left = self._expression.count("(")
        right = self._expression.count(")")
        if left == right:
            self._expression = self._expression + "("
        if left > right:
            self._expression = self._expression + ")"