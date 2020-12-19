import sqlite3
class DatabaseContextManager():
    def __init__(self, path):
        self.path = path
    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()



def bank_account_table():
    query = """CREATE TABLE IF NOT EXISTS Account(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    balance FLOAT)"""
    with DatabaseContextManager("Bank") as db:
        db.execute(query)


def transaction(from_account, to_account, amount):
    query = """UPDATE Account
                SET balance = balance - ?
                WHERE id = ?"""


    query1 = """UPDATE Account
                    SET balance = balance + ?
                    WHERE id = ?"""

    params = [amount, from_account]
    params1 = [amount, to_account]
    with DatabaseContextManager("Bank") as db:
        db.execute(query)
