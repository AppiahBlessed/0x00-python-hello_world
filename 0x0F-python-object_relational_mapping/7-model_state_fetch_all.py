#!/usr/bin/python3
"""
    pull state objects from DB
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    # bind base
    Base.metadata.bind = engine

    # Create session to manipulate data
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Execute query
    results = session.query(State).order_by(State.name).all()
    # Print output
    for res in results:
        print(f"{res.id}: {res.name}")

