#!/usr/bin/python3
"""
Script that changes the name of a State object in the database hbtn_0e_6_usa.

- Uses SQLAlchemy ORM.
- Imports Base and State from model_state.
- Connects to a MySQL server running on localhost at port 3306.
- Changes the name of the State where id=2 to "New Mexico".
- Does not execute when imported.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_name(mysql_user, mysql_pass, db_name):
    """
    Connects to the database, updates the State with id=2
    to have the name "New Mexico".
    """
    # Create engine
    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Retrieve the State object with id=2
        state = session.query(State).get(2)

        if state:
            # Update the name
            state.name = "New Mexico"
            session.commit()
    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: {} <mysql_user> <mysql_password> <db_name>".format(sys.argv[0])
        )
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    update_state_name(user, password, db_name)
