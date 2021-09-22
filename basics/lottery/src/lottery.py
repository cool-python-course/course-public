import random
from typing import List

import numpy as np

LOTTERY_NUMBERS_MINIMUM = 1
LOTTERY_NUMBER_MAXIMUM = 90
LOTTERY_NUMBER_COUNT = 5


def generate_lottery_tickets(count: int) -> List[np.ndarray]:
    result = []
    for _ in range(count):
        result.append(np.sort(generate_lottery_ticket()))
    return result


def generate_lottery_ticket() -> np.ndarray:
    """
    Generate a Lottery Ticket

    :return:
    """
    result = []
    while np.unique(result).size != 5:
        result = []
        for _ in range(LOTTERY_NUMBER_COUNT):
            result.append(random.randint(LOTTERY_NUMBERS_MINIMUM, LOTTERY_NUMBER_MAXIMUM))
    return result
