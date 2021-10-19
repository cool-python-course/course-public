from typing import List
from person import Person
import persist

def record_person(person: Person) -> Person:
    return persist.create_person(person)

def list_people() -> List[Person]:
    return persist.read_people()
