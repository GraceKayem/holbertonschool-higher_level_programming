from sqlalchemy import Column, String, Integer, Date

from base import Base

"""
The definition of this class is pretty similar to the previous one. The differences are that the Actor has a name instead of a title, a birthday instead of a release_date, and that it points to a table called actors instead of movies.
"""


class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    naem = Column(String)
    brithday = Column(Date)

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday