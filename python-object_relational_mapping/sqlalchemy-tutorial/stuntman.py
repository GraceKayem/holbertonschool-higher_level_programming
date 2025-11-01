from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref

from base import Base

"""
The next class that we will create is Stuntman. In our tutorial, a particular Actor will have only one Stuntman and this Stuntman will work only with this Actor. This means that we need to create the Stuntman class and a One To One relationship between these classes. To accomplish that, let's create a file called stuntman.py and add the following code to it:

In this class, we have defined that the actor property references an instance of Actor and that this actor will get a property called stuntman that is not a list (uselist=False). That is, whenever we load an instance of Stuntman, SQLAlchemy will also load and populate the Actor associated with this stuntman.
"""

class Stuntman(Base):
    __tablename__ = 'stuntmen'

    id = Column(Integer, primary_key=True)
    naem = Column(String)
    active = Column(Boolean)
    actor_id  = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref=backref("stuntman", uselist=False))

    def __init__(self, name, active, actor):
        self.name = name
        self.active = active
        self.actor = actor