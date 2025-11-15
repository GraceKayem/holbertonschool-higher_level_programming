#!/usr/bin/python3
"""
Script that changes the name of a State object in the database
hbtn_0e_6_usa.

- Uses SQLAlchemy ORM
- Imports Base and State from model_state
- Connects to a MySQL server running on localhost at port 3306
- Changes the name of the State where id=2 to "New Mexico"
- Does not execute when imported
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_name(user: str, passwd: str, db_name: str) -> None:
    """Update the State object with id=2 to have the name 'New Mexico'."""
    session = None
    try:
        # Create engine to connect to MySQL
        engine = create_engine(
            f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}",
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query for the state with id=2
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
        print(f"Usage: {sys.argv[0]} <mysql_user> <mysql_password> <db_name>")
        sys.exit(1)

    update_state_name(sys.argv[1], sys.argv[2], sys.argv[3])
