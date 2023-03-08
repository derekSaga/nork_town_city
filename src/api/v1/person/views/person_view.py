from uuid import UUID
from apiflask import APIBlueprint
from api.v1.person.views.busisness import person_busisness
from api.v1.person.schema import PersonSchema

person_bp = APIBlueprint("person", __name__, url_prefix="/person")


@person_bp.delete("/<uuid:person_id>")
@person_bp.output({}, status_code=204)
def delete_car(person_id: UUID):
    person_busisness.delete_person(person_id)
    return ""


@person_bp.post("/")
@person_bp.input(PersonSchema)
@person_bp.output(PersonSchema, status_code=201)
def create_car(person_data: PersonSchema) -> PersonSchema:
    result = person_busisness.create_person(person_data)
    return result
