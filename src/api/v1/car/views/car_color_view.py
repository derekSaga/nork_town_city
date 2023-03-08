from typing import List
from uuid import UUID

from apiflask import APIBlueprint
from apiflask import HTTPError
from flask import Response

from api.v1.car.schemas import CarColorSchema
from api.v1.car.views.busisness import car_color

car_color_bp = APIBlueprint("car_color", __name__, url_prefix="/car/color")


@car_color_bp.get("/")
@car_color_bp.output(CarColorSchema(many=True))
def get_colors() -> List[Response]:
    car_colors = car_color.get_all_colors()
    return car_colors


@car_color_bp.get("/<uuid:color_id>")
@car_color_bp.output(CarColorSchema)
def get_color(color_id: UUID):
    result = car_color.get_color(color_id)
    if result is None:
        raise HTTPError(404, "Color ID %s: Not Found" % color_id, detail=None)
    return result
