#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def connect_and_query():
    """Connect to the database and display cities of the given state."""
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    try:
        # Execute query joining cities and states filtered by state name
        query = (
            "SELECT cities.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC"
        )
        cursor.execute(query, (state_name,))

        # Fetch results and extract city names
        rows = cursor.fetchall()
        city_names = [row[0] for row in rows]

        # Print city names, separated by commas
        print(", ".join(city_names))

    except MySQLdb.Error as e:
        print(e)

    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    connect_and_query()
