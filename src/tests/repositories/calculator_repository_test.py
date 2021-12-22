import unittest
from repositories.calculator_repository import calculator_repository



class TestCalculatorRepository(unittest.TestCase):
    def setUp(self):
        calculator_repository._clear_file()

        self.expression1 = "2+2=4"
        self.expression2 = "3+3=6"

    def test_add(self):
        calculator_repository.add(self.expression1)
        calculations = calculator_repository.find_all()

        self.assertEqual(len(calculations), 1)
        self.assertEqual(calculations[0], self.expression1)

    def test_find_all(self):
        calculator_repository.add(self.expression1)
        calculator_repository.add(self.expression2)

        calculations = calculator_repository.find_all()

        self.assertEqual(len(calculations),2)
        self.assertTupleEqual((calculations[0],calculations[1]),(self.expression1,self.expression2))

