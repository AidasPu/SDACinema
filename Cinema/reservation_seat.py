from Cinema import DatabaseContextManager, DB_NAME


def create_cinema_reservation_seat_table():
    query = """CREATE TABLE IF NOT EXISTS Reservation_seat(
    reservationSeatId INTEGER PRIMARY KEY AUTOINCREMENT,
    reservationId INTEGER NOT NULL,
    seatId INTEGER NOT NULL,
    FOREIGN KEY (reservationId) REFERENCES reservations(reservationId) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (seatId) REFERENCES Seats(seatId) ON DELETE NO ACTION ON UPDATE NO ACTION)"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)

def create_reservation_seat():
    query = """INSERT INTO reservation_seat VALUES (1,1,1),(2,1,2)"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)

