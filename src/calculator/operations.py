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
    """Toinen sovelluslogiikasta vastaavavista luokista"""

    def __init__(self):
        """Luokan konstruktori. Luo uuden olion, joka vastaa sovelluslogiikan laskennallisesta puolesta.
        """
        self._expression = ""
        self._answer = 0
        self._round = 5
        self._form = "Decimal"

    def change_round(self, num):
        """Asettaa luokan muutetun pyöristys tarkkuuden.

        Args:
            nums: Numeroarvo, joka määrittää uuden tarkkuuden pyöristämiselle.
        """
        self._round = num

    def change_form(self, name):
        """Asettaa luokan muutetun vastauksen muodon.

        Args:
            name: Merkkijonoarvo, joka määrittää uuden muodon vastaukselle. 
        """
        self._form = name

    def set_expression(self):
        """Lisää lausekkeeseen vastauksen.
        """
        self._expression = f"{self._expression}={self._answer}"

    def error(self):
        """Virheen sattuessa asettaa lausekkeen arvoksi error.
        """
        self._answer = "error"

    def press(self, symbol):
        """Lisää annetun symbolin lausekkeeseen ja palauttaa sitten lausekkeen käyttöliittymään kirjoitettavaksi.

        Args:
            symbol: Merkkijono-, numeroarvo. Määrittää, mikä symboli lisätään lausekkeeseen self._expression.
        """
        self._expression = self._expression + str(symbol)
        return self._expression

    def equal(self):
        """Määrittää missä muodossa lausekkeen arvo lasketaan ja palauttaa lausekkeen käyttöliittymään kirjoitettavaksi.
        """
        if self._expression == "":
            self._expression = "0"
        if self._form == "Decimal":
            self.calculate_decimal()
        if self._form == "Fraction":
            self.calculate_fraction()
        self.set_expression()
        return self._expression

    def clear_expression(self):
        """Tyhjentää lausekkeen.
        """
        self._expression = ""
        return self._expression

    def brackets(self):
        """Laskee, kuinka monta sulkumerkkiä lausekkeessa on ja sen perusteella lisää sulku merkin lausekkeeseen.
        """
        left = self._expression.count("(")
        right = self._expression.count(")")
        if left == right:
            self._expression = self._expression + "("
        if left > right:
            self._expression = self._expression + ")"
        return self._expression

    def calculate_decimal(self):
        """Laskee lausekkeen ja antaa vastauksen desimaalina.
        """
        try:
            self._answer = str(round(eval(self._expression), self._round))
        except (SyntaxError, ZeroDivisionError, OverflowError, TypeError, NameError):
            self.error()

    def calculate_fraction(self):
        """Laskee lausekkeen ja antaa vastauksen murtolukuna.
        """
        try:
            self._answer = Fraction(eval(self._expression)).limit_denominator()
        except (SyntaxError, ZeroDivisionError, OverflowError, TypeError, NameError):
            self.error()

    def ans(self):
        """Asettaa edellisen laskun vastauksen lausekkeseen.
        """
        return self.press(self._answer)
