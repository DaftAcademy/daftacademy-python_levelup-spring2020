import sqlite3


def query(query: str, params=None):
    with sqlite3.connect("chinook.db") as connection:
        try:
            cursor = connection.cursor()
            cursor.row_factory = sqlite3.Row
            if params:
                return cursor.execute(query, params)
            return cursor.execute(query)
        except Exception:
            raise Exception
