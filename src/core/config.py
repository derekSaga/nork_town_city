import os
from distutils.util import strtobool


class Config(object):
    DEBUG = True
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
    HOST = os.environ["HOST"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]
    DATABASE_ENGINE = os.environ["DATABASE_ENGINE"]
    SQLALCHEMY_DATABASE_URI = "%s://%s:%s@%s:%s/%s" % (
        DATABASE_ENGINE,
        POSTGRES_USER,
        POSTGRES_PASSWORD,
        HOST,
        POSTGRES_PORT,
        POSTGRES_DB,
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = strtobool(
        os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]
    )

    SQLALCHEMY_ECHO = strtobool(os.environ["SQLALCHEMY_ECHO"])
