import uuid

from sqlalchemy import types
from ..main import migrate


db = migrate.db


class BaseModelMixin(db.Model):
    __abstract__ = True
    id = db.Collumn(types.UUID, default=uuid.uuid4())
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
