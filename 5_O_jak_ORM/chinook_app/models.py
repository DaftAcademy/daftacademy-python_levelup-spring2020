# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Artist(Base):
    __tablename__ = 'artist'

    artist_id = Column(Integer, primary_key=True)
    name = Column(String(120))
