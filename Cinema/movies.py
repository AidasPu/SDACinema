from Cinema import DatabaseContextManager, DB_NAME
from datetime import datetime

def create_cinema_movies_table():
    query = """CREATE TABLE IF NOT EXISTS Movies (
                movieId INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(45) NOT NULL,
                category VARCHAR(45) NOT NULL,
                durationInMinutes INTEGER NOT NULL,
                description VARCHAR(255) NOT NULL)"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)


def create_movies():
    query = """INSERT INTO `movies` VALUES (1,'Men in Black: International','Action',114,'The Men in Black have always protected the Earth from the scum of the universe. In this new adventure, they tackle their biggest threat to date: a mole in the Men in Black organization.'),
    (2,'Joker','Crime, Drama, Thriller ',122,'In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society. He then embarks on a downward spiral of revolution and bloody crime. This path brings him face-to-face with his alter-ego: the Joker.'),
    (3,'Frozen II','Animation, Adventure, Comedy ',103,'Anna, Elsa, Kristoff, Olaf and Sven leave Arendelle to travel to an ancient, autumn-bound forest of an enchanted land. They set out to find the origin of Elsas powers in order to save their kingdom.'),
    (4,'Parasite','Comedy, Crime, Drama',132,'A poor family, the Kims, con their way into becoming the servants of a rich family, the Parks. But their easy life gets complicated when their deception is threatened with exposure.')"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)

create_movies()
def get_all_movies():
    query = """SELECT * FROM Movies"""
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)
        print(db.fetchall())

# # 2.List all movies running on 2020-01-01.

def get_movies_today():
    query = """SELECT * FROM Movies
                JOIN Schedules ON Movies.movieId = Schedules.movieId
                WHERE startTime >= ?"""
    date = datetime.today()
    params = [date]
    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query, params)
        print(db.fetchall())

# get_movies_today()

# 3.List all movies that are not yet scheduled to run in the cinema.

def get_unscheduled_movies():
    query = """SELECT * FROM Movies
                JOIN Schedules ON Movies.movieId = Schedules.movieId
                WHERE scheduleId == NULL"""

    with DatabaseContextManager(DB_NAME) as db:
        db.execute(query)
        print(db.fetchall())

