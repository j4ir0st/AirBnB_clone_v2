#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship(
                            "City",
                            backref="state",
                            cascade="all, delete")

    @property
    def cities(self):
        from models.__init__ import storage
        dict_city = storage.all(City)
        list_store = []
        for key, value in dict_city.items():
            if value.state_id == self.id:
                list_store.append(value)
        return list_store
