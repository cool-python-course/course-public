import pandas as pd

def read_wine_dataset() -> pd.DataFrame:
    wine = pd.read_csv(filepath_or_buffer='./data/winemag-data-130k-v2.csv',
                       sep=',',
                       dtype={
                           'country': 'category',
                           'description': str,
                           'designation': 'category',
                           'points': float,
                           'price': float,
                           'province': 'category',
                           'region_1': 'category',
                           'region_2': 'category',
                           'winery': 'category',
                           'title': str
                       })
    return wine

