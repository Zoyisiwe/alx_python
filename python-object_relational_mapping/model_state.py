"""a python file that contains the class definition
of a State and an instance Base = declarative_base()"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection
DATABASE_URI = 'mysql://username:password@localhost:3306/your_database_name'
engine = create_engine(DATABASE_URI)
Base = declarative_base()


# State class definition
class State(Base):
    """This is a class for state and a instance of a base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == '__main__':
    # Create tables
    Base.metadata.create_all(engine)
