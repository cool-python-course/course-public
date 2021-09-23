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

def mask_user_data(log_entries: List[str]) -> List[str]:
    """
    Replace username with the hash of a 8 character long MD5 hash of the name.
    Mask the email with the following rules:
     - 2 character long usernames will be masked with single * e.g. aa@host.com => a*@host.com
     - usernames longer than 2 characters are masked in their middle with starts while their length remains the same e.g. apple@host.com => a***e@host.com
     - providers are also masked with the same rules but the TLD will not be masked e.g. apple@google.com => apple@g****e.com
     - Examples:
       - alice@my.com => a****e@m*.com
       - bob@gmail.com => b*b@g***l.com
       - charlie@sheen.com => c*****e@s***n.com

       Hints:
        - Use hashlib for MD5 hassing
        - Use Regular Expressions
    """
