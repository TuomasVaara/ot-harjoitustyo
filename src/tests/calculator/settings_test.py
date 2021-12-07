import unittest
from tests.testclass.settings_test_class import SettingsTest

class TestSettings(unittest.TestCase):
    
    def setUp(self):
        self._settings = SettingsTest()
        self._test_expression = self._settings._operations.press("2/3")

    def test_settings_exist(self):
        self.assertEqual(self._settings._form, "Decimal")
        self.assertEqual(self._settings._round, 1)

    def test_increase_round_works_in_calculator(self):
        self._settings.increase_round()
        self._settings._operations.equal()
        self.assertEqual(self._settings._operations._expression, f"={round((2/3), 2)}")

    def test_increase_default_round(self):
        self._settings.increase_round()
        self.assertEqual(self._settings._round, 2)
        self._settings.default_round()
        self.assertEqual(self._settings._round, 1)

    def test_default_round_works_in_calculator(self):
        self._settings.increase_round()
        self._settings.default_round()
        self._settings._operations.equal()
        self.assertEqual(self._settings._operations._expression, f"={round((2/3), 1)}")

    def test_switch_fraction_decimal(self):
        self._settings.switch_fraction_decimal()
        self.assertEqual(self._settings._form, "Fraction")
        self._settings.switch_fraction_decimal()
        self.assertEqual(self._settings._form, "Decimal")

    def test_switch_fraction_decimal_works_in_calculator(self):
        self._settings.switch_fraction_decimal()
        self._settings._operations.equal()
        self.assertEqual(self._settings._operations._expression, f"=2/3")
