from math import sqrt

class Operations:
    def __init__(self, equation):
        self._equ = equation
        self._expression = ""
    
    def press(self, symbol):
        self._expression = self._expression + str(symbol)
        self._equ.set(self._expression)

    def equal(self):
        try:
            self._equ.set(str(eval(self._expression)))
            self._expression = ""

        except:
            self._equ.set("????error????")
            self._expression = ""

    def power(self):
        self._expression = self._expression + str("sqrt(")
        self._equ.set(self._expression)

    