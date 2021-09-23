from typing import Tuple, List
from faker import Faker
import random


def generate_users(count: int = 1) -> List[Tuple[str,str]]:
    fake = Faker()
    return [(fake.name(), fake.email()) for _ in range(count)]

def generate_logs_entries(entry_count: int = 1e2, user_count: int = 1e1) -> List[str]:
    result = []
    fake = Faker()
    users = generate_users(user_count)
    for _ in range(entry_count):
        current_user = random.sample(users, 1)[0]
        result.append(
            f'{current_user[0]} <{current_user[1]}>: {fake.paragraph(random.randint(3,5))}'
        )
    return result
