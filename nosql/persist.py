import config
from typing import List
from person import Person
from pymongo import MongoClient

COLLECTION_NAME = 'people'

def get_client() -> MongoClient:
    CONNECTION_STRING = config.get_mongodb_connection_string()
    client = MongoClient(CONNECTION_STRING)
    return client

def get_database():
    client = get_client()
    return client[config.get_database_name()]

def create_person(person: Person) -> Person:
    db = get_database()
    id = db[COLLECTION_NAME].insert(person.__dict__)
    person.id = id
    return person

def read_people() -> List[Person]:
    result = []
    db = get_database()
    for document in  db[COLLECTION_NAME].find():
        curr_person = Person(document['name'], document['age'],document['skills'])
        curr_person.id = document['_id']
        result.append(curr_person)
    return result
