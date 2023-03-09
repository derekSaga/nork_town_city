from apiflask import Schema
from apiflask import fields


class BaseSchema(Schema):
    __abstract__ = True
    id = fields.UUID(required=False, allow_none=False)
    created_on = fields.DateTime(required=False)
    updated_on = fields.DateTime(required=False)
