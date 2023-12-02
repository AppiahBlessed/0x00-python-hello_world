#!/usr/bin/python3
"""
    This script adds anew state object
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    quer = f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}'
    engine = create_engine(quer)

    Session = sessionmaker(bind=engine)
    session = Session()
    # Define
    new = State(name='Louisiana')
    # Add new state object
    session.add(new)
    # Commit changes
    session.commit()
    #Print new states
    print(new.id)

