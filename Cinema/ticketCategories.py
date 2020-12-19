from Cinema import DatabaseContextManager, DB_NAME


def create_cinema_ticket_category_table():
    query = """CREATE TABLE IF NOT EXISTS TicketCategories (
                ticketCategoryId INTEGER PRIMARY KEY AUTOINCREMENT,
                type varchar(45) NOT NULL,
                price INTEGER NOT NULL)"""

    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)

def create_ticket_categories():
    query = """INSERT INTO ticketCategories VALUES (1,'ADULT',100),(2,'CHILDREN',80),(3,'ELDERLY',50)"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)


