from typing import List
from uuid import UUID

from api.v1.car.model import CarType


def get_all_types() -> List[CarType]:
    return CarType.query.all()


def get_car_type(uuid: UUID) -> CarType:
    result = CarType.query.get(ident=uuid)
    return result
