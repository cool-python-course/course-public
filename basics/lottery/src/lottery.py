import random
from typing import List, Dict

import numpy as np

LOTTERY_NUMBERS_MINIMUM = 1
LOTTERY_NUMBERS_MAXIMUM = 90
LOTTERY_NUMBERS_COUNT = 5


def generate_lottery_tickets(count: int) -> List[np.ndarray]:
    """
    Tasks:
     - Refactor the code to use Generators

     One Line Implementation
     [ np.array(random.sample(range(LOTTERY_NUMBERS_MAXIMUM-LOTTERY_NUMBERS_MINIMUM),LOTTERY_NUMBERS_COUNT))+LOTTERY_NUMBERS_MINIMUM for _ in range(count)]
     Explain it!
    :param count:
    :return:
    """
    result = []
    for _ in range(count):
        result.append(np.sort(generate_lottery_ticket()))
    return result


def generate_lottery_ticket() -> np.ndarray:
    """
    Generate a Lottery Ticket

    Tasks:
     - Refactor the code to use random.randint
     - Refactor the code to use random
    :return:
    """
    result = []
    while np.unique(result).size != 5:
        result = []
        for _ in range(LOTTERY_NUMBERS_COUNT):
            lottery_number = round((LOTTERY_NUMBERS_MAXIMUM - LOTTERY_NUMBERS_MINIMUM) * random.random()) + LOTTERY_NUMBERS_MINIMUM
            result.append(lottery_number)
    return np.sort(result)

def check_winner_tickets(tickets : List[np.ndarray], pulled_numbers: np.ndarray) -> Dict:
    """
    Count how many 1,2,3,4 and 5 matching tickets are.

    :param tickets:
    :param pulled_numbers:
    :return:
    """
    return {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0
    }

def calculate_total_prizes(tickets: List[np.ndarray], pulled_numbers: np.ndarray, prize_lookup: np.ndarray) -> int:
    """
    Calculate the total amount of prizes won.

    :param tickets:
    :param pulled_numbers:
    :param prize_lookup:
    :return:
    """
    return 0