from uuid import UUID

from api.v1.person.model import Person
from api.v1.person.schema import PersonSchema
from core.config import Config

db = Config.DB


def retrieve_person(user_id: UUID) -> Person:
    return Person.query.get_or_404(user_id)


def delete_person(user_id: UUID) -> None:
    person = retrieve_person(user_id)
    session = db.session
    try:
        db.session.delete(person)
        db.session.commit()
        return
    except Exception as e:
        session.rollback()
        raise e


def create_person(person_data: PersonSchema) -> PersonSchema:
    new_person = Person(**person_data)
    session = db.session
    try:
        session.add(new_person)
        session.commit()
        return new_person
    except Exception as e:
        session.rollback()
        raise e
