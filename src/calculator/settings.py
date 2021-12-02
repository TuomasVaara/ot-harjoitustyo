
class Settings:
    def __init__(self, label1, label2, operations):
        self._round_view = label1
        self._fraction_decimal = label2
        self._operations = operations

    def increase_round(self):
        self._operations._round += 1
        self._round_view.set(str(self._operations._round))
        lambda: self._operations.set_round(self._operations._round)

    def default_round(self):
        self._operations._round = 1
        self._round_view.set(str(self._operations._round))
        lambda: self._operations.set_round(self._operations._round)

    def switch_fraction_decimal(self):
        if self._operations._form == "Decimal":
            self._operations._form = "Fraction"
        else:
            self._operations._form = "Decimal"
        self._fraction_decimal.set(self._operations._form)
        lambda: self._operations.set_form(self._operations._form)
