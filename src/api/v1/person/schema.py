from apiflask import fields

from api.v1.car.schemas import CarSchema
from core.base_schema import BaseSchema


class PersonSchema(BaseSchema):
    name = fields.String(required=True, allow_none=False)
    cars = fields.Nested(CarSchema, many=True, only=("id", "car_name"), dump_only=True)
