#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.

- Uses SQLAlchemy ORM.
- Takes 3 arguments: mysql username, mysql password, database name
- Imports State and Base from model_state
- Connects to a MySQL server on localhost at port 3306
- Results sorted by cities.id
- Display format: <state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City


def fetch_cities(mysql_user, mysql_pass, db_name):
    """Fetch and print cities with their states."""
    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Join cities and states and order by city.id
        cities = session.query(City, State).join(State).order_by(City.id).all()
        for city, state in cities:
            print(f"{state.name}: ({city.id}) {city.name}")
    finally:
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: {} <mysql_user> <mysql_password> <db_name>".format(sys.argv[0])
        )
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    fetch_cities(user, password, database)
