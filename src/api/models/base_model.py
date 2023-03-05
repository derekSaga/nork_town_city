import uuid

from sqlalchemy import types

from api import db


class BaseModelMixin(db.Model):
    __abstract__ = True
    id = db.Column(types.UUID, default=uuid.uuid4(), primary_key=True)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
