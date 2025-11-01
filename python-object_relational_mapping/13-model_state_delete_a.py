#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.

- Uses SQLAlchemy ORM.
- Imports Base and State from model_state.
- Connects to a MySQL server running on localhost at port 3306.
- Does not execute when imported.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(mysql_user, mysql_pass, db_name):
    """
    Connects to the database and deletes all State objects
    where the name contains the letter 'a'.
    """
    # Create the engine
    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query all states containing 'a'
        states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

        # Delete each state
        for state in states_to_delete:
            session.delete(state)

        # Commit changes
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

    delete_states_with_a(user, password, db_name)
