#!/usr/bin/python3
"""
Script that lists all State objects containing the letter 'a'
from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def connect_and_query(user: str, passwd: str, db_name: str, search: str):
    """
    Connect to the MySQL database using SQLAlchemy ORM and return the
    State object whose name exactly matches `state_name`.

    Returns:
        the id of the matched State as an integer (or whatever type is used),
        or None if no matching State is found.
    """
    try:
        # Create the engine. The connection string targets localhost on the default MySQL port (3306). Using SQLAlchemy ORM methods prevents SQL injection by passing values as parameters to the query engine.
        engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                mysql_user, mysql_pass, db_name
            ),
            pool_pre_ping=True,
        )

        # Create a configured "Session" class bound to this engine
        Session = sessionmaker(bind=engine)

        # Create a Session instance for DB operations
        session = Session()

         # Use ORM filter to safely query for the State with exact name match.
        # .first() returns the first matching State object or None.
        state = session.query(State).filter(State.name == state_name).first()

        if state:
            return state.id
        return None

            
        finally:
            # Always close the session to release DB resources
            session.close()
            


# Only executes the function when running the script directly
# Takes command-line arguments for MySQL credentials and database name
if __name__ == "__main__":
    connect_and_query(sys.argv[1], sys.argv[2], sys.argv[3])

    # Ensure the user provided exactly 4 arguments (username, password,
    # database, state_name). Use a helpful usage output if not.
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_user> <mysql_password> <db_name> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    state_id = get_state_id_by_name(mysql_user, mysql_pass, db_name, state_name)

    # Print result according to the project's requirements
    if state_id is None:
        print("Not found")
    else:
        print(state_id)