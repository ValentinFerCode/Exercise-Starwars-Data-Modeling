import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(Integer)


class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer)
    homeworld = Column(String(250))
    starship = Column(String(250))


class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    vehicle_class = Column(String(250), nullable=False)
    passengers = Column(Integer, ForeignKey('person.id'))


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    gravity = Column()
    climate = Column(Integer, ForeignKey('person.id'))


class Likes(Base):
    __tablename__ = 'likes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)

    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle) 

    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')