#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship(
                                'Review',
                                cascade='all, delete',
                                backref='place')
    else:
        @property
        def reviews(self):
            """Getter attribute reviews that returns the list of Review"""
            from models.review import Review
            from models.__init__ import storage
            list_reviews = []
            reviews = storage.all(Review)
            for review in reviews.values():
                if review.place_id == self.id:
                    list_reviews.append(review)
            return list_reviews
