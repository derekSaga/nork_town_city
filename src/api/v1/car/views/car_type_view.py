from http import HTTPStatus
from typing import List
from uuid import UUID

from apiflask import APIBlueprint
from apiflask import HTTPError
from flask import Response

from api.v1.car.schemas import CarTypeSchema
from api.v1.car.views.busisness import car_type

car_type_db = APIBlueprint("car_type", __name__, url_prefix="/car/type")


@car_type_db.get("/")
@car_type_db.output(CarTypeSchema(many=True))
def get_colors() -> List[Response]:
    car_colors = car_type.get_all_types()
    return car_colors


@car_type_db.get("/<uuid:car_type_id>")
@car_type_db.output(CarTypeSchema)
def get_color(car_type_id: UUID):
    result = car_type.get_car_type(car_type_id)
    if result is None:
        raise HTTPError(
            HTTPStatus.NOT_FOUND, "Type ID %s: Not Found" % car_type_id, detail=None
        )
    return result
