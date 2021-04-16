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


def create_table(conn: Connection, create_tbl_statement: str) -> None:
    """ Create a table from create_tbl_statement on the conn connection passed """
    try:
        c = conn.cursor()
        c.execute(create_tbl_statement)
    except Error as e:
        print(e)

