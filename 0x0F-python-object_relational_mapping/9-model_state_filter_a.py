#!/usr/bin/python3

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
    a_states = session.query(State).filter(
        State.name.contains('a')).order_by(State.id)
    # Loop trough the array and print id and name for each object
    for a_state in a_states:
        print("{}: {}".format(a_state.id, a_state.name))
    session.close()
