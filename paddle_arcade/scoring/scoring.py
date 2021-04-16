import sqlite3

from sqlite3 import Error
from sqlite3.dbapi2 import Connection, Cursor

from datetime import date


def create_connection(db_file: str="./paddle_arcade/scoring/Games.db") -> Connection:
    """ Create a database connection to an SQLite database """
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn