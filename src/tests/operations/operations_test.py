import unittest
import tkinter
from math import sin, cos, tan, pi, e, log, sqrt, factorial
from operations.operations import Operations



class TestOperations(unittest.TestCase):

    def setUp(self):
        self._e = tkinter.StringVar()
        self._operations = Operations(self._e)

    def test_operations_exist(self):
        self.assertEqual(str(self._operations), "")
    
    def test_press_works_numbers(self):
        self.assertEqual(self._operations.press("1"), "1")
    
    def test_press_works_abc(self):
        None

    def test_equal_works_without_expression(self):
        None

    def test_equal_error_works(self):
        None
    
    def test_equal_expression_works(self):
        None

    def test_equal_sincostan_works(self):
        None
    
    def test_equal_pi_neper_log_works(self):
        None

    def test_equal_power_square_factorial_works(self):
        None

    def test_equal_basic_operations(self):
        None

    def test_equal_error_with_false_expression(self):
        None

    def test_equal_negative_numbers_work(self):
        None

    def test_clear_expression_works(self):
        None

    def test_brackets_work(self):
        None
    
    def test_brackets_right_bracket(self):
        None
    
    def test_brackets_left_bracket(self):
        None
    

    

    
    