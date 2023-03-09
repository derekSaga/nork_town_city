from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy.orm import relationship

from api.v1.car.model import Car
from core.base_model import BaseModelMixin


class Person(BaseModelMixin):
    name = Column(types.String(155), nullable=False)
    cars = relationship(Car, backref="person", passive_deletes=True)
