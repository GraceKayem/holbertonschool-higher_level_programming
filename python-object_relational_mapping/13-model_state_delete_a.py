#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing 'a'
from the database hbtn_0e_6_usa using SQLAlchemy ORM.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(user: str, passwd: str, db_name: str) -> None:
    """Connect to the database and delete states containing 'a' in their name."""
    session = None
    try:
        engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db_name),
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query all states containing 'a'
        states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

        # Delete each state
        for state in states_to_delete:
            session.delete(state)

        session.commit()

    except Exception as e:
        print(e)
    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: {} <mysql_user> <mysql_password> <db_name>".format(sys.argv[0])
        )
        sys.exit(1)

    delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
