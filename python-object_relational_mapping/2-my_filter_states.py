#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

Usage: ./1-filter_states.py <username> <password> <database> <state_name>
"""

import sys
import MySQLdb


def connect_and_query():
    """Connect to the database and display states matching the argument."""
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor
    cursor = db.cursor()

    try:
        # Execute query safely to avoid SQL injection
        cursor.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
            (state_name,)
        )
        # Fetch all matching rows
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(e)
    finally:
        # Close cursor and connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)
    connect_and_query()
