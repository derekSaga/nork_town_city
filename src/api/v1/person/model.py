from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy.orm import relationship

from api.models.base_model import BaseModelMixin
from api.v1.car.model import Car


class Person(BaseModelMixin):
    name = Column(types.String(155), nullable=False)
    cars = relationship(Car, backref="person", passive_deletes=True)
