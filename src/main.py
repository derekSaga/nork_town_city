from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_migrate import upgrade
from flask_sqlalchemy import SQLAlchemy
from src.core.config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(
    app, db, compare_type=True, compare_server_default=True, render_as_batch=False
)

ma = Marshmallow(app)


@app.before_first_request
def init_db():
    upgrade(directory="./migrations")


if __name__ == "__main__":
    app.run()
