from sqlalchemy import UUID
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import types

from api import db
from src.api.models.base_model import BaseModelMixin


class CarType(BaseModelMixin):
    type_car_name = db.Column(types.String(155), nullable=False)


class CarColor(BaseModelMixin):
    color_name = db.Column(types.String(155), nullable=False)


class Car(BaseModelMixin):
    car_name = db.Column(types.String(155), nullable=False, unique=True)
    color_id = Column(UUID, ForeignKey("car_color.id"), nullable=False)
    type_car_id = Column(UUID, ForeignKey("car_type.id"), nullable=False)
    person_id = Column(
        UUID, ForeignKey("person.id", ondelete="CASCADE"), nullable=False
    )
