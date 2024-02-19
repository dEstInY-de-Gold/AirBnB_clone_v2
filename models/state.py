#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel):
    """ State class and table module """
    __tablename__ = 'states'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='states',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """
            Returns a list of city instances with state_id equal
            to the current State.id
            """
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for cty in cities.values():
                if cty.state_id == self.id:
                    related_cities.append(cty)
            return related_cities
