#!/usr/bin/python3
"""
    This script that searches for a name
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

    search = session.query(State).filter_by(name=sys.argv[4]).first()
    if search is None:
        print("Not found")
    else:
        print(search.id)
