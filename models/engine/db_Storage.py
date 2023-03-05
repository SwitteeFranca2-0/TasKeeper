#!/usr/bin/python3
"""This is initialising a class database storage"""
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from sqlalchemy import create_engine


class DBStorage():
    """Setting the database storage """
    __engine = None
    __session = None

    def __init__(self):
        """Initialising the dbstorage"""
        user = getenv('HBNB_MYSQL_USER')
        db = getenv('HBNB_MYSQL_DB')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db), pool_pre_ping=True)
        
        
