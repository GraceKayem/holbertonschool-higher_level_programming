#!/usr/bin/python3
"""
Script that lists all State objects containing the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def connect_and_query(user: str, passwd: str, db_name: str):
    """
    Connect to the database and list all State objects containing 'a',
    sorted by ascending id.
    """
    try:
        # Connect to the MySQL database using SQLAlchemy
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(user, passwd, db_name))

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a session instance to perform queries
        session = Session()

        # Query State objects where name contains 'a', ordered by id
        states_containing_a = session.query(State)\
                                     .filter(State.name.like('%a%'))\
                                     .order_by(State.id)\
                                     .all()
        # .all() fetches all matching State objects as a list

        # Iterate over the retrieved states and print each
        for state in states_containing_a:
            print(state)
            # Each state prints as "id: name" due to __repr__ in model_state

    except Exception as e:
        # Catch any errors during connection, session creation, or querying
        return e


# Only executes the function when running the script directly
# Takes command-line arguments for MySQL credentials and database name
if __name__ == "__main__":
    connect_and_query(sys.argv[1], sys.argv[2], sys.argv[3])
