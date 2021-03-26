#!/usr/bin/env python3

"""
contains the class definition of a City
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    """City Class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
