from pathlib import Path
from entities.calculation import Calculation
from config import CALCULATOR_FILE_PATH


class CalculatorRepository:
    """[summary]
    """

    def __init__(self, file_path):
        """[summary]

        Args:
            file_path ([type]): [description]
        """

        self._file_path = file_path

    def add(self, calculation):
        """

        Args:
            calculations ([type]): [description]
        """

        calculations = self.find_all()

        calculations.append(calculation)

        self._write(calculations)

        return calculation

    def clear_file(self):
        """[summary]
        """

        self._write([])

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        calculations = []

        self._ensure_file_exists()

        with open(self._file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                expression = parts[0]
                solution = parts[1]

                calculations.append(Calculation(expression, solution))

        return calculations

    def _write(self, calculations):
        self._ensure_file_exists()

        with open(self._file_path, "w") as file:
            for calculation in calculations:
                
                row = f"{calculation.expression};{calculation.solution}"

                file.write(row+"\n")

calculator_repository = CalculatorRepository(CALCULATOR_FILE_PATH)