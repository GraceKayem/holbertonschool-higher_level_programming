#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa"""


import sys
import MySQLdb

def connect_and_query():
    #getting arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    #connect to a MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                        user=username, passwd=password, db=db_name) 
    #getting a cursor
    cursor = db.cursor()
    #Results must be sorted in ascending order by states.id
    try: 
        cursor.execute("SELECT cities.name, states.name " \
        "FROM cities " \
        "JOIN states ON cities.state_id = states.id " \
        "WHERE states.name = %s " \
        "ORDER BY cities.id ASC",(state_name,))
        #fetch and print result: must be displayed as they are in the example below
        rows = cursor.fetchall()
        city_names = [row[0] for row in rows]  # extract city names
        unique_city_names = list(dict.fromkeys(city_names))  # remove duplicates
        print(", ".join(unique_city_names))
    except MySQLdb.Error as e:
        print(e)
    
    #close connnections
    cursor.close()
    db.close()

if __name__ == "__main__":
    connect_and_query()
