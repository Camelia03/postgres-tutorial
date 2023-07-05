from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


class Favorite_Places(base):
    __tablename__ = ("Favorite_Places")
    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)
    population = Column(Integer)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

maldives = Favorite_Places(
    country="Maldives",
    city="Male",
    population=6936
)

italy = Favorite_Places(
    country="Italy",
    city="Rome",
    population=693663
)

france = Favorite_Places(
    country="France",
    city="Paris",
    population=693685
)

spain = Favorite_Places(
    country="Spain",
    city="Barcelona",
    population=6936888
)

# session.add(maldives)
session.add(italy)
session.add(france)
session.add(spain)

session.commit()

places = session.query(Favorite_Places)

for place in places:
    print(place.id,
          place.country,
          place.city,
          place.population,
          sep=" | ")
