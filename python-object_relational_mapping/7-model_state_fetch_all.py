""" a script that lists all State objects from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Database connection
DATABASE_URI = 'mysql://{}:{}@localhost:3306/{}'.format
(sys.argv[1], sys.argv[2], sys.argv[3])
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # Query and list all State objects
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}:{}".format(state.id, state.name))
    
    # Close the session
    session.close()
