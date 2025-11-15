#!/usr/bin/python3
"""
Module to add the State object "Louisiana" to the database hbtn_0e_6_usa
using SQLAlchemy ORM.
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def connect_and_query(user: str, passwd: str, dbase: str) -> None:
    """
    Connect to the database, add a new State named "Louisiana",
    and print its id.
    """
    session = None
    try:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, passwd, dbase),
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        # Add Louisiana
        louisiana = State(name="Louisiana")
        session.add(louisiana)
        session.commit()

        # Print the id of the new State
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
