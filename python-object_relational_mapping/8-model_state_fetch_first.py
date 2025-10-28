#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""


from model_state import Base, State #State is your ORM class representing the states table.
from sqlalchemy import create_engine #connects to MySQL
from sqlalchemy.orm import sessionmaker #creates a session to interact with the database
import sys #to read command-line arguments

def connect_and_query(user: str, passwd: str, db_name: str):

    try: 
        #Connect to the database and make queries using ORM
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                          .format(user, passwd, db_name))
        
        #Create a configured "Session" class
        Session = sessionmaker(bind=engine)
        state_session = Session() #state_session to perform queries
        #Query the first State object ordered by id (ascending)
        states = state_session.query(State).order_by(State.id).first()
        #.order_by(State.id) ensures ascending order by id
        #.first() → fetches the first result of State objects

        #Print the result or "Nothing" if table is empty
        if states is not None:
            print(states)
        else:
            print("Nothing")
    #Catches any error during connection, session creation, or query execution
    except Exception as e:
        return(e)

#Only executes the function when running the script directly
#Takes command-line arguments for MySQL credentials and database name
if __name__ == "__main__":
    #Only runs when script executed directly
    connect_and_query(sys.argv[1], sys.argv[2], sys.argv[3])