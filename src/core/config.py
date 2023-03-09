import os
from distutils.util import strtobool

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class ConfigBase(object):
    DB = SQLAlchemy(metadata=metadata)


class Config(ConfigBase):
    DEBUG = True
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
    POSTGRES_HOST = os.environ["POSTGRES_HOST"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]
    DATABASE_ENGINE = os.environ["DATABASE_ENGINE"]
    SQLALCHEMY_DATABASE_URI = "%s://%s:%s@%s:%s/%s" % (
        DATABASE_ENGINE,
        POSTGRES_USER,
        POSTGRES_PASSWORD,
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DB,
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = strtobool(
        os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]
    )

    SQLALCHEMY_ECHO = strtobool(os.environ["SQLALCHEMY_ECHO"])
