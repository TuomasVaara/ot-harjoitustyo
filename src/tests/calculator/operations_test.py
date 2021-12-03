import unittest
from math import sin, cos, tan, pi, e, log, sqrt, factorial
from tests.calculator.operations_test_class import OperationsTest


class TestOperations(unittest.TestCase):

    def setUp(self):
        self._operations = OperationsTest()

    def test_operations_exist(self):
        self.assertEqual(self._operations._expression, "")

    def test_press_works_numbers(self):
        self._operations.press(1)
        self.assertEqual(self._operations._expression, "1")

    def test_press_works_var(self):
        self._operations.press("+")
        self.assertEqual(self._operations._expression, "+")

    def test_equal_works_without_expression(self):
        self._operations.equal()
        self.assertEqual(self._operations._expression, "=0")

    def test_equal_error_works(self):
        self._operations.press("5/0")
        self._operations.equal()
        self.assertEqual(self._operations._expression, "=error")

    def test_equal_expression_works(self):
        self._operations.press("5+8*2-1")
        self._operations.equal()
        self.assertEqual(self._operations._expression, "=20")

    def test_equal_sin_works(self):
        self._operations.press("sin(0)")
        self._operations.equal()
        self.assertEqual(self._operations._expression, f"={sin(0)}")

    def test_equal_con_works(self):
        self._operations.press("cos(0)")
        self._operations.equal()
        self.assertEqual(self._operations._expression, f"={cos(0)}")

    def test_equal_tan_works(self):
        self._operations.press("tan(0)")
        self._operations.equal()
        self.assertEqual(self._operations._expression, f"={tan(0)}")

    def test_equal_pi_neper_log_works(self):
        self._operations.press("π")
        self._operations.equal()
        self.assertEqual(self._operations._expression, f"={pi}")

    def test_equal_log_works(self):
        self._operations.press("log(1)")
        self._operations.equal()
        self.assertEqual(self._operations._expression, f"={log(1)}")

    def test_equal_neper_works(self):
        self._operations.press("e")
        self._operations.equal()
        self.assertEqual(self._operations._expression, f"={e}")

    def test_equal_power_square_factorial_works(self):
        self._operations.press("2**2+sqrt(4)+factorial(2)")
        self._operations.equal()
        self.assertEqual(self._operations._expression,
                         f"={2**2+sqrt(4)+factorial(2)}")

    def test_equal_basic_operations(self):
        self._operations.press("2+3-1*8/8")
        self._operations.equal()
        self.assertEqual(self._operations._expression, f"=4.0")

    def test_equal_error_with_false_expression(self):
        self._operations.press("2+3(8)-9*/89")
        self._operations.equal()
        self.assertEqual(self._operations._expression, "=error")

    def test_equal_negative_numbers_work(self):
        self._operations.press("-6--6-6--66")
        self._operations.equal()
        self.assertEqual(self._operations._expression, "=60")

    def test_clear_expression_works(self):
        self._operations.press("87558*+89/89*98*989+8854898584857**8")
        self._operations.clear_expression()
        self.assertEqual(self._operations._expression, "")

    def test_brackets_work(self):
        self._operations.brackets()
        self._operations.brackets()
        self.assertEqual(self._operations._expression, "()")

    def test_brackets_right_bracket(self):
        self._operations.brackets()
        self.assertEqual(self._operations._expression, "(")

    def test_brackets_left_bracket(self):
        self._operations.press("sqrt(16")
        self._operations.brackets()
        self.assertEqual(self._operations._expression, "sqrt(16)")
