import random
from typing import Tuple, Dict

from tqdm import tqdm

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def random_walk(number_of_turns: int) -> Tuple[int, int]:
    location = (0, 0)
    for _ in tqdm(range(number_of_turns)):
        direction = random.sample(DIRECTIONS, 1)[0]
        location = (location[0] + direction[0], location[1] + direction[1])
    return location

def manhattan_distance(location : Tuple[int,int]) -> int:
    return abs(location[0]) + abs(location[1])

def random_walk_simulation(distance_threshold: int, number_of_walks: int, max_number_of_turns: int) -> Dict[int, int]:
    result = {}
    for turn_count in tqdm(range(max_number_of_turns)):
        result[turn_count] = 0
        for _ in tqdm(range(number_of_walks)):
            location = random_walk(turn_count)
            if manhattan_distance(location) < distance_threshold:
                result[turn_count] += 1
    return result