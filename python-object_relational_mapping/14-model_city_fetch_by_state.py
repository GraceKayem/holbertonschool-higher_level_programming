#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa

Usage: ./14-model_city_fetch_by_state.py <mysql_user> <mysql_password> <database_name>

Output format:
<state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities(mysql_user, mysql_pass, db_name):
    """Fetch all cities joined with states, sorted by city id ascending."""
    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_pass}"
        f"@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Join cities to states and order by city.id
        results = (
            session.query(City, State)
            .join(State)
            .order_by(City.id)
            .all()
        )
        for city, state in results:
            print(f"{state.name}: ({city.id}) {city.name}")
    finally:
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: {} <mysql_user> <mysql_password> <db_name>".format(
                sys.argv[0]
            )
        )
        sys.exit(1)

    fetch_cities(sys.argv[1], sys.argv[2], sys.argv[3])
