from flask import Blueprint

from src.api.v1.car.busisness.car_colors import list_car_colors
from src.api.v1.car.schemas import CarColorSchema

car_bp = Blueprint("cat_bp", __name__, url_prefix="/api/v1/car")


@car_bp.route(
    "/",
)
def list():
    car_colors = list_car_colors
    serializer = CarColorSchema(many=True)
    return serializer.jsonify({"data": car_colors}, 200)
