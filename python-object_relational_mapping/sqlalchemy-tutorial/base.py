from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLAlchemy Engine that will interact with our dockerized PostgreSQL database
engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
#SQLAlchemy ORM session factory bound to this engine
Session = sessionmaker(bind=engine)

#base class for our classes definitions
Base = declarative_base()

