#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.

- Uses SQLAlchemy ORM
- Imports Base and State from model_state
- Connects to a MySQL server running on localhost at port 3306
- Prints the new state's id after creation
- Does not execute when imported
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_louisiana(user: str, passwd: str, db_name: str) -> None:
    """Connect to the database, add Louisiana, and print its id."""
    session = None
    try:
        # Connect to MySQL database
        engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db_name),
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
        print("Usage: {} <mysql_user> <mysql_password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    add_louisiana(sys.argv[1], sys.argv[2], sys.argv[3])
