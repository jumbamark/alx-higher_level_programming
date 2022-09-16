#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    import imp
    from venv import create
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()
