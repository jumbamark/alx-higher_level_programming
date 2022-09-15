#!/usr/bin/python3
"""
lists all state objects from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine(
                           "mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True
                           )
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
