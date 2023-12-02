#!/usr/bin/pyhton3
"""
    This is a script that defines a class
"""

# Neccessary imports
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Connection strig
url = 'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa'
# Create Engine
engine = create_engine(url)

# Instance of Declarative base
Base = declarative_base()

class State(Base):
    '''
        This state class inherits from the ase superclass
    '''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)

# Create connection and manipulate

# Bind one
# Base.metadata.create_all(engine)

# Create session
# Session = sessionmaker(bind=engine)
# session = Session()
