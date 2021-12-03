import unittest
from tests.calculator.settings_test_class import SettingsTest

class TestSettings(unittest.TestCase):
    
    def setUp(self):
        self._settings = SettingsTest()
        self._form = self._settings._form
        self._round = self._settings._round
        self._test_expression = self._settings._operations.press("2/3")

    def test_settings_exist(self):
        self.assertEqual(self._form, "Decimal")
        self.assertEqual(self._round, 1)

    def test_increase_round(self):
        self._settings.increase_round()
        self.assertEqual(self._round, 2)

    def test_increase_round_works(self):
        None

    def test_default_round(self):
        self._settings.increase_round()
        self._settings.default_round()
        self.assertEqual(self._round, 1)

    def test_default_round_works(self):
        None

    def test_switch_fraction_decimal(self):
        self._settings.switch_fraction_decimal()
        self.assertEqual(self._form, "Fraction")
        self._settings.switch_fraction_decimal()
        self.assertEqual(self._form, "Decimal")

    def test_switch_fraction_decimal_works(self):
        None
