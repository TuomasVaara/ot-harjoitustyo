from pathlib import Path
from config import CALCULATOR_FILE_PATH


class CalculatorRepository:
    """Laskujen lukemista ja lisäämistä hoitava luokka.
    """

    def __init__(self, file_path):
        """Luokan konstruktori. Luo uuden tiedon hoitamisesta vastaavan palvelun.

        Args:
            file_path : polku tiedostoon.
        """

        self._file_path = file_path

    def add(self, calculation):
        """ Lisää tietokantaan laskun 

        Args:
            calculations : Merkkijono olio, joka lisätään tiedostoon.
        """

        calculations = self.find_all()

        calculations.append(calculation)

        self._write(calculations)

        return calculation

    def find_all(self):
        """Palauttaa kaikki lasketut laskut.

        Returns:
            Palauttaa listan kaikista laskuista.
        """
        return self._read()

    def _clear_file(self):
        """Tyhjentää tiedoston.
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

                calculations.append(row)

        return calculations

    def _write(self, calculations):
        self._ensure_file_exists()

        with open(self._file_path, "w") as file:
            for calculation in calculations:

                file.write(calculation+"\n")


calculator_repository = CalculatorRepository(CALCULATOR_FILE_PATH)
