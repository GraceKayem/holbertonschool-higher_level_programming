#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""


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
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        #fetch and print rows: must be displayed as they are in the example below
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
