from apiflask import fields

from api.schemas.base_schema import BaseSchema
from api.v1.car.schemas import CarSchema


class PersonSchema(BaseSchema):
    name = fields.String(required=True, allow_none=False)
    cars = fields.Nested(CarSchema, many=True)
