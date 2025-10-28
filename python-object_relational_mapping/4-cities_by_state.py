#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""


import sys
import MySQLdb

def connect_and_query():
    #getting arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    #connect to a MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                        user=username, passwd=password, db=db_name) 
    #getting a cursor
    cursor = db.cursor()
    #Results must be sorted in ascending order by states.id
    try: 
        cursor.execute("SELECT cities.id, cities.name, states.name " \
        "FROM cities " \
        "JOIN states " \
        "WHERE cities.state_id = states.id " \
        "ORDER BY cities.id ASC")
        #fetch and print result: must be displayed as they are in the example below
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(e)
    
    #close connnections
    cursor.close()
    db.close()

if __name__ == "__main__":
    connect_and_query()
