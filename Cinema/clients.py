from Cinema import DatabaseContextManager, DB_NAME


def create_cinema_client_table():
    query = """CREATE TABLE IF NOT EXISTS Clients(
              clientId INTEGER PRIMARY KEY AUTOINCREMENT,
              firstName varchar(45) NOT NULL,
              lastName varchar(45) NOT NULL,
              email varchar(45) NOT NULL,
              dateOfBirth date NOT NULL)"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)


def create_clients():
    query = """INSERT INTO clients VALUES (1,'John','Johnson','john@johnson.com','1980-01-01'),(2,'Jim','Jameson','jim@jameson.com','1990-02-02'),(3,'Sofia','Sophie','sofia@sophie','2000-01-01');"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)


# 4.List all movies reserved by John Johnson.

def get_movies_by_name(name):
    query = """SELECT name, firstName FROM Clients
                JOIN Reservations ON Clients.clientId = Reservations.clientId
                JOIN Schedules ON Reservations.scheduleId = Schedules.scheduleId
                JOIN Movies ON Movies.movieId = Schedules.movieId
                WHERE firstName = ?"""
    params = [name]
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query, params)
        print(db.fetchall())

# get_movies_by_name("John")

# 5.List all the seat rows and numbers reserved by John Johnson.
def get_seat_rows_and_numbers_by_client(client):
    query = """SELECT row, number FROM Clients
                JOIN Reservations ON Reservations.clientId = Clients.clientId
                JOIN Reservation_seat ON Reservations.reservationId = Reservation_seat.reservationId
                JOIN Seats ON Seats.seatId = Reservation_seat.seatId
                WHERE firstName = ?"""

    params = [client]
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query,params)
        print(db.fetchall())

get_seat_rows_and_numbers_by_client("John")