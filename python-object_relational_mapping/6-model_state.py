#!/usr/bin/python3
"""
Start link of the State class to the database table.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and connect to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username,
            password,
            db_name
        ),
        pool_pre_ping=True
    )

    # Create all tables defined in Base metadata (State table)
    Base.metadata.create_all(engine)
