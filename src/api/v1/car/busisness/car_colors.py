from typing import List

from api.v1.car.model import CarColor


def list_car_colors() -> List[CarColor]:
    try:
        car_colors = CarColor.query.all()
        return car_colors
    except Exception as e:
        raise e
