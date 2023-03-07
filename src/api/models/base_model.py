import uuid

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModelMixin(db.Model):
    __abstract__ = True
    id = db.Column(db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now()
    )
