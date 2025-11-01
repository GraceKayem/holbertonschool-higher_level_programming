#!/usr/bin/python3
"""
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
import sys


def connect_and_query(user: str, passwd: str, db_name: str):
    """
    Connect to the database and list all State objects containing 'a',
    sorted by ascending id.
    """
    if __name__ == "__main__":
    # Check that exactly 3 arguments are provided (user, password, db_name)
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_user> <mysql_password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve CLI arguments
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Create a SQLAlchemy engine to connect to the MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(mysql_user, mysql_pass, db_name),
        pool_pre_ping=True
    )

    # Bind the engine to a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for "Louisiana"
    new_state = State(name="Louisiana")

    # Add the object to the session and commit to save to the database
    session.add(new_state)
    session.commit()

    # Print the new state's id after creation
    print(new_state.id)

    # Close the session
    session.close()
