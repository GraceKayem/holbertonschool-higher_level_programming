#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
with their corresponding state names.
"""

import sys
import MySQLdb


def connect_and_query():
    """Connect to the database and display cities with their state names."""
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

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
        # Execute query joining cities and states, ordered by city id
        query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )
        cursor.execute(query)

        # Fetch and print results
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(e)

    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    connect_and_query()
