import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean 
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

    
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
   

     # Booleanos
    is_banned = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    favorite_characters = relationship("FavoriteCharacter", backref="user_favorite_characters") 
    favorite_characters = relationship("FavoritePlanet", backref="user_favorite_Planets") 
    favorite_characters = relationship("FavoriteVehicle", backref="user_favorite_Vehicles") 

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    height = Column(String(30), unique=True, nullable=False)
    mass = Column(String(60), unique=True, nullable=False)
    hair_color = Column(String(60), unique=True, nullable=False)    
    skin_color = Column(String(60), nullable=False)
    eye_color = Column(String(60), nullable=False)
    birth_year = Column(String(60), unique=True, nullable=False)
    gender = Column(String(60), unique=True, nullable=False)

    favorite_characters = relationship("FavoriteCharacter", backref="character_favorite_characters") 

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    rotation_period = Column(String(50), unique=True, nullable=False)
    orbital_period = Column(String(100), unique=True, nullable=False)
    diameter = Column(String(100), unique=True, nullable=False)
    climate = Column(String(100), unique=True, nullable=False)
    gravity = Column(String(100), unique=True, nullable=False)
    terrain = Column(String(100), unique=True, nullable=False)
    surface_water = Column(String(100), unique=True, nullable=False)
    population = Column(String(100), unique=True, nullable=False)
    
    favorite_Planets = relationship("FavoritePlanet", backref="character_favorite_planets") 


class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    model = Column(String(100), unique=True, nullable=False)
    manufacturer = Column(String(100), unique=True, nullable=False)
    cost_in_credits = Column(String(100), unique=True, nullable=False)
    length = Column(String(100), unique=True, nullable=False)
    max_atmosphering_speed = Column(String(30), unique=True, nullable=False)
    crew = Column(String(100), unique=True, nullable=False)
    passengers = Column(String(100), unique=True, nullable=False)
    cargo_capacity = Column(String(100), unique=True, nullable=False)
    consumables = Column(String(100), unique=True, nullable=False)

    favorite_Vehicles = relationship("FavoriteVehicle", backref="character_favorite_Vehicles") 

class FavoriteCharacter(Base):
    __tablename__ = "favorite_character"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    
    
class FavoritePlanet(Base):
    __tablename__ = "favorite_planet"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))



class FavoriteVehicle(Base):
    __tablename__ = "favorite_vehicle"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
