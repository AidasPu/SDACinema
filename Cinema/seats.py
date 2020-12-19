from Cinema import DatabaseContextManager, DB_NAME


def create_cinema_seats_table():
    query = """CREATE TABLE IF NOT EXISTS Seats(
                seatId INTEGER PRIMARY KEY AUTOINCREMENT,
                row INTEGER NOT NULL,
                number INTEGER NOT NULL,
                roomId INTEGER NOT NULL,
                FOREIGN KEY (roomId) REFERENCES Rooms(roomId))"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)

def create_seats():
    query = """INSERT INTO Seats VALUES (1,1,1,1),(2,1,2,1),(3,1,3,1),(4,2,1,1),(5,2,2,1),(6,2,3,1),(12,1,1,2),(13,1,2,2),(14,1,3,2),(15,2,1,2),(16,2,2,2),(17,2,3,2)"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)


