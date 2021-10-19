from typing import List

import service
from person import Person


def read_person() -> Person:
    print('name: ')
    name = input()
    print('age:')
    age = int(input())
    print('skills: ')
    skills_list = input()
    skills = [skill.lstrip() for skill in skills_list.split(',')]
    return Person(name, age, skills)


def record_person() -> Person:
    new_person = read_person()
    return service.record_person(new_person)


def list_all_people() -> List[Person]:
    return service.list_people()
