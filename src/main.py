from apiflask import APIBlueprint
from apiflask import APIFlask
from flask_migrate import Migrate

from api.models.base_model import db
from api.v1.car.views.car_color_view import car_color_bp
from api.v1.car.views.car_type_view import car_type_db
from api.v1.car.views.car_view import car
from api.v1.person.views.person_view import person_bp
from core.config import Config


def initdb(flask_app):
    db.init_app(flask_app)

    from api.v1.car.model import Car
    from api.v1.car.model import CarColor
    from api.v1.car.model import CarType
    from api.v1.person.model import Person


def create_app():
    app = APIFlask(
        __name__,
    )

    app.config.from_object(Config)

    initdb(app)

    return app


app = create_app()
from api.v1.car import view

api_bp_v1 = APIBlueprint("bp_v1", __name__, url_prefix="/api/v1/")

api_bp_v1.register_blueprint(car_color_bp)
api_bp_v1.register_blueprint(car_type_db)
api_bp_v1.register_blueprint(car)
api_bp_v1.register_blueprint(person_bp)

app.register_blueprint(api_bp_v1)

migrate = Migrate(
    app,
    db,
    compare_type=True,
    compare_server_default=True,
    render_as_batch=False,
)


if __name__ == "__main__":
    app.run()
