#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def connect_and_query(user: str, passwd: str, db_name: str):
    """Connect to the database and print the first State object by id."""
    try:
        # Connect to the MySQL database using SQLAlchemy
        engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}")

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the first State object ordered by id ascending
        state = session.query(State).order_by(State.id).first()

        # Print the state or "Nothing" if table is empty
        if state is not None:
            print(state)
        else:
            print("Nothing")

        # Close the session
        session.close()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)
    connect_and_query(sys.argv[1], sys.argv[2], sys.argv[3])
