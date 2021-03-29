#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    # Query (Returns an array of objects)
    state_1 = session.query(State).first()
    # Loop trough the array and print id and name for each object
    print("{}: {}".format(state_1.id, state_1.name))
    session.close()
