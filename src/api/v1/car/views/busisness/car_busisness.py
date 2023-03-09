from http import HTTPStatus
from uuid import UUID

from apiflask import HTTPError
from sqlalchemy.exc import IntegrityError

from api.v1.car.model import Car
from api.v1.car.schemas import CarSchema
from core.config import Config

db = Config.DB


def create_car(car_data: CarSchema) -> CarSchema:
    if Car.query.filter(Car.person_id == car_data.get("person_id")).count() >= 3:
        raise HTTPError(
            status_code=HTTPStatus.NOT_ACCEPTABLE,
            message="The person has reached the limit of allowed cars.",
            detail={"rule": "Limit 3 per person."},
        )
    new_car = Car(**car_data)
    session = db.session
    try:
        session.add(new_car)
        session.commit()
        return new_car
    except IntegrityError as e:
        session.rollback()
        raise HTTPError(
            status_code=HTTPStatus.CONFLICT,
            message=e.orig.pgerror,
            detail={"pgerror": e.orig.pgcode},
        )
    except Exception as e:
        session.rollback()
        raise HTTPError(status_code=HTTPStatus.NOT_ACCEPTABLE, message=str(e))


def get_car(car_id: UUID) -> CarSchema:
    car = Car.query.get_or_404(car_id)
    return car


def delete_car(car_id: UUID) -> CarSchema:
    car_delete = get_car(car_id)
    session = db.session
    try:
        db.session.delete(car_delete)
        db.session.commit()
        return
    except Exception as e:
        session.rollback()
        raise e
