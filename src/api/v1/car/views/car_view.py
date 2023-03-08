from apiflask import APIBlueprint

from api.v1.car.schemas import CarSchema
from api.v1.car.views.busisness import car_busisness

car = APIBlueprint("car", __name__, url_prefix="/car")


@car.post("/")
@car.input(CarSchema)
@car.output(CarSchema, status_code=201)
def create_car(car_data: CarSchema) -> CarSchema:
    result = car_busisness.create_car(car_data=car_data)
    return result


@car.delete("/<uuid:car_id>")
@car.output({}, status_code=204)
def delete_pet(car_id):
    car_busisness.delete_car(car_id)
    return ""
