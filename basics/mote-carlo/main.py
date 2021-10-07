from manhattan import random_walk_simulation
from dice import dice_game_simulation

if __name__ == '__main__':
    print('Hello World')
    sample_count = int(1e6)
    simulation = dice_game_simulation(sample_count)
    print(simulation)
    print({key: value / sample_count for key, value in simulation.items()})

    DISTANCE_THRESHOLD = 5
    NO_WALKS = int(1e2)
    MAX_NO_OF_TURNS = int(25)
    random_walk_result = random_walk_simulation(DISTANCE_THRESHOLD, NO_WALKS, MAX_NO_OF_TURNS)
    print(random_walk_result)
