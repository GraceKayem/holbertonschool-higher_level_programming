#!/usr/bin/python3
"""
Module to perform simple queries on the model_state model
using an ORM - SQLAlchemy.
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def delete_states_with_a(user: str, passwd: str, dbname: str) -> None:
    """Delete all State objects containing 'a' in their name."""
    session = None
    try:
        engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, dbname),
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        states = session.query(State).filter(State.name.like('%a%')).all()
        for state in states:
            session.delete(state)

        session.commit()

    except Exception as e:
        print(e)

    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_user> <mysql_password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
