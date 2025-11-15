#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.

- Uses SQLAlchemy ORM
- Imports Base and State from model_state
- Connects to a MySQL server running on localhost at port 3306
- Does not execute when imported
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(user: str, password: str, dbname: str) -> None:
    """Delete all State objects containing 'a' in their name."""
    session = None
    try:
        # Create engine and session
        engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@localhost:3306/{dbname}",
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        # Find and delete states with 'a' in the name
        states_to_delete = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .all()
        )
        for state in states_to_delete:
            session.delete(state)

        session.commit()

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            f"Usage: {sys.argv[0]} <mysql_user> <mysql_password> <db_name>"
        )
        sys.exit(1)

    delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
