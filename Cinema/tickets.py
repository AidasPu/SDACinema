from Cinema import DatabaseContextManager, DB_NAME


def create_cinema_tickets_table():
    query = """CREATE TABLE IF NOT EXISTS Tickets(
                ticketId INTEGER PRIMARY KEY AUTOINCREMENT,
                scheduleId INTEGER NOT NULL,
                seatId INTEGER NOT NULL,
                categoryId INTEGER NOT NULL,
                FOREIGN KEY (scheduleId) REFERENCES Schedules(scheduleId),
                FOREIGN KEY (seatId) REFERENCES Seats(seatId),
                FOREIGN KEY (categoryId) REFERENCES ticketCategories(ticketCategoryId))"""

    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)


def create_tickets():
    query = """INSERT INTO tickets VALUES (1,2,1,1),(2,2,1,2)"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)