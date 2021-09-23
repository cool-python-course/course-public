import numpy as np
from src import gdpr

if __name__ == '__main__':
    print('Hello World')
    print(gdpr.generate_users())
    print(gdpr.generate_logs_entries(10,2))
