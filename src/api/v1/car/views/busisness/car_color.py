from typing import List
from uuid import UUID

from api.v1.car.model import CarColor


def get_all_colors() -> List[CarColor]:
    return CarColor.query.all()


def get_color(uuid: UUID) -> CarColor:
    result = CarColor.query.get(ident=uuid)
    return result
