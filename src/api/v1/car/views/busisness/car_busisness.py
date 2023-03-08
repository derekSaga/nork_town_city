from uuid import UUID

from api.models.base_model import db
from api.v1.car.model import Car
from api.v1.car.schemas import CarSchema


def create_car(car_data: CarSchema) -> CarSchema:
    new_car = Car(**car_data)
    session = db.session
    try:
        session.add(new_car)
        session.commit()
        return new_car
    except Exception as e:
        session.rollback()
        raise e


def delete_car(car_id: UUID) -> CarSchema:
    car_delete = Car.query.get_or_404(car_id)
    session = db.session
    try:
        db.session.delete(car_delete)
        db.session.commit()
        return
    except Exception as e:
        session.rollback()
        raise e
