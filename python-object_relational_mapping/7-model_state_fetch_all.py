#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def connect_and_query(user: str, passwd: str, db_name: str):
    """Connect to the database and list all State objects sorted by id."""
    try:
        # Create engine and connect to MySQL database
        engine = create_engine(
            f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}"
        )

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a session instance to perform queries
        session = Session()

        # Query all State objects, ordered by id
        states = session.query(State).order_by(State.id).all()

        # Print each state in the format: id: name
        for state in states:
            print(f"{state.id}: {state.name}")

        # Close the session
        session.close()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)
    connect_and_query(sys.argv[1], sys.argv[2], sys.argv[3])
