from marshmallow import fields

from api.v1.car.model import CarColor
from main import ma


class CarColorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CarColor
        fields = "__all__"
        ordered = True

    color_name = fields.String(required=True)
