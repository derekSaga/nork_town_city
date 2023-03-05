from sqlalchemy import types

from models.base_model import BaseModelMixin
from models.base_model import db


class PersonModl(BaseModelMixin):
    name = db.Column(types.String(155), nullable=False)
