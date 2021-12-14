class Setter:
    """Huolehtii käyttöliittymän muuttuvista elementeistä.
    """
    def __init__(self, equation, form_view, round_view, operations, settings):
        """Luokan konstruktori. Luo olion, joka vastaa, että sovelluslogiikka ja käyttöliittymä toimivat yhdessä.

        Args:
            equation: Tkinter StringVar olio. Määrittää calculator näkymässä, lausekkeen.
            form_view: Tkinter StringVar olio. Määrittää settings näkymässä, laskujen vastausten muodon.
            round_view: Tkinter StringVar olio. Määrittää settings näkymässä, laskujen pyöristys tarkkuuden.
            operations: Operations olio. Määrittää ohjelman laskutoimitukset ja palauttaa arvot, joilla muokataan equation oliota.
            settings: Settings olio. Määrittää ohjelman asetuksia, kuten pyöristyksen ja vastauksen muodon. Palauttaa arvot, joilla muokataa form_view ja round_view olioita
        """
        self._equation = equation
        self._round = round_view
        self._form = form_view

        self._operations = operations
        self._settings = settings
# Calculator

    def set_press(self, symbol):
        """Kirjoittaa annetun symbolin/symbolit equation olioon.

        Args:
            symbol: Merkkijono- tai numeroarvo, joka määrittää mitä equattion olioon kirjoitetaan.
        """
        self._equation.set(self._operations.press(symbol))

    def set_equation(self):
        """Kutsuu Operation oliota laskemaam nykyisen lausekkeen ja kirjoittaa saadun vastauksen equation olioon.
        """
        self._equation.set(self._operations.equal())
        self._operations.clear_expression()

    def set_clear_expression(self):
        """Tyhjentää Operation olion lausekkeen.
        """
        empty = self._operations.clear_expression()
        self._equation.set(empty)

    def set_brackets(self):
        """Kirjoittaa equation olioon sulkumerkin riippuen lausekkeen sulkumerkkien määrästä.
        """
        self._equation.set(self._operations.brackets())

    def set_ans(self):
        """Kirjoittaa edellisen laskun vastauksen equation olioon.
        """
        self._equation.set(self._operations.ans())
# Settings

    def set_increase_round(self):
        """Kasvattaa Settings olion avulla ohjelman pyöristys tarkkuutta. Kirjoittaa nykyisen tarkkuuden round_view olioon.
        """
        new_round = self._settings.increase_round()
        self._round.set(new_round)
        self._operations.change_round(new_round)

    def set_decrease_round(self):
        """Laskee Settings olion avulla ohjelman pyöristys tarkkuutta. Kirjoittaa nykyisen tarkkuuden round_view olioon.
        """
        new_round = self._settings.decrease_round()
        self._round.set(new_round)
        self._operations.change_round(new_round)

    def set_default_round(self):
        """Muuttaa Settings olion avulla ohjelman pyöristys tarkkuuden alkuperäiseksi. Kirjoittaa nykyisen tarkkuuden round_view olioon.
        """
        default = self._settings.default_round()
        self._round.set(default)
        self._operations.change_round(default)

    def set_form(self):
        """Muuttaa Settings olion avulla ohjelman vastauksen muotoa. Kirjoittaa nykyisen muodon form_view olioon.
        """
        new_form = self._settings.switch_form()
        self._form.set(new_form)
        self._operations.change_form(new_form)
