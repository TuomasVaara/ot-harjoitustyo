
class Settings:
    def __init__(self, label1, label2, operations):
        self._round_view = label1
        self._fraction_decimal = label2
        self._operations = operations
        self._form = self._operations._form
        self._round = self._operations._round

    def increase_round(self):
        self._round += 1
        self._round_view.set(str(self._round))
        self._operations.set_round(self._round)

    def default_round(self):
        self._round = 1
        self._round_view.set(str(self._round))
        self._operations.set_round(self._round)

    def switch_fraction_decimal(self):
        if self._form == "Decimal":
            self._form = "Fraction"
        else:
            self._form = "Decimal"
        self._fraction_decimal.set(self._form)
        self._operations.set_form(self._form)
