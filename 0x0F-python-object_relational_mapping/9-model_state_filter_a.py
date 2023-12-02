#!/usr/bin/python3
"""
    This script that lists all State
    objects that contain the letter a
    from the database hbtn_0e_6_usa
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

    filter_name = session.query(State).filter(State.name.like('%a%')).all()

    for filt in filter_name:
        print(f"{filt.id}: {filt.name}")
