from Cinema import DatabaseContextManager, DB_NAME


def create_cinema_reservation_table():
    query = """CREATE TABLE IF NOT EXISTS Reservations(
  reservationId INTEGER PRIMARY KEY AUTOINCREMENT,
  isPaid INTEGER NOT NULL,
  clientId INTEGER NOT NULL,
  scheduleId INTEGER NOT NULL,
  FOREIGN KEY (clientId) REFERENCES Clients (clientId) ON DELETE NO ACTION ON UPDATE NO ACTION,
  FOREIGN KEY (scheduleId) REFERENCES Schedules(scheduleId) ON DELETE NO ACTION ON UPDATE NO ACTION)"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)


def create_reservations():
    query = """INSERT INTO reservations VALUES (1,0,1,1)"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)

