from tests.testclass.operations_test_class import OperationsTest

class SettingsTest:
    def __init__(self):
        self._operations = OperationsTest()
        self._form = self._operations._form
        self._round = self._operations._round

    def increase_round(self):
        self._round += 1
        self._operations.set_round(self._round)

    def default_round(self):
        self._round = 1
        self._operations.set_round(self._round)

    def switch_fraction_decimal(self):
        if self._form == "Decimal":
            self._form = "Fraction"
        else:
            self._form = "Decimal"
        self._operations.set_form(self._form)