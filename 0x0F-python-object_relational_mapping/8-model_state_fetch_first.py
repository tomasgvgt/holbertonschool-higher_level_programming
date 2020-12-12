#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        first_state = session.query(State).filter(State.id == 1).first()
        print("{}: {}".format(first_state.id, first_state.name))
    except Exception:
        print("Nothing")
    session.close()
