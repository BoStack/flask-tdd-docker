import os

from lib2to3.pytree import Base


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATION = False 

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABSE_URI')

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABSE_URI')
