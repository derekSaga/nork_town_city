from sqlalchemy import UUID
from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import types

from api.models.base_model import BaseModelMixin
from api.v1.car.enums import CarColorsEnum
from api.v1.car.enums import CarTypeEnum


class CarType(BaseModelMixin):
    type_car_name = Column(Enum(CarTypeEnum), nullable=False, name="type_car_name")


class CarColor(BaseModelMixin):
    color_name = Column(Enum(CarColorsEnum), nullable=False, name="color_name")


class Car(BaseModelMixin):
    car_name = Column(types.String(155), nullable=False, unique=True)
    color_id = Column(UUID, ForeignKey("car_color.id"), nullable=False)
    type_car_id = Column(UUID, ForeignKey("car_type.id"), nullable=False)
    person_id = Column(
        UUID, ForeignKey("person.id", ondelete="CASCADE"), nullable=False
    )
