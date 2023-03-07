from apiflask import Schema
from apiflask import fields


class BaseSchema(Schema):
    __abstract__ = True
    id = fields.UUID(required=False, allow_none=False)
    created_on = fields.DateTime(required=False)
    updated_on = fields.DateTime(required=False)


class CarColorSchema(BaseSchema):
    color_name = fields.Method("extract_enum_name")

    def extract_enum_name(self, obj):
        return obj.color_name.name


class CarTypeSchema(BaseSchema):
    type_car_name = fields.Method("extract_enum_name")

    def extract_enum_name(self, obj):
        return obj.type_car_name.name
