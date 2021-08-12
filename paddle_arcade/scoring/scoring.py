import sqlite3

from sqlite3 import Error
from sqlite3.dbapi2 import Connection, Cursor

from datetime import date


def create_connection(db_file: str = "./paddle_arcade/scoring/Games.db") -> Connection:
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


def add_game_rec(conn: Connection, p1: int, p2: int) -> None:
    statement = "INSERT INTO Games (p1, p2, date) VALUES (?, ?, ?)"

    with conn:
        c = conn.cursor()
        c.execute(statement, (p1, p2, str(date.today())))


def delete_by_id(conn: Connection, id: int) -> None:
    """ Delete game record by id """
    statement = "DELETE FROM Games WHERE id=?"

    with conn:
        c = conn.cursor()
        c.execute(statement, (id,))
