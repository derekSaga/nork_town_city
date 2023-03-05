import os
from distutils.util import strtobool

DEBUG = True
USER = os.environ["USER"]
SENHA = os.environ["SENHA"]
HOST = os.environ["HOST"]
PORT = os.environ["PORT"]
SCHEMA = os.environ["SCHEMA"]
DATABASE_ENGINE = os.environ["DATABASE_ENGINE"]
SQLALCHEMY_DATABASE_URI = f"{DATABASE_ENGINE}://{USER}:{SENHA}@{HOST}/{SCHEMA}"
SQLALCHEMY_TRACK_MODIFICATIONS = strtobool(
    os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]()
)

SQLALCHEMY_ECHO = strtobool(os.environ["SQLALCHEMY_ECHO"])
