import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import parking


if __name__ == '__main__':
    # dataset = parking.read_dataset()

    PARKING_CODE = 'Shopping'
    SELECTED_DATE = '2016-12-19'
    parking.plot_occupancy_of_parking_on_day(PARKING_CODE, SELECTED_DATE)




