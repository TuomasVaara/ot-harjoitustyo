
class Settings:
    """Toinen sovelluslogiikan toteuttavista luokista.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo olion vastaamaan sovelluksen sovelluslogiikasta.
        """
        self.form = "Decimal"
        self.round = 5

    def increase_round(self):
        """Kasvattaa laskimen pyöristys tarkkuutta.
        """
        self.round += 1
        return self.round

    def decrease_round(self):
        """Vähentaa laskimen pyöristys tarkkuutta.
        """
        if self.round > 1:
            self.round -= 1
        return self.round

    def default_round(self):
        """Asettaa laskimen pyöristys tarkkuuden takaisin alkuperäiseen tarkkuuteen.
        """
        self.round = 5
        return self.round

    def switch_form(self):
        """Vaihtaa laskimen vastauksen muodon.
        """
        if self.form == "Decimal":
            self.form = "Fraction"
        else:
            self.form = "Decimal"
        return self.form
