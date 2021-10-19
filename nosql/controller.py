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


def print_all_people() -> None:
    for person in list_all_people():
        print(f'{person}')


def print_options():
    print('[R]ecord Person \n[L]ist People\n[Q]uit')


def is_option_string_valid(option: str) -> bool:
    if not option:
        return False
    if len(option) != 1:
        return False
    if option not in ['R','L','Q']:
        return False
    return True


def read_option() -> str:
    selected_option = ""
    while not is_option_string_valid(selected_option):
        selected_option = input()
    return selected_option
