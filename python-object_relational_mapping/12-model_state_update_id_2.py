#!/usr/bin/python3
"""
Script that changes the name of a State object with id=2
in the database hbtn_0e_6_usa using SQLAlchemy ORM.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_name(user: str, passwd: str, dbname: str) -> None:
    """Connect to the database and update State.id=2 to 'New Mexico'."""
    session = None
    try:
        engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                user, passwd, dbname
            ),
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter_by(id=2).first()
        if state:
            state.name = "New Mexico"
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

    update_state_name(sys.argv[1], sys.argv[2], sys.argv[3])
