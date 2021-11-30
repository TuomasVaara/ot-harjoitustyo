import unittest
from builders.build_home_view.py import HomeBuilder
from ui.home_view import HomeView

class TestHomeBuilder(unittest.TestCase):

    def setUp(self):
        self._homebuilder = HomeBuilder()
        self._homeview = HomeView()

    def homebuilder_exists_test(self):
        None
    def buttons_are_created_test(self):
        None
    def exit_button_workd_test(self):
        None
    def calculator_button_works_test(self):
        None