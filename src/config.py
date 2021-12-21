import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

CALCULATOR_FILENAME = os.getenv("CALCULATOR_FILENAME") or "calculations.csv"
CALCULATOR_FILE_PATH = os.path.join(dirname, '..', 'data', CALCULATOR_FILENAME)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)
