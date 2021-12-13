
class Settings:
    def __init__(self, label1, label2, operations):
        self._round_view = label1
        self._fraction_decimal = label2
        self._operations = operations
        self.form = self._operations._form
        self.round = self._operations._round

    def increase_round(self):
        self.round += 1
        self._round_view.set(str(self.round))
        self._operations.set_round(self.round)

    def decrease_round(self):
        if self.round > 1:
            self.round -= 1
        self._round_view.set(str(self.round))
        self._operations.set_round(self.round)

    def default_round(self):
        self.round = 5
        self._round_view.set(str(self.round))
        self._operations.set_round(self.round)

    def switch_fraction_decimal(self):
        if self.form == "Decimal":
            self.form = "Fraction"
        else:
            self.form = "Decimal"
        self._fraction_decimal.set(self.form)
        self._operations.set_form(self.form)
