#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.

- Uses SQLAlchemy ORM.
- Imports Base and State from model_state.
- Connects to a MySQL server running on localhost at port 3306.
- Prints the id of the new State after creation.
- Does not execute when imported.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state(mysql_user, mysql_pass, db_name):
    """
    Connect to the database, add a new State named "Louisiana",
    and print its id.
    """
    # Create SQLAlchemy engine
    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Create a new State object
        new_state = State(name="Louisiana")

        # Add to session and commit
        session.add(new_state)
        session.commit()

        # Print the id of the new state
        print(new_state.id)
    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_user> <mysql_password> <db_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    add_state(user, password, db_name)
