#!/usr/bin/python3
"""
script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create a State Instance for Louisiana
    cali_state = State(name='California')
    sanfran_city = City(name='San Francisco')
    cali_state.cities.append(sanfran_city)
    session.add(cali_state)
    session.add(sanfran_city)
    session.commit()
    session.close()
