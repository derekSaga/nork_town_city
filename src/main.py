from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_migrate import upgrade

from api.models.base_model import db
from core.config import Config


def initdb(flask_app):
    db.init_app(flask_app)

    from api.v1.car.model import Car
    from api.v1.car.model import CarColor
    from api.v1.car.model import CarType
    from api.v1.person.model import Person


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    initdb(app)

    return app


app = create_app()

migrate = Migrate(
    app,
    db,
    compare_type=True,
    compare_server_default=True,
    render_as_batch=False,
)

ma = Marshmallow(app)


@app.before_first_request
def init_db():
    upgrade(directory="./migrations")


if __name__ == "__main__":
    app.run()
