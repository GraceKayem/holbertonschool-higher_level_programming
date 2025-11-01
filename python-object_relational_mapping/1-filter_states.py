#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa (case-sensitive).
"""

import sys
import MySQLdb


def connect_and_query():
    """Connect to the database and list states starting with 'N'."""
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    try:
        # Use BINARY to make the LIKE case-sensitive
        cursor.execute(
            "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(e)

    cursor.close()
    db.close()


if __name__ == "__main__":
    connect_and_query()
