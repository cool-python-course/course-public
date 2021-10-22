import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import parking


if __name__ == '__main__':
    # dataset = parking.read_dataset()

    # PARKING_CODE = 'Shopping'
    # SELECTED_DATE = '2016-12-19'
    # parking.plot_occupancy_of_parking_on_day(PARKING_CODE, SELECTED_DATE)

    fig, ax = plt.subplots(2,2)
    x = np.linspace(-10, +10, 100)
    y = [i**2 for i in x]
    y2 =[i**3 for i in x]
    y3 = np.sin(x)
    y4 = np.abs(x)
    ax[0][0].plot(x,y)
    ax[0][0].set_title('My 1st Figure')
    ax[0][1].plot(x,y2)
    ax[0][1].set_title('My 2nd Figure')
    ax[1][0].plot(x,y3)
    ax[1][0].set_title('My 3rd Figure')
    ax[1][1].plot(x,y4)
    ax[1][1].set_title('My 4th Figure')
    plt.show()




