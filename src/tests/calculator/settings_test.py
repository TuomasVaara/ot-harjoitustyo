import unittest
from calculator.settings import Settings
from calculator.operations import Operations


class TestSettings(unittest.TestCase):

    def setUp(self):
        self._settings = Settings()
        self._operations = Operations()
        self._test_expression = self._operations.press("2/3")

    def test_settings_exist(self):
        self.assertEqual(self._settings._form, "Decimal")
        self.assertEqual(self._settings._round, 5)
        self.assertEqual(self._operations._expression, self._test_expression)

    def test_increase_default_decrese_round(self):
        self._settings.increase_round()
        self.assertEqual(self._settings._round, 6)
        self._settings.default_round()
        self.assertEqual(self._settings._round, 5)
        self._settings.decrease_round()
        self.assertEqual(self._settings._round, 4)

    def test_increase_round_works_in_calculator(self):
        self._operations.change_round(self._settings.increase_round())
        self._operations.equal()
        self.assertEqual(self._operations._expression,
                         f"2/3={round((2/3), 6)}")

    def test_decrease_round_works_in_calculator(self):
        self._operations.change_round(self._settings.decrease_round())
        self._operations.equal()
        self.assertEqual(self._operations._expression,
                         f"2/3={round((2/3), 4)}")

    def test_switch_fraction_decimal(self):
        self._settings.switch_form()
        self.assertEqual(self._settings._form, "Fraction")
        self._settings.switch_form()
        self.assertEqual(self._settings._form, "Decimal")

    def test_switch_fraction_decimal_works_in_calculator(self):
        self._operations.change_form(self._settings.switch_form())
        self._operations.equal()
        self.assertEqual(self._operations._expression, f"2/3=2/3")
