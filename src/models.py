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
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    favorite = relationship("Favorite")
    
    def response(self):
        return f"User #{self.id} : {self.username}" 


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)

    def response(self):
        return f"Character #{self.id} : {self.character_name}"


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    location_name = Column(String(250), nullable=False)

    def response(self):
        return f"Location #{self.id} : {self.location_name}"

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("user.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("character.id")) 
    location_id = Column(Integer, ForeignKey("location.id"))

    def response(self):
        return f"User #{self.user} marcó {self.location} {self.character} como favorito"


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
