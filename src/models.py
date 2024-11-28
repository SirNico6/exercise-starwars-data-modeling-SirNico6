import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import DateTime


Base = declarative_base()

class User(Base):
    __tablename__ = 'USER'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    subscribe_date = Column(DateTime)

class Planet(Base):
    __tablename__ = 'PLANET'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    climate = Column(String(50), nullable=True)
    terrain = Column(String(50), nullable=True)

class People(Base):
    __tablename__ = 'PEOPLE'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    age = Column(Integer)
    birthday_year = Column(String(50), nullable=True)
    
class Favorite(Base):
    __tablename__ = 'FAVOURITE'
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('PEOPLE.id'))
    people = relationship(People)
    user_id = Column(Integer, ForeignKey('USER.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('PLANET.id'))
    planet = relationship(Planet)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')