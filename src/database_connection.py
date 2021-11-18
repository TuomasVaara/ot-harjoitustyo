import sqlite3
from config import Database_File_Path

connection = sqlite3.connect(Database_File_Path)
connection.rowfactory = sqlite3.Row


def get_database_connection():
    return connection