#!/usr/bin/python3
"""
Contains the City class definition

City class:
- Inherits from Base (imported from model_state)
- Links to MySQL table 'cities'
- Attributes:
    - id: integer, primary key, auto-generated, not null
    - name: string of 128 characters, not null
    - state_id: integer, not null, foreign key to states.id
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Representation of a City linked to a State"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        return "<City(id={}, name={}, state_id={})>".format(
            self.id, self.name, self.state_id
        )
