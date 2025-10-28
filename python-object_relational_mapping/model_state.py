#!/usr/bin/python3
"""Write a python file that contains the class definition of a State and an instance Base = declarative_base()"""


from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

engine = create_engine('mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa')
Base = declarative_base()


class State(Base):
    """
    State class inherits from Base.
    Maps to the 'states' table in the MySQL database.
    """
    __tablename__ = 'states'

    # Columns of the 'states' table
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the State object.
        Example: 1: California
        """
        return "{}: {}".format(self.id, self.name)