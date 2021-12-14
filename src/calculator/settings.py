
class Settings:
    """Toinen sovelluslogiikan toteuttavista luokista.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo olion vastaamaan sovelluksen sovelluslogiikasta.
        """
        self._form = "Decimal"
        self._round = 5

    def increase_round(self):
        """Kasvattaa laskimen pyöristys tarkkuutta.
        """
        self._round += 1
        return self._round

    def decrease_round(self):
        """Vähentaa laskimen pyöristys tarkkuutta.
        """
        if self._round > 1:
            self._round -= 1
        return self._round

    def default_round(self):
        """Asettaa laskimen pyöristys tarkkuuden takaisin alkuperäiseen tarkkuuteen.
        """
        self._round = 5
        return self._round

    def switch_form(self):
        """Vaihtaa laskimen vastauksen muodon.
        """
        if self._form == "Decimal":
            self._form = "Fraction"
        else:
            self._form = "Decimal"
        return self._form
