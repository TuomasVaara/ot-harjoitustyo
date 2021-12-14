import unittest
from tests.testclass.settings_test_class import SettingsTest

class TestSettings(unittest.TestCase):
    
    def setUp(self):
        self._settings = SettingsTest()
        self._test_expression = self._settings._operations.press("2/3")

    def test_settings_exist(self):
        self.assertEqual(self._settings._form, "Decimal")
        self.assertEqual(self._settings._round, 5)

    def test_increase_round_works_in_calculator(self):
        self._settings.increase_round()
        self._settings._operations.equal()
        self.assertEqual(self._settings._operations._expression, f"2/3={round((2/3), 6)}")

    def test_increase_default_decrese_round(self):
        self._settings.increase_round()
        self.assertEqual(self._settings._round, 6)
        self._settings.default_round()
        self.assertEqual(self._settings._round, 5)
        self._settings.decrease_round()
        self.assertEqual(self._settings._round, 4)

    def test_decrease_round_works_in_calculator(self):
        self._settings.decrease_round()
        self._settings._operations.equal()
        self.assertEqual(self._settings._operations._expression, f"2/3={round((2/3), 4)}")

    def test_default_round_works_in_calculator(self):
        self._settings.increase_round()
        self._settings.default_round()
        self._settings._operations.equal()
        self.assertEqual(self._settings._operations._expression, f"2/3={round((2/3), 5)}")

    def test_switch_fraction_decimal(self):
        self._settings.switch_fraction_decimal()
        self.assertEqual(self._settings._form, "Fraction")
        self._settings.switch_fraction_decimal()
        self.assertEqual(self._settings._form, "Decimal")

    def test_switch_fraction_decimal_works_in_calculator(self):
        self._settings.switch_fraction_decimal()
        self._settings._operations.equal()
        self.assertEqual(self._settings._operations._expression, f"2/3=2/3")
