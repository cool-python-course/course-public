import pandas as pd
import datetime

def round_time_to_n_mins(time : datetime.datetime, n: int) -> datetime:
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
    parking['date'] = parking['LastUpdated'].dt.date
    parking['time'] = parking['LastUpdated'].dt.time
    parking['timeFuzzy'] = parking.apply(lambda row: round_time_to_n_mins(row['LastUpdated'], 5), axis=1)
    parking['freeSlots'] = parking['Capacity'] - parking['Occupancy']
    return parking