#!/usr/bin/python3
"""
Contains the State class definition and Base instance
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

# SQLAlchemy Base instance
Base = declarative_base()


class State(Base):
    """
    State class inherits from Base.
    Maps to the 'states' table in the MySQL database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the State object.
        Example: 1: California
        """
        return "{}: {}".format(self.id, self.name)
