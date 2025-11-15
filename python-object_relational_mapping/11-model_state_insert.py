#!/usr/bin/python3
"""
Module to perform simple queries on the model_state model
using an ORM - SQLAlchemy
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def connect_and_query(user: str, passwd: str, dbase: str) -> None:
    """
    Connect to the database and add a State named "Louisiana"
    """
    session = None
    try:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, passwd, dbase),
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create and add Louisiana
        louisiana = State(name="Louisiana")
        session.add(louisiana)
        session.commit()

        # Print the id of the new state
        print(louisiana.id)
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

    connect_and_query(sys.argv[1], sys.argv[2], sys.argv[3])
