#!/usr/bin/python3
"""
Module containing the City class.

City class:
- Inherits from Base (from SQLAlchemy ORM)
- Links to the 'cities' table
- Attributes:
    - id: primary key, integer, auto-increment, not null
    - name: string(128), not null
    - state_id: integer, not null, foreign key to states.id
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Representation of a City linked to states."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        return "<City(id={}, name={}, state_id={})>".format(self.id, self.name,
                                                           self.state_id)
