from Cinema import DatabaseContextManager, DB_NAME


def create_cinema_rooms_table():
    query = """CREATE TABLE IF NOT EXISTS Rooms(
  roomId INTEGER PRIMARY KEY AUTOINCREMENT,
  number INTEGER NOT NULL,
  maxSeats INTEGER NOT NULL,
  location varchar(45) DEFAULT NULL)"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)
