#!/usr/bin/python3
"""
Module to perform simple queries on the model_state model
using an ORM - SQLAlchemy
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def connect_and_query(user: str, passwd: str, dbase: str, search: str) -> None:
    """
    Connect to the database and make queries using ORM

    Args:
        user (str): MySQL user
        passwd (str): MySQL password for `user`
        dbase (str): Database to use
        search (str): State to search for
    """
    session = None
    try:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                user, passwd, dbase
            ),
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).order_by(State.id).all()

        for state in states:
            if state.name == search:
                print(state.id)
                break
        else:
            print("Not found")
    except Exception as e:
        print(e)
    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: {} <user> <passwd> <db_name> <state_name>".format(
                sys.argv[0]
            )
        )
        sys.exit(1)

    connect_and_query(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
