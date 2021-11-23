import unittest


import unittest
from Operations.operations import Operations

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.operations = Operations()

    def test_operations_exist(self):
        self.assertEqual(str(self.operations), "4 operations")

    def test_add_works_way_with_int(self):
        self.assertEqual(self.operations.Add(3,4), 7)

    def test_add_works_with_float(self):
        self.assertEqual(self.operations.Add(3.11,4.11), 7.22)

    def test_add_works_with_negative_numbers(self):
        self.assertEqual(self.operations.Add(-5,-9), -14)

    def test_add_round_correctly(self):
        self.assertEqual(self.operations.Add(2,5.5555), 7.56)