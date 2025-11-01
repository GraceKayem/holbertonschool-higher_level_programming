#!/usr/bin/python3
"""
Script that prints the State object ID with the name passed as argument
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_id_by_name(mysql_user, mysql_pass, db_name, state_name):
    """
    Connects to the MySQL database using SQLAlchemy ORM and returns
    the id of the State object whose name exactly matches `state_name`.

    Returns:
        state.id if found, None otherwise.
    """
    session = None
    try:
        # Create engine with connection to MySQL
        engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                mysql_user, mysql_pass, db_name
            ),
            pool_pre_ping=True
        )

        # Create session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query State object by exact name match
        state = session.query(State).filter(State.name == state_name).first()
        return state.id if state else None

    except Exception as e:
        print(e)
        return None

    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: {} <mysql_user> <mysql_password> <db_name> <state_name>"
            .format(sys.argv[0])
        )
        sys.exit(1)

    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    state_id = get_state_id_by_name(mysql_user, mysql_pass, db_name, state_name)

    if state_id is None:
        print("Not found")
    else:
        print(state_id)
