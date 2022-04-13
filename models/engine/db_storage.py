#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base


class DBStorage:
    """Class Database management"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor of the class DBStorage"""
        db_user = getenv("HBNB_MYSQL_USER")
        db_password = getenv("HBNB_MYSQL_PWD")
        db_database = getenv("HBNB_MYSQL_DB")
        db_host = getenv("HBNB_MYSQL_HOST")
        db_env = getenv("HBNB_ENV")

        self.__engine = create_engine(
                    'mysql+mysqldb://{}:{}@{}/{}'.format(
                            db_user,
                            db_password,
                            db_host,
                            db_database),
                    pool_pre_ping=True)

        if db_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns the list of objects of one type of class or all"""
        dict_return = {}
        if cls:
            results = self.__session.query(cls).all()
            for item in results:
                key = "{}.{}".format(type(item).__name__, item.id)
                dict_return[key] = item
        else:
            list_class = [State, City, User, Place, Review, Amenity]
            for class_name in list_class:
                results = self.__session.query(class_name).all()
                for item in results:
                    key = "{}.{}".format(type(item).__name__, item.id)
                    dict_return[key] = item
        return (dict_return)

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """Initilize the current database session"""
        Base.metadata.create_all(self.__engine)
        tmp_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(tmp_session)
        self.__session = Session()

    def close(self):
        """Close de current session"""
        self.__session.close()
