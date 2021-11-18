import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

Budjet_Filename = os.getenv('Budjet_Filename') or 'budjet.csv'
Budjet_File_Path = os.path.join(dirname, '..', 'data', Budjet_Filename)

Database_Filename = os.getenv('Database_Filename') or "budjet.sqlite"
Database_File_Path = os.path.join(dirname, '..', 'data', Database_Filename)