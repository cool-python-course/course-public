import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt


def round_time_to_n_mins(time: datetime.datetime, n: int) -> datetime:
    return (time - datetime.timedelta(
        minutes=time.minute % n,
        seconds=time.second,
        microseconds=time.microsecond
    )
            ).time()


def read_dataset() -> pd.DataFrame:
    parking = pd.read_csv(
        filepath_or_buffer='./data/parking/dataset.csv',
        sep=',',
        dtype={
            'SystemCodeNumber': 'category',
            'Capacity': int,
            'Occupancy': int
        },
        parse_dates=['LastUpdated']
    )
    parking['date'] = pd.to_datetime(parking['LastUpdated'].dt.date)
    parking['time'] = pd.to_timedelta(parking['LastUpdated'].dt.time, errors='coerce')
    parking['timeFuzzy'] = parking.apply(lambda row: round_time_to_n_mins(row['LastUpdated'], 5), axis=1)
    parking['minuteOfDay'] = parking.apply(lambda row: 60 * row['timeFuzzy'].hour + row['timeFuzzy'].minute, axis=1)
    parking['freeSlots'] = parking['Capacity'] - parking['Occupancy']
    return parking


def plot_occupancy_of_parking_on_day(parking_code_number: str, day: str) -> None:
    dataset = read_dataset()
    usage = dataset.loc[(dataset['date'] == day) & (dataset['SystemCodeNumber'] == parking_code_number)]
    sns.set()
    sns.lineplot(data=usage, x='minuteOfDay', y='Occupancy')
    p = sns.lineplot(data=usage, x='minuteOfDay', y='freeSlots')
    p.set_xlabel('Minute of Day')
    p.set_ylabel('# Cars')
    plt.title(f'{parking_code_number} -- {day}')
    plt.show()
