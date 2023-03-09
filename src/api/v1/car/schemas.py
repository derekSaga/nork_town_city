from apiflask import fields

from core.base_schema import BaseSchema


class CarColorSchema(BaseSchema):
    color_name = fields.Method("extract_enum_name")

    def extract_enum_name(self, obj):
        return obj.color_name.name


class CarTypeSchema(BaseSchema):
    type_car_name = fields.Method("extract_enum_name")

    def extract_enum_name(self, obj):
        return obj.type_car_name.name


class CarSchema(BaseSchema):
    car_name = fields.String(required=True, allow_none=False)
    color_id = fields.UUID(required=True, allow_none=False)
    type_car_id = fields.UUID(required=True, allow_none=False)
    person_id = fields.UUID(required=True, allow_none=False)
