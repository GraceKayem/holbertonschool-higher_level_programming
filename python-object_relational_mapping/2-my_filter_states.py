#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb


def connect_and_query():
    """Connect to the database and display states matching the argument."""
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to a MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Get a cursor
    cursor = db.cursor()

    # Execute query safely using parameterized statements to avoid SQL injection
    try:
        cursor.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
            (state_name,)
        )
        # Fetch and print result
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(e)

    # Close conne
