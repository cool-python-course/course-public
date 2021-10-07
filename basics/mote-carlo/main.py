from dice import dice_game_simulation

if __name__ == '__main__':
    print('Hello World')
    sample_count = int(1e6)
    simulation = dice_game_simulation(sample_count)
    print(simulation)
    print({key: value / sample_count for key, value in simulation.items()})
