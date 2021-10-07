from tqdm import tqdm
import math
import random
from typing import Tuple, Dict

DICE_MIN_VALUE = 1
DICE_MAX_VALUE = 6

def roll() -> int:
    return random.randint(DICE_MIN_VALUE, DICE_MAX_VALUE)

def roll_dice_pair() -> Tuple[int, int]:
    return (roll(), roll())

def dice_game_simulation(sample_count: int) -> Dict[int, int]:
    """
    Monte Carlo Simulation of the sum of two dice.

    :param sample_count:
    :return:
    """
    result = {}
    for i in range(2,12+1):
        result[i] = 0
    # Use tqdm for fancy for loops :)
    # for _ in range(sample_count):
    for _ in tqdm(range(sample_count)):
        dice_pair = roll_dice_pair()
        sum = int(math.fsum(dice_pair))
        result[sum] += 1
    return result