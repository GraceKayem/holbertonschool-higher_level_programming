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

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
        cursor = db.cursor()

        # REQUIRED: use format()
        query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"\
            .format(state_name)

        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(e)

    finally:
        # Only close if they exist
        try:
            cursor.close()
            db.close()
        except:
            pass


if __name__ == "__main__":
    connect_and_query()

