from Person import Person

def read_person() -> Person:
    print('name: ')
    name = input()
    print('age:')
    age = int(input())
    print('skills: ')
    skills_list = input()
    skills = [skill.lstrip() for skill in skills_list.split(',')]
    return Person(name,age,skills)