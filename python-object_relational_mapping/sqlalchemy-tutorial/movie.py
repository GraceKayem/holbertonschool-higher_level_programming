from sqlalchemy import Column, String, Integer, Date 

from base import Base

"""
The definition of this class and its mapping characteristics is quite simple. We start by making this class extend the Base class defined in the base.py module and then we add four properties to it:

A __tablename__ to indicate what is the name of the table that will support this class.
An id to represent the primary key in the table.
A title of type String.
A release_date of type Date.
"""


movies_actors_association = Table(
    #As many movies can have many actors and vice-versa, we will need to. create a Many To Many relationship between these two classes. #Let's #create this relationship by updating the movie.py file as follows:
    'movies_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)

class Movie(Base):
    __tablename__= 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_data = Column(Date)
    #The difference between this version and the previous one is that: we imported three new entities: Table, ForeignKey, and relationship; we created a movies_actors_association table that connects rows of actors and rows of movies; and we added the actors property to Movie and configured the movies_actors_association as the intermediary table.
    actors = relationship("Actor", secondary=movies_actors_association)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date