from Cinema import DatabaseContextManager, DB_NAME


def create_cinema_schedules_table():
    query = """CREATE TABLE IF NOT EXISTS Schedules(
                scheduleId INTEGER PRIMARY KEY AUTOINCREMENT,
                startTime DATE NOT NULL,
                movieId INTEGER NOT NULL,
                roomId INTEGER NOT NULL,
                FOREIGN KEY (movieId) REFERENCES Movies(movieId),
                FOREIGN KEY (roomId) REFERENCES Rooms(roomId)
  )"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)

def create_schedules():

    query = """    INSERT INTO schedules VALUES(1, '2020-01-01 20:00:00', 1, 1), 
    (2, '2020-01-01 20:00:00', 2, 2), 
    (3, '2020-01-01 23:00:00', 3, 1), 
    (4, '2020-01-02 18:00:00', 1, 1)"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)


# create_schedules()